import graphene
from graphql_auth import mutations
# from graphql_auth.decorators import login_required
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
# from tugas_kerja.models import TugasKerj
from accounts.models import ExtendUser, m_bidang, m_jabatan, kode_kantor
from .models import TargetRealisasi, JenisUraian, Uraian
from detil_mkro.models import DetilMkro
from .converter import BigInt

class ExtendUserType(DjangoObjectType):
    class Meta:
        model = ExtendUser

class JabatanType(DjangoObjectType):
    class Meta:
        model = m_jabatan

class BidangType(DjangoObjectType):
    class Meta:
        model = m_bidang

class KodeKantorType(DjangoObjectType):
    class Meta:
        model = kode_kantor

class JenisUraianType(DjangoObjectType):
    class Meta:
        model = JenisUraian
        fields = '__all__'

class UraianType(DjangoObjectType):
    class Meta:
        model = Uraian
        fields = '__all__'

class TargetRealiasiType(DjangoObjectType):
    
    class Meta:
        model = TargetRealisasi
        fields = '__all__'
        

class DetilMkroType(DjangoObjectType):
    total_iuran_berjalan = graphene.Field(BigInt)
    class Meta:
        model = DetilMkro
        exclude = ('no',)

class TargetRealisasiMutation(graphene.Mutation):
    class Arguments:
        jenis = graphene.ID()
        uraian = graphene.ID()
        target_tahun = graphene.String()
        target_bln_lapor = graphene.String()
        realisasi_sd_bulan_lalu = graphene.String()
        realisasi_bln_lapor = graphene.String()
        realisasi_sd_bln_lapor = graphene.String()
        periode = graphene.Date()

    target = graphene.Field(TargetRealiasiType)

    @classmethod
    def mutate(cls,root,info, jenis,uraian,target_tahun,target_bln_lapor,realisasi_sd_bulan_lalu,realisasi_bln_lapor, realisasi_sd_bln_lapor, periode):
        qs = TargetRealisasi()
        # qs = TargetRealisasi.objects.filter()
        user = info.context.user
        if user.is_authenticated:
            qs.jenis_id = jenis
            qs.uraian_id = uraian
            qs.target_tahun = target_tahun
            qs.target_bln_lapor = target_bln_lapor
            qs.realisasi_sd_bulan_lalu = realisasi_sd_bulan_lalu
            qs.realisasi_bln_lapor = realisasi_bln_lapor
            qs.realisasi_sd_bln_lapor = realisasi_sd_bln_lapor
            qs.periode = periode
            qs.user = user 
            qs.save()
        
        return TargetRealisasiMutation(target=qs)

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    verify_token = mutations.VerifyToken.Field()
    

class Query(UserQuery, MeQuery, graphene.ObjectType):
    # all_tugas_user = graphene.List(TugasKerjaType, user=graphene.Int())
    all_target_realisasi = graphene.List(TargetRealiasiType, user=graphene.Int())
    all_jabatan = graphene.List(JabatanType)
    all_bidang = graphene.List(BidangType)
    all_kode_kantor = graphene.List(KodeKantorType)
    all_detil_mkro = graphene.List(DetilMkroType, npp=graphene.String())
    pass

    def resolve_all_target_realisasi(root, info, periode=None, user=None):
        
        user = info.context.user
        if user.is_authenticated:
            return TargetRealisasi.objects.select_related('user','jenis','uraian').filter(user=user)
    
    def resolve_all_jabatan(root, info, **kwargs):
        return m_jabatan.objects.all()

    def resolve_all_bidang(root, info, **kwargs):
        return m_bidang.objects.all()

    def resolve_all_kode_kantor(root, info, **kwargs):
        return kode_kantor.objects.all()

    def resolve_all_detil_mkro(root, info, npp):
        user = info.context.user
        print(user)
        if user.is_authenticated:
            return DetilMkro.objects.all().filter(npp=npp).order_by('-tgl_upload')[:1]
        else:
            return DetilMkro.objects.none()
class Mutation(AuthMutation, graphene.ObjectType):
    # buat_tugas = TugasKerjaMutation.Field()
    target_realisasi = TargetRealisasiMutation.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
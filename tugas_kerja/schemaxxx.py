import graphene
from graphql_auth import mutations
# from graphql_auth.decorators import login_required
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from .models import TugasKerja
from accounts.models import ExtendUser, m_bidang, m_jabatan, kode_kantor
from kepesertaan.models import TargetRealisasi, JenisUraian, Uraian

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

class UraianType(DjangoObjectType):
    class Meta:
        model = Uraian

class TargetRealiasiType(DjangoObjectType):
    class Meta:
        model = TargetRealisasi
        fields = '__all__'

class TugasKerjaType(DjangoObjectType):
    class Meta:
        model = TugasKerja
        fields = '__all__'

class TugasKerjaMutation(graphene.Mutation):
    class Arguments:
        judul = graphene.String(required=True)
        isi = graphene.String()
        # user = graphene.Int()
        # id = graphene.ID()

    tugas = graphene.Field(TugasKerjaType)

    @classmethod
    def mutate(cls,root,info,judul,isi):
        tugas = TugasKerja()
        user = info.context.user
        if user.is_authenticated:
            tugas.judul = judul
            tugas.isi = isi
            tugas.user = user
            tugas.save()

        return TugasKerjaMutation(tugas=tugas)

class TargetRealisasiMutation(graphene.Mutation):
    class Arguments:
        jenis = graphene.String()
        uraian = graphene.String()
        target_tahun = graphene.String()
        target_bln_lapor = graphene.String()
        realisasi_sd_bulan_lalu = graphene.String()
        realisasi_bln_lapor = graphene.String()
        realiasi_sd_bln_lapor = graphene.String()
        periode = graphene.Date()

    target = graphene.Field(TargetRealiasiType)

    @classmethod
    def mutate(cls,root,info,*kwargs,**args):
        target = TargetRealiasi()
        user = info.context.user
        if user.is_authenticated:
            target.user = user
            target.jenis = jenis
            target.iuran = iuran
            target.target_tahun = target_tahun
            target.target_bln_lapor = target_bln_lapor
            target.realisasi_sd_bulan_lalu = realisasi_sd_bulan_lalu
            target.realisasi_bln_lapor = realisasi_bln_lapor
            terget.realisasi_sd_bln_lapor = realisasi_sd_bulan_lapor
            target.periode = periode
            target.save()
        
        return TargetRealisasiMutation(target=target)

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    

class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_tugas_user = graphene.List(TugasKerjaType, user=graphene.Int())
    all_target_realisasi = graphene.List(TargetRealisasi, user=graphene.Int())
    pass

    def resolve_all_tugas_user(root, info, user=None):
        user = info.context.user
        if user.is_authenticated:
            return TugasKerja.objects.select_related('user__jabatan','user__bidang','user__kd_kantor').filter(user=user)

    def resolve_all_target_realisasi(root, info, periode=None, user=None):
        user = info.context.user
        if user.is_authenticated and not periode:
            return TargetRealisasi.objects.select_related('user','jenis','uraian').filter(user=user, periode=periode)
        else:
            return TargetRealisasi.objects.select_related('user','jenis','uraian').filter(user=user)

class Mutation(AuthMutation, graphene.ObjectType):
    buat_tugas = TugasKerjaMutation.Field()
    target_realisasi = TargetRealisasiMutation.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
import graphene
from graphene_django import DjangoObjectType
from .models import DetilMkro
from accounts.models import ExtendUser, m_jabatan, m_bidang, kode_kantor

class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = '__all__'

class bidangType(DjangoObjectType):
    class Meta:
        model = m_bidang
        fields = '__all__'
    
class jabatanType(DjangoObjectType):
    class Meta:
        model = m_jabatan
        fields = '__all__'

class kantorType(DjangoObjectType):
    class Meta:
        model = kode_kantor
        fields = '__all__'

class DetilMkroType(DjangoObjectType):
    class Meta:
        model = DetilMkro
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_mkro = graphene.List(DetilMkroType)

    def resolve_all_users(root,info):
        return ExtendUser.objects.select_related('jabatan','bidang','kd_kantor').all()

    def resolve_all_mkro(root,info):
        return DetilMkro.objects.all()[:100]

schema = graphene.Schema(query=Query)
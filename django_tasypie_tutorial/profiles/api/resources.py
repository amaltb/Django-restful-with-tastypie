from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource

from profiles.models import Member, Dependent


class MemberResource(ModelResource):
    dependents = fields.ToManyField('profiles.api.resources.DependentResource', 'dependents', related_name='member',
                                    use_in='detail', full=True, blank=True, null=True)

    class Meta:
        object_class = Member
        queryset = Member.objects.all()
        resource_name = 'members'
        allowed_methods = ['get', 'post', 'put', 'delete']
        excludes = ['member_photo']
        authentication = BasicAuthentication()


class DependentResource(ModelResource):
    member = fields.ForeignKey(MemberResource, 'member', full=True, use_in='detail')

    class Meta:
        object_class = Dependent
        queryset = Dependent.objects.all()
        resource_name = 'dependents'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()





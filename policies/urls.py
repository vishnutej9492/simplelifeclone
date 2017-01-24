from django.conf.urls import url
from . import views
from .forms import PolicyForm, PolicyForm2, PolicyForm3

urlpatterns = [
    url(r'^$', views.PolicyList.as_view(), name='policies_list'),
    url(r'^policy/(?P<pk>\d+)/$', views.PolicyDetail.as_view(), name='policy_detail'),
    url(r'^policy/new/$', views.PolicyWizard.as_view(), name='policy_new'),
    url(r'^policy/(?P<pk>\d+)/edit/$', views.PolicyUpdate.as_view(), name='policy_edit'),
]

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.shortcuts import redirect
from authtools.models import User
from .models import Policy
from .forms import PolicyForm


# Create your views here.

class PolicyList(ListView):
    model = Policy
    template_name = 'policies/policies_list.html'
    context_object_name = 'policies'

    def get_queryset(self):
        """
        Ensures only the logged in user can see their own policies
        """

        qs = super(PolicyList, self).get_queryset()
        if self.request.user.is_authenticated():
            user = User.objects.get(email=self.request.user.email)
            qs = qs.filter(owner=user)
        return qs


class PolicyDetail(DetailView):
    model = Policy
    template_name = 'policies/policies_detail.html'


class PolicyFormViewMixin(object):
    model = Policy
    form_class = PolicyForm
    template_name = 'policies/policy_edit.html'

    def form_valid(self, form):
        policy = form.save(commit=False)
        policy.owner = self.request.user
        policy.save()
        return redirect('policy_detail', pk=policy.pk)


class PolicyCreate(PolicyFormViewMixin, CreateView):
    template_name = 'policies/policy_new.html'


class PolicyUpdate(PolicyFormViewMixin, UpdateView):
    pass

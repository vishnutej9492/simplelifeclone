from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from authtools.models import User
from .models import Policy
from .forms import PolicyForm, PolicyForm2, PolicyForm3
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import sys,os

# Create your views here.

FORMS = [("create_policy", PolicyForm, "policies/policy_new.html"),
         ("upload_pdf", PolicyForm2, "policies/policy_upload_pdf.html"),
         ("attach_image", PolicyForm3, "policies/policy_attach_image.html")]

TEMPLATES = {item[0]:item[2] for item in FORMS}

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

class PolicyWizard(SessionWizardView):
    form_list = FORMS
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'pdf'))
    def get_context_data(self, form, **kwargs):
        context = super(PolicyWizard, self).get_context_data(form, **kwargs)

        # Make the organization name available to all forms
        create_policy_data = self.get_cleaned_data_for_step('create_policy')
        if create_policy_data:
            context.update({'create_policy_data': create_policy_data['policy_number']})

        return context

    def get_template_names(self):
        return TEMPLATES[self.steps.current]

    def done(self, form_list, **kwargs):
        return redirect('policies_list')

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

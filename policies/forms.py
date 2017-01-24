from django import forms
from .models import Policy
from parsley.decorators import parsleyfy
from django.utils.safestring import mark_safe

@parsleyfy
class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = (
            'carrier_name',
            'policy_number',
            'start_date',
            'end_date',
            'cust_serv_number',
            'cust_serv_email',
            'premium',
            'frequency',
            'pdf',
        )

    def __init__(self, *args, **kwargs):
        super(PolicyForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['cust_serv_number'].required = False
        self.fields['cust_serv_email'].required = False
        self.fields['premium'].required = False
        self.fields['frequency'].required = False
        self.fields['pdf'].required = False

class PolicyForm2(forms.ModelForm):
    class Meta:
        model = Policy
        fields = (
            'pdf',
        )

    def __init__(self, *args, **kwargs):
        super(PolicyForm2, self).__init__(*args, **kwargs)
        self.fields['pdf'].required = False

class PolicyForm3(forms.ModelForm):
    class Meta:
        model = Policy
        fields = (
            'image_name',
        )

    def __init__(self, *args, **kwargs):
        super(PolicyForm3, self).__init__(*args, **kwargs)
        self.fields['image_name'].required = False

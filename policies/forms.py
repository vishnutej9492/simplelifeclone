from django import forms
from .models import Policy
from parsley.decorators import parsleyfy


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

from django.db import models
from django.conf import settings
from django import forms
from django.core.files.storage import FileSystemStorage
# Create your models here.

def file_name(instance, filename):
    return 'files/{0}/{1}/{2}'.format(instance.owner.id, instance.policy_number, filename)

FREQ_CHOICES = (
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    )

IMAGE_CHOICES =(
    ('auto','Auto'),
    ('umbrella','Umbrella'),
    ('workers','Workers comp'),
    ('aircraft','Aircraft'),
    ('boat','Boat'),
    ('pet','Pet'),
    ('renters','Renters'),
    ('home owners','Home owners'),
)

class Policy(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    carrier_name = models.CharField(max_length=100)
    policy_number = models.IntegerField(primary_key=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True, null=True)
    cust_serv_number = models.IntegerField(blank=True, null=True)
    cust_serv_email = models.EmailField(blank=True, null=True)
    premium = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    frequency = models.CharField(max_length=20, choices=FREQ_CHOICES, blank=True, null=True)
    pdf=models.FileField(upload_to=file_name, blank=True, null=True)
    image_name=models.CharField(max_length=100, choices=IMAGE_CHOICES, blank=True, null=True)

    def save_policy(self):
        self.save()

    def __str__(self):
        return str(self.policy_number)

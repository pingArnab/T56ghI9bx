from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SpecsValueMap(models.Model):
    class USE_FLAG(models.TextChoices):
        YES = 'Y', _('Yes')
        NO = 'N', _('No')

    spec_id = models.CharField(blank=False, null=False, max_length=100)
    spec_name = models.CharField(blank=True, null=True, max_length=100)
    model_id = models.CharField(blank=False, null=False, max_length=100)
    model_name = models.CharField(blank=True, null=True, max_length=100)
    value = models.CharField(blank=True, null=True, max_length=100)
    use_flag = models.CharField(choices=USE_FLAG.choices, max_length=2)


from django.db import models
from django.core.validators import MinLengthValidator

class Lender(models.Model):

    """Model for the lenders table"""

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
    upfront_commission_rate = models.DecimalField(decimal_places=2, max_digits=3)
    trial_commission_rate = models.DecimalField(decimal_places=2, max_digits=3)
    active = models.BooleanField()
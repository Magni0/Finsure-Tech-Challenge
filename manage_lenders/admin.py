from django.contrib import admin
from manage_lenders.models import Lender

@admin.register(Lender)
class LenderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'code', 
        'upfront_commission_rate', 
        'trial_commission_rate', 
        'active'
    )

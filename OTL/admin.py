from django.contrib import admin


# Register your models here.
from OTL.models import SpecsValueMap


class SpecsValueMapAdmin(admin.ModelAdmin):
    list_display = (
        'spec_id', 'model_id', 'value', 'use_flag'
    )
    search_fields = [
        'spec_id', 'model_id', 'value', 'use_flag'
    ]
    list_filter = ('use_flag', )


admin.site.register(SpecsValueMap, SpecsValueMapAdmin)

from django.contrib import admin
from .models import Evaluation, Role
# Register your models here.
class EvalAdmin(admin.ModelAdmin):
    list_display = ('institute', 'profName', 'created_at')

admin.site.register(Evaluation, EvalAdmin)

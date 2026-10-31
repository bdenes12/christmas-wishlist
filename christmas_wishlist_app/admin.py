from django.contrib import admin

from .models import FamilyMember, Gift

admin.site.register(FamilyMember)
admin.site.register(Gift)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-licensing: admin/admin_License.py
##

from django.contrib import admin
from licensing.models import License

class LicenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(License, LicenseAdmin)

##
# End of File
##

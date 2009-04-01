#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-licensing: admin/admin_LicenseDesc.py
##

from django.contrib import admin
from licensing.models import LicenseDesc

class LicenseDescAdmin(admin.ModelAdmin):
    pass

admin.site.register(LicenseDesc, LicenseDescAdmin)

# End of File
##

#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-licensing: admin/admin_Attribution.py
##

from django.contrib import admin
from licensing.models import Attribution

class AttributionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attribution, AttributionAdmin)

##
# End of File
##

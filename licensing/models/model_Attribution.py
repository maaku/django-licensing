#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-licensing: models/model_Attribution.py
##

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from model_License import License

import tagging

class Attribution(models.Model):
    """
    A table that records copyright-owner and licensing information for
    arbitrary objects.

        Field     Type  Attributes
        =====     ----  ----------
         work   Object
      artists  *String
      license  License

         Keys: {object, license}
      Meaning: "The object identified by *object* is made available to us by
                the copyright-holders in *artists* (possibly empty) and under
                the terms of the license *license*."

    The artists field may be empty for license types where license.isattr is
    False.
    """

    ##
    # Referencing a generic object is not as easy as it should be in Django.
    # Together the fields content_type, object_id, and object represent a
    # generic object reference.
    content_type = models.ForeignKey(ContentType, verbose_name='content type')
    object_id    = models.PositiveIntegerField(verbose_name='object id', db_index=True)
    work         = generic.GenericForeignKey('content_type', 'object_id')

    ##
    # Django-tagging is probably the best way to implement the artist field.
    # See the call to tagging.register() at the bottom of this file.
    ##

    ##
    # See model_License.py
    license = models.ForeignKey(License)

    class Meta(object):
        app_label = "licensing"
        unique_together = (("content_type", "object_id"),
                           ("content_type", "object_id", "license"))

# This file might get loaded twice, causing an "already registered" exception.
try:
    tagging.register(Attribution,
                     tag_descriptor_attr='artist',
                     tagged_item_manager_attr='by_artist')
except:
    pass

##
# End of File
##

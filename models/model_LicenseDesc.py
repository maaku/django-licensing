#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-licensing: models/model_LicenseDesc.py
##

from django.db import models

from License import License
from languages.models import LangId

class LicenseDesc(models.Model):
    """
    A short, localized description of a license.

         Field     Type  Attributes
         =====     ----  ----------
       license  License
      language   LangId
          desc   String

         Keys: {license, language}, {language, desc}
      Meaning: "The license identified by *license* is best described in
                language *language* by the short description *desc*."

    A given license has only one description per language.  Two licenses will
    never have the same description in a given language (to avoid ambiguity in
    user interfaces).
    """
    # e.g, License.objects.filter(name="CC-BY-SA-3.0)
    license  = models.ForeignKey(License)
    # e.g, id:1 # for English
    language = models.ForeignKey(LangId)
    # e.g, "Creative Commons Attribution-Share Alike 3.0"
    desc     = models.CharField(max_length=92)

    ##
    # FIXME: A __unicode__() function should be written which returns a localized
    #        string that describes the record pretty well.
    #def __unicode__(self):
    #  pass

    class Meta(object):
        unique_together = (( 'license', 'language'),
                           ('language',     'desc'))
        verbose_name        = "Localized License Description"
        verbose_name_plural = "Localized License Descriptions"

# End of File
##

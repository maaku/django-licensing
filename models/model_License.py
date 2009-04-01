#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-licensing: models/model_License.py
##

from django.db import models

class License(models.Model):
    """
    The License table contains licenses which have been approved for use on
    this site.

    Note: This is the one table on this site that contains user-visible text
          that is *NEVER* translated into the user's desired language.  This
          is of course for legal reasons--a translated license is (in legal
          terms) a separate and distinct contract.  And we all ought to be
          very, very careful with respect to legal issues.

    Note: A localized short, non-binding description of each license can be
          found in the LicenseDesc table.

    Note: The name field is a bit redundant, since the user is more likely to
          see a localized description from LicenseDesc.  However a localized
          description might not exist (yet) in LicenseDesc, so name provides a
          (reasonable) language-neutral fallback.

       Field     Type  Attributes
       =====     ----  ----------
        name   String  unique
        text   String
         uri      URI  unique
      isattr  Boolean

         Keys: {name}, {uri}
      Meaning: "The license identified by *name*, and with the full license
                text in *text*, described at the website *uri* is approved
                for use on this site.  *isattr* specifies whether the license
                is an attribution-required license."

    If isattr is set to True, any attribution which uses this license *must*
    have a non-empty artist field.  Such licenses have an "Attribution" clause
    which requires that attribution be given to some of, or all of the
    copyright owners.
    """
    # e.g, "CC-BY-SA-3.0"
    name   = models.CharField(max_length=24,unique=True)
    # e.g, "License\n\nTHE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS
    #       OF..."
    text   = models.TextField()
    # e.g, "http://creativecommons.org/licenses/by-sa/3.0/"
    uri    = models.URLField(unique=True)
    # e.g, True # for CC Attribution licenses
    isattr = models.BooleanField()

    def __unicode__(self):
        return self.name

# End of File
##

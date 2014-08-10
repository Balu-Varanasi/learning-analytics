""" Models for 'colleges' app """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class College(models.Model):
    name = models.CharField(_("Name of the College"),
                            max_length=120)
    code = models.CharField(_("College Code"),
                            max_length=10)

    class Meta:
        verbose_name = _('College')
        verbose_name_plural = _('Colleges')

    def __unicode__(self):
        pass
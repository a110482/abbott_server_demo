# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models


def pdf_path(instance, filename):
    return instance.get_upload_path(filename)


class Tags(models.Model):
    tag = models.TextField(unique=True)

    def __unicode__(self):
        return unicode(self.tag)


class PDFDateBase(models.Model):
    pdf_file = models.FileField(upload_to='./', blank=True)
    file_name = models.TextField(blank=True, auto_created=pdf_file.name)
    tag_list = models.ManyToManyField(Tags, blank=True)

    def filename(self):
        return os.path.basename(self.pdf_file.name)



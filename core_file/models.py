# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def pdf_path(instance, filename):
    return instance.get_upload_path(filename)


class Tags(models.Model):
    tag = models.TextField(unique=True)


class PDFDateBase(models.Model):
    pdf_file = models.FileField(upload_to="pdf_dir", blank=True)
    file_name = models.TextField(blank=True)
    tag_list = models.ManyToManyField(Tags, blank=True)




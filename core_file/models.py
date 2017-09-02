# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now as timezone_now
import random
import string
import os

from django.db import models


def pdf_path(instance, filename):
    return instance.get_upload_path(filename)


class Tags(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return unicode(self.tag)


class PDFDateBase(models.Model):
    pdf_file = models.FileField(upload_to='./', blank=True)
    file_name = models.CharField(max_length=255, blank=True, auto_created=pdf_file.name)
    tag_list = models.ManyToManyField(Tags, blank=True)

    # 給 admin 抓每個檔案的 Tags 用的，預設不支援 m2m
    # https://stackoverflow.com/a/18108586/5352825
    def fileTags(self):
        return "\n/\n".join([p.tag for p in self.tag_list.all()])

    def filename(self):
        return os.path.basename(self.pdf_file.name)


# .......

def create_random_string(length=30):
    if length <= 0:
        length = 30

    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for x in range(length)])


def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'my_uploads/{}_{}{}'.format(
        now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),
        create_random_string(),
        filename_ext.lower()
    )


class Attachment(models.Model):
    parent_id = models.CharField(max_length=18)
    file_name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to=upload_to)

    def __unicode__(self):
        return unicode(self.file_name)

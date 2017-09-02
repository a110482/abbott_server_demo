# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']


@admin.register(PDFDateBase)
class PDFDateBaseAdmin(admin.ModelAdmin):
    list_display = ['pdf_file', 'file_name']
    list_filter = ['tag_list']

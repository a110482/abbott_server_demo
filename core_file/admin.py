# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *
# import bulk_admin


class ProjectInline(admin.ModelAdmin):
    model = PDFDateBase
    raw_id_fields = ('tag',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']
    # bulk_inline = ProjectInline


@admin.register(PDFDateBase)
class PDFDateBaseAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # bulk_upload_fields = ('pdf_file')
    search_fields = ('pdf_file', 'file_name', 'id',)
    list_display = ['file_name', 'pdf_file', 'fileTags']
    list_filter = ['tag_list']
    bulk_inline = ProjectInline
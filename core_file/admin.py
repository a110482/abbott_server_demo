# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *
import bulk_admin


class ProjectInline(bulk_admin.StackedBulkInlineModelAdmin):
    model = PDFDateBase
    raw_id_fields = ('tag',)


@admin.register(Tags)
class TagsAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['tag']
    # bulk_inline = ProjectInline


@admin.register(PDFDateBase)
class PDFDateBaseAdmin(bulk_admin.BulkModelAdmin):
    # date_hierarchy = 'pub_date'
    # bulk_upload_fields = ('pdf_file')
    search_fields = ('pdf_file', 'file_name', 'id',)
    list_display = ['file_name', 'pdf_file', 'fileTags']
    list_filter = ['tag_list']
    bulk_inline = ProjectInline
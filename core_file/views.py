# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import json
from django.db.models import Q
from django.http import JsonResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def demo_url(request):
    request_data = request.POST
    request_data_msg = json.loads(request_data["msg"])
    mode = request_data["mode"]
    if mode == "get_query_advice":
        search_text = request_data_msg["search_text"]
        tag_query = Tags.objects.filter(tag__icontains=search_text)
        query = PDFDateBase.objects.filter(
            Q(file_name__icontains=search_text) |
            Q(tag_list__in=tag_query)
        ).order_by('-id').all()
        return_dic = {
            "result_list": []
        }
        append_isd = []
        for data_s in query:
            temp_tag_list = []
            for tag_text in data_s.tag_list.all():
                temp_tag_list.append(tag_text.tag)
            temp_dic = {
                "id": str(data_s.id),
                "file_name": data_s.file_name,
                "file_path": str(data_s.pdf_file),
                "tags": temp_tag_list
            }
            if data_s.id not in append_isd:
                append_isd.append(data_s.id)
                return_dic["result_list"].append(temp_dic)
        return JsonResponse(return_dic)

















# Create your views here.

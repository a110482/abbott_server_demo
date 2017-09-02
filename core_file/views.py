# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response

from .models import Attachment
import json
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import re


@csrf_exempt
def demo_url(request):
    request_data = request.POST
    request_data_msg = json.loads(request_data["msg"])
    mode = request_data["mode"]
    if mode == "get_query_advice":
        search_text = request_data_msg["search_text"]
        search_list = re.split(r'\s*', search_text)
        # 關鍵字清單

        if '' in search_list:
            search_list.remove('')
        query = PDFDateBase.objects.filter(
            reduce(lambda x, y: x | y, [Q(file_name__icontains=word) for word in search_list]) |
            reduce(lambda x, y: x | y, [Q(tag_list__tag__icontains=word) for word in search_list])
        ).distinct().all()

        result_list = []
        # 製作結果清單
        for data_s in query:
            temp_tag_list = []
            for tag_text in data_s.tag_list.all():
                temp_tag_list.append(tag_text.tag)
            temp_dic = {
                "id": str(data_s.id),
                "file_name": data_s.file_name,
                "file_path": str(data_s.pdf_file),
                "tags": temp_tag_list,
                "point": 0
            }
            result_list.append(temp_dic)

        # 製作相關度分數  速度待驗證
        # for key_word in search_list:

        # 依照相關度排序
        def result_relative(a, b):
            # 所有元素都轉成小寫才做比對
            def str_lower(str_in):
                return str_in.lower()
            # 兩個元素 越符合條件者分數越大
            a_point = 0
            b_point = 0
            for key_word in search_list:
                if key_word.lower() in a["file_name"].lower() or key_word in map(str_lower, a["tags"]):
                    a_point += 1
                if key_word.lower() in b["file_name"].lower() or key_word in map(str_lower, b["tags"]):
                    b_point += 1
            if a_point > b_point:
                return -1
            return 1
        new_result_list = sorted(result_list, result_relative)
        return_dic = {
            "result_list": new_result_list
        }
        return JsonResponse(return_dic)


def pdf_dir(request, file_name):
    response = HttpResponse(content_type='application/pdf')
    # 強制user下載的code
    # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    print "-----------------"
    print './pdf_dir/%s'%(file_name)
    with open('./pdf_dir/%s'%(file_name)) as f:
        c = f.read()
    response.write(c)
    return response


def add_attachment(request):
    # web 上傳頁面用的
    if request.method == "POST":
        tag = request.POST['tag']
        files = request.FILES.getlist('myfiles')
        for number, a_file in enumerate(files):
            tags = ['a', 'b', 'c']
            tagObjectList = []
            for tag_text in tags:
                query = Tags.objects.filter(tag=tag_text)
                if query.count() > 0:
                    tagObjectList.append(query.all()[0])
                else:
                    instance = Tags(
                        tag=tag_text
                    )
                    instance.save()
                    tagObjectList.append(instance)

            instance = PDFDateBase(
                # tag=tag,
                file_name=a_file.name,
                pdf_file=a_file
            )
            instance.save()
            for tagObject in tagObjectList:
                instance.tag_list.add(tagObject)
            instance.save()


        request.session['number_of_files'] = number + 1
        return redirect("multiple_files:add_attachment_done")

    return render(request, "multiple_files/add_attachment.html")


def add_attachment_done(request):
    return render_to_response('multiple_files/add_attachment_done.html',
        context={"num_files": request.session["number_of_files"]})


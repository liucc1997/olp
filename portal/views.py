from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.views import View
from django.contrib import messages
import lib.file as lib_file
SIZE1 = 20
SIZE2 = 200
# Create your views here.
class PortalView(View):
    def get(self, request):
        src = request.GET.get("src",None)
        return render(request,"portal/portal.html")
    def post(self,request):
        context = {}
        src = request.POST.get("src", None)
        url = src
        check_result = lib_file.check_remote_file(url) #检查url的合理性 获取url请求类型
        if check_result is None:
            messages.add_message(request, messages.ERROR, '请输入合理的url')
        else:
            size = check_result.get('size',None)
            if size == -1:
                messages.add_message(request, messages.INFO, '-1: 文件大小未知，下载中断')
            if size == -2:
                messages.add_message(request, messages.INFO, '-2: 请求失败')
            if size > SIZE2:
                messages.add_message(request, messages.INFO, '暂时不支持下载超过%dM的文件'%(SIZE1))
            if size > SIZE1 and size < SIZE2:
                messages.add_message(request, messages.INFO, '暂时不支持下载超过%dM的文件'%(SIZE1))
            if size <= SIZE1 and size > 0:
                remote_file = lib_file.download_remote_file(src)
                file_name = lib_file.get_remote_file_name(src)
                if type(file_name) is int:
                    return HttpResponse("下载失败")
                response = HttpResponse(remote_file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename=%s'%(file_name)
                return response
        # context['url'] = url
        # context['download'] = True
        return render(request,"portal/portal.html",context)


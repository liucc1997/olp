from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.views import View
import lib.file as lib_file
# Create your views here.
class PortalView(View):
    def get(self, request):
        src = request.GET.get("src",None)
        return render(request,"portal/portal.html")
    def post(self,request):
        context = {}
        src = request.POST.get("src", None)
        #检验src
        if src == None:
            return render(request,"portal/portal.html",context)
        url = src
        remote_file = lib_file.download_remote_file(src)
        file_name = lib_file.get_remote_file_name(src)
        response = HttpResponse(remote_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=%s'%(file_name)
        return response

        context['url'] = url
        context['download'] = True
        return render(request,"portal/portal.html",context)


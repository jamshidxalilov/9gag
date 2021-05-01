from django.http import request
from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class MainIndex(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "9gaguz"

    def get(self, request):
        return render(request, 'main/index.html')

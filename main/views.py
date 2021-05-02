from django.http import request
from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from main.models import Post
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class MainIndex(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "9gaguz"

    def get(self, request):
        return render(request, 'main/index.html')



class UploadPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'comment', 'file']
    template_name = 'layouts/form.html'
    success_url = reverse_lazy('main:upload')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Yuklash")

    def form_valid(self, form):
        messages.success(self.request, _("Muvaffaqiyatli qo'shildi."))
        return super().form_valid(form)

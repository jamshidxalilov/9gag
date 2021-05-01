from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from django.utils.translation import gettext_lazy as _

from client.forms import RegistrationForm, LoginForm
from client.models import User


class RegistrationView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yxatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz.")

            return redirect('main:index')

        return render(request, 'layouts/form.html', {
            'form': form
        })


class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Tizimga kirish")

        def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                messages.warning(request, "Siz tizimga kirgansiz!")
                return redirect('main:index')

            return super(ClientLogin, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, _("Xush kelibsiz, {}".format(user.username)))

                return redirect('main:index')

            form.add_error('password', _("Login va/yoki parol noto'g'ri."))


        return render(request, 'layouts/form.html', {
            'form': form
        })


class ClientLogout(LoginRequiredMixin, View):
    def get(self, request):
        messages.success(request, _("Xayr {}".format(request.user.username)))
        logout(request)

        return redirect('main:index')



class ClientProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'photo']
    template_name = 'layouts/form.html'
    success_url = reverse_lazy('client:profile')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Profil")
        request.button_title = _("Saqlash")

    def get_object(self, queryset=None):
        return self.request.user

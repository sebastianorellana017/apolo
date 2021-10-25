from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CustomCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Create your views here.

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'miapp:login'


def registro(request):
    data = {
        'form': CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al home
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="/pagina")
        data["form"] = formulario

    return render(request, 'bases/registro.html', data)

@login_required(login_url='miapp:login')
def pagina(request):

    return render(request, 'bases/pagina.html')

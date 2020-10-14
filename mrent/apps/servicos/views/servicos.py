from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_contratante:
            return redirect('contratante:quiz_change_list')
        else:
            return redirect('marido:quiz_list')
    return render(request, 'servicos/index.html')

def maridodealuguel(request):
    return render(request, 'maridodealuguel/maridodealuguel.html')
from django.shortcuts import redirect, render
from .models import nota
from .forms import NotaFormulario
# Create your views here.

def nuevaNota(request):
    formulario = NotaFormulario()
    if request.method == 'POST':
        formulario = NotaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('principal')
    context = {
        'formulario': formulario
    }
    return render(request, 'nuevaNota.html', context)

def principal(request):
    return render(request, 'base.html')
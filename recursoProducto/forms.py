from django import forms
from django.forms import widgets
from .models import nota

class NotaFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NotaFormulario, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        widgets = {
            'fecha_finalizacion': forms.DateTimeInput(attrs={'type':'date'})
        }
        model = nota
        fields = '__all__'
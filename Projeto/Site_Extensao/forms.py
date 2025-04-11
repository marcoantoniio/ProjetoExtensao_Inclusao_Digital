from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'carga_horaria', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(
                attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'},
                format='%d/%m/%Y'
            ),
            'data_fim': forms.DateInput(
                attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'},
                format='%d/%m/%Y'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['data_inicio'].input_formats = ['%d/%m/%Y']
        self.fields['data_fim'].input_formats = ['%d/%m/%Y']
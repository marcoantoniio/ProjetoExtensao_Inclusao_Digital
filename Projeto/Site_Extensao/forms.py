from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'carga_horaria', 'data_inicio', 'data_fim', 'anotacoes']
        widgets = {
            'data_inicio': forms.DateInput(
                attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'},
                format='%d/%m/%Y'
            ),
            'data_fim': forms.DateInput(
                attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'},
                format='%d/%m/%Y'
            ),
            'anotacoes': forms.Textarea(attrs={
                'placeholder': 'Digite suas anotações aqui...',
                'rows': 6,
                'style': 'resize: none; height: 120px;'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        # Recebendo o request explicitamente
        self.request = kwargs.pop('request', None)  # Retirando o 'request' do kwargs, se existir
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # Associando o usuário ao curso antes de salvar
        curso = super().save(commit=False)
        if self.request:
            curso.user = self.request.user  # Associando o usuário logado
        if commit:
            curso.save()
        return curso

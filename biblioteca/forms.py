from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Usuario, Titulo, Exemplar, Emprestimo


class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(), label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")
    
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        
        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError("As senhas não coincidem.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha"])
        if commit:
            user.save()
        return user


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo
        fields = ['nome', 'autor', 'co_autor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'co_autor': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ExemplarForm(forms.ModelForm):
    class Meta:
        model = Exemplar
        fields = ['id_titulo', 'data_aquisicao']
        widgets = {
            'id_titulo': forms.Select(attrs={'class': 'form-control'}),
            'data_aquisicao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['id_usuario', 'id_exemplar', 'previsao_devolucao']
        widgets = {
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
            'id_exemplar': forms.Select(attrs={'class': 'form-control'}),
            'previsao_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas exemplares disponíveis
        self.fields['id_exemplar'].queryset = Exemplar.objects.filter(disponivel=True)
        
        # Definir data padrão de devolução (15 dias a partir de hoje)
        if not self.instance.pk:
            self.fields['previsao_devolucao'].initial = timezone.now().date() + timedelta(days=15)


class DevolucaoForm(forms.Form):
    confirmar_devolucao = forms.BooleanField(
        required=True,
        label="Confirmo que desejo devolver este exemplar",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


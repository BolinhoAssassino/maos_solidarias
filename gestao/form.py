from django import forms
from .models import Pessoa, Empresa, Conjugues, Dependentes, FrequenciaEvento, Evento,FrequenciaEventoPublico

class FormPessoas(forms.ModelForm):
  class Meta:
    model = Pessoa
    fields = ('nome','cpf','uf','cep','cedula_indentificacao','telefone','celular','data_emissao','orgao_expedidor','n_carteira_trabalho','nacionalidade','data_nascimento','data_de_entrada_no_brasil','email','estado_civil','reg_casamento','tipo_moradia','nome_pai','naturalidade_pai','nome_mae','naturalidade_mae','escolaridade','trabalha','profissao','empresa','nome_conjuge')

    widgets = {'data_emissao': forms.DateInput(attrs={'type':'date'}),
               'data_nascimento': forms.DateInput(attrs={'type':'date'}),
               'data_de_entrada_no_brasil' : forms.DateInput(attrs={'type':'date'}),
               'data_admissao' : forms.DateInput(attrs={'type':'date'})}
class FormEmpresa(forms.ModelForm):
  class Meta:
    model = Empresa
    fields = ('nome','cnpj','telefone','email','uf','cidade','bairro','rua','numero','complemento')

class FormConjugues(forms.ModelForm):
  class Meta:
    model = Conjugues
    fields = ('nome','cpf','data_nascimento','cedula_indentificacao','data_emissao','orgao_expedidor','telefone','celular','n_carteira_trabalho','nacionalidade','trabalha','empresa','data_admissao','escolaridade')
    widgets = {'data_nascimento': forms.DateInput(attrs={'type':'date'}),
               'data_emissao': forms.DateInput(attrs={'type':'date'}),
               'data_admissao': forms.DateInput(attrs={'type':'date'})}
class FormDependentes(forms.ModelForm):
  class Meta:
    model = Dependentes
    fields = ('nome','data_nascimento','cpf','responsavel')
    widgets = {'data_nascimento': forms.DateInput(attrs={'type':'date'})}
class FormEventos(forms.ModelForm):
  class Meta:
    model = Evento
    fields = ('evento','data','descricao','publico')
    widgets = {'data': forms.DateInput(attrs={'type':'date'})}
class FormEventosFrequencia(forms.ModelForm):
  class Meta:
    model = FrequenciaEvento
    fields = ('pessoa','evento')
class FormEventosFrequenciaPublicos(forms.ModelForm):
  class Meta:
    model = FrequenciaEventoPublico
    fields = ('pessoa','evento')
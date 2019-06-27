from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView, View,UpdateView
from .models import Pessoa, Cep, Dependentes, Conjugues,Evento, FrequenciaEventoPublico, FrequenciaEvento
from .form import FormPessoas,FormEmpresa,FormConjugues,FormDependentes,FormEventos,FormEventosFrequencia,FormEventosFrequenciaPublicos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
# Create your views here.

class Deslogar(LogoutView):
	template_name = 'login.html'

class Logar(LoginView):
	template_name = 'login.html'

class Pessoas(LoginRequiredMixin,DetailView):
	model = Pessoa
	template_name = "pessoas.html"
	def get_context_data(self, **kwargs):
		context = super(Pessoas, self).get_context_data(**kwargs)
		context['dependentes'] = Dependentes.objects.filter(responsavel=context['pessoa'])
		return context

@login_required
def principal(request):
	empregados = Pessoa.objects.values('trabalha').order_by('trabalha').annotate(count=Count('trabalha'))
	empregados = [empregados[1]['count'], empregados[0]['count']]
	escQuantia = []
	escEsc = []
	escolaridade = Pessoa.objects.values('escolaridade__escolaridade').annotate(count=Count('escolaridade'))
	for esc in escolaridade:
		if esc['count'] >0 and esc['escolaridade__escolaridade'] is not None:
			escQuantia.append(esc['count'])
			escEsc.append(esc['escolaridade__escolaridade'])
		else:
			pass
	return render(request, 'principal.html', {'empregados':empregados, 'escolaridade':escEsc, 'quantia':escQuantia})

@login_required
def redMenu(request):
	return redirect('principal')

@login_required
def procurar(request):
	nome = request.GET.get('busca')
	page = request.GET.get('page')
	pessoas = Pessoa.objects.filter(nome__contains=nome)
	paginacao = Paginator(pessoas, 10)
	page = paginacao.get_page(page)
	return render(request, 'procurar.html' ,{'pessoas': page, 'busca':nome})

@login_required
def eventos(request):
	eventual = Evento.objects.all().order_by('-data')
	paginacao = Paginator(eventual, 10)
	page = request.GET.get('page')
	page = paginacao.get_page(page)
	return render(request, 'eventos.html', {'eventos':page})
def ativar(request, pk, status):
	e = Evento.objects.get(pk=pk)
	if status == 'ativ':
		e.ativo = True
		e.save()
		return redirect('evento_pessoa', pk=pk)
	elif status == 'dis':
		print('dis')
		e.ativo = False
		e.save()
		return redirect('evento_pessoa', pk=pk)
	else:
		return redirect('evento_pessoa', pk=pk)

@login_required
def eventosPessoas(request, pk):
	context = {}
	evento = Evento.objects.get(pk=pk)
	if evento.ativo ==False and datetime.datetime.now().date() == evento.data:
		print('yes')
		evento.ativo = True
		evento.save()
	if evento.publico:
		frequencia = FrequenciaEventoPublico.objects.filter(evento=evento)
		if evento.ativo:
			if request.method == "POST":
				form = FormEventosFrequenciaPublicos(request.POST)
				if form.is_valid():
					form = form.save(commit=False)
					form.evento = evento
					form.save()
					return redirect('evento_pessoa', pk=evento.id)
			else:
				form= FormEventosFrequenciaPublicos(initial={"evento":evento})
			return render(request,'gerenciar_eventos.html' ,{'evento':evento, 'frequencia':frequencia, 'form':form})
		else:
			return render(request,'gerenciar_eventos.html' ,{'evento':evento, 'frequencia':frequencia})
	else:
		frequencia = FrequenciaEvento.objects.filter(evento=evento)
		if evento.ativo:
			if request.method == "POST":
				form = FormEventosFrequencia(request.POST)
				if form.is_valid():
					form = form.save(commit=False)
					form.evento = evento
					form.save()
					return redirect('evento_pessoa', pk=evento.id)
			else:
				form = FormEventosFrequencia(initial={"evento":evento})
			return render(request,'gerenciar_eventos.html' ,{'evento':evento, 'frequencia':frequencia, 'form':form})
		else:
			return render(request,'gerenciar_eventos.html' ,{'evento':evento, 'frequencia':frequencia})

@login_required
def formCEventos(request):
	firula = 'Adicionar Evento'
	if request.method == 'POST':
		form = FormEventos(request.POST)
		if form.is_valid():
			form.save()
			return redirect('evento')
	else:
		form = FormEventos()
	return render(request, 'evento_form.html',{'form': form, 'titulo':firula})

@login_required
def formCPessoa(request):
	firula = 'Cadastro de pessoa'
	if request.method == 'POST':
		form = FormPessoas(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastro_dependentes')
	else:
		form = FormPessoas()
	return render(request, 'pessoa_form.html', {'form': form,'titulo':firula})

@login_required
def formCPessoaEditar(request, pk):
	firula = 'Editar pessoa'
	pessoa = get_object_or_404(Pessoa, pk=pk)
	if request.method == "POST":
		form = FormPessoas(request.POST, instance=pessoa)
		if form.is_valid():
			form.save()
			return redirect('people',pk=pk)
	else:
		form = FormPessoas(instance=pessoa)
	return render(request, 'pessoa_form.html', {'form': form,'titulo':firula})

@login_required
def formCEmpresa(request):
	url = request.get_full_path()
	if 'conjuge' in url:
		pessoa ='<a href="cadastro_pessoa"><button> PULAR CADASTRO CONJUGAL </button></a>'
		firula = 'Cadastrar empresa onde trabalha cônjuge'
		url = 'cadastro_conjuge'
	else:
		pessoa = '<a href="cadastro_pessoa"><button> PULAR CADASTRO DE EMPRESA</button></a>'
		url = 'cadastro_pessoa'
		firula = 'Cadastrar empresa onde a pessoa trabalha'
	if request.method == 'POST':
		form = FormEmpresa(request.POST)
		if form.is_valid():
			form.save()
			return redirect(url)
	else:
		form = FormEmpresa()
	return render(request, 'empresa_form.html', {'form': form, 'titulo':firula, 'pessoa': pessoa})

@login_required
def formCconjugue(request):
	pessoa ='<a href="principal"><button> PULAR CADASTRO CONJUGAL </button></a>'
	firula = 'cadastro_pessoa'
	if request.method == 'POST':
		form = FormConjugues(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastro_empresa_p')
	else:
		form = FormConjugues()
	return render(request, 'conjuge_form.html', {'form': form , 'titulo': firula, 'pessoa': pessoa})

@login_required
def formCDependentes(request):
	pessoa ='<a href="cadastro_finnaly"><button> PULAR E RETORNAR A PAGINA PRINCIPAL </button></a>'
	firula = 'Cadastro de dependentes'
	if request.method == 'POST':
		form = FormDependentes(request.POST)
		if form.is_valid():
			form.save()
			return redirect('principal')
	else:
		form = FormDependentes()
	return render(request, 'dependente_form.html', {'form': form, 'titulo':firula, 'pessoa':pessoa, 'verdade':True})

@login_required
def formCDependentesEditar(request, pk):
	firula = 'Adicionar dependente pessoa'
	pessoa = get_object_or_404(Pessoa, pk=pk)
	if request.method == 'POST': 
		form = FormDependentes(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.responsavel = pessoa
			form.save()
			return redirect('people',pk=pessoa.id)
	else:
		form = FormDependentes()
	return render(request, 'dependente_form.html', {'form': form, 'titulo':firula,'verdade':False})

@login_required
def mudar_senha(request):
	#adicionar evento, marcar como fechado e gerenciar evento :)
	return render(request, 'forms.html', {'form': form})
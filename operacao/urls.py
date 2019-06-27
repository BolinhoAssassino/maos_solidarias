"""operacao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestao.views import formCEventos,ativar,formCDependentesEditar,eventosPessoas,Pessoas,Deslogar,Logar,principal,procurar,redMenu,eventos,formCPessoa,formCPessoaEditar,formCEmpresa,formCconjugue,formCDependentes 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name='principal'),
    path('procurar/', procurar, name='procurar'),
    path('pessoa/<pk>', Pessoas.as_view(), name='people'),
    path('pessoa/editar/<pk>', formCPessoaEditar, name='editar_people'),
    path('pessoa/adicionar_dependente/<pk>', formCDependentesEditar, name='dependente_people'),
    path('login', Logar.as_view(), name='login'),
    path('reset', Logar.as_view(), name='password_reset'),
    path('login/logando', Deslogar.as_view(), name='login_sucess'),
    path('evento/', eventos ,name='evento'),
    path('evento/<pk>', eventosPessoas, name='evento_pessoa'),
    path('evento/ativar/<pk>/<status>', ativar, name='evento_ativar'),
    path('evento/cadastrar/', formCEventos, name='evento_cadastro'),
    path('cadastrarpessoa/cadastro_pessoa', formCPessoa, name='cadastro_pessoa'),
    path('cadastrarpessoa/cadastro_conjuge_empresa', formCEmpresa, name='cadastro_empresa_c'),
    path('cadastrarpessoa/cadastro_pessoa_empresa', formCEmpresa, name='cadastro_empresa_p'),
    path('cadastrarpessoa/cadastro_dependente', formCDependentes, name='cadastro_dependentes'),
    path('cadastrarpessoa/cadastro_conjuge', formCconjugue, name='cadastro_conjuge'),
    path('cadastrarpessoa/cadastro_finnaly', redMenu, name='return'),

]

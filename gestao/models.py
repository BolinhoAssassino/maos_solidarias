# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TipoEstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=240, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.tipo)

class TipoImovel(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.tipo)

class Ufs(models.Model):
    id = models.AutoField(primary_key=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.uf)

class GrauEscolaridade(models.Model):
    id = models.AutoField(primary_key=True)
    escolaridade = models.CharField(max_length=240, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.escolaridade)

class Cep(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=240, blank=True, null=True)
    bairro = models.CharField(max_length=240, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    cidade = models.CharField(max_length=240, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.cep)

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=240, blank=True, null=False)
    cnpj = models.CharField(verbose_name='CNPJ',unique=True, max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=240, blank=True, null=True)
    uf = models.ForeignKey(Ufs, models.DO_NOTHING, verbose_name='UF', blank=True, null=True)
    cidade = models.CharField(max_length=240, blank=True, null=True)
    bairro = models.CharField(max_length=240, blank=True, null=True)
    rua = models.CharField(max_length=240, blank=True, null=True)
    numero = models.CharField(verbose_name='Número',max_length=5, blank=True, null=True)
    complemento = models.CharField(max_length=5, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.nome)

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=240, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    ativo = models.BooleanField(blank=False, null=False, default=False)
    descricao = models.TextField(blank=True, null=True)
    publico = models.BooleanField(verbose_name='Público', blank=False, null=False, default=False)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.evento)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
class Conjugues(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(blank=False, null=False,max_length=240)
    cpf = models.CharField(verbose_name='CPF', unique=True, max_length=9, blank=True, null=True)
    data_nascimento = models.DateField(blank=False)
    cedula_indentificacao = models.CharField(verbose_name='Cédula de indentificacao',max_length=9, blank=True, null=True)
    data_emissao = models.DateField(verbose_name='Data de emissão',blank=True, null=True)
    orgao_expedidor = models.CharField(verbose_name='Orgão expedidor',max_length=240, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    n_carteira_trabalho = models.CharField(verbose_name='Número da carteira de trabalho',max_length=12, blank=True, null=True)
    nacionalidade = models.CharField(max_length=240, blank=True, null=True)
    trabalha = models.BooleanField(verbose_name='Trabalha com carteira assinada',blank=False, null=False, default=False)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    data_admissao = models.DateField(verbose_name='Data de admissão', blank=True, null=True)
    escolaridade = models.ForeignKey(GrauEscolaridade, models.DO_NOTHING, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.nome)

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=240)
    cpf = models.CharField(verbose_name='CPF',unique=True, max_length=9, blank=True, null=True)
    uf = models.ForeignKey(Ufs, models.DO_NOTHING,verbose_name='UF', blank=True, null=True)
    cep = models.ForeignKey(Cep, models.DO_NOTHING, blank=True, null=True)
    cedula_indentificacao = models.CharField(verbose_name='Cédula de indentificação',max_length=9, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    data_emissao = models.DateField(verbose_name='Data de emissão', blank=True, null=True)
    orgao_expedidor = models.CharField(verbose_name='Orgão expedidor',max_length=240, blank=True, null=True)
    n_carteira_trabalho = models.CharField(verbose_name='Número da carteira de trabalho',max_length=12, blank=True, null=True)
    nacionalidade = models.CharField(max_length=240, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_de_entrada_no_brasil = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=240, blank=True, null=True)
    estado_civil = models.ForeignKey(TipoEstadoCivil, models.DO_NOTHING, blank=True, null=True)
    reg_casamento = models.CharField(max_length=240, blank=True, null=True)
    tipo_moradia = models.ForeignKey(TipoImovel, models.DO_NOTHING, blank=True, null=True)
    nome_pai = models.CharField(max_length=240, blank=True, null=True)
    naturalidade_pai = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=240, blank=True, null=True)
    naturalidade_mae = models.CharField(max_length=100, blank=True, null=True)
    escolaridade = models.ForeignKey(GrauEscolaridade, models.DO_NOTHING, blank=True, null=True)
    trabalha = models.BooleanField(verbose_name='Trabalha com carteira assinada',blank=False, null=False, default=False)
    profissao = models.CharField(verbose_name='profissão',max_length=240, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    data_admissao = models.DateField(verbose_name='Data de admissão',blank=True, null=True)
    nome_conjuge = models.ForeignKey(Conjugues, models.DO_NOTHING, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.nome)

class Dependentes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=240, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=True)
    cpf = models.CharField(max_length=9, blank=True, null=True)
    responsavel = models.ForeignKey(Pessoa, models.DO_NOTHING, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.nome)
class FrequenciaEvento(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, blank=False, null=False)
    evento = models.ForeignKey(Evento, models.DO_NOTHING, blank=False, null=False)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.evento.evento)
    def save(self, *args, **kwargs):
        if self.evento.ativo is False:
            raise ValidationError('ahah aha aha')
        super(FrequenciaEvento, self).save(*args, **kwargs)

class FrequenciaEventoPublico(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.CharField(blank=False, null=False, max_length=240)
    evento = models.ForeignKey(Evento, models.DO_NOTHING, blank=False, null=False)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.evento.evento)
    def save(self, *args, **kwargs):
        print('lol')
        if self.evento.publico is False:
            raise ValidationError('Não é possivel adicionar um evento não público')
        super(FrequenciaEventoPublico, self).save(*args, **kwargs)
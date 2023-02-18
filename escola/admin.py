from django.contrib import admin
from escola.models import Aluno, Curso, Matricula             #importar os models

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')    #o que vai disponibilizar no admin
    list_display_links = ('id', 'nome')                              #cria link no id e no nome
    search_fields = ('nome', )                                       #filtrar no nome
    list_per_page = 20                                               #apresentar 20 alunos por pgs
    
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao') 
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', )
    
admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo') 
    list_display_links = ('id',)
    
admin.site.register(Matricula, Matriculas)




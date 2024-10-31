from aluno import *
from boletim import *
from funcionario import *
from professor import *
from sistema import *

# Create instances of Boletim
boletim1 = Boletim([7, 8, 9], True)
boletim2 = Boletim([6, 5, 4], False)
boletim3 = Boletim([10, 9, 8], True)
boletim4 = Boletim([5, 4, 6], False)

# Create instances of Aluno
aluno1 = Aluno(nome="João", matricula=123, pais="Brasil", serie="1º ano", bolsa=True, boletim=boletim1, mensalidade=15000)
aluno2 = Aluno(nome="Maria", matricula=124, pais="Brasil", serie="2º ano", bolsa=False, boletim=boletim2, mensalidade=16000)
aluno3 = Aluno(nome="Lucas", matricula=125, pais="Brasil", serie="1º ano", bolsa=True, boletim=boletim3, mensalidade=15000)
aluno4 = Aluno(nome="Ana", matricula=126, pais="Brasil", serie="2º ano", bolsa=False, boletim=boletim4, mensalidade=16500)

# Create instances of Funcionario
funcionario1 = Funcionario(nome="Carlos", cargo="Secretário", salario=3000)
funcionario2 = Funcionario(nome="Ana", cargo="Janitor", salario=2000)

# Create instances of Professor
professor1 = Professor(nome="Dr. Silva", salario=7000, leciona="Matemática", email="silva@escola.com")
professor2 = Professor(nome="Profa. Oliveira", salario=7500, leciona="Português", email="oliveira@escola.com")

# Create new instances for testing
Sistema.cadastrar_aluno(Aluno(nome="Gabriel", matricula=127, pais="Brasil", serie="3º ano", bolsa=False, boletim=Boletim([7, 6, 8], True), mensalidade=16000))
Sistema.cadastrar_aluno(aluno1)
Sistema.cadastrar_aluno(aluno2)
Sistema.cadastrar_aluno(aluno3)
Sistema.cadastrar_aluno(aluno4)
Sistema.cadastrar_funcionario(Funcionario(nome="Joana", cargo="Coordenadora", salario=5000))
Sistema.cadastrar_funcionario(funcionario1)
Sistema.cadastrar_funcionario(funcionario2)
professor_x = Professor(nome="Prof. Almeida", salario=7200, leciona="História", email="almeida@escola.com")
Sistema.cadastrar_professor(professor_x)
Sistema.cadastrar_professor(professor1)
Sistema.cadastrar_professor(professor2)
Sistema.excluir_aluno(aluno4)
Sistema.excluir_professor(professor_x)
Sistema.excluir_funcionario(funcionario1)
# Test various methods
print("Total alunos:", Sistema.alunos_serie("2º ano"))

# Calculate approved students percentage
print("Porcentagem de alunos aprovados:", Sistema.porcentagem_alunos_aprovados(), "%")

# Calculate average salary of employees
print("Média salarial dos funcionários:", Sistema.relacao_salario_funcionario())

# Test media da série
print("Média de notas do 1º ano:", Sistema.media_serie("1º ano"))
print("Média de notas do 2º ano:", Sistema.media_serie("2º ano"))
print("Média de notas do 3º ano:", Sistema.media_serie("3º ano"))

# Check the number of students with scholarships
print("Porcentagem de alunos bolsistas:", Sistema.porcentagem_alunos_bolsistas(), "%")
print("Porcentagem de alunos não bolsistas:", Sistema.porcentagem_alunos_nao_bolsistas(), "%")

print(Sistema.alunos_serie("1º ano"))
print(Sistema.faturamento_escola())
print(Sistema.despesa_escola())
print(Sistema.lucro_escola())
print(Sistema.lista_professores_por_materia("Matemática"))
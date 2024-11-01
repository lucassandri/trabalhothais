from tela_abstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):

    def __init__(self):
        pass
    
    def tela_opcoes(self):
        print("-------- PROFESSORES ----------")
        print("1 - Incluir Professor")
        print("2 - Alterar Professor")
        print("3 - Excluir Professor")
        print("4 - Listar Professores")
        print("5 - Mostrar professor por email")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
        return opcao
    
    def pega_dados_professor(self):
        print("-------- DADOS PROFESSOR ----------")
        nome = self.le_string("Nome: ")
        salario = self.le_float("Salário: ")
        leciona = self.le_string("Lecionando: ")
        email = self.le_string("Email: ")
        
        return {"nome": nome, "salario": salario, "leciona": leciona, "email": email}
    
    def seleciona_professor(self):
        email = self.le_string("Digite o email do professor: ")
        return email
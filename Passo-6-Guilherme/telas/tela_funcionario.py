from telas.tela_abstrata import TelaAbstrata

class TelaFuncionario(TelaAbstrata):

    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- FUNCIONÁRIOS ----------")
        print("1 - Incluir funcionário")
        print("2 - Alterar funcionário")
        print("3 - Excluir funcionário")
        print("4 - Listar funcionários")
        print("5 - Mostrar funcionário por email")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
        return opcao
    
    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONÁRIO ----------")
        nome = self.le_string("Nome: ")
        cargo = self.le_string("Cargo: ")
        salario = self.le_float("Salário: ")
        email = self.le_string("Email: ")
        
        return {"nome": nome, "cargo": cargo, "salario": salario, "email": email}
    
    def seleciona_funcionario(self):
        email = self.le_string("Digite o email do funcionario: ")
        return email
    
    def mostra_funcionario(self, dados_funcionario):
        print('Nome do funcionário: ', dados_funcionario["nome"])
        print('Cargo do funcionário: ', dados_funcionario["cargo"])
        print('Salário do funcionário: ', dados_funcionario["salario"])
        print('Email do funcionário: ', dados_funcionario["email"])
        print('---------------------------------------------')
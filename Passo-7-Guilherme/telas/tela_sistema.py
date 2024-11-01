from telas.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    
    def __init__(self):
        pass
    
    def tela_opcoes(self):
        print("-------- SISTEMA ---------")
        print("1 - Alunos")
        print("2 - Finanças")
        print("3 - Funcionários")
        print("4 - Professores")
        print("0 - Finalizar sistema")

        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao

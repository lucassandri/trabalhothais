from tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisEscola ---------")
        print("Escolha sua opcao")
        print("1 - Alunos")
        print("2 - Financas")
        print("3 - Funcionarios")
        print("4 - Professores")
        print("0 - Finalizar sistema")

        opcao = int(input("Escolha a opcao:"))
        return opcao
from entidades.professor import Professor
from telas.tela_professor import TelaProfessor
from controlador_abstrato import ControladorAbstrato

class ControladorProfessor(ControladorAbstrato):
    
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__professores = []
        self.__tela_professor = TelaProfessor()
    
    @property
    def professores(self):
        return self.__professores

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["salario"], dados_professor["leciona"], dados_professor["email"])
        
        if len(self.__professores) == 0:
            self.__professores.append(professor)
        else:
            try:
                for teacher in self.__professores:
                    if teacher.email == professor.email:
                        raise KeyError
                else:
                    self.__professores.append(professor)
            except KeyError:
                self.__tela_professor.mostra_mensagem('Atenção! Professor já existente no sistema!')
  
    def alterar_professor(self):
        
        email_professor = self.__tela_professor.seleciona_professor()
        
        for teacher in self.__professores:
            if teacher.email == email_professor:
                professor = teacher
                novos_dados_professor = self.__tela_professor.pega_dados_professor()
                professor.nome = novos_dados_professor["nome"]
                professor.salario = novos_dados_professor["salario"]
                professor.leciona = novos_dados_professor["leciona"]
                professor.email = novos_dados_professor["email"]
                break

        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente no sistema!")

    def lista_professores(self):
        if len(self.__professores) == 0:
            print("Atenção! Não existem professores cadastrados no sistema!")
            return None
        else:
            for professor in self.__professores:
                print(f'Nome do professor: {professor.nome}')
                print(f'Salário do professor: {professor.salario}')
                print(f'Matéria que o professor leciona: {professor.leciona}')
                print(f'Email do professor {professor.email}')
                print('-----------------------------------------')

    def excluir_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        for professor in self.__professores:
            if professor.email == email_professor:
                self.__professores.remove(professor)
                break
        else:
            print("Atenção! Professor selecionado não consta no sistema!")
    
    def achar_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        for professor in self.__professores:
            if professor.email == email_professor:
                print(f'Nome do professor: {professor.nome}')
                print(f'Salário do professor: {professor.salario}')
                print(f'Matéria que o professor leciona: {professor.leciona}')
                print(f'Email do professor {professor.email}')
                break
        else:
            print("Atenção! Não existem Professores com esse email no sistema!")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor, 2: self.alterar_professor, 3: self.excluir_professor, 4: self.lista_professores, 5: self.achar_professor, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
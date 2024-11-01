from entidades.aluno import Aluno
from entidades.boletim import Boletim
from telas.tela_aluno import TelaAluno
from controlador_abstrato import ControladorAbstrato

class ControladorAluno(ControladorAbstrato):
  
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
    
    @property
    def alunos(self):
        return self.__alunos

    def cadastrar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for student in self.__alunos:
          if student.matricula == matricula_aluno:
            aluno = student
            if aluno.boletim is None:
                tem_boletim = False
                if tem_boletim == False:
                    dados_boletim = self.__tela_aluno.pega_dados_notas_boletim()
                    b1 = Boletim(0,0,0,0,0,0,0,0,0,0)
                    b1.media_matematica = dados_boletim["matematica"]
                    b1.media_lingua_portuguesa = dados_boletim["lingua_portuguesa"]
                    b1.media_geografia = dados_boletim["geografia"]
                    b1.media_historia = dados_boletim["historia"]
                    b1.media_ciencias = dados_boletim["ciencias"]
                    b1.media_artes = dados_boletim["artes"]
                    b1.media_filosofia = dados_boletim["filosofia"]
                    b1.media_lingua_inglesa = dados_boletim["lingua_inglesa"]
                    b1.media_educacao_fisica = dados_boletim["educacao_fisica"]
                    dados_frequencia_boletim = self.__tela_aluno.pega_dados_frequencia_boletim()
                    b1.frequencia = dados_frequencia_boletim
                    aluno.boletim = b1
                    return None
                else:
                    print("Atenção! Aluno já possui um boletim cadastrado no sistema!")
                    return None
        else:
          print("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def alterar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for student in self.__alunos:
          if student.matricula == matricula_aluno:
            aluno = student
            if aluno.boletim is not None:
                tem_boletim = True
            elif aluno.boletim is None:
                tem_boletim = False
                
            if tem_boletim == True:
                novos_dados_notas_boletim = self.__tela_aluno.pega_dados_notas_boletim()
                aluno.boletim.media_matematica = novos_dados_notas_boletim["matematica"]
                aluno.boletim.media_lingua_portuguesa = novos_dados_notas_boletim["lingua_portuguesa"]
                aluno.boletim.media_geografia = novos_dados_notas_boletim["geografia"]
                aluno.boletim.media_historia = novos_dados_notas_boletim["historia"]
                aluno.boletim.media_ciencias = novos_dados_notas_boletim["ciencias"]
                aluno.boletim.media_artes = novos_dados_notas_boletim["artes"]
                aluno.boletim.media_filosofia = novos_dados_notas_boletim["filosofia"]
                aluno.boletim.media_lingua_inglesa = novos_dados_notas_boletim["lingua_inglesa"]
                aluno.boletim.media_educacao_fisica = novos_dados_notas_boletim["educacao_fisica"]
                novos_dados_frequencia_boletim = self.__tela_aluno.pega_dados_frequencia_boletim()
                aluno.boletim.frequencia = novos_dados_frequencia_boletim
                return None
            
            elif tem_boletim == False:
                print('Atenção! Aluno ainda não tem boletim cadastrado!')
                return None
        else:
            print("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def aluno_aprovado(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for student in self.__alunos:
          if student.matricula == matricula_aluno:
            if student.boletim is None:
              print("Atenção! Boletim do aluno ainda não foi cadastrado!")
              return None
            else:
              if student.boletim.aprovado():
                print("O aluno selecionado está aprovado!")
                return None
              else:
                print("O aluno selecionado está reprovado!")
                return None
        else:
          print("Atenção! Aluno não cadastrado no sistema")

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["responsavel"], dados_aluno["serie"], dados_aluno["bolsa"], dados_aluno["mensalidade"], None)
        if len(self.__alunos) == 0:
          self.__alunos.append(aluno)
        else:
          try:
            for student in self.__alunos:
              if student.matricula == aluno.matricula:
                raise KeyError
            else:
              self.__alunos.append(aluno)
          except KeyError:
            self.__tela_aluno.mostra_mensagem("Atenção! Aluno já cadastrado no sistema!")

    def alterar_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for student in self.__alunos:
            if student.matricula == matricula_aluno:
                aluno = student
                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
                aluno.nome = novos_dados_aluno["nome"]
                aluno.matricula = novos_dados_aluno["matricula"]
                aluno.responsavel = novos_dados_aluno["responsavel"]
                aluno.serie = novos_dados_aluno["serie"]
                aluno.bolsa = novos_dados_aluno["bolsa"]
                aluno.mensalidade = novos_dados_aluno["mensalidade"]
                return None
        else:
            print("Atenção! Não existem alunos com essa matrícula cadastrados no sistema!")


    def lista_alunos(self):
        if len(self.__alunos) == 0:
            print("Atenção! Não existem alunos cadastrados no sistema!")
            return None
        else:
            for aluno in self.__alunos:
                print(f'Nome do aluno: {aluno.nome}')
                print(f'Matrícula do aluno: {aluno.matricula}')
                print(f'Responsável pelo aluno: {aluno.responsavel}')
                print(f'Série do aluno: {aluno.serie}')
                print(f'Aluno bolsista: {aluno.bolsa}')
                print(f'Mensalidade do aluno: {aluno.mensalidade}')
                if aluno.boletim is not None and isinstance(aluno.boletim, Boletim):
                    print(f'Boletim do aluno:')
                    print(f'Matemática: {aluno.boletim.media_matematica}')
                    print(f'Língua Portuguesa: {aluno.boletim.media_lingua_portuguesa}')
                    print(f'Geografia: {aluno.boletim.media_geografia}')
                    print(f'História: {aluno.boletim.media_historia}')
                    print(f'Ciências: {aluno.boletim.media_ciencias}')
                    print(f'Artes: {aluno.boletim.media_artes}')
                    print(f'Filosofia: {aluno.boletim.media_filosofia}')
                    print(f'Língua Inglesa: {aluno.boletim.media_lingua_inglesa}')
                    print(f'Educação Física: {aluno.boletim.media_educacao_fisica}')
                    print(f'Frequência anual (em %): {(aluno.boletim.frequencia / 2):.2f}')
                    print('---------------------------------------------------')
                else:
                    print('Boletim do aluno: Não cadastrado ainda')
                    print('---------------------------------------------------')

    def excluir_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()

        for aluno in self.__alunos:

          if aluno.matricula == matricula_aluno:
            self.__alunos.remove(aluno)
            break
        else:
          print("Atenção! Aluno selecionado não consta no sistema!")
  
    def achar_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for aluno in self.__alunos:
            print(f'Nome do aluno: {aluno.nome}')
            print(f'Matrícula do aluno: {aluno.matricula}')
            print(f'Responsável pelo aluno: {aluno.responsavel}')
            print(f'Série do aluno: {aluno.serie}')
            print(f'Aluno bolsista: {aluno.bolsa}')
            print(f'Mensalidade do aluno: {aluno.mensalidade}')
            if aluno.boletim is not None and isinstance(aluno.boletim, Boletim):
                print(f'Boletim do aluno:')
                print(f'Matemática: {aluno.boletim.media_matematica}')
                print(f'Língua Portuguesa: {aluno.boletim.media_lingua_portuguesa}')
                print(f'Geografia: {aluno.boletim.media_geografia}')
                print(f'História: {aluno.boletim.media_historia}')
                print(f'Ciências: {aluno.boletim.media_ciencias}')
                print(f'Artes: {aluno.boletim.media_artes}')
                print(f'Filosofia: {aluno.boletim.media_filosofia}')
                print(f'Língua Inglesa: {aluno.boletim.media_lingua_inglesa}')
                print(f'Educação Física: {aluno.boletim.media_educacao_fisica}')
                print(f'Frequência anual (em %): {(aluno.boletim.frequencia / 2):.2f}')
                return None
            else:
                print('Boletim do aluno: Não cadastrado ainda')
                return None
        else:
            print("Atenção! Não existem alunos com essa matrícula no sistema!") 

    def abre_tela(self):
          lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 5: self.cadastrar_boletim, 6: self.achar_aluno, 7: self.aluno_aprovado, 8: self.alterar_boletim, 0: self.retornar}
          continua = True
          while continua:
              lista_opcoes[self.__tela_aluno.tela_opcoes()]()
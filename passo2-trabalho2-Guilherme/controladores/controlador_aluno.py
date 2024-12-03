from entidades.aluno import Aluno
from entidades.boletim import Boletim
from telas.tela_aluno import TelaAluno
from controladores.controlador_abstrato import ControladorAbstrato
from daos.aluno_dao import AlunoDAO

class ControladorAluno(ControladorAbstrato):
  
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_aluno = TelaAluno()
        self.__aluno_DAO = AlunoDAO()
    
    @property
    def alunos_DAO(self):
        return self.__aluno_DAO

    @property
    def tela_aluno(self):
        return self.__tela_aluno

    def cadastrar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for aluno in self.__aluno_DAO.get_all():
          if aluno.matricula == matricula_aluno:
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
                    self.__tela_aluno.mostra_mensagem("Atenção! Aluno já possui um boletim cadastrado no sistema!")
                    return None
        else:
          self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def alterar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for aluno in self.__aluno_DAO.get_all():
          if aluno.matricula == matricula_aluno:
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
                self.__tela_aluno.mostra_mensagem('Atenção! Aluno ainda não tem boletim cadastrado!')
                return None
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def aluno_aprovado(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        for aluno in self.__aluno_DAO.get_all():
          if aluno.matricula == matricula_aluno:
            if aluno.boletim is None:
              self.__tela_aluno.mostra_mensagem("Atenção! Boletim do aluno ainda não foi cadastrado!")
              return None
            else:
              if aluno.boletim.aprovado():
                self.__tela_aluno.mostra_mensagem("O aluno selecionado está aprovado!")
                return None
              else:
                self.__tela_aluno.mostra_mensagem("O aluno selecionado está reprovado!")
                return None
        else:
          self.__tela_aluno.mostra_mensagem("Atenção! Aluno não cadastrado no sistema")

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["responsavel"], dados_aluno["serie"], dados_aluno["bolsa"], dados_aluno["mensalidade"], None)
        self.__aluno_DAO.add(aluno)

    def alterar_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.achar_aluno(matricula_aluno)
        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.matricula = novos_dados_aluno["matricula"]
            aluno.responsavel = novos_dados_aluno["responsavel"]
            aluno.serie = novos_dados_aluno["serie"]
            aluno.bolsa = novos_dados_aluno["bolsa"]
            aluno.mensalidade = novos_dados_aluno["mensalidade"]
            return None
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula cadastrados no sistema!")

    def lista_alunos(self):
        dados_alunos = []
        for aluno in self.__aluno_DAO.get_all():
            dados_alunos.append({"nome": aluno.nome, "matricula": aluno.matricula, "responsavel": aluno.responsavel, "serie": aluno.serie, "bolsa": aluno.bolsa, "mensalidade": aluno.mensalidade, "boletim": aluno.boletim})
        if len(dados_alunos) == 0:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos cadastrados no sistema!")
        else:
            self.__tela_aluno.mostra_aluno(dados_alunos)

    def excluir_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.achar_aluno(matricula_aluno)
        if aluno is not None:
            self.__aluno_DAO.remove(aluno)
        else:
          self.__tela_aluno.mostra_mensagem("Atenção! Aluno selecionado não consta no sistema!")
  
    def achar_aluno(self, matricula_aluno):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.matricula == matricula_aluno:
               return aluno
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula no sistema!") 

    def abre_tela(self):
          lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 5: self.cadastrar_boletim, 6: self.achar_aluno, 7: self.aluno_aprovado, 8: self.alterar_boletim, 0: self.retornar}
          continua = True
          while continua:
              lista_opcoes[self.__tela_aluno.tela_opcoes()]()

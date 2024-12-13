from entidades.aluno import Aluno
from entidades.boletim import Boletim
from telas.tela_aluno import TelaAluno
from controladores.controlador_abstrato import ControladorAbstrato
from daos.aluno_dao import AlunoDAO
from daos.turma_dao import TurmaDAO
from excecoes.entrada_invalida_exception import *


class ControladorAluno(ControladorAbstrato):
  
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_aluno = TelaAluno()
        self.__aluno_DAO = AlunoDAO()
        self.__turma_DAO = TurmaDAO()
    
    @property
    def alunos_DAO(self):
        return self.__aluno_DAO

    @property
    def tela_aluno(self):
        return self.__tela_aluno
    
    def _validar_dados_aluno(self, dados_aluno):
        """Valida os dados do aluno antes de criar/alterar"""
        if not isinstance(dados_aluno["nome"], str) or not dados_aluno["nome"].strip():
            raise CampoTextoException("Nome do aluno deve ser uma string não vazia")
        
        try:
            int(dados_aluno["matricula"])
        except ValueError:
            raise CampoNumericoException("Matrícula deve ser um número inteiro")

        if not isinstance(dados_aluno["responsavel"], str) or not dados_aluno["responsavel"].strip():
            raise CampoTextoException("Nome do responsável deve ser uma string não vazia")
        
        if not isinstance(dados_aluno["bolsa"], bool):
            raise TypeError("Bolsa deve ser um valor booleano (True/False)")
        
        try:
            float(dados_aluno["mensalidade"])
        except ValueError:
            raise CampoNumericoException("Mensalidade deve ser um número")

    def cadastrar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        
        if matricula_aluno is None:
            return None
        
        for aluno in self.__aluno_DAO.get_all():
            if str(aluno.matricula) == matricula_aluno:
                if aluno.boletim is None:
                    dados_boletim = self.__tela_aluno.pega_dados_notas_boletim()
                    if dados_boletim is None:
                        return None
                    
                    dados_frequencia_boletim = self.__tela_aluno.pega_dados_frequencia_boletim()
                    if dados_frequencia_boletim is None:
                        return None
                    
                    b1 = Boletim(0,0,0,0,0,0,0,0,0,0)
                    b1.media_matematica = float(dados_boletim["matematica"])
                    b1.media_lingua_portuguesa = float(dados_boletim["lingua_portuguesa"])
                    b1.media_geografia = float(dados_boletim["geografia"])
                    b1.media_historia = float(dados_boletim["historia"])
                    b1.media_ciencias = float(dados_boletim["ciencias"])
                    b1.media_artes = float(dados_boletim["artes"])
                    b1.media_filosofia = float(dados_boletim["filosofia"])
                    b1.media_lingua_inglesa = float(dados_boletim["lingua_inglesa"])
                    b1.media_educacao_fisica = float(dados_boletim["educacao_fisica"])
                    b1.frequencia = int(dados_frequencia_boletim)
                    
                    aluno.boletim = b1

                    self.__aluno_DAO.update(aluno)
                    
                    self.__tela_aluno.mostra_mensagem("Boletim cadastrado com sucesso!")
                    return None
                else:
                    self.__tela_aluno.mostra_mensagem("Atenção! Aluno já possui um boletim cadastrado no sistema!")
                    return None
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def alterar_boletim(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        
        if matricula_aluno is None:
            return None
        
        for aluno in self.__aluno_DAO.get_all():
            if str(aluno.matricula) == matricula_aluno:
                if aluno.boletim is not None:
                    novos_dados_notas_boletim = self.__tela_aluno.pega_dados_notas_boletim()
                    aluno.boletim.media_matematica = float(novos_dados_notas_boletim["matematica"])
                    aluno.boletim.media_lingua_portuguesa = float(novos_dados_notas_boletim["lingua_portuguesa"])
                    aluno.boletim.media_geografia = float(novos_dados_notas_boletim["geografia"])
                    aluno.boletim.media_historia = float(novos_dados_notas_boletim["historia"])
                    aluno.boletim.media_ciencias = float(novos_dados_notas_boletim["ciencias"])
                    aluno.boletim.media_artes = float(novos_dados_notas_boletim["artes"])
                    aluno.boletim.media_filosofia = float(novos_dados_notas_boletim["filosofia"])
                    aluno.boletim.media_lingua_inglesa = float(novos_dados_notas_boletim["lingua_inglesa"])
                    aluno.boletim.media_educacao_fisica = float(novos_dados_notas_boletim["educacao_fisica"])
                    novos_dados_frequencia_boletim = int(self.__tela_aluno.pega_dados_frequencia_boletim())
                    aluno.boletim.frequencia = novos_dados_frequencia_boletim
                    return None
                else:
                    self.__tela_aluno.mostra_mensagem('Atenção! Aluno ainda não tem boletim cadastrado!')
                    return None
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Não existem alunos com essa matrícula no sistema!")
  
    def aluno_aprovado(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        
        if matricula_aluno is None:
            return None
        
        for aluno in self.__aluno_DAO.get_all():
            if str(aluno.matricula) == matricula_aluno:
                if aluno.boletim is None:
                    self.__tela_aluno.mostra_mensagem("Atenção! Boletim do aluno ainda não foi cadastrado!")
                    return None
                else:
                    if aluno.boletim.aprovado():
                        self.__tela_aluno.mostra_mensagem("O aluno selecionado está aprovado!")
                    else:
                        self.__tela_aluno.mostra_mensagem("O aluno selecionado está reprovado!")
                    return None
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Aluno não cadastrado no sistema")

    def incluir_aluno(self):
        try:
            dados_aluno = self.__tela_aluno.pega_dados_aluno()
            
            dados_aluno["bolsa"] = dados_aluno["bolsa"].lower() in ['true', 'sim', '1']
            
            self._validar_dados_aluno(dados_aluno)
            
            if dados_aluno is not None:
                aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["responsavel"], dados_aluno["serie"], dados_aluno["bolsa"], dados_aluno["mensalidade"], None)
                
                turma = self.__turma_DAO.get(f"{dados_aluno['serie']}° Ano")
                if turma:
                    turma.adicionar_aluno(aluno)
                
                self.__aluno_DAO.add(aluno)
                
        except (CampoTextoException, CampoNumericoException, TypeError) as e:
            self.__tela_aluno.mostra_mensagem(str(e))

    def alterar_aluno(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        
        if matricula_aluno is None:
            return None
        
        aluno = self.achar_aluno(matricula_aluno)
        if aluno is not None:
            try:
                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
                
                novos_dados_aluno["bolsa"] = novos_dados_aluno["bolsa"].lower() in ['true', 'sim', '1']
                
                self._validar_dados_aluno(novos_dados_aluno)
                
                aluno.nome = novos_dados_aluno["nome"]
                aluno.matricula = int(novos_dados_aluno["matricula"])
                aluno.responsavel = novos_dados_aluno["responsavel"]
                aluno.serie = novos_dados_aluno["serie"]
                aluno.bolsa = novos_dados_aluno["bolsa"]
                aluno.mensalidade = float(novos_dados_aluno["mensalidade"])
                return None
            except (CampoTextoException, CampoNumericoException, TypeError) as e:
                self.__tela_aluno.mostra_mensagem(str(e))
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
        if matricula_aluno is None:
            return None
        aluno = self.achar_aluno(matricula_aluno)
        if aluno is not None:
            self.__aluno_DAO.remove(int(matricula_aluno))
        else:
            self.__tela_aluno.mostra_mensagem("Atenção! Aluno selecionado não consta no sistema!")
  
    def achar_aluno(self, matricula_aluno):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.matricula == int(matricula_aluno):
               return aluno
        return None
    
    def mostrar_aluno_por_matricula(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        if matricula_aluno is not None:
            aluno = self.achar_aluno(matricula_aluno)
            if aluno is not None:
                dados_alunos = [{
                    "nome": aluno.nome, 
                    "matricula": aluno.matricula, 
                    "responsavel": aluno.responsavel, 
                    "serie": aluno.serie, 
                    "bolsa": aluno.bolsa, 
                    "mensalidade": aluno.mensalidade, 
                    "boletim": aluno.boletim
                }]
                self.__tela_aluno.mostra_aluno(dados_alunos)
            else:
                self.__tela_aluno.mostra_mensagem("Atenção! Aluno não encontrado no sistema!")

    def abre_tela(self):
          lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 5: self.cadastrar_boletim, 6: self.mostrar_aluno_por_matricula, 7: self.aluno_aprovado, 8: self.alterar_boletim, 0: self.retornar}
          continua = True
          
          while continua:
              lista_opcoes[self.__tela_aluno.tela_opcoes()]()

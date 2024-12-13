class Turma():
    def __init__(self, nome):
        self.nome = nome
        self.__alunos = []
        self.__professores = []

    @property
    def alunos(self):
        return self.__alunos.copy()
    
    @property
    def professores(self):
        return self.__professores.copy()

    def adicionar_aluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)
    
    def adicionar_professor(self, professor):
        if professor not in self.__professores:
            self.__professores.append(professor)
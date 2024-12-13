class Financas():
    def __init__(self, despesas_agua: float, despesas_luz: float, despesas_internet: float, despesas_estrutura: float):
        self.__despesas_agua = despesas_agua
        self.__despesas_luz = despesas_luz
        self.__despesas_internet = despesas_internet
        self.__despesas_estrutura = despesas_estrutura
        self.__id = None


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def despesas_agua(self):
        return self.__despesas_agua
    
    @despesas_agua.setter
    def despesas_agua(self, despesas_agua):
        self.__despesas_agua = despesas_agua
    
    @property
    def despesas_luz(self):
        return self.__despesas_luz
    
    @despesas_luz.setter
    def despesas_luz(self, despesas_luz):
        self.__despesas_luz = despesas_luz
    
    @property
    def despesas_internet(self):
        return self.__despesas_internet
    
    @despesas_internet.setter
    def despesas_internet(self, despesas_internet):
        self.__despesas_internet = despesas_internet
    
    @property
    def despesas_estrutura(self):
        return self.__despesas_estrutura
    
    @despesas_estrutura.setter
    def despesas_estrutura(self, despesas_estrutura):
        self.__despesas_estrutura = despesas_estrutura

    def despesas_basicas(self):
        """Calcula despesas básicas (água, luz, internet, estrutura)"""
        despesa = 0
        despesa += float(self.__despesas_agua)
        despesa += float(self.__despesas_luz)
        despesa += float(self.__despesas_internet)
        despesa += float(self.__despesas_estrutura)
        return despesa

    def despesa_colaboradores(self, professores, funcionarios):
        """Calcula despesas com salários de professores e funcionários"""
        despesa = 0
        for professor in professores:
            despesa += professor.salario
        for funcionario in funcionarios:
            despesa += funcionario.salario
        return despesa

    def despesa_escola(self, professores, funcionarios):
        """Calcula despesas totais da escola (básicas + colaboradores)"""
        return self.despesas_basicas() + self.despesa_colaboradores(professores, funcionarios)

    def faturamento_escola(self, alunos):
        """Calcula faturamento total com mensalidades dos alunos"""
        return sum(aluno.mensalidade for aluno in alunos)

    def lucro_escola(self, alunos, professores, funcionarios):
        """Calcula lucro da escola (faturamento - despesas totais)"""
        faturamento = self.faturamento_escola(alunos)
        despesas = self.despesa_escola(professores, funcionarios)
        return faturamento - despesas

    def porcentagem_bolsistas(self, alunos):
        """Calcula porcentagem de alunos bolsistas"""
        if not alunos:
            return 0
        
        bolsistas = sum(1 for aluno in alunos if aluno.bolsa == 'Bolsista')
        return (bolsistas / len(alunos)) * 100
from tela_abstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):
    
    def __init__(self):
        pass
    
    def le_nota(self, mensagem=" "):
        while True:
            nota_lida = input(mensagem)
            try:
                valor_float = float(nota_lida)
                if valor_float < 0 or valor_float > 10:
                    raise ValueError
                return valor_float
            except ValueError:
                print("Valor incorreto! Insira um valor de 0 a 10")

    def le_frequencia(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos or (valor_int < 0 and valor_int > 200):
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto! Digite um valor de 0 a 200")

    def tela_opcoes(self):
        print("-------- ALUNOS ----------")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("5 - Cadastrar boletim de um aluno")
        print("6 - Mostrar aluno por matricula")
        print("7 - Verificar se o aluno está aprovado")
        print("8 - Alterar boletim de um aluno")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5,6,7,8] )
        return opcao
  
    def pega_dados_aluno(self):
        print("-------- DADOS ALUNO ----------")
        nome = self.le_string("Nome do aluno: ")
        matricula = self.le_num_inteiro("Matrícula do aluno: ")
        responsavel = self.le_string("Responsável pelo aluno: ")
        serie = self.le_num_inteiro("Série do aluno: ", [1,2,3,4,5,6,7,8])
        mensalidade = self.le_num_inteiro("Mensalidade do aluno: ")
        conversor = self.le_num_inteiro("Aluno é bolsista? (1 para bolsista) (2 para não bolsista)", [1,2])
        bolsa = 'Bolsista' if conversor == 1 else 'Não bolsista'
        return {"nome": nome, "matricula": matricula, "responsavel": responsavel, "serie": serie, "mensalidade": mensalidade, "bolsa": bolsa}

    def seleciona_aluno(self):
        matricula = self.le_num_inteiro("Matrícula do aluno que deseja selecionar: ")
        return matricula
  
    def pega_dados_notas_boletim(self):
        semestre_mtm1 = self.le_nota("Nota do primeiro semestre de matemática do aluno: ")
        semestre_mtm2 = self.le_nota("Nota do segundo semestre de matemática do aluno: ")
        semestre_lp1 = self.le_nota("Nota do primeiro semestre de língua portuguesa do aluno: ")
        semestre_lp2 = self.le_nota("Nota do segundo semestre de língua portuguesa do aluno: ")
        semestre_geo1 = self.le_nota("Nota do primeiro semestre de geografia do aluno: ")
        semestre_geo2 = self.le_nota("Nota do segundo semestre de geografia do aluno: ")
        semestre_hst1 = self.le_nota("Nota do primeiro semestre de história do aluno: ")
        semestre_hst2 = self.le_nota("Nota do segundo semestre de história do aluno: ")
        semestre_cie1 = self.le_nota("Nota do primeiro semestre de ciências do aluno: ")
        semestre_cie2 = self.le_nota("Nota do segundo semestre de ciências do aluno: ")
        semestre_art1 = self.le_nota("Nota do primeiro semestre de artes do aluno: ")
        semestre_art2 = self.le_nota("Nota do segundo semestre de artes do aluno: ")
        semestre_fil1 = self.le_nota("Nota do primeiro semestre de filosofia do aluno: ")
        semestre_fil2 = self.le_nota("Nota do segundo semestre de filosofia do aluno: ")
        semestre_ing1 = self.le_nota("Nota do primeiro semestre de língua inglesa do aluno: ")
        semestre_ing2 = self.le_nota("Nota do segundo semestre de língua inglesa do aluno: ")
        semestre_edf1 = self.le_nota("Nota do primeiro semestre de educação física do aluno: ")
        semestre_edf2 = self.le_nota("Nota do segundo semestre de educação física do aluno: ")
        media_notas = {"matematica": (semestre_mtm1 + semestre_mtm2) / 2, "lingua_portuguesa": (semestre_lp1 + semestre_lp2) / 2, "geografia": (semestre_geo1 + semestre_geo2) / 2, "historia": (semestre_hst1 + semestre_hst2) / 2, "ciencias": (semestre_cie1 + semestre_cie2) / 2, "artes": (semestre_art1 + semestre_art2) / 2, "filosofia": (semestre_fil1 + semestre_fil2) / 2, "lingua_inglesa": (semestre_ing1 + semestre_ing2) / 2, "educacao_fisica": (semestre_edf1 + semestre_edf2) / 2}
        return media_notas
    
    def pega_dados_frequencia_boletim(self):
        frequencia = self.le_num_inteiro("Frequência anual do aluno durante o ano letivo (em dias presentes): ")
        return frequencia
class Boletim():

    def __init__(self, media_matematica: float, media_lingua_portuguesa: float, media_geografia: float, media_historia: float, media_ciencias: float, media_artes: float, media_filosofia: float, media_lingua_inglesa: float, media_educacao_fisica: float, frequencia: int):
        
        self.__media_matematica = media_matematica
        self.__media_lingua_portuguesa = media_lingua_portuguesa
        self.__media_geografia = media_geografia
        self.__media_historia = media_historia
        self.__media_ciencias = media_ciencias
        self.__media_artes = media_artes
        self.__media_filosofia = media_filosofia
        self.__media_lingua_inglesa = media_lingua_inglesa
        self.__media_educacao_fisica = media_educacao_fisica
        self.__frequencia = frequencia

    @property
    def media_matematica(self):
            return self.__media_matematica

    @media_matematica.setter
    def media_matematica(self, media_matematica):
            self.__media_matematica = media_matematica
    
    @property
    def media_lingua_portuguesa(self):
            return self.__media_lingua_portuguesa

    @media_lingua_portuguesa.setter
    def media_lingua_portuguesa(self, media_lingua_portuguesa):
            self.__media_lingua_portuguesa = media_lingua_portuguesa
    
    @property
    def media_geografia(self):
            return self.__media_geografia

    @media_geografia.setter
    def media_geografia(self, media_geografia):
            self.__media_geografia = media_geografia

    @property
    def media_historia(self):
            return self.__media_historia

    @media_historia.setter
    def media_historia(self, media_historia):
            self.__media_historia = media_historia
    
    @property
    def media_ciencias(self):
            return self.__media_ciencias

    @media_ciencias.setter
    def media_ciencias(self, media_ciencias):
            self.__media_ciencias = media_ciencias
    
    @property
    def media_artes(self):
            return self.__media_artes

    @media_artes.setter
    def media_artes(self, media_artes):
            self.__media_artes = media_artes

    @property
    def media_filosofia(self):
            return self.__media_filosofia

    @media_filosofia.setter
    def media_filosofia(self, media_filosofia):
            self.__media_filosofia = media_filosofia
    
    @property
    def media_lingua_inglesa(self):
            return self.__media_lingua_inglesa

    @media_lingua_inglesa.setter
    def media_lingua_inglesa(self, media_lingua_inglesa):
            self.__media_lingua_inglesa = media_lingua_inglesa
    
    @property
    def media_educacao_fisica(self):
            return self.__media_educacao_fisica

    @media_educacao_fisica.setter
    def media_educacao_fisica(self, media_educacao_fisica):
            self.__media_educacao_fisica = media_educacao_fisica

    @property
    def frequencia(self):
            return self.__frequencia

    @frequencia.setter
    def frequencia(self, frequencia):
            self.__frequencia = frequencia

    def aprovado(self):
        if self.__frequencia / 200 < 0.75:
               return False
        else:
            notas_finais = []
            notas_finais.append(self.__media_matematica)
            notas_finais.append(self.__media_lingua_portuguesa)
            notas_finais.append(self.__media_geografia)
            notas_finais.append(self.__media_historia)
            notas_finais.append(self.__media_ciencias)
            notas_finais.append(self.__media_artes)
            notas_finais.append(self.__media_filosofia)
            notas_finais.append(self.__media_lingua_inglesa)
            notas_finais.append(self.__media_educacao_fisica)
            for nota in notas_finais:
                if nota < 7:
                       return False
            return True

from beartype import beartype
import re
import logging

class UltimasNoticias():
    @beartype
    def __init__(self, conteudo: dict) -> None:
        """Transforma um dicionário com informações de uma notícia em objeto

        Args:
            conteudo (dict): conteúdo que irá gerar a notícia
        """
        self.titulo = self.recebe_titulo(conteudo["titulo"])
        self.url = self.recebe_url(conteudo["url"])
        self.chamada = conteudo["chamada"]
        self.data = conteudo["data"]
        self.imagem_url = self.recebe_imagem_url(conteudo["url_imagem"])
        self.conteudo = None

    @beartype
    def recebe_titulo(self, titulo: str) -> str:
        """Verifica se o primeiro caractere do título é em maiúscula

        Args:
            titulo (str): Título recebido

        Raises:
            errors.Titulo_nao_capitalizado: Erro caso o título seja capturado incorretamente

        Returns:
            str: Título da notícia
        """
        # evita que suba erro quando título começa com aspas ou pontuação
        titulo_limpo = re.sub('[^A-Za-z]+', '', titulo)
        if titulo_limpo[0].isupper():
            return titulo
        else:
            raise errors.Titulo_nao_capitalizado("Título não começa com letra maiúscula: %s", titulo)

    def recebe_url(self, url: str) -> str:
        """Verifica se a URL possui 'http' no início

        Args:
            url (str): url referente a notícia

        Raises:
            errors.Url_sem_http: O url não possui http no começo

        Returns:
            str: url retornado no início, confirmando que está correto
        """
        if url[0:4] == "http":
            return url
        else:
            raise errors.Url_sem_http("Url recebido não possui 'http' no começo, inválido: %s", url)

    def recebe_imagem_url(self, imagem_url: str) -> str:
        """Verifica se URL da imagem possui http no começo e formato de extensão de imagem

        Args:
            imagem_url (str): endereço que aponta para imagem de notícia

        Raises:
            errors.Imagem_url_sem_extensao: URL incompatível com formato de imagem

        Returns:
            str: imagem_url
        """
        imagem_url = self.recebe_url(imagem_url)
        ocorrencias_formato = re.findall(r'.jpg|.png|.jpeg|.gif|.jfif', imagem_url, re.IGNORECASE)
        if any(ocorrencias_formato): # url da imagem possui uma das extensões suportadas
            return imagem_url
        else:
            raise errors.Imagem_url_sem_extensao("URL da imagem não possui extensão suportada: %s", imagem_url)


class errors():
    class Titulo_nao_capitalizado(Exception):
        pass
    class Url_sem_http(Exception):
        pass
    class Imagem_url_sem_extensao(Exception):
        pass

if __name__ == "__main__":
    dicionario = {"titulo": "Auashdiausdh", "url": "http://aisudhiads", "chamada": "aiushdasid", "data": "aisuhdiuads", "url_imagem": "http://ais.JPGuhdiaus"}
    ultimas_noticias = UltimasNoticias(dicionario)
    print(ultimas_noticias.imagem_url)
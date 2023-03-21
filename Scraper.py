from beartype import beartype
from bs4 import BeautifulSoup
from conf.settings import URL_LIBERAL_ULTIMAS_NOTICIAS, URL_LIBERAL_BASE
import requests
import logging
from Noticia import UltimasNoticias
logging.basicConfig(level=logging.DEBUG)

class Scraper():
    @beartype
    def __init__(self, url: str) -> None:
        """Obtém e extrai informações da página de notícias O Liberal

        Args:
            url (str): Endereço da página a ser extraída
        """
        self._url = url
        logging.debug("url recebido: %s", self._url)
        _pagina_ultimas_noticias = self.obter_pagina(self._url)
        self.lista_ultimas_noticias = self.parse_pagina_ultimas_noticias(_pagina_ultimas_noticias)
        for x in self.lista_ultimas_noticias:
            conteudo = self.parse_conteudo_noticia(x.url)
            # substitui o url das imagens para endereço completo com domínio base do Liberal
            x.conteudo = conteudo.replace('src="/image/', f'src="{URL_LIBERAL_BASE}/image/')
            
    
    @beartype
    def obter_pagina(self, url: str) -> str:
        """Recebe o HTML bruto da página

        Args:
            url (str): URL a ser tratado

        Raises:
            errors.URL_invalido: URL não possui "http"
            errors.URL_invalido: Falha de conexão

        Returns:
            str: html completo da págin
        """
        try:
            pagina_completa = requests.get(url, verify=False)
            
            if pagina_completa.status_code == 200:
                logging.debug("Status  200, retornando texto da página recebida")
                return pagina_completa.text
            else:
                logging.error("Código de status: %s", pagina_completa.status_code)
        except requests.exceptions.MissingSchema:
            raise errors.URL_invalido("URL inválido, verifique arquivo .env")
        except requests.exceptions.ConnectionError:
            raise errors.FalhaConexao("Conexão com o URL malsucedida, verifique arquivo .env")

    @beartype
    def parse_pagina_ultimas_noticias(self, pagina_completa: str) -> list:
        """Interpreta o HTML bruto para localizar informações de cada notícia na página

        Args:
            pagina_completa (str): HTML bruto da página

        Returns:
            list: Lista de objetos UltimaNoticia
        """
        soup =  BeautifulSoup(pagina_completa, "html.parser")
        soup_container_ultimas_noticias = soup.find_all(
            "div", class_="teaser-featured estilo5 has-image"
            )
        logging.debug("Tamanho do elemento container %i", len(
            soup_container_ultimas_noticias
            ))
        lista_noticias = []
        for x in soup_container_ultimas_noticias:
            imagem_url = x.find("img")["src"]
            titulo = x.find("p", class_="titulo").text
            chamada = x.find("p", class_="chamada").text
            data = x.find("p", class_="datetime").text
            url = x.find("p", class_="titulo").a["href"]
            conteudo = self.parse_conteudo_noticia(str(URL_LIBERAL_BASE + url))
            dict_noticia = {"titulo": titulo, 
                            "chamada": chamada, 
                            "data": data, 
                            "url": str(URL_LIBERAL_BASE + url), 
                            "url_imagem": str(URL_LIBERAL_BASE + imagem_url),
                            "conteudo": conteudo}
            
            noticia = UltimasNoticias(dict_noticia)
            lista_noticias.append(noticia)
        return lista_noticias

    def parse_conteudo_noticia(self, url_noticia: str) -> str:
        """Extrai o conteúdo em forma de HTML de uma notícia

        Args:
            url_noticia (str): endereço direto da notícia

        Returns:
            str: HTML bruto com conteúdo de uma notícia
        """
        pagina_conteudo = self.obter_pagina(url_noticia)
        soup =  BeautifulSoup(pagina_conteudo, "html.parser")
        container_conteudo = soup.find_all("div", class_="textbody article__body")
        conteudo_bruto = container_conteudo[0].find_all("p")
        conteudo = str()
        for x in conteudo_bruto:
            for y in x.contents:
                conteudo = conteudo + str(y)
        return conteudo
  
            
                
    
class errors():
    class URL_invalido(Exception):
        pass

    class FalhaConexao(Exception):
        pass

if __name__ == "__main__":
    
    scraper  = Scraper(URL_LIBERAL_ULTIMAS_NOTICIAS)
    
    #url = "https://www.oliberal.com/ananindeua/cirio-solidario-imagem-de-nossa-senhora-visita-devotos-durante-acao-social-em-ananindeua-1.658519"
    
    #conteudo = scraper.parse_conteudo_noticia(url)
    #print(conteudo)
    #pagina_completa = scraper.obter_pagina()
    #lista_noticias = scraper.parse_pagina_ultimas_noticias(pagina_completa)
    #for x in scraper.lista_ultimas_noticias:
    #noticia = scraper.lista_ultimas_noticias[0]
    
    
    #for x in container_conteudo:
    #    print(x.find_all("p"))
        #print(x)
        #soup_container_conteudo = soup.find_all(
        #    "div", class_="textbody article__body "
        #    )
        #print(soup_container_conteudo)
        #for y in soup_container_conteudo:
            #print(y.find("p", class_="paragrafo").text)
    #print("titulo: ", noticia.titulo)
    #print("chamada: ", noticia.chamada)
    #print("url: ", noticia.url)
    #rint("conteudo: ", noticia.conteudo)
    

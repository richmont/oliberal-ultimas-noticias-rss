from beartype import beartype
from bs4 import BeautifulSoup
from conf.settings import URL_LIBERAL_ULTIMAS_NOTICIAS, URL_LIBERAL_BASE
import requests
import logging
from Noticia import Noticia
logging.basicConfig(level=logging.DEBUG)

class Scraper():
    @beartype
    def __init__(self, url: str) -> None:
        self.url = url
        logging.debug("url recebido: %s", self.url)
    
    @beartype
    def obter_pagina(self) -> str:
        try:
            pagina_completa = requests.get(self.url, verify=False)
            
            if pagina_completa.status_code == 200:
                logging.debug("Status  200, retornando texto da página recebida")
                return pagina_completa.text
            else:
                logging.error("Código de status: %s", pagina_completa.status_code)
        except requests.exceptions.MissingSchema:
            raise errors.URL_invalido("URL inválido, verifique arquivo .env")
        except requests.exceptions.ConnectionError:
            raise errors.URL_invalido("URL inválido, verifique arquivo .env")

    @beartype
    def parse_pagina(self, pagina_completa: str) -> list:
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
            dict_noticia = {"titulo": titulo, 
                            "chamada": chamada, 
                            "data": data, 
                            "url": str(URL_LIBERAL_BASE + url), 
                            "url_imagem": str(URL_LIBERAL_BASE + imagem_url)}
            noticia = Noticia(dict_noticia)
            lista_noticias.append(noticia)
        return lista_noticias


class errors():
    class URL_invalido(Exception):
        pass

if __name__ == "__main__":
    
    scraper  = Scraper(URL_LIBERAL_ULTIMAS_NOTICIAS)
    pagina_completa = scraper.obter_pagina()
    lista_noticias = scraper.parse_pagina(pagina_completa)
    for x in lista_noticias:
        print("titulo: ", x.titulo)
        print("chamada: ", x.chamada)
        print("url: ", x.url)
    

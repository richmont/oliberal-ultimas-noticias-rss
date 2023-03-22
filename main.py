from Scraper import Scraper
from RSS import RSS
from conf.settings import URL_LIBERAL_ULTIMAS_NOTICIAS, URL_LIBERAL_BASE, DESCRICAO, TITULO, IDIOMA


if __name__ == "__main__":
    scraper  = Scraper(URL_LIBERAL_ULTIMAS_NOTICIAS)
    dict_channel = {"titulo": TITULO, "link": URL_LIBERAL_BASE, "descricao": DESCRICAO, "idioma": IDIOMA}
    rss = RSS(dict_channel)
    for x in scraper.lista_ultimas_noticias:
        rss.adicionar_item(x)
    rss.gravar_xml("docs/rss.xml")
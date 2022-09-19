from Scraper import Scraper
from RSS import RSS
from conf.settings import URL_LIBERAL_ULTIMAS_NOTICIAS, URL_LIBERAL_BASE, DESCRICAO, TITULO, IDIOMA


if __name__ == "__main__":
    scraper  = Scraper(URL_LIBERAL_ULTIMAS_NOTICIAS)
    pagina_completa = scraper.obter_pagina()
    lista_noticias = scraper.parse_pagina(pagina_completa)
    dict_channel = {"titulo": TITULO, "link": URL_LIBERAL_BASE, "descricao": DESCRICAO, "idioma": IDIOMA}
    rss = RSS(dict_channel)
    for x in lista_noticias:
        rss.adicionar_item(x)
    rss.gravar_xml("rss.xml")
from lxml import etree
from beartype import beartype
from Noticia import UltimasNoticias

class RSS():
    @beartype
    def __init__(self, dict_channel: dict) -> None:
        """
        Gerador de documento XML a partir de notícias
        Parâmetro: dict_channel (dict)
        Elementos do dicionário:
            titulo
            descricao
            link
            idioma
        """
        self.dict_channel = dict_channel
        self.tag_base_rss = etree.Element('rss',version="2.0")        
        self.documento = etree.ElementTree(self.tag_base_rss)        
        self.channel_tag = self.construir_channel()

    @beartype
    def construir_channel(self) -> etree._Element:
        """
        Constrói a tag channel, serve de base para tags item\n
        Contém informações do canal de notícias\n
        Preenchido com dados do dict_channel\n

        Retorna:\n
            channel_tag (etree._Element)\n
        """
        channel_tag = etree.SubElement(self.tag_base_rss, "channel")

        titulo = etree.SubElement(channel_tag, "title")
        link = etree.SubElement(channel_tag, "link")
        descricao = etree.SubElement(channel_tag, "description")
        idioma = etree.SubElement(channel_tag, "language")

        titulo.text = self.dict_channel["titulo"]
        link.text = self.dict_channel["link"]
        descricao.text = self.dict_channel["descricao"]
        idioma.text = self.dict_channel["idioma"]

        return channel_tag
    
    @beartype
    def adicionar_item(self, ultimas_noticias: UltimasNoticias) -> etree._Element:
        """
        Adiciona um elemento item com notícia na tag channel de base
        Parâmetro: dict_item (dict)\n
        Elementos do dicionário:\n
            titulo\n
            descricao\n
            link\n
            data
        """
        item = etree.SubElement(self.channel_tag, "item")

        titulo = etree.SubElement(item, "title")
        link = etree.SubElement(item, "link")
        descricao = etree.SubElement(item, "description")
        data = etree.SubElement(item, "pubDate")

        titulo.text = ultimas_noticias.titulo
        link.text = ultimas_noticias.url
        descricao.text = str(f"<![CDATA[{ultimas_noticias.chamada}]]>")
        data.text = ultimas_noticias.data
        return item
    
    @beartype
    def gravar_xml(self, nome_arquivo):
        self.documento.write(nome_arquivo, encoding='utf-8', xml_declaration=True, pretty_print=True)



if __name__ == "__main__":
    dict_channel = {"titulo": "O Liberal", "link": "https://www.oliberal.com", "descricao": "Site O Liberal", "idioma": "pt_BR"}
    dict_item = {"titulo": "Igreja Católica chegou a proibir o Sairé por quase meio século", \
        "descricao": "Leia essa e outras histórias na coluna do Padre Sidney Augusto Canto",\
            "link": "https://www.oliberal.com/castanhal/igreja-catolica-chegou-a-proibir-o-saire-por-quase-meio-seculo-1.589257",\
                "data": "19.09.22 18h16"}
    rss = RSS(dict_channel)
    rss.adicionar_item(dict_item)
    rss.adicionar_item(dict_item)
    rss.adicionar_item(dict_item)
    #print(etree.tostring(rss.tag_base_rss, pretty_print=True, encoding='utf-8', xml_declaration=True))
    rss.gravar_xml("rss.xml")

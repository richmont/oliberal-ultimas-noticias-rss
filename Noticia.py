class Noticia():
    def __init__(self, conteudo) -> None:
        
        self.titulo = conteudo["titulo"]
        self.url = conteudo["url"]
        self.chamada = conteudo["chamada"]
        self.data = conteudo["data"]
        self.imagem_url = conteudo["url_imagem"]


if __name__ == "__main__":
    dicionario = {"titulo": "iuashdiausdh", "url": "aisudhiads", "chamada": "aiushdasid","data": "aisuhdiuads", "url_imagem": "aisuhdiaus"}
    noticia = Noticia(dicionario)
    print(noticia.titulo)
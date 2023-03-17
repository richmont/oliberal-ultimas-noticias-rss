from Noticia import UltimasNoticias, errors
import pytest

class Test_noticia_correta():
    def dict_noticia_ok(self):
        dicionario_ok = {
            "titulo": "Lorem ipsum",
            "url": "http://aisudhiads",
            "chamada": "asdasdad",
            "data": "asdadads",
            "url_imagem": "http://asduihasd.jpg"
        }
        return dicionario_ok

    def test_noticia_ok(self):
        noticia = UltimasNoticias(self.dict_noticia_ok())

class Test_noticia_incorreta():
    def noticia_titulo_minusculo(self):
        dicionario_titulo_minusculo = {
            "titulo": "lorem ipsum",
            "url": "http://aisudhiads",
            "chamada": "asdasdad",
            "data": "asdadads",
            "url_imagem": "http://asduihasd.jpg"
        }
        return dicionario_titulo_minusculo

    def test_noticia_titulo_minusculo(self):
        try:
            noticia = UltimasNoticias(self.noticia_titulo_minusculo())
        except errors.Titulo_nao_capitalizado:
            assert True

    def noticia_url_sem_http(self):
        dicionario_url_sem_http = {
            "titulo": "Lorem ipsum",
            "url": "aisudhiads",
            "chamada": "asdasdad",
            "data": "asdadads",
            "url_imagem": "http://asduihasd.jpg"
        }
        return dicionario_url_sem_http

    def test_noticia_url_sem_http(self):
        try:
            noticia = UltimasNoticias(self.noticia_url_sem_http())
        except errors.Url_sem_http:
            assert True
    
    def noticia_url_imagem_extensao_errada(self):
        dicionario_url_imagem_extensao_errada = {
            "titulo": "Lorem ipsum",
            "url": "http://aisudhiads",
            "chamada": "asdasdad",
            "data": "asdadads",
            "url_imagem": "http://asduihasd"
        }
        return dicionario_url_imagem_extensao_errada

    def test_noticia_url_imagem_extensao_errada(self):
        try:
            noticia = UltimasNoticias(self.noticia_url_imagem_extensao_errada())
        except errors.Imagem_url_sem_extensao:
            assert True
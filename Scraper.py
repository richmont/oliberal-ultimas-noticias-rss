from bs4 import BeautifulSoup
import asyncio
import time
from aiohttp import ClientSession, TCPConnector
import platform

class Requisicao():
    def __init__(self, *lista_urls) -> None:
        loop = asyncio.new_event_loop()
        self.session = None
        self.lista_urls = list(*lista_urls)
        self.resultado = loop.run_until_complete(self.enfileirar_tarefas())
        self.session.connector.close()
        

    async def coletar_url(self, url, session):
        resposta = await session.request(method='GET', url=str(url))
        r = resposta
        return r

    async def enfileirar_tarefas(self):
        lista_resultado = []
        self.session = ClientSession()
        for x in self.lista_urls:
            resultado = await self.coletar_url(x, self.session)
            lista_resultado.append(resultado)
        return lista_resultado

class Homepage():
    pass

class Noticia():
    pass

if __name__ == "__main__":
    lista = []
    for x in range(1,10):
        lista.append(str(f"http://httpbin.org/get?valor={x}/"))
    req = Requisicao(lista)
    print(req.resultado)
    """
    start_time = time.time()
    async def main():
        async with ClientSession() as session:
            for number in range(1, 10):
                pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
                async with session.get(pokemon_url) as resp:
                    pokemon = await resp.json()
                    print(pokemon['name'])
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
    """
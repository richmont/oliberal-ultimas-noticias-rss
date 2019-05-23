# https://stackoverflow.com/questions/2833185/write-xml-file-using-lxml-library-in-python
# https://pox.globo.com/rss/g1/brasil/
base_url = 'https://www.oliberal.com'
noticia = {'author': 'Redação Integrada',
 'data_pub': '21.05.19 21h48',
 'imagem_url': '/image/contentid/policy:1.143167:1558485950/Internacional-Treino.jpg?f=2x1&w=200&$p$f$w=4fc2bcc',
 'img_sub': 'Técnico Odair Hellmann comandou mais um treino nesta terça-feira '
            'para a partida contra o Paysandu  (Ricardo Duarte/ SCI)',
 'link': 'https://www.oliberal.com/esportes/futebol/internacional-ter%C3%A1-apenas-uma-mudan%C3%A7a-para-enfrentar-o-paysandu-pela-copa-do-brasil-1.143160',
 'texto': 'O Internacional realizou na terça-feira mais um treino de '
          'preparação para o jogo de ida das oitavas da Copa do Brasil contra '
          'o Paysandu. A partida será às 20 horas, no Estádio Beira-Rio.\xa0'
          '.\xa0O técnico\xa0Odair Hellmann comandou um\xa0trabalho técnico em '
          'campo reduzido apenas com os reservas no gramado do Beira-Rio. Os '
          'titulares realizaram um trabalho físico na beira do campo.Mas para '
          'enfrentar o Paysandu, o Internacional deve ter apenas uma mudança '
          'no time que venceu o CSA-AL pelo Campeonato Brasileiro. O zagueiro '
          'Rodrigo Moledo,\xa0que ficará por três semanas sem jogar após '
          'sofrer\xa0lesão muscular na coxa direita, está de fora da partida. '
          'Emerson Santos será a dupla de zaga do\xa0Víctor Cuesta.\xa0Já o '
          'volante Rodrigo Dourado\xa0segue no departamento médico se '
          'recuperando da cirurgia no joelho esquerdo. Rodrigo Lindosos '
          'seguirá na vaga dentro do time titular.O Colorado deve enfrentar o '
          'Paysandu com Marcelo Lomba; Zeca, Emerson Santos, Victor Cuesta e '
          'Iago; Rodrigo Lindoso, Edenílson, Nonato e D´Alessandro; Nico López '
          'e Paolo Guerrero.O Internacional faz a\xa0última atividade nesta '
          'quarta-feira, às 16 horas, com os portões fechados.\xa0O jogo de '
          'ida das oitavas da Copa do Brasil entre Internacional e Paysandu '
          'vai ter transmissão no Lance a Lance de .\xa0',
 'title': 'Internacional terá apenas uma mudança para enfrentar o Paysandu '
          'pela Copa do Brasil '}



from lxml import etree as ET
# definir as tags XML
root = ET.Element('rss',version="2.0" )

channel = ET.SubElement(root,'channel')
title = ET.SubElement(channel,'title')
link = ET.SubElement(channel,'link')
description = ET.SubElement(channel,'description')
language = ET.SubElement(channel,'language')
link = ET.SubElement(channel,'link')
atom = ET.SubElement(channel,'atom', href='https://www.oliberal.com', type='application/rss+xml')

title.text = 'O Liberal'
link.text = base_url
description.text = 'O Liberal é um jornal brasileiro que circula em Belém e maior parte do Pará desde o ano de 1946'
language.text = 'pt-BR'


# image
image = ET.SubElement(channel,'image')
url = ET.SubElement(image,'title')
title = ET.SubElement(image,'title')
link = ET.SubElement(image,'link')
width = ET.SubElement(image,'width')
heigh = ET.SubElement(image,'heigh')

url.text = 'https://www.oliberal.com/img/ol-logo.png'
title.text = 'O Liberal'
link = base_url
width.text = '144'
heigh.text = '144'


# template da notícia em si, item
item = ET.SubElement(channel,'item')
title = ET.SubElement(item,'title')
link = ET.SubElement(item,'link')
description = ET.SubElement(item,'description')
media = ET.SubElement(item,'media')
#category = ET.SubElement(item,'category')
pubDate = ET.SubElement(item,'pubDate')

# preencher
title.text = noticia['title']
link.text = noticia['link']
description.text = '<img src="'+  base_url + noticia['imagem_url']  + '" /><br />' + noticia['texto']
pubDate.text = noticia['data_pub']

tree = ET.ElementTree(root)
tree.write('teste.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")

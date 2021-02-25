#!python3
#Multi_clipboard_automatic.py
"""Um programa que armazena varias frases"""

"""Vocé quer ser capaz de rodar este programa com uma linha de comando de argumento
que é uma frase chave - por exemplo, 'condordo' ou 'ocupado'. A mensagem associada
com a chave ira ser copiada para o clipboard, assim o usuário pode copia-la em um 
email """


#dicionarioas com suas chaves e valores que são as frases automaticas
conjunto_frases = { 'agree':'Totalmente de acordo','busy':'No momento estou impossibilitado de responder',
                     'wait':'Aguarde um momento que será atendido','bruno':'Bruno Felipe Costa da Silva' }

#a linha de comando sera armazenada na variavel sys.argv, necessário importa a biblioteca sys
import sys
import pyperclip


if len(sys.argv) < 2:
    print('Uitlização: pyton Multi_clipboard_atomatic.py - chave ')
    sys.exit()

#primeira argumento da linha de comando é a chave
chave = sys.argv[1]

#após armazenar a chave na variavel chave é necessário checar se ela é uma chave no diconario

if chave in conjunto_frases:
    pyperclip.copy(conjunto_frases[chave])
    print('Texto de' +chave+ 'Copiado para clipboard')
else:
    print('Não há texto para' +chave)




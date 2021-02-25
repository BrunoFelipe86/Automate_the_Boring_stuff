#!python3

"""O scrip ira pegar o texto do clipboard, addcionar um marcador e um espaço ao começo de cada linha
   e então colar o novo texto de volta para o clipboard """


import pyperclip

texto = pyperclip.paste() #O pyperclip ira colar o texto na area do clipboar como uma unica string com cada linha separa por \n

# Separar linhas e adicionar estrelas
linhas = texto.split('\n') # o método split() retorna uma lista de string

for i in range(len(linhas)): #laço que percorre todos os indexes da lista 'linhas'
    linhas[i] = '*' +linhas[i] #adiciona uma estrela a cada linha

#para copiar o texto usando pyperclip devemos passar apenas um argumento, assim usamos o método join para juntar as strings
texto = '\n'.join(linhas)

pyperclip.copy(texto)
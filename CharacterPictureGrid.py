"""Trabalhando com listas e loop dentro de loops"""
"""programa passa uma lista de lista e pede que imprima as colunas como linhas"""
lista = [["1","1","1","1","1","1"]
        ,['2','2','2','2','2','2']
        ,['3','3','3','3','3','3']
        ,['4','4','4','4','4','4']]

# j corresponde ao numero de linhas que a matriz tera
for j in range(len(lista[0])):
    for i in range(len(lista)):
        print (lista[i][j], end="")#A palavra reservada "end" para imprimir
    print('')                              # Na mesma linha 
        



    

lista = []

def listString (lista):
    lista.insert(len(lista)-2, 'and')
    for i in range(len(lista)):
        if i%2 != 0:
            lista.insert(i, ',')
    print(lista)
    print(' '.join(lista))


print("Transforma lista em string\n")
print("digite valores para serem inseridos na lista\n")


while True:
    name = input("nome:  ")
    lista.append(name)
    if name == '':
        break

    
    
listString(lista)






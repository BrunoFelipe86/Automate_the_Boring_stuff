"""Esse escript verifica se um número é par ou impar"""
"""e realiza uma operação matematica"""
def collatz(number):
        if (number % 2) == 0: #significa que o número é par
            num = number//2
        else:
            num = 3*number+1
        return num

#adicionando uma validação de entrada de dados
valid_entry = False
while valid_entry == False:
    a = input("Número desejado: ")
    try:
        a = int(a)
        if type(a) != int:
            print("Valor invalido")
        else:
            valid_entry = True
    except:
        print("valor invalido")
            
            
while a != 1:
    a = collatz(a)
    print(a)


            

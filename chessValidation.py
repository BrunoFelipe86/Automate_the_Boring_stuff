def isValidChessBoard (board):

    piecesCount = {'b':0, 'w':0}  #conta número de peças
    pawnCount = {'b':0,'w':0}     #conta número de peões
    qkings = {'b':False, 'w':False}  #Verificando reis
    letterAxis = ('a','b','c','d','e','f','g','h')
    pieceColors = ('b','w')
    pieceType = ('pawn','knight','bishop','rook','queen','king')

    #verificando se cada jogador tem 16 peças
    for j, i in board.items():
        #checa posição dos valores
        #todas as peças devem ter uma posição valida de 1a ate 8h
        if int(j[0]) >= 9:
            print("ERRO EM POSIÇÃO")
            return False

        if j[1] not in letterAxis:
            print ("ERRO DE POSIÇÂO")

        #Checando dados das peças
        if i != "":
            # nome das peças devem começar com 'w' ou 'b'
            if i[0] not in pieceColors:
                print ('ERRO DE TIPO DE PEÇA')
                return False

            thisPieceColour = i[0]  #recebe primeira letra do Valor do dicionario
            piecesCount[thisPieceColour] +=1  #adiciona 1 a variavel

            if piecesCount[thisPieceColour] >= 17:
                print('ERRO no total de peças')
                return False

            #verificando o nome das peças
            thisPieceType = i[1:] #variavel com os valores excluindo a primeira letra

            if thisPieceType not in pieceType: #verifica se os valores se encontram na tupla que guarda os nomes das peças
                print ('ERRO DE TIPO DE PEÇA')
                return False

            elif thisPieceType == 'pawn':
                pawnCount[thisPieceColour] += 1

                #cada jogador tem 8 peões
                if pawnCount[thisPieceColour] >= 9:
                    print('ERRO DE PEÕES')
                    return False

            elif thisPieceType == 'king':
                #apenas 1 rei branco e um rei negro
                if qkings[thisPieceColour] == True:
                    print("alreadyHaskingError")

                qkings[thisPieceColour] = True

    if list(qkings.values()) != [True, True]:
        print ("Rei desaparecido ERRO")
        return False

    return "tabuleio checado"

board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

print(isValidChessBoard(board))


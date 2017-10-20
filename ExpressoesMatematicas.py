# operadores:
    # cada variavel de operador possui uma string com sua representacao simbolica e sua prioridade em uma tupla.
adicao = ['+',1]
subtracao = ['-',1]
multiplicacao = ['*',2]
divisao = ['/',2]
exponenciacao = ['^',3]
parentesesInicio = ['(',4]
parentesesFinal = [')',4]

listaOperadoresEseparadores = [adicao[0],subtracao[0],multiplicacao[0],divisao[0],exponenciacao[0],parentesesInicio[0],parentesesFinal[0]]
listaVariaveis = []

expressaoInfixada = input()

def identificaVariaveis():
    global expressaoInfixada
    global listaOperadoresEseparadores
    global listaVariaveis

    '''for x in listaOperadoresEseparadores:
        expressaoInfixada = expressaoInfixada.replace(x, '.')'''

    def replaceOperEsep(x):
        global expressaoInfixada

        expressaoInfixada = expressaoInfixada.replace(x, ' ')


    map(lambda x: replaceOperEsep(x),listaOperadoresEseparadores)

    listaVariaveis = expressaoInfixada.split()

    def eliminaRepeticoes():
        global listaVariaveis

        for x in range(len(listaVariaveis)):
            for y in range(len(listaVariaveis)-1, x, -1):
                print listaVariaveis[x], listaVariaveis[y]
                if listaVariaveis[y] == listaVariaveis[x]:
                    del listaVariaveis[y]

    eliminaRepeticoes()


identificaVariaveis()

print listaOperadoresEseparadores[0]

print listaOperadoresEseparadores

print listaVariaveis

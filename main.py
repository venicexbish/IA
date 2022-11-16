from matrix import Matriz
from graph import Grafo
from node import Node

def main():
    #leitura e representação do circuito do ficheiro txt
    file = open ('circuito.txt', 'r')
    leitura = file.readlines()
    arr=[]
    for line in leitura:
        arr.append(line.strip()) # para remover o \n
        
    saida = -1
    matriz = Matriz()
    grafo = Grafo()
    nodo = Node()

    while saida != 0:
        print("1 -> Gerar Circuito ")
        print("2 -> Representar pista em forma de grafo")
        print ("3 -> Obter caminho mais rápido - algoritmo")
        saida = int(input("introduza a sua opcao-> "))
        if saida == 1:
            matriz.imprimeCircuito(arr)
            #print(matriz.returnPositionsOfMatrix(arr)) 
        #if saida == 2:
            #print(grafo.getNodes) 
        else:
            print("não introduziu nada")
            l = input("prima enter para continuar") 
   
if __name__ == "__main__":
    main() 
    
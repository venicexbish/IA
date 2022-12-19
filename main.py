from matrix import Matriz
from arestas import Arestas
from dictionary import Dictionary
from naoInformados import NaoInformados
from informados import Informados


def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

def main():
    #leitura e representação do circuito do ficheiro txt
    file1 = open ('./circuitos/circuito.txt', 'r')
    file2 = open ('./circuitos/circuito1.txt', 'r')
    file3 = open ('./circuitos/circuito2.txt', 'r')
    file4 = open ('./circuitos/circuito3.txt', 'r')
    leitura = file1.readlines()
    leitura1 = file2.readlines()
    leitura2 = file3.readlines()
    leitura3 = file4.readlines()
    
    arr=[]
    for line in leitura:
        arr.append(line.strip()) # para remover o \n
    
    arr1=[]
    for line in leitura1:
        arr1.append(line.strip()) # para remover o \n
    
    arr2=[]
    for line in leitura2:
        arr2.append(line.strip()) # para remover o \n
    
    arr3=[]
    for line in leitura3:
        arr3.append(line.strip()) # para remover o \n
        
    c = -1
    matriz = Matriz()
    arestas = Arestas()
    dict= Dictionary()

    circuitos=[arr,arr1,arr2,arr3]
    njog=0
    j=1

    printDFS=0
    printBFS=0
    printGreedy=0
    printA=0

    while c != 0:
        print ("########## BEM VINDO AO VECTOR RACE  ##########")
        print("  ")
        print("########## MENU CIRCUITOS ##########" )
        print("1 -> Circuito 1 ")
        print("2 -> Circuito 2" )
        print("3 -> Circuito 3 ")
        print("4 -> Circuito 4 ")
        print("0 -> Sair")
        print ("###############################################")
        c = int(input("Indique a opção pretendida-> "))
        print("    ")
        if c != 0:
            saida2= -1
            print("###### SELECIONOU O CIRCUITO ",c," ######" )
            njog = int(input("Indique o número de jogadores-> "))
            
            while saida2 !=0 and j<=njog: 
                    print("    ")
                    print("######  MENU JOGADOR ",j," ######" )
                    print("1 -> Gerar o Circuito ")
                    print("2 -> Representar a pista em forma de grafo")

                    if (printDFS == 0): print("3 -> Pesquisa DFS")
                    else: print(strike("3 -> Pesquisa DFS"))
                    if (printBFS == 0): print("4 -> Pesquisa BFS")
                    else:print(strike("4 -> Pesquisa BFS"))
                    if (printGreedy == 0): print("5 -> Pesquisa Greedy")
                    else: print(strike("5 -> Pesquisa Greedy"))
                    if (printA == 0): print("6 -> Pesquisa A*")
                    else: print(strike("6 -> Pesquisa A*"))

                    print("0 -> Voltar ao menu")
                    print("##############################################" )
                    saida2 = int(input("Introduza a sua opção-> "))
                    print("    ")
                    if saida2 == 1:
                            matriz.imprimeCircuito(circuitos[c-1])
                    if saida2 == 2:
                            l= arestas.getEdges(circuitos[c-1])
                            [print(i) for i in l]   
                    if saida2 == 3 and printDFS == 0 :
                            inicio = matriz.encontraPosicaoInicial(circuitos[c-1])
                            fins = matriz.encontraPosicoesFinais(circuitos[c-1])
                            grafo = NaoInformados(circuitos[c-1])
                            path =[]
                            visited = set()
                            mylist =[]
                            for i in fins:
                                path2 =[]
                                visited2 = set()
                                f= grafo.verificaDFSfins(inicio,i,path2,visited2)
                                mylist.append(f)
                            menor = 10000
                            dest =(0,0)
                            for i in mylist:
                                if (i[1] < menor): 
                                    dest = i[0]
                                    menor = i[1]
                            caminho =grafo.procura_DFS(inicio,dest,path,visited)
                            printDFS = 1
                    if saida2 == 4 and printBFS == 0:
                            inicio = matriz.encontraPosicaoInicial(circuitos[c-1])
                            fins = matriz.encontraPosicoesFinais(circuitos[c-1])
                            grafo = NaoInformados(circuitos[c-1])
                            mylist=[]
                            for i in fins:
                                f= grafo.verificaBFSfins(inicio,i)
                                mylist.append(f)
                            menor = 10000
                            dest =(0,0)
                            for i in mylist:
                                if (i[1] < menor): 
                                    dest = i[0]
                                    menor = i[1]
                            caminho =grafo.procura_BFS(inicio,dest)
                            printBFS = 1
                    if saida2 == 5 and printGreedy == 0: 
                            inicio = matriz.encontraPosicaoInicial(circuitos[c-1])
                            grafo = dict.makeGrafo(circuitos[c-1], inicio)
                            fins = matriz.encontraPosicoesFinais(circuitos[c-1])
                            inf = Informados()
                            
                            greedy = inf.greedy(dict, grafo, circuitos[c-1], inicio, fins[0])
                            printGreedy = 1

                    if saida2 == 6 and printA == 0: 
                            inicio = matriz.encontraPosicaoInicial(circuitos[c-1])
                            grafo = dict.makeGrafo(circuitos[c-1], inicio)
                            fins = matriz.encontraPosicoesFinais(circuitos[c-1])
                            inf = Informados()
                            
                            aStar = inf.aStar(dict, grafo, circuitos[c-1], inicio, fins[0])
                            printA = 1


                    j=j+1
            print("A sair ...")
            saida2=0
            c=0

if __name__ == "__main__":
    main() 
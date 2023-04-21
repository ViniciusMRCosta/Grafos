#nome: vinicius moura rodrigues da costa
#matricula: 201920441911

try:
    file = open("grafosArquivo.txt", 'a+')# se der algum erro substituir por r+
    class Grafo:

        def __init__(self, vertices):
            self.vertices = vertices
            self.grafo = [[0]*self.vertices for i in range(self.vertices)]

        def adiciona_aresta(self, i, j):
            self.grafo[i-1][j-1] = 1
            #self.grafo[j - 1][i - 1] = 1
            #self.grafo[j - 1][i - 1] = 1 grafo espelhado

        def mostra_matriz(self):
            print('A matriz de adjacencia e´: ')
            for i in range(self.vertices):
                print(self.grafo[i])
                if (i < self.vertices - 1):
                    file.write(str(self.grafo[i]) + "-v")
                else:
                    file.write(str(self.grafo[i]) + "\n")


    def carregar_grafos():
        file.seek(0)
        grafos = file.readlines()
        for i in range(len(grafos)):
            if (i % 2) == 0:
                print(str(int(i / 2) + 1) + "º grafo:")
                print(grafos[i])

        tem = False

        while tem == False:
            nome = input("Insira o nome do grafo: ")
            for i in range(0, len(grafos), 2):
                if (nome + "\n") == grafos[i]:
                    tem = True
                    index = i
            if not tem:
                print("Nome nao encontrado.")
        mat = grafos[index + 1].split("-v")

        matriz = []
        for i in range(len(mat)):
            matriz.append([])
            for j in range(1, len(mat[i]), 3):
                matriz[i].append(int(mat[i][j]))

        print("Nome: " + grafos[index])
        print("Matriz: ")
        for i in range(len(matriz)):
            print(matriz[i])
        return matriz

    op=3
    while(op!=1 and op!=2 and op!=0):
        print ("digite 0 para encerrar")
        print ("digite 1 para montar uma matriz adjacencia")
        print ("digite 2 para visualizar os grafos que ja foram montados")
        op = int(input("escolha a sua opcao: "))
        if (op == 0):
           print("saindo")
        elif(op==1):
            tem = True
            file.seek(0)
            grafos = file.readlines()
            while tem:
                tem = False
                nome = input("Insira o nome do grafo:")
                for i in range(0, len(grafos), 2):
                    if (nome + "\n") == grafos[i]:
                        tem = True
                        print("Nome ja¡ usado, por favor escolha outro.")
            file.write(nome + "\n")

            v = int(input('Digite a quantidade de Vertices: '))
            g = Grafo(v)
            a = int(input('Digite a quantidade de Arestas: '))

            for i in range(a):
                u = int(input('De qual Vertice parte esta Aresta? '))
                v = int(input('Para qual Vertice vai essa Aresta? '))
                g.adiciona_aresta(i,j)
            print (nome)
            g.mostra_matriz()
            op=3
        else:
            carregar_grafos()
            op=3
finally:
    file.close()


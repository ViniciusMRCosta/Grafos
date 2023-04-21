#nome: vinicius moura rodrigues da costa
#matricula: 201920441911

class Fila:
    def __init__(self):
        self.items = []
    def enfileirar(self, item):
        self.items.insert(0, item)
    def desenfileirar(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
        
class Vertice:
    def __init__(self, distancia=None, cor="white", pai=None, vizinhanca=None):
        self.distancia=distancia
        self.cor=cor
        self.pai=pai
        self.vizinhanca=vizinhanca
    def setPai(self, pai):
        self.pai=pai
    def setCor(self, cor):
        self.cor=cor
    def setDistancia(self, distancia):
        self.distancia=distancia
    def setVizinhanca(self, vizinhanca):
        self.vizinhanca=vizinhanca
    def getPai(self):
        return self.pai
    def getCor(self):
        return self.cor
    def getDistancia(self):
        return self.distancia
    def getVizinhanca(self):
        return self.vizinhanca
    

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, i, j):
        #self.grafo[i-1][j-1] = 1  #grafo simples
        self.grafo[i - 1][j - 1] = 1
        self.grafo[j - 1][i - 1] = 1 #grafo espelhado

    def mostra_matriz(self):
        print('A matriz de adjacencia e: ')
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
            print(str(int(i / 2) + 1) + "� grafo:")
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

op=4
while(op!=1 and op!= 3 and op!=0):
    print ("digite 0 para encerrar")
    print ("digite 1 para montar uma matriz adjacencia")
    print ("digite 2 para ir para o menu de classes")
    print ("digite 3 para realizar a Busca em Largura")
    op = int(input("escolha a sua opcao: "))
    if(op>=4):
        print("opcao invalida")
        op=4
    elif (op == 0):
       print("saindo")
       
    elif(op==1):
        try:
            file = open("grafosArquivo.txt", 'a+')# se der algum erro substituir por r+
            print("digite 1 se deseja montar um grafo\ndigite 2 se deseja carregar os grafos montados")
            e=3
            while(e!=1 and e!=2):
                e=int(input("digite a opcao: "))
            if(e==1):    
                tem = True
                file.seek(0)
                grafos = file.readlines()
                while tem:
                    tem = False
                    nome = input("Insira o nome do grafo:")
                    for i in range(0, len(grafos), 2):
                        if (nome + "\n") == grafos[i]:
                            tem = True
                            print("Nome ja usado, por favor escolha outro.")
                file.write(nome + "\n")
    
                v = int(input('Digite a quantidade de Vertices: '))
                g = Grafo(v)
                a = int(input('Digite a quantidade de Arestas: '))
    
                for i in range(a):
                    print ("restam ",a-i," arestas")
                    u = int(input('De qual Vertice parte esta Aresta? '))
                    v = int(input('Para qual Vertice vai essa Aresta? '))
                    g.adiciona_aresta(u,v)
                print (nome)
                g.mostra_matriz()
                op=4
            else:
                carregar_grafos()
                op=4
                
        finally:
            file.close()
       
    elif(op==2):
        print ("digite 0 para voltar ao menu anterior")
        print ("digite 'a' para grafo Completo Kn")
        print ("digite 'b' para grafo Bipartido Completo Kn1, n2,...")
        print ("digite 'c' para grafo Estrela Sn")
        print ("digite 'd' para grafo Ciclo Cn") #n>=3
        print ("digite 'e' para grafo Roda Wn") #n>=3
        print ("digite 'f' para grafo Caminho Pn")
        print ("digite 'g' para grafo Cubico Qn")
        ch = input("escolha a sua opcao: ") #choice
        if (ch == 0):
            op=4
            
        if(ch== 'a'):
            print("\n para todo par u,v ∈ V, a aresta uv ∈ E.\n")
            try:
                file = open("grafosCompleto.txt", 'a+')
                print("digite 1 se deseja montar um grafo Completo\ndigite 2 se deseja carregar os grafos Completos montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v=0
                    while(v<=0):
                        v = int(input('Digite a quantidade de Vertices: '))
                    g = Grafo(v)
                    a= (v*(v-1)/2)
                    if(v==1):
                        u = 1 
                        g.adiciona_aresta(u,0)
                    elif (v==2):
                        u = int(input('De qual Vertice parte esta Aresta? '))
                        v = int(input('Para qual Vertice vai essa Aresta? '))
                        g.adiciona_aresta(u,v)
                    else:
                        for i in range(v):
                            testa_completo = a-i
                            print("restam ", a-i," arestas")
                            u = int(input('De qual Vertice parte esta Aresta? '))
                            v = int(input('Para qual Vertice vai essa Aresta? '))
                            g.adiciona_aresta(u,v)
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
        
        elif(ch=='b'):
            print("\n se u ∈ V1 e v ∈ V2, entao uv ∈ E \n")
            try:
                file = open("grafosBipartidoCompleto.txt", 'a+')
                print("digite 1 se deseja montar um grafo Bipartido Completo\ndigite 2 se deseja carregar os grafos Bipartidos Completos montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v1=0
                    v2=0 
                    while(v1<=0 and v2<=0):
                        v1 = int(input('Digite a quantidade de Vertices de V1: '))
                        v2 = int(input('Digite a quantidade de Vertices de V2: '))
                    g = Grafo(v1+v2)
                    a = v1*v2
                    for i in range(a):
                        print ("restam ",a-i," arestas")
                        u = int(input('De qual Vertice parte esta Aresta? '))
                        v = int(input('Para qual Vertice vai essa Aresta? '))
                        g.adiciona_aresta(u,v)
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
        
        elif(ch=='c'):
            print("\n um grafo estrela Sk é o grafo bipartido completo com um nó interno e k folhas. \n")
            try:
                file = open("grafosEstrela.txt", 'a+')
                print("digite 1 se deseja montar um grafo Estrela\ndigite 2 se deseja carregar os grafos Estrela montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v=0
                    while(v<=0):
                        v = int(input('Digite a quantidade de Vertices ao redor do no central (no 1): '))
                    g = Grafo(v+1)
                    #a=v
                    u=1
                    for i in range(v):
                        u = u + 1
                        g.adiciona_aresta(1,u)
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
            
        elif(ch=='d'):
            print("\n um número de vértices conectados em uma rede fechada \n")
            try:
                file = open("grafosCiclo.txt", 'a+')
                print("digite 1 se deseja montar um grafo Ciclo\ndigite 2 se deseja carregar os grafos Ciclo montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v=2
                    while(v<3):
                        v = int(input('Digite a quantidade de Vertices: '))
                    g = Grafo(v)
                    #a=v
                    u=0
                    for i in range(v-1):
                        u = u + 1
                        g.adiciona_aresta(u,u+1)
                        
                    g.adiciona_aresta(v,1)    
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
            
        elif(ch=='e'):
            print("\n Ciclo+estrela, grafo ciclo com um no central \n")
            try:
                file = open("grafosRoda.txt", 'a+')
                print("digite 1 se deseja montar um grafo Roda\ndigite 2 se deseja carregar os grafos Roda montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v=2
                    while(v<3):
                        v = int(input('Digite a quantidade de Vertices ao redor do no central: '))
                    g = Grafo(v+1)
                    #a=2v
                    u=1
                    for i in range(v-1):
                        u = u + 1
                        g.adiciona_aresta(1,u)
                        g.adiciona_aresta(u,u+1)
                        
                    g.adiciona_aresta(1,v)
                    g.adiciona_aresta(v,2)
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
            
        elif(ch=='f'):
            print("\n cada vertice esta ligado ao vertice seguinte, mas o ultimo nao esta em nenhum \n")
            try:
                file = open("grafosCaminho.txt", 'a+')
                print("digite 1 se deseja montar um grafo Caminho\ndigite 2 se deseja carregar os grafos Caminho montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        nome = input("Insira o nome do grafo:")
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    v=0
                    while(v<=0):
                        v = int(input('Digite a quantidade de Vertices: '))
                    g = Grafo(v)
                    #a=v-1
                    if(v==1):
                        g.adiciona_aresta(1,0)
                    else:    
                        u=0
                        for i in range(v-1):
                            u = u + 1
                            g.adiciona_aresta(u,u+1)
                        
                    print (nome)
                    g.mostra_matriz()
                    op=4
                else:
                    carregar_grafos()
                    op=4
                    
            finally:
                file.close()
        
        elif(ch=='g'): #inacabado
            print("\ncada no tem grau 3 \n")
            #v=2^n
            
            try:
                file = open("grafosCubo.txt", 'a+')
                print("digite 1 se deseja montar um grafo Cubico\ndigite 2 se deseja carregar os grafos Cubico montados")
                e=3
                while(e!=1 and e!=2):
                    e=int(input("digite a opcao: "))
                if(e==1):
                    tem = True
                    file.seek(0)
                    grafos = file.readlines()
                    while tem:
                        tem = False
                        n = int(input("Insira o n>=0 do n-cubo:"))
                        nome = input("Insira o nome do grafo:")+str(n)
                        for i in range(0, len(grafos), 2):
                            if (nome + "\n") == grafos[i]:
                                tem = True
                                print("Nome ja usado, por favor escolha outro.")
                    file.write(nome + "\n")
                    
                    matriz = [[0]]
                    for i in range(n):
                        q = int(2 ** i)
                        mataux = []
                        for j in range(q * 2):
                            mataux.append([0] * (q * 2))
                        for j in range(q):
                            for k in range(q):
                                mataux[j][k] = matriz[j][k]
                                mataux[j + q][k + q] = matriz[j][k]
                        for j in range(q):
                            mataux[j + q][j] = 1
                            mataux[j][j + q] = 1
                        matriz = []
                        for j in range(q * 2):
                            matriz.append(mataux[j])
        
                    for i in range(len(matriz)):
                        print(matriz[i])
                        
                    for i in range(2**n):
                        if (i < (2**n)-1 ):
                            file.write(str(matriz[i]) + "-v")
                        else:
                            file.write(str(matriz[i]) + "\n")
                else:
                    carregar_grafos()
                    op=4
            finally:
                file.close()
                
    elif(op==3):
        e =3
        while (e!=0 and e != 1 and e != 2):
            print("Digite 0 para voltar ao menu inicial\nDigite 1 para inserir grafo \nDigite 2 para Carregar grafo")
            e = int(input("Por favor, escolha a opcao desejada:"))

        if(e==0):
            op=4
        matriz = []
        if (e==1):
            try:
                file=open("grafosArquivo.txt", 'a+')
                tem = True
                file.seek(0)
                grafos = file.readlines()
                while tem:
                    tem = False
                    nome = input("Insira o nome do grafo:")
                    for i in range(0, len(grafos), 2):
                        if (nome + "\n") == grafos[i]:
                            tem = True
                            print("Nome ja usado, por favor escolha outro.")
                file.write(nome + "\n")
    
                v = int(input('Digite a quantidade de Vertices: '))
                g = Grafo(v)
                a = int(input('Digite a quantidade de Arestas: '))
    
                for i in range(a):
                    print ("restam ",a-i," arestas")
                    u = int(input('De qual Vertice parte esta Aresta? '))
                    v = int(input('Para qual Vertice vai essa Aresta? '))
                    g.adiciona_aresta(u,v)
                print (nome)
                g.mostra_matriz()
                op=4
            finally:
                file.close()
                op=4
                
        elif (e==2):
            print("arquivos disponiveis:")
            print("[1] - grafosArquivo.txt")
            print("[2] - grafosCompleto.txt")
            print("[3] - grafosBipartidoCompleto.txt")
            print("[4] - grafosEstrela.txt")
            print("[5] - grafosCiclo.txt")
            print("[6] - grafosRoda.txt")
            print("[7] - grafosCaminho")
            print("[8] - grafosCubo.txt")
            
            e=0
            while(e!=1 and e!=2 and e!=3 and e!=4 and e!=5 and e!=6 and e!=7 and e!=8):
                e=int(input("digite de qual arquivo deseja carregar o grafo: "))
                
            if(e==1):
                try:
                    file=open("grafosArquivo.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==2):
                try:
                    file=open("grafosCompleto.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==3):
                try:
                    file=open("grafosBipartidoCompleto.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==4):
                try:
                    file=open("grafosEstrela.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==5):
                try:
                    file=open("grafosCiclo.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==6):
                try:
                    file=open("grafosRoda.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==7):
                try:
                    file=open("grafosCaminho.txt", 'a+')
                    matriz = carregar_grafos()
                    op=4
                finally:
                    file.close()
                    op=4
            if(e==8):
                try:
                    file=open("grafosCubo.txt","a+")
                    matriz = carregar_grafos()
                    op=4 
                finally:
                    file.close()
                    op=4
            
            
        q = Fila()
        vertice=[]

        for i in range(len(matriz)):
            v = Vertice([])
            vertice.append(v)
        for i in range(len(matriz)):
            lista=[]
            for j in range(len(matriz)):
                if (matriz[i][j]==1):
                    lista.append(j)
            vertice[i].setVizinhanca(lista)
        contcc=0
        arrcc=[]
        for k in range(len(vertice)):
            if(vertice[k].getCor()=='white'):
                vertice[k].setCor("gray")
                vertice[k].setDistancia(0)
                q.enfileirar(vertice[k])
                contcc = contcc + 1
                arrcc.append([])
                arrcc[contcc-1].append(k)

            while not q.isEmpty():
                u=q.desenfileirar()
                vizinho = u.getVizinhanca()
                for i in range(len(vizinho)):
                    if (vertice[vizinho[i]].getCor()=='white'):
                        arrcc[contcc-1].append(vizinho[i])
                        vertice[vizinho[i]].setCor('gray')
                        vertice[vizinho[i]].setPai(u)
                        vertice[vizinho[i]].setDistancia(u.getDistancia()+1)
                        q.enfileirar(vertice[vizinho[i]])
                u.setCor('black')

        print("numero de componentes conexas: ",contcc)
        for i in range(contcc):
            print("componente conexa ",i+1,": ",arrcc[i])
        op=4

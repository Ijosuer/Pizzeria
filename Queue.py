from tkinter import N
from Node import Pizza
from graphviz import Source
# pizza = Pizza()

class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def Enqueue(self,name,total):
        if self.first is None:
            self.first = self.last = Pizza(name,total)
            self.size +=1
            print('agregado ',self.first.name)
        else:
            self.last.next = Pizza(name,total)
            self.size +=1
            print('agregado ',self.last.next.name)
            self.last = self.last.next

    def Dequeue(self):
        if self.first is None:
            print("Dude, it's empty here")
        else:
            item = self.first.name
            self.first = self.first.next
            self.size -=1
            print('Eliminado',item) 
    
    def isEmpty(self):
        if self.first is None:
            print('yep')
        else:
            print('nope')
    
    def len(self):
        count = 0
        aux = self.first
        while(aux):
            count += 1
            aux = aux.next
        print(count)

    def Front(self):
        print(self.first.name)
    
    def Rear(self):
        print(self.last.name)
    
    def Report(self):
        aux = self.first
        text=""
        text=""
        text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n"
        text+="labelloc = \"t;\"label = \"Pizzas\";\n"
        
        while aux:
            text+=""+str(aux.name)+"[dir=both label = \"Nombre = "+str(aux.name)+"\"]"
            text+=""+str(aux.next.name)+"-> "+str(aux.name)+"\n"
            aux=aux.next
            if aux!=self.first:    
                text+=""+str(aux.name)+"[dir=both label = \"Nombre = "+str(aux.name)+"\"]"
            if aux==self.last:
                text+=""+str(aux.name)+"\n"
                break
            
        
        
        return text
    def crearReporte(self): 
        contenido="digraph G {\n\nsubgraph cluster_p{"
        contenido+=str(self.Report())
        contenido+="\n}}"
        grafica = Source(contenido, filename=('archivos/image'),format='png')
        grafica.view()
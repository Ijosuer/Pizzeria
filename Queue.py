from Pizza import Pizza
from graphviz import Source
from colorama import Fore, Style

class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def Enqueue(self,name,total,time):
        if self.first is None:
            self.first = self.last = Pizza(name,total,time)
            self.first.time_real = time
            self.size +=1
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'Pizza de ',self.first.name.upper(),'en el horno 🔥', 'sale en ⌚',time,'min!')
        else:
            self.last.next = Pizza(name,total,self.last.time_real)
            self.last.next.time_real +=  time
            self.size +=1
            self.last = self.last.next
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'\nPizza de ',self.last.name.upper(),'en el horno 🔥', 'sale en ⌚',self.last.time_real,'min!')

    def Dequeue(self):
        item = self.first.name
        if self.first is None:
            print("Dude, it's empty here")
        else:
            if self.size == 1:
                self.size -=1
                self.last == None 
            
            elif self.size >= 2:
                time = self.first.time_real
                aux = self.first
                while aux != self.last:
                    aux.time_real -= time
                    aux = aux.next
                self.last.time_real -= time
                self.first = self.first.next
                self.size -=1

            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'\nPizza de ',item.upper(),'está saliendo del horno!! 💯')
    def Size(self):
        count = 0
        cur = self.first
        while(cur):
            count+=1
            cur = cur.next
        return count

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
        print(self.first.name,self.first.time_real)
    
    def Rear(self):
        print(self.last.name,self.last.time_real)
    
    def Report(self):
        aux = self.first
        size = self.size
        text=""
        text=""
        text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n"
        text+="labelloc = \"t;\"label = \"🍕 Pizzas 🍕\";\n"
        if size == 0:
                text+='VACIO'
                return text
        while aux:
            text+=""+str(aux.name)+"[dir=both label = \"Nombre = "+str(aux.name.upper())+"\\nCantidad = "+str(aux.total)+"\\nTiempo = "+str(aux.time_real)+"\"]"
            if self.first == self.last:
                break
            text+=""+str(aux.next.name)+"-> "+str(aux.name)+"\n"
            aux=aux.next
            if aux!=self.first:    
                text+=""+str(aux.name)+"[dir=both label = \"Nombre = "+str(aux.name)+"\\nCantidad = "+str(aux.total)+"\\nTiempo = "+str(aux.time_real)+"\"]"
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
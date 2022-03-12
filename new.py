class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# from Queue import Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def Enqueue(self,data):
        if self.rear is None:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
            
    def Dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return
        
    def IsEmpty(self):
        return self.front is None
    
    def Size(self):
        count = 0
        cur = self.front
        while(cur):
            count+=1
            cur = cur.next
        return count
    
    def Front(self):
        print( self.front.data)
    
    def Rear(self):
        print(self.rear.data)

    def p(self):
        aux = self.front
        while aux != self.rear:
            print(aux.data)
            aux = aux.next
        print(aux.data)
        

q = Queue()
q.Enqueue('1')
q.Enqueue('2')
q.Enqueue('3')
q.Enqueue('4')
q.p()
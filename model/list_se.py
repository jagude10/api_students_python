from.node import Node

class ListSE:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        #elif data ["identification"] in self.student:

          #  raise
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            #posicionados en el ultimo
            temp.next = Node(data)
        self.count =+1

    def add_to_start(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next= self.head
            self.head = temp
        self.count=+1
   # def valid_exist(self , id):
    #    while temp.next == True:
     #       if self.head is None:
      #          return False

  #  else:
        #temp = self.head
         #   while temp != None:
          #  if temp.data.identification == id:
           #     return True
           # temp = temo.next
           # return False
    def add_to_position(self,position:int, data):
        if position >0 and position <= (self.count+1):
            if position == 1:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp !=None:
                    if count == position -1:
                        new_node = Node(data)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count =+1
                        break
                    temp = temp.next
                    count =+1

            self.count=+1
        else:
            raise Exception("La posición no es válida")

    def invert(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp != None:
                list_cp.add_to_start(temp.data)
                temp = temp.next
            self.head = list_cp.head

    def delete_posicion(self,p):
        position = 0
        if position == 1 and self.head.data != None:
            self.head = self.head.next

        temp = self.head
        while   temp.next != None:
            position = position + 1
            if temp.next.data != None and p == position:
                temp.next = temp.next.next
                break
            temp = temp.next

    def delete_multiplo(self,p):
        list_cp = ListSE ()
        multiplo = (input("ingrese un numero entero que ente entre 0 y 9"))
        position = 0
        while temp.next != None:
            position = position + 1
            if temp.next.data != None and p == position:
                temp.next = temp.next.next
                position = position / multiplo % > 0






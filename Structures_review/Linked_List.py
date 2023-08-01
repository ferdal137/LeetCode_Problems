#Linked List

#Create the node class

class Node:
    def __init__(self,Value):
        self.Value = Value
        self.Next = None
    
    def __str__(self):
        return str(self.Value)

#Create the Linked List

class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0 
 
    def Append(self, Value):      #Method to append a node in the final of the list
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        else:
            Current = self.First
            while(Current.Next!=None):
                Current = Current.Next
            Current.Next = MyNode
        
        self.Size += 1

        return MyNode
    
    def Remove(self,Value):      #Remove a Node given its value
        if self.Size == 0:
            return False
        else:
            Current = self.First
            while(Current.Next.Value != Value):
                if Current.Next == None:
                    return False
                else:
                    Current = Current.Next
            DeletedNode = Current.Next
            Current.Next = DeleteNode.Next
        
        self.Size -= 1

        return DeletedNode

    def _len_(self):
        return self.Size
    
    def _str_(self):
        String = "["
        Current = self.First
        while Current != None:
            String += str(Current)
            String += str(",")
            Current = Current.Next
        String = "]"

        return String


MyList = LinkedList()

MyList.Append(1)
MyList.Append(2)
MyList.Append(3)
MyList.Append(4)

print(MyList)
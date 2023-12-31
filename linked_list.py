# A way to store data in ordered manner 
# Normal arrays or lists is simply data stored with no relation to one other besides being next to another element and being inside a same list.
# a linked list has every element being connected to the next element in the list 

class node:
    def __init__(self, data=None) :
        self.data=data
        self.next=None

class linked_list:
    def __init__(self) -> None:
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self,index):
        if index >= self.length():
            print("Get index out of range")
            return None 
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:return cur_node.data
            cur_idx+=1


my_list = linked_list()


my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print(my_list.get(5))

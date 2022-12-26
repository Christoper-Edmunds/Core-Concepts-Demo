#user_input = input("enter some data to start the linked list \n")
#user_choice_input = input("Select a command:\n A: Append a value to the linked list \n B: Prepend a value to the linked list \n C: Delete last value of linked list \n D: Delete first value of linked list \n E: Search linked list for first iteration of value \n F: Search linked list for all iterations of value \n G: Count Length of Linked List \n")
from dataclasses import dataclass

#hello 
print ("Generates multiple linked list types, filled with randomly generated integers from 0 to 99")
user_choice_input = input("Select a command:\n A: Singly Linked List \n B: Doubly Linked List \n C: Adjacency Linked List \n")

if user_choice_input.isalpha() != True and len(user_choice_input) != 1:
    print("invalid entry")
    user_choice_input = input("Select a command:\n A: Singly Linked List \n B: Doubly Linked List \n C: Circular Linked List \n D: Adjacency Linked List \n")

elif user_choice_input.lower() == "a":
    print("Singly Linked List selected")
    for x in range (1 , 10):
        pass #add a node here


elif user_choice_input.lower() == "b":
    print("Doubly Linked List selected")

elif user_choice_input.lower() == "c":
    print("Adjacency Linked List selected")


class LinkedList():
    
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        return self.data 

class Node: 
    
    def __init__(self, data):
        self.data = data
        self.next = None 
    
    def __repr__(self):
        node = self.head
        nodes = [] 
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

from ctypes.wintypes import CHAR
from email import charset
from multiprocessing.dummy import current_process


class DataTree:
    def __init__(self):
        self.name=None
        self.pw=None
        self.d_left=None
        self.d_right=None

class LengthTree:
    def __init__(self):
        self.l_lenght=None
        self.l_right=DataTree()
        self.l_left=DataTree()

class Node:
    def __init__(self,data):
        self.CharAlphbet=data
        self.c_right=None
        self.c_left=None
        
        # self.pointer=LengthTree()

def dataInsertion():
    
    
    root=Node('p')
    
    root.c_left=Node('h')
    root.c_left.c_left=Node('d')
    root.c_left.c_right=Node('l')
    root.c_left.c_left.c_left=Node('b')
    root.c_left.c_left.c_right=Node('f')
    root.c_left.c_right.c_left=Node('j')
    root.c_left.c_right.c_right=Node('n')
    root.c_left.c_left.c_left.c_left=Node('a')
    root.c_left.c_left.c_left.c_right=Node('c')
    root.c_left.c_left.c_right.c_left=Node('e')
    root.c_left.c_left.c_right.c_right=Node('g')

    root.c_left.c_right.c_left.c_left=Node('i')
    root.c_left.c_right.c_left.c_right=Node('k')
    root.c_left.c_right.c_right.c_left=Node('m')
    root.c_left.c_right.c_right.c_right=Node('o')


    root.c_right=Node('t')
    root.c_right.c_left=Node('r')

    root.c_right.c_right=Node('x')

    root.c_right.c_left.c_left=Node('q')
    root.c_right.c_left.c_right=Node('s')

    root.c_right.c_right.c_left=Node('v')
    root.c_right.c_right.c_right=Node('y')

    root.c_right.c_right.c_left.c_left=Node('u')
    root.c_right.c_right.c_left.c_right=Node('w')

    root.c_right.c_right.c_right.c_right=Node('z')
    

    return root

def inorder(root):
    if root is not None:
        inorder(root.c_left)
        print((root.CharAlphbet)+'->',end=' ')
        inorder(root.c_right)



def searching(root,Oo):
    if root is not None:
        currentValue=ord(root.CharAlphbet)
        incomeValue=ord(Oo)
    
        
        print(currentValue,incomeValue)
        if currentValue==incomeValue:
            print("work here")
            return True
        elif currentValue < incomeValue:
            searching(root.c_right,Oo)
        elif currentValue > incomeValue:
            searching(root.c_left,Oo)
        
    

if __name__ == "__main__":
    root=dataInsertion()
    inorder(root)
    while True:
        name=input("Please enter name!")
        
        Oo=name[0]
        print(Oo)
        flag = searching(root,Oo)
        if flag:
            print("found")
        else:
            print("not Found")


        

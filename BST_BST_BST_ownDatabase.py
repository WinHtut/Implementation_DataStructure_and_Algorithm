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
    def __init__(self):
        self.CharAlphbet=None
        self.c_right=None
        self.c_left=None
        self.pointer=LengthTree()


if __name__ == "__main__":
    myDB=Node()
    firstData = "name"
    l_firstData=len(firstData)
    if l_firstData==1:
        myDB.CharAlphbet=firstData

    else:
        myDB.pointer.l_lenght=l_firstData

        if myDB.pointer.l_lenght==10:
            myDB.pointer.l_right.name="winhtut"


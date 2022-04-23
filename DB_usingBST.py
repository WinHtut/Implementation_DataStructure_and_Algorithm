class Node:
    def __init__(self,name,pw):
        self.name=name
        self.pw = pw
        self.left=None
        self.right=None

def insert(node,name,pw):
    if node is None:
        return Node(name,pw)
    oldName=asciiValue(node.name)
    newName=asciiValue(name)
    bigLength=0
    if len(oldName) > len(newName):
        bigLength=len(newName)
    else:
        bigLength=len(oldName)

    for i in range(bigLength):
        if oldName[i] > newName[i]:
            node.left = insert(node.left,name,pw)
            return node
        elif oldName[i] < newName[i]:
            node.right = insert(node.right,name,pw)
            return node
    print("Not allowed same name")
    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.name)
        inorder(root.right)
    else:
        return root
def asciiValue(name):
    list=[]
    name=name.lower()
    for i in name:
        data=ord(i)
        list.append(data)
    list.append(1)
    return list
if __name__=="__main__":
    root=None
    while True:
        name=input("enter username>:")
        pw=input("enter password")
        root=insert(root,name,pw)
        inorder(root)



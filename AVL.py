class Tree:
    def __init__(self,value):
        self.key=value     
        self.left=None
        self.right=None
        self.height=1
        
class AVL_tree():
    
    def __init__(self):
        self.root = None
        self.path=[]
        self.roots=[]
        self.AVL_Check=[]
        
    def insert(self,value,root):
        if(root==None):
            root=Tree(value)
        else:
            self.roots.append(root.key)
            if(value>=root.key):
                self.path.append("R")
                root.right=self.insert(value,root.right)
                if(self.AVL_Condition(root)):
                    if(value<root.right.key):
                        self.AVL_Check.append({"value":[root.key,root.right.key,root.right.left.key],"case":"CASE 3","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Double Rotation Right Left"})
                        root=self.AVL_Right_Left_Rotation(root)
                    else:
                        self.AVL_Check.append({"value":[root.key,root.right.key,root.right.right.key],"case":"CASE 4","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Single Rotation Right Right"})
                        root=self.AVL_Right_Rotations(root)
            else:
                self.path.append("L")
                root.left=self.insert(value,root.left)
                if(self.AVL_Condition(root)):
                    if(value>=root.left.key):
                        self.AVL_Check.append({"value":[root.key,root.left.key,root.left.right.key],"case":"CASE 2","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Double Rotation Left Right"})
                        root=self.AVL_Left_Right_Rotation(root)
                    else:
                        self.AVL_Check.append({"value":[root.key,root.left.key,root.left.left.key],"case":"CASE 1","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Single Rotation left left"})
                        root=self.AVL_Left_Rotations(root)
            root.height=max(self.find_height(root.left),self.find_height(root.right))+1
        return(root)
    
    def AVL_Condition(self,root):
        left_height=self.find_height(root.left)
        right_height=self.find_height(root.right)
        diff_height = left_height - right_height
        if(diff_height<0):
            diff_height=-1*diff_height 
        if(diff_height==2):
            return(True)
        else:
            return(False)
    
    def AVL_Left_Rotations(self,root):
        temp=root
        new_root=root.left
        temp.left=new_root.right
        new_root.right=temp
        temp.height=self.height(temp)
        return(new_root)
    
    def AVL_Right_Rotations(self,root):
        temp=root
        new_root=root.right
        temp.right=new_root.left
        new_root.left=temp
        temp.height=self.height(temp)
        return(new_root)
    
    def AVL_Left_Right_Rotation(self,root):
        temp=root.left
        root.left=temp.right
        root.left.left=temp
        temp.right=None
        temp.height=self.height(temp)
        return(self.AVL_Left_Rotations(root))
    
    def AVL_Right_Left_Rotation(self,root):  
        temp=root.right 
        root.right=temp.left
        root.right.right=temp
        temp.left=None
        temp.height=self.height(temp)
        return(self.AVL_Right_Rotations(root))
    
    def find_height(self,root):
        if(root==None):
            return(0)
        else:
            return(root.height)
    
    def height(self,root):
        if(root==None):
            return(0)
        else:
            return(1+max(self.height(root.left),self.height(root.right)))
                  
    def search(self,root,x):
        if(root==None):
            return(False)
        elif(root.key==x):
            return(True)
        elif(root.key<x):
            self.roots.append(root.key)
            self.path.append("R")
            return(self.search(root.right,x))
        else:
            self.roots.append(root.key)
            self.path.append("L")
            return(self.search(root.left,x))

    def delete_find(self,root,x):
        if(root==None):
            return(None,None)
        if(root.key==x):
            if(root.left!=None and root.right!=None):
                temp=self.successor(root.right)
                return("case 1",temp.key)
            elif(root.left==None and root.right!=None):
                return("case 2",root.right.key)
            elif(root.left!=None and root.right==None):
                return("case 3",root.left.key,)
            else:
                return("case 4",None)
        elif(x<root.key):
            self.path.append("L")
            self.roots.append(root.key)
            return(self.delete_find(root.left,x))
        else:
            self.path.append("R")
            self.roots.append(root.key)
            return(self.delete_find(root.right,x))

    def check_Avl_for_root(self,root):
        if(root==None):
            return root
        if(self.AVL_Condition(root)):
            if(self.height(root.right)>self.height(root.left)):
                if(root.right.right==None):
                    self.AVL_Check.append({"value":[root.key,root.right.key,root.right.left.key],"case":"CASE 3","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Double Rotation Right Left"})
                    root=self.AVL_Right_Left_Rotation(root)
                else:
                    self.AVL_Check.append({"value":[root.key,root.right.key,root.right.right.key],"case":"CASE 4","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Single Rotation Right Right"})
                    root=self.AVL_Right_Rotations(root)
            else:
                if(root.left.left==None):
                    self.AVL_Check.append({"value":[root.key,root.left.key,root.left.right.key],"case":"CASE 2","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Double Rotation Left Right"})
                    root=self.AVL_Left_Right_Rotation(root)
                else:
                    self.AVL_Check.append({"value":[root.key,root.left.key,root.left.left.key],"case":"CASE 1","L":self.find_height(root.left),"R":self.find_height(root.right),"rot":"Single Rotation left left"})
                    root=self.AVL_Left_Rotations(root)
        return(root)
        
    def delete(self,root,x):
        if(root.key==x):
            if(root.left!=None and root.right!=None):
                temp=self.successor(root.right)
                root.right=self.delete(root.right,temp.key)
                temp.left=root.left
                temp.right=root.right
                root=temp
                root.height=self.height(root)
            elif(root.left==None and root.right!=None):
                root=root.right
            elif(root.left!=None and root.right==None):
                root=root.left
            else:
                root=None 
        elif(x<root.key):
            if(root.left!=None):
                root.left=self.delete(root.left,x)
                root.height=self.height(root)  
        else:
            if(root.right!=None):
                root.right=self.delete(root.right,x)
                root.height=self.height(root)
        if(len(self.AVL_Check)==0):
            root=self.check_Avl_for_root(root)
        return(root)
    
    def successor(self,root):
        if(root.left==None):
            return(root)
        else:
            return(self.successor(root.left))
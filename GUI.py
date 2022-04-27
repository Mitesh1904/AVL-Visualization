from tkinter import messagebox
import pyautogui
from AVL import AVL_tree
import time
from tkinter import *

class Tree:
    
    def __init__(self):
        self.AVL = AVL_tree()
        self.GUI = Tk()
        self.GUI.title("AVL Visualization")
        self.GUI.iconbitmap("ICON.ico")
        self.Width,self.Height= pyautogui.size()
        self.GUI.geometry(f"{self.Width}x{self.Height}")
        self.change_width=self.Width/4
        self.Width=self.Width/4
        self.change_Height=self.Height/4
        self.Tree_Height=0
        self.number_of_node=0
        self.default_Screen=True
        self.default_txt=[]
        self.node_value=[]
        self.node=[]
        self.txt=[]
        self.cordinates_path=[]
        self.line=[]
        self.Theme_value= IntVar()
        self.Theme_value.set(1)
        self.Create_Canvas()
        self.Create_frame()
        self.Set_Colors()
        self.set_defaul_Screen()
        self.GUI.mainloop()

    def set_defaul_Screen(self):
        self.default_txt.clear()
        self.Status_bar_variable.set("AVL Visualization")
        self.default_txt.append(self.canvas.create_text(self.Width*2,150,text="INNOVATIVE ASSIGNMENT",fill=self.fill_color,font="Comic 30 bold underline"))
        self.default_txt.append(self.canvas.create_text(self.Width*2-325,250,text="COURSE : ",fill=self.fill_color,font="Comic 24 bold"))
        self.default_txt.append(self.canvas.create_text(self.Width*2-287,300,text="CREATED BY : ",fill=self.fill_color,font="Comic 24 bold"))
        self.default_txt.append(self.canvas.create_text(self.Width*2+80,250,text="ADVANCE DATA STRUCTURE (2CSDE75)",fill=self.outline_color,font="Comic 24 italic"))
        self.default_txt.append(self.canvas.create_text(self.Width*2+20,300,text="Mitesh Panchal ~ 19BCE149",fill=self.outline_color,font="Comic 20 "))
        self.default_txt.append(self.canvas.create_text(self.Width*2+27,350,text="Chintan Patoliya ~ 19BCE206",fill=self.outline_color,font="Comic 20 "))
        self.default_txt.append(self.canvas.create_text(self.Width*2+14,400,text="Zeel Prajapati ~ 19BCE212",fill=self.outline_color,font="Comic 20 "))
        self.canvas.update()
    
    def Set_Colors(self):
        if(self.Theme_value.get()==1):
            self.background_color="#282828"
            self.button_color="#F13C20"
            self.outline_color="#F13C20"
            self.fill_color="#D2EFF5"
            self.create_outline_color="#16E2F5"
            self.create_fill_color="#FFF380"
            self.delete_outline_color="#CCCCFF"
            self.delete_fill_color="#E41B17"
            self.search_outline_color="#00FF00"
            self.search_fill_color="#FED8B1"
            self.disable_fill="#282828"
            self.disable_outline="black"
        else:
            self.background_color="#C7F6EC"
            self.outline_color="#02231C"
            self.button_color="#FFE5B4"
            self.fill_color="#4DD8AD"
            self.create_outline_color="#F03625"
            self.create_fill_color="#14325C"
            self.delete_outline_color="#F13C20"
            self.delete_fill_color="#282828"
            self.search_outline_color="#F3CD05"
            self.search_fill_color="#36688D"  
            self.disable_fill="#C7F6EC"
            self.disable_outline="White"
        self.Update_Theme_colors()
        self.High_light_color()
            
    def Update_Theme_colors(self):
        self.frame.config(background=self.background_color,highlightbackground=self.outline_color)
        self.canvas.config(background=self.background_color,highlightbackground=self.outline_color)  
        self.MyDelete.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                             fg=self.create_outline_color)
        self.MyInsert.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                             fg=self.create_outline_color)
        self.MySearch.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                             fg=self.create_outline_color)
        self.Insert_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.Search_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.Delete_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.status_bar.config(background=self.fill_color,foreground=self.outline_color)
        self.status_bar_frame.config(background=self.outline_color)
        self.radio_1.config(background=self.background_color,foreground=self.outline_color,activebackground=self.background_color,
                            activeforeground=self.create_outline_color)
        self.radio_2.config(background=self.background_color,foreground=self.outline_color,activebackground=self.background_color,
                            activeforeground=self.create_outline_color)
        
        if(self.number_of_node>0):
            for i in range(0,self.number_of_node):
                self.canvas.itemconfig(self.node[i],outline=self.outline_color,fill=self.fill_color,disabledoutline=self.disable_outline,disabledfill=self.disable_fill)
                self.canvas.itemconfig(self.txt[i],fill=self.outline_color,disabledfill=self.disable_outline)
                if(i>0):
                    self.canvas.itemconfig(self.line[i-1],fill=self.outline_color,disabledfill=self.disable_outline)
            self.canvas.update()
        
        if(self.default_Screen): 
            for i in range(len(self.default_txt)):
                if(i<3):
                    self.canvas.itemconfig(self.default_txt[i],fill=self.fill_color)
                else:
                    self.canvas.itemconfig(self.default_txt[i],fill=self.outline_color)
            
        
    def Create_frame(self): 
        self.frame=Frame(self.GUI,width=50,height=50,highlightthickness=2)
        self.frame.pack(fill=X,padx=0,pady=0)
        self.Input_from_GUI()
        
    def High_light_color(self):
        self.frame.config(highlightcolor=self.outline_color)
        self.canvas.config(highlightcolor=self.outline_color)
        self.status_bar.config(highlightcolor=self.outline_color,highlightbackground=self.create_outline_color,highlightthickness=3)
        self.canvas.update()
        
    def Create_Canvas(self):
        self.scroll_y=Scrollbar(self.GUI,orient="vertical")
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x=Scrollbar(self.GUI,orient='horizontal')
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.canvas=Canvas(self.GUI,borderwidth=0,width=168,height=100,highlightthickness=3,yscrollcommand=self.scroll_y.set,xscrollcommand=self.scroll_x.set)
        self.canvas.pack(fill=BOTH,expand=True,padx=0,pady=0)
        self.Status_bar_variable= StringVar()
        self.Status_bar_variable.set("AVL Visualization")
        self.status_bar_frame=Frame(self.canvas)
        self.status_bar_frame.pack(fill=X,side=TOP)
        self.status_bar = Label(self.status_bar_frame,height=1,textvariable=self.Status_bar_variable,relief="groove",font="Comic 14 bold")
        self.status_bar.pack(fill=X,side=TOP,padx=3,pady=3)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.MyScroll()
        
    def _on_mousewheel(self, e): 
        self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")

    def Input_from_GUI(self):
        
        self.MyInsert = Button(self.frame,text="Insert",command=self.create_node,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyDelete = Button(self.frame,text="Delete",command=self.delete_node,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)               
        self.MySearch = Button(self.frame,text="Search",command=self.search_node,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyInsert.grid(row=7,column=4,padx=5,pady=10)
        self.MyDelete.grid(row=7,column=6,padx=5)
        self.MySearch.grid(row=7,column=8,padx=5)
        self.Insert_value = StringVar()
        self.Delete_value = StringVar()
        self.Search_value = StringVar()  
        self.Insert_Entry = Entry(self.frame,textvariable=self.Insert_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Delete_Entry = Entry(self.frame,textvariable=self.Delete_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Search_Entry = Entry(self.frame,textvariable=self.Search_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Insert_Entry.grid(row=7,column=3,padx=10)
        self.Delete_Entry.grid(row=7,column=5,padx=10)
        self.Search_Entry.grid(row=7,column=7,padx=10)
        self.radio_1=Radiobutton(self.frame,text="Dark mode",font="Comic 10 bold",variable=self.Theme_value,value=1,command=self.Set_Colors)
        self.radio_1.grid(row=7,column=10,padx=20)
        self.radio_2=Radiobutton(self.frame,text="Light mode",font="Comic 10 bold",variable=self.Theme_value,value=2,command=self.Set_Colors)
        self.radio_2.grid(row=7,column=11,padx=10)
        
    def Disable_inputs(self,state):
        self.Insert_Entry.config(state=state)
        self.Delete_Entry.config(state=state)
        self.Search_Entry.config(state=state)
        self.radio_1.config(state=state)
        self.radio_2.config(state=state)
        
    def Disable_data(self,state,index):
        for i in range(0,len(self.node)):
            if(not i in index):
                self.canvas.itemconfig(self.node[i],state=state,disabledoutline=self.disable_outline,disabledfill=self.disable_fill)
                self.canvas.itemconfig(self.txt[i],state=state,disabledfill=self.disable_outline)
                if(i>0):
                    self.canvas.itemconfig(self.line[i-1],state=state,disabledfill=self.disable_outline)
                    
    def check_error(self,str1):
        if(not (str1.strip().isdigit())): 
            messagebox.showerror("Input Error","Error : Invalid input \nPlease enter valid integers!! (Eg. 8) ")
            self.Search_value.set("")
            self.Delete_value.set("")
            self.Insert_value.set("")
            return True
        else:
            return False

    def search_node(self):
        self.High_light_color()
        self.Status_bar_variable.set("Search : "+self.Search_value.get())
        if(self.check_error(self.Search_value.get())):
            self.Status_bar_variable.set("Tree is Empty!!")
            self.Search_value.set("")
            return
        if(self.number_of_node<1):
            messagebox.showerror("Input Error","Error : Invalid input \nYou don't have elements in tree!! (first add) ")
            self.Status_bar_variable.set("Tree is Empty!!")
            self.Search_value.set("")
            return
        self.Disable_inputs(DISABLED)
        self.AVL.path.clear()
        self.AVL.roots.clear()
        search_check=self.AVL.search(self.AVL.root,int(self.Search_value.get()))
        self.canvas.create_oval(50,50,125,125,width=5,outline=self.search_outline_color,fill=self.search_fill_color,tags="ID_search_node",)
        self.canvas.create_text(87.5,87.5,text=""+self.Search_value.get().strip(),fill=self.search_outline_color,font="Comic 15 bold",tags="ID_search_txt")
        if(not search_check):
            self.AVL.path=self.AVL.path[0:len(self.AVL.path)-1]
        value=int(self.Search_value.get().strip())
        self.Move_node("ID_search_node","ID_search_txt",value,True,False)
        if(search_check):
            self.Status_bar_variable.set(f"Search found for {value} at height {len(self.AVL.path)}")
        else:
            self.Status_bar_variable.set(f"Search not found for {value}!!")
        if(search_check):
            for i in range(0,500):
                self.canvas.itemconfig("ID_search_node",fill=self.search_outline_color,outline=self.search_fill_color)
                self.canvas.itemconfig("ID_search_txt",fill=self.search_fill_color)
                self.canvas.update()
                self.canvas.itemconfig("ID_search_node",fill=self.fill_color,outline=self.outline_color,width=5)
                self.canvas.itemconfig("ID_search_txt",fill=self.outline_color)
                self.canvas.update()
            self.canvas.itemconfig("ID_search_node",fill=self.search_outline_color,outline=self.search_fill_color)
            self.canvas.itemconfig("ID_search_txt",fill=self.search_fill_color)
            self.canvas.update()
            time.sleep(1)
            self.canvas.delete("ID_search_node")
            self.canvas.delete("ID_search_txt")
        else:
            for i in range(0,int(self.Set_Cordinates(0,self.Width,self.AVL.path))):
                self.canvas.move("ID_search_node",-1,0)
                self.canvas.move("ID_search_txt",-1,0)
                self.canvas.update()
            self.canvas.delete("ID_search_node")
            self.canvas.delete("ID_search_txt")  
            self.canvas.update()
            time.sleep(1)
            
        self.Search_value.set("")
        self.Disable_inputs(NORMAL)
        self.Status_bar_variable.set("")
    
    def create_node(self):
        self.High_light_color()
        self.Status_bar_variable.set("Insert : "+self.Insert_value.get())
        if(self.check_error(self.Insert_value.get())):
            return
        self.Disable_inputs(DISABLED)
        if(self.default_Screen):
            self.default_Screen=False
            self.canvas.delete("all")
        self.AVL.path.clear()
        self.AVL.roots.clear()
        self.AVL.AVL_Check.clear()
        self.AVL.root=self.AVL.insert(int(self.Insert_value.get().strip()),self.AVL.root)    
        y_point=len(self.AVL.path)
        self.node.append(self.canvas.create_oval(50,50,125,125,width=5,outline=self.create_outline_color,fill=self.create_fill_color))
        self.txt.append(self.canvas.create_text(87.5,87.5,text=""+self.Insert_value.get().strip(),fill=self.create_outline_color,font="Comic 15 bold"))
        self.canvas.update()
        value=int(self.Insert_value.get().strip())
        self.node_value.append(value)
        self.cordinates_path.append(self.AVL.path.copy())
        self.Move_node(self.node[self.number_of_node],self.txt[self.number_of_node],value,True,True)
        if(y_point>0):
            x1=self.Set_Cordinates(0,self.Width,self.AVL.path[:y_point-1])
            x2=self.Set_Cordinates(0,self.Width,self.AVL.path)
            self.create_node_line(x1,x2,y_point,self.AVL.path[y_point-1])

        if(len(self.AVL.AVL_Check)>0):
            self.Move_for_AVL()
        
        if(self.AVL.height(self.AVL.root)>self.Tree_Height):
            self.Tree_Height=self.AVL.height(self.AVL.root)    
            self.set_canvas()
        
        self.number_of_node+=1
        self.canvas.update()
        self.Disable_inputs(NORMAL)
        self.Status_bar_variable.set("After Insert : "+self.Insert_value.get())
        self.Insert_value.set("")
        
    def Move_for_AVL(self):
        for moves in self.AVL.AVL_Check:
            self.Status_bar_variable.set(f'{moves["case"]} {moves["rot"]} \t Left Height : {moves["L"]} | Right Height : {moves["R"]}')
            self.canvas.update()
            time.sleep(1)
            y=[]
            index=[]
            for data in moves["value"]:
                i=self.node_value.index(data)
                while(i in index):
                    i=self.node_value.index(data,i+1)
                y.append(len(self.cordinates_path[i]))
                index.append(i)
            index.sort()
            y.sort()

            self.Disable_data(DISABLED,index)
            if(moves["case"]=="CASE 2" or moves["case"]=="CASE 3"):
                x1=self.Set_Cordinates(0,self.Width,self.cordinates_path[index[2]])
                x2=self.Set_Cordinates(0,self.Width,self.cordinates_path[index[2]][0:-1])
                if(self.cordinates_path[index[2]][-1]=="R"):
                    self.cordinates_path[index[2]][-1]="L"
                    j=-1
                else:
                    self.cordinates_path[index[2]][-1]="R"
                    j=1
                time.sleep(1)
                n=abs(int(x1-x2))
                o=self.change_Height/n
                for p in range(0,n):
                    self.canvas.move(self.node[index[1]],j,o)
                    self.canvas.move(self.txt[index[1]],j,o)
                    self.canvas.move(self.node[index[2]],j,-1*o)
                    self.canvas.move(self.txt[index[2]],j,-1*o)
                    self.canvas.update()
                time.sleep(1)
                x1=self.Set_Cordinates(0,self.Width,self.cordinates_path[index[2]])
                x2=self.Set_Cordinates(0,self.Width,self.cordinates_path[index[2]][0:-1])
                y1=len(self.cordinates_path[index[2]])*self.change_Height
                self.canvas.delete(self.line[index[2]-1])
                if(j==1):
                    self.line[index[2]-1]=self.canvas.create_line(x2+75,y1-self.change_Height+37.5,x1+37.5,y1,fill=self.outline_color,width=5)
                else:
                    self.line[index[2]-1]=self.canvas.create_line(x2,y1-self.change_Height+37.5,x1+37.5,y1,fill=self.outline_color,width=5)
                self.canvas.update()    
                time.sleep(1)
                for change in [self.node_value,self.node,self.txt]:
                    temp=change[index[1]]
                    change[index[1]]=change[index[2]]
                    change[index[2]]=temp
                self.canvas.delete(self.line[index[2]-1])
            x=[]
            for i in index:
                x.append(self.Set_Cordinates(0,self.Width,self.cordinates_path[i]))
            x=[abs(x[i]-x[i-1]) for i in range(1,3)]
            y=y[0:-1]
            if(y[0]==0):
                root_replace=-50
            else:
                root_replace=0
            if(self.cordinates_path[index[2]][-1]=='L'):
                self.cordinates_path[index[0]]=self.cordinates_path[index[0]]+["R"]
                self.cordinates_path[index[1]]=self.cordinates_path[index[1]][0:-1]
                j=1
            else:
                self.cordinates_path[index[0]]=self.cordinates_path[index[0]]+["L"]
                self.cordinates_path[index[1]]=self.cordinates_path[index[1]][0:-1]
                j=-1
            self.cordinates_path[index[2]]=self.cordinates_path[index[2]][0:-1]
            for p in range(0,int(max(x))):
                self.canvas.move(self.node[index[1]],j*x[0]/max(x),-1*(self.change_Height+root_replace)/max(x))
                self.canvas.move(self.txt[index[1]],j*x[0]/max(x),-1*(self.change_Height+root_replace)/max(x))
                self.canvas.move(self.node[index[0]],j*x[0]/max(x),(self.change_Height+root_replace)/max(x))
                self.canvas.move(self.txt[index[0]],j*x[0]/max(x),(self.change_Height+root_replace)/max(x))
                self.canvas.move(self.node[index[2]],j*x[1]/max(x),-1*(self.change_Height)/max(x))
                self.canvas.move(self.txt[index[2]],j*x[1]/max(x),-1*(self.change_Height)/max(x))
                self.canvas.update()
            for change in [self.cordinates_path,self.node_value,self.node,self.txt]:
                temp=change[index[0]]
                change[index[0]]=change[index[1]]
                change[index[1]]=temp
            self.Disable_data(NORMAL,index)
            time.sleep(1)
            for i in range(0,len(self.node_value)):
                if(i in index):
                    continue
                self.AVL.path.clear()
                self.AVL.roots.clear()
                _=self.AVL.search(self.AVL.root,self.node_value[i])
                self.cordinates_path[i]=self.AVL.path.copy()
                self.canvas.coords(self.node[i],50,50,125,125)
                self.canvas.coords(self.txt[i],87.5,87.5)
                self.Move_node(self.node[i],self.txt[i],self.node_value[i],False,False)
                self.Set_Colors()
            self.Set_Lines()
    
    def delete_node(self):
        self.High_light_color()
        self.Status_bar_variable.set("Delete : "+self.Delete_value.get())
        if(self.check_error(self.Delete_value.get())):
            self.Status_bar_variable.set("Tree is Empty!!")
            self.Delete_value.set("")
            return
        if(self.number_of_node<1):
            messagebox.showerror("Input Error","Error : Invalid input \nYou don't have elements in tree!! (first add)")
            self.Status_bar_variable.set("Tree is Empty!!")
            self.Delete_value.set("")
            return
        self.Disable_inputs(DISABLED)
        value=int(self.Delete_value.get().strip())
        self.AVL.path.clear()
        self.AVL.roots.clear()
        self.AVL.AVL_Check.clear()
        case_number,successor_value_1=self.AVL.delete_find(self.AVL.root,value)
        if(case_number==None):
            self.Status_bar_variable.set(f" Value {value} is not present in Tree ")
            self.Delete_value.set("")
            self.Disable_inputs(NORMAL)
            return
        change_index_1=self.cordinates_path.index(self.AVL.path)
        self.canvas.itemconfig(self.node[change_index_1],fill=self.delete_fill_color,outline=self.delete_outline_color)
        self.canvas.itemconfig(self.txt[change_index_1],fill=self.delete_outline_color)
        self.canvas.update()
        check_case1=False
        self.Status_bar_variable.set(f" Delete : {case_number} >>> For value : {value} successor is : {successor_value_1}")
        self.canvas.update()                
        time.sleep(2)
        self.canvas.itemconfig(self.node[change_index_1],fill=self.fill_color,outline=self.outline_color)
        self.canvas.itemconfig(self.txt[change_index_1],fill=self.outline_color)
        self.canvas.update()
        if(case_number != "case 4"):
            self.canvas.itemconfig(self.txt[change_index_1],text=""+str(successor_value_1),fill=self.outline_color)
            change_index=self.node_value.index(successor_value_1)
            self.node_value[change_index_1]=successor_value_1
            change_index_1=change_index

        self.node_value.pop(change_index_1)
        self.cordinates_path.pop(change_index_1)
        self.canvas.delete(self.node[change_index_1])
        self.canvas.delete(self.txt[change_index_1])
        self.node.pop(change_index_1)
        self.txt.pop(change_index_1)
        self.AVL.root=self.AVL.delete(self.AVL.root,value)
        
        self.number_of_node-=1
        if(len(self.AVL.AVL_Check)>0):
            self.Move_for_AVL()
        if(self.AVL.height(self.AVL.root)<self.Tree_Height):
            self.Tree_Height=self.AVL.height(self.AVL.root)    
            self.set_canvas(Increase_Width=False)
        
        self.Delete_value.set("")
        self.canvas.update()
        self.Disable_inputs(NORMAL)
        if(self.number_of_node==1):
            self.Status_bar_variable.set(f"Now {self.node_value[0]} its becomes our new root!!")
            self.canvas.update()
            time.sleep(1)
            self.Status_bar_variable.set(f"After Delete : {value}")    
        elif(self.number_of_node==0):
            self.Status_bar_variable.set(f"Now Tree becomes Empty!!")
            self.canvas.update()
            time.sleep(1)
            self.default_Screen=True
            self.set_defaul_Screen()
        else:
            self.Status_bar_variable.set(f"After Delete : {value}")    
        for i in range(0,len(self.node_value)):
            self.AVL.path.clear()
            self.AVL.roots.clear()
            _=self.AVL.search(self.AVL.root,self.node_value[i])
            self.cordinates_path[i]=self.AVL.path.copy()
            self.canvas.coords(self.node[i],50,50,125,125)
            self.canvas.coords(self.txt[i],87.5,87.5)
            self.Move_node(self.node[i],self.txt[i],self.node_value[i],False,False)
            self.Set_Colors()
        
        self.Set_Lines()
        
            
    def set_canvas(self,Increase_Width=True):
        if(Increase_Width):
            new_width_2=self.change_width
            new_width_1=0
        else:
            new_width_1=-1*self.change_width
            new_width_2=0
        for i in range(0,len(self.cordinates_path)):
            x1=self.Set_Cordinates(0,self.Width+new_width_1,self.cordinates_path[i])
            x2=self.Set_Cordinates(0,self.Width+new_width_2,self.cordinates_path[i])
            if(Increase_Width):
                self.canvas.move(self.node[i],x2-x1,0)
                self.canvas.move(self.txt[i],x2-x1,0)
            else:
                self.canvas.move(self.node[i],x1-x2,0)
                self.canvas.move(self.txt[i],x1-x2,0)
        if(Increase_Width):
            self.Width=self.Width+self.change_width
            self.Height=self.Height+self.change_Height
        else:
            self.Width=self.Width-self.change_width
            self.Height=self.Height-self.change_Height
        self.Set_Lines()
        self.canvas.update()
        self.MyScroll()          
        
    def Set_Lines(self):
        for i in range(len(self.line)):
            self.canvas.delete(self.line[i])
        self.line.clear()
        for i in range(1,len(self.cordinates_path)):
            y1=len(self.cordinates_path[i])
            x1=self.Set_Cordinates(0,self.Width,self.cordinates_path[i][:y1-1])
            x2=self.Set_Cordinates(0,self.Width,self.cordinates_path[i])
            self.create_node_line(x1,x2,y1,self.cordinates_path[i][-1])
                      
    def Set_Cordinates(self,start,end,l):
        for i in l:
            if(i=="L"):
                end=(start+end)/2
            else:
                start=(start+end)/2+1
        return((start+end)/2-37.5)  
       
    def create_node_line(self,x1,x2,y2,move):
        if(y2==1):
            y1=87.5
        else:
            y1=37.5
        if(move=="L"):
            self.line.append(self.canvas.create_line(x1,(self.change_Height*(y2-1))+y1,x2+37.5,y2*self.change_Height,width=5,fill=self.outline_color))
        else:
            self.line.append(self.canvas.create_line(x1+75,(self.change_Height*(y2-1))+y1,x2+37.5,y2*self.change_Height,width=5,fill=self.outline_color))
        self.canvas.update()
        
    def Move_node(self,ID1,ID2,value,show_update,change_color):       
        if(change_color):
            if(show_update):
                time.sleep(1)
            self.canvas.itemconfig(ID1,fill=self.create_fill_color,outline=self.create_outline_color,width=5)
            self.canvas.itemconfig(ID2,fill=self.create_outline_color,font="Comic 15 bold")
        x1=self.Set_Cordinates(0,self.Width,[])
        if(self.number_of_node==0):
            self.Status_bar_variable.set(f"Now {value} is root Node for AVL")
        for i in range(0,int(x1-50)):
            self.canvas.move(ID1,1,0)
            self.canvas.move(ID2,1,0)
            if(show_update):
                self.canvas.update()
        
        if(show_update):
            time.sleep(1)
        
        if(self.number_of_node>0):
            l=[]
            y_point=int(self.change_Height-50)
            for k in range(0,len(self.AVL.path)):
                if(show_update):
                    if(self.AVL.path[k]=="L"):
                        self.Status_bar_variable.set(f"For value {value}<{self.AVL.roots[k]} move to left")
                    else:
                        self.Status_bar_variable.set(f"For value {value}>{self.AVL.roots[k]} move to Right")
                l.append(self.AVL.path[k])
                x_point=int(self.Set_Cordinates(0,self.Width,l))
                if(x1>x_point):
                    x_point=x1-x_point
                else:
                    x_point=x_point-x1
                x_point=int(x_point)
                check_negative=1
                if(self.AVL.path[k]=="L"):
                    check_negative=-1
                if(x_point>y_point):
                    point_1=x_point
                    step2=y_point/x_point
                    step1=1
                else:
                    point_1=y_point
                    step1=x_point/y_point
                    step2=1
                for i in range(0,point_1):
                    self.canvas.move(ID1,step1*check_negative,step2)
                    self.canvas.move(ID2,step1*check_negative,step2)
                    if(show_update):
                        self.canvas.update()
                if(show_update):
                    time.sleep(1)
                x1=int(self.Set_Cordinates(0,self.Width,l))
                if(k==0):
                    y_point=y_point+50
        if(change_color):
            self.canvas.itemconfig(ID1,outline=self.outline_color,fill=self.fill_color)
            self.canvas.itemconfig(ID2,fill=self.outline_color)
    
    def MyScroll(self):   
        self.canvas.config(scrollregion=(0,0,self.Width+self.change_width,self.Height+self.change_Height))
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)
        self.canvas.update()
                
t = Tree();
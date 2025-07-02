from tkinter import Image
from PIL import Image
from tkinter import ttk,messagebox
from customtkinter import *
import customtkinter as CTK
import database
#functions


def search_customer():
     if searchEntry.get()=='':
         messagebox.showerror("Error","Enter value to search")
     elif searchBox.get()=='search By':
         messagebox.showerror("Error","Please Select an option ")
     else:
         searched_data=database.search(searchBox.get(),searchEntry.get())  
         print(searched_data)  
         
         
        


def delete_customer():
    selected_item=  tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to Delete')
    else:
        database.delete(idEntry.get())  
        treeview_data()  
        clear()
        messagebox.showerror('Error ','Data is Deleted')


def update_customer():
    selected_item=  tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),genderBox.get(),salaryEntry.get())   
        treeview_data() 
        clear()
        messagebox.showinfo('Success','Data is Updated')
    


def selection(event):
    select_items= tree.selection()
    if select_items:
        row= tree.item(select_items)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        genderBox.set(row[3])
        salaryEntry.insert(0,row[4])
        
    


def clear(value= False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    genderBox.set('Male')
    salaryEntry.delete(0,END)

    
def treeview_data():
    customers = database.fetch_customer()
    tree.delete(*tree.get_children())
    for customer in customers:
        clean_data = [str(item).strip("(),'") for item in customer]
        tree.insert("", 'end', values=clean_data)



def add_customer():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='' :
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')
            
        



#GUI 

window=CTk()
window.geometry('900x550')
window.resizable(False,False)
window.title("Bank system")
window.configure(fg_color ='#beccea')

logo=CTkImage(Image.open('logo1.webp'),size=(1000,150))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)
logoLabel.place(x=-100,y=7)


leftFram=CTkFrame(window,fg_color='#beccea')
leftFram.grid(row=1,column=0)
leftFram.place(x=-5,y=150)

idLabel=CTkLabel(leftFram,text='Id',font=('arial',18,'bold'),text_color='#cc3434')
idLabel.grid(row=0,column=0,padx=10,pady=15,sticky='w')

idEntry=CTkEntry(leftFram,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)



nameLabel=CTkLabel(leftFram,text='Name',font=('arial',18,'bold'),text_color='#cc3434')
nameLabel.grid(row=1,column=0,padx=10,pady=15,sticky='w')

nameEntry=CTkEntry(leftFram,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)


phoneLabel=CTkLabel(leftFram,text='Phone',font=('arial',18,'bold'),text_color='#cc3434')
phoneLabel.grid(row=2,column=0,padx=10,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFram,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)


genderLabel=CTkLabel(leftFram,text='Gender',font=('arial',18,'bold'),text_color='#cc3434',)
genderLabel.grid(row=3,column=0,padx=10,pady=15,sticky='w')

gender_options=['Male','Femal']

genderBox=CTkComboBox(leftFram,values=gender_options,width=180,font=('arial',15,'bold'),text_color='#cc3434',state='readonly')
genderBox.grid(row=3,column=1,padx=10,pady=15,sticky='w')
genderBox.set('Male')

salaryLabel=CTkLabel(leftFram,text='Salary',font=('arial',18,'bold'),text_color='#cc3434')
salaryLabel.grid(row=4,column=0,padx=10,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFram,font=('arial',15,'bold'),text_color='#cc3434',width=180)
salaryEntry.grid(row=4,column=1)

rightFram=CTkFrame(window)
rightFram.grid(row=1,column=1)
rightFram.place(x=275,y=150)



search_options=['Id','Name','Phone','Gender','Salary']

searchBox=CTkComboBox(rightFram,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('search By')


searchEntry=CTkEntry(rightFram)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFram,text='Search',width=100,command=search_customer)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFram,text='Show All',width=100)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFram,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Gender',width=200)
tree.column('Salary',width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',12),rowheight=20,background="#beccea",foreground='white')

scrollbar=ttk.Scrollbar(rightFram,orient=VERTICAL,)
scrollbar.grid(row=1,column=4,sticky='ns')

buttonFram=CTkFrame(window,fg_color='#beccea')
buttonFram.grid(row=2,column=0)
buttonFram.place(x=30,y=500)

newButton=CTkButton(buttonFram,text="New Customer",font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFram,text="Add Customer",font=('arial',15,'bold'),width=160,corner_radius=15,command=add_customer)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFram,text="Update Customer",font=('arial',15,'bold'),width=160,corner_radius=15,command=update_customer)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFram,text="Delete Customer",font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_customer)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

delete_allButton=CTkButton(buttonFram,text="Delete All Customer",font=('arial',15,'bold'),width=160,corner_radius=15)
delete_allButton.grid(row=0,column=4,pady=5,padx=5)


treeview_data()
window.bind('<ButtonRelease>', selection)

window.mainloop()








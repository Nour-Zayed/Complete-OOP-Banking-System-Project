import customtkinter as CTK
from PIL import Image
from tkinter import messagebox


def login():
    if user_name_Entry.get()=='' or password_Entry.get()=='':
        messagebox.showerror('Error','ALL fielfs are required')
    elif user_name_Entry.get()=='Nour' and password_Entry.get()=='123':
        messagebox.showinfo('success','login is success')
        root.destroy()
        import ems
            
    else:
        messagebox.showerror('Error','wrong ')
            


root = CTK.CTk()  # Corrected CTK.CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('Login Page')

# Load and set the image
image = CTK.CTkImage(Image.open(r'cover1.jpg'), size=(930, 478))  # Ensure 'cover.webp' is present
image_label = CTK.CTkLabel(root, image=image)  # Corrected CTKLabel usage
image_label.place(x=20, y=0)
headinglable=CTK.CTkLabel(root,text='Bank system',bg_color='#FAFAFA',font=('Goudy Old Style',35,'bold'),text_color='red')
headinglable.place(x=20,y=100)
user_name_Entry=CTK.CTkEntry(root,placeholder_text='Enter you name',width=130)
user_name_Entry.place(x=50,y=150)
password_Entry=CTK.CTkEntry(root,placeholder_text='Enter your password',width=130,show='*')
password_Entry.place(x=50,y=200)


loginButton=CTK.CTkButton(root,text='Login',cursor='hand2',command=login,width=100)
loginButton.place(x=100,y=250)

# Start the main loop
root.mainloop()

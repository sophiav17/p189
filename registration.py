import hashlib 
from tkinter import *
from firebase import firebase
import messagebox

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.configure(background = "SteelBlue1")

firebase = firebase.FirebaseApplication("https://p188-9504d-default-rtdb.europe-west1.firebasedatabase.app/", None)

login_username_entry = ""
login_password_entry = ""

def login(): 
    print("login function")
    global login_password_entry
    global login_username_entry
    username = login_username_entry.get()
    password = login_password_entry.get()
    encrypted_password = haslib.md5(password.encode())
    hexadecimal_password = encrypted_password.hexdigest()
    get_password = firebase.get('/', username)
    print(hexadecimal_password)
    if(get_password != None) :
        if(get_password == hexadecimal_password) :
            successful_log_in = messagebox.showinfo("Successfully logged in")
        else : 
            check_password = messagebox.showinfo("Please check ypur password")
    else : 
        register = messagebox.showinfo("User not registered! \n Get yourself registered first to login")                

def register(): 
    print("register function")
    username = login_username_entry.get()
    password = login_password_entry.get()
    ciphercode = hashblib.md5(password)
    ciphercode_encrypt = ciphercode.hexdigest()
    firebase.put("/", username, ciphercode_encrypt)
    
messagebox = messagebox.showinfo("User is registered")     
    
def login_window():
    global login_password_entry
    global login_username_entry
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.configure(background = "peach puff")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold', bg = "peach puff")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13', bg = "peach puff")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13', bg = "peach puff")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT, bg = "DarkSlateGrey1", fg ="black")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    registration_window.destroy()
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', bg = "peach puff")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg = "peach puff")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg = "peach puff")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10, bg = "DarkSlateGrey1", fg = "black")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT, bg = "DarkSlateGrey1", fg = "black")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from tkinter import filedialog
from PIL import ImageTk, Image
from Encryptor import Encryptor

def Log():
    # Creating a new window
    Login = tk.Tk()
    Login.geometry('500x500')
    Login.title('Login to System !')

    # Background Colors
    Login.configure(background='#7fb8f5')

    # Locking the window size
    Login.resizable(width=False, height=False)

    # Creating title icon
    Login.iconbitmap('img/loginlogo.ico')

    # Top Frame
    top_frame = Label(Login, text='Login',font = ('Cosmic', 25, 'bold'), bg='#bbfa0c',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='White')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Creating function for connecting to database and checking username
    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Oops', 'Enter Username !!')
        elif password_entry.get() == '':
            ms.showerror('Oops', 'Enter Password !!')
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()
            # Making connection
            conn = sqlite3.connect('Database.db')
            # Creating cursor
            with conn:
                cursor = conn.cursor()
            # Searching for users
            find_user = ('SELECT * FROM Users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()
            print(results)  
            # if user then new window
            if results:
                Login.destroy()
                system1 = tk.Tk()
                # Creating size of window
                system1.geometry('500x500')
                # Background Colors
                system1.configure(background='#7fb8f5')
                # Locking the window size
                system1.resizable(width=False, height=False)
                # Creating Title
                system1.title('Encrypt and Decrypt System')
                
                # Top Frame
                top_frame1 = Label(system1, text='WELCOME TO THE ImCrypt',font = ('Cosmic', 25, 'bold'), bg='#bbfa0c',relief='groove',padx=500, pady=30)
                top_frame1.pack(side='top')
                # Creating Frame
                frame1 = LabelFrame(system1, padx=50, pady=30, bg='white', bd='5', relief='groove')
                frame1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                key1 = tk.Label(frame1, text = 'Key.', font=('Arial',12, 'bold'), bg='white', fg='green')
                key1_entry = tk.Entry(frame1, font=('Arial',12,'normal'), bg='#FBB13C')
                key1.pack()
                key1_entry.pack()
                # Label for seperating Buttons
                label = Label(frame1, bg='white').pack()
                
                def encrypt1():
                    conn1 = sqlite3.connect('Database.db')
                    with conn1:
                        cursor1 = conn1.cursor()
                    # Searching for users
                    find_key = ('SELECT * FROM Users')
                    cursor1.execute(find_key)
                    key_users = cursor1.fetchall()
                    print(username)
                    for key_user in key_users:
                        #print(key_user[2])
                        if (username == key_user[2]):
                            key = key_user[4]
                            #print(type(key_user[4]))
                    print(len(str(key)))  
                    if key1_entry.get() == '': 
                        ms.showerror('Oops', 'Enter key !!')
                    elif key1_entry.get() == str(key):    
                        file1 = filedialog.askopenfile(mode='r')
                        if file1 is not None:
                            file_name = file1.name
                            enc = Encryptor(str(key))
                            enc.encrypt_file(file_name)
                            
                    else:
                        ms.showerror('Oops', 'Key is invalid !!')
                        
                def decrypt1():
                    conn1 = sqlite3.connect('Database.db')
                    with conn1:
                        cursor1 = conn1.cursor()
                    # Searching for users
                    find_key = ('SELECT * FROM Users')
                    cursor1.execute(find_key)
                    key_users = cursor1.fetchall()
                    print(username)
                    for key_user in key_users:
                        #print(key_user[2])
                        if (username == key_user[2]):
                            key = key_user[4]
                            #print(type(key_user[4]))
                    print(len(str(key)))  
                    if key1_entry.get() == '': 
                        ms.showerror('Oops', 'Enter key !!')
                    elif key1_entry.get() == str(key):    
                        file1 = filedialog.askopenfile(mode='r')
                        if file1 is not None:
                            file_name = file1.name
                            file1.close()
                            enc = Encryptor(str(key))
                            enc.decrypt_file(file_name)
                            
                    else:
                        ms.showerror('Oops', 'Key is invalid !!')
                        
                # Creating Encrypt button and positioning it
                Encrypt = tk.Button(frame1, text = "Encrypt", width="10", bd = '3', command = encrypt1, font = ('Times', 12, 'bold'), bg='#097eeb',relief='groove', justify = 'center', pady='5')
                Encrypt.pack()
                label = Label(frame1, bg='white').pack()
                # Creating Decrypt button and positioning it   
                Decrypt = tk.Button(frame1, text = "Decrypt", width="10", bd = '3',  command = decrypt1, font = ('Times', 12, 'bold'), bg='#4018f2',fg='white', relief='groove', justify = 'center', pady='5')
                Decrypt.pack()
                
                # Quit Button of main frame 
                def Quit():
                    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
                    if response == 1:
                        system.destroy()
                    else:
                        pass
                    
                Quit = tk.Button(system1, text = "Quit", width="10", command = system1.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
                Quit.place(anchor ='sw',rely=1,relx=0.775)
                
                # Displyaing Widget to Screen
                system1.mainloop()
            else:
                ms.showerror('Oops','User Not Found !! Check Username and Password Again !!')

    # creating a label for username and password using Label 
    username = tk.Label(frame, text = 'Username',font=('Arial',12, 'bold'),bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'),bg='white', fg='green')   

    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'), show = '*', justify = 'center', bg='#FBB13C') 
    password_entry.bind('<Return>', Search)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Login', command = Search, width="10",bd = '3',  font = ('Times', 12, 'bold'), bg='#097eeb', fg='white',relief='groove', justify = 'center', pady='5') 

    # Placing the label and entry   
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Login, text = "Quit", width="10", command = Login.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
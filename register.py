from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from tkinter import filedialog
from PIL import ImageTk, Image

def is_number_tryexcept(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# Creating register function
def Register():
    
    # Creating a new window
    Reg = tk.Tk()
    Reg.title('Register in System')
    Reg.geometry('700x700')

    # Background Colors
    Reg.configure(background='#7fb8f5')

    # Locking the window size
    Reg.resizable(width=False, height=False)

    # Creating title icon
    Reg.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Reg, text='Registration',font = ('Cosmic', 25, 'bold'), bg='#bbfa0c',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Connecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        name = name_entry.get()
        email = email_entry.get()        
        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()
        key = key_entry.get()

        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(name)
        validation.append(email)
        validation.append(username)
        validation.append(password)
        validation.append(confirm)
        validation.append(key)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
            # Making connection
            conn = sqlite3.connect('Database.db')

                #Creating cursor
            with conn:
                cursor = conn.cursor() 
            # Searching for users
            find_user = ('SELECT Username FROM Users ')
            cursor.execute(find_user)
            results = cursor.fetchall()
            condi = True
            for result in results:
                #print(type(str(result)))
                #print(str(result[0]))
                #print(username_entry.get())
                if (username_entry.get() == str(result[0])):
                 #   print(result)
                    condi = False
                    break
            # Checking for password match
            flag = 0
            while True:   
                if (len(password)<8): 
                    flag = -1
                    break
                elif not re.search("[a-z]", password): 
                    flag = -1
                    break
                elif not re.search("[A-Z]", password): 
                    flag = -1
                    break
                elif not re.search("[0-9]", password): 
                    flag = -1
                    break
                elif not re.search("[!@#$%^&*_]", password): 
                    flag = -1
                    break
                elif re.search("\s", password): 
                    flag = -1
                    break
                else: 
                    flag = 0
                    break
              
            if flag ==-1: 
                ms.showerror('Your password ss not strong enough!!!',' A strong password must contain number, lowercase, uppercase, special character: !@#$%^&*_ and without space')
                #top_frame = Label(ms, text=' A strong password must contain number, lowercase, uppercase, special character: !@#$%^&*_ and without space')
            elif password != confirm:
                ms.showerror('Oops', 'Password Does Not Match!!!')    
            elif is_number_tryexcept(key) == False:
                ms.showerror('Oops', 'Please Enter a Valid Key!!!')
                
            elif condi == False:
                ms.showerror('Username already used')
            else:        
                # Making table if not exist
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL, Key TEXT NOT NULL)')

                # Inserting Data into Table
                cursor.execute('INSERT INTO Users (FullName, Email, Username, Password, Key) VALUES (?,?,?,?,?)', (name, email, username, password, key))
                conn.commit()

                # Showing success message
                ms.showinfo('Successful', 'Account Created Successfully!! Now You Can Login To System!!')

                # Closing the window
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
    
    # creating a label for username and password using Label
    name = tk.Label(frame, text = 'Full Name', font=('Arial',12, 'bold'), bg='white', fg='green')
    email = tk.Label(frame, text = 'Email', font=('Arial',12, 'bold'), bg='white', fg='green')
    username = tk.Label(frame, text = 'Username', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'), bg='white', fg='green')
    confirm = tk.Label(frame, text = 'Confirm Password', font=('Arial',12, 'bold'), bg='white', fg='green')
    key = tk.Label(frame, text = 'Key.', font=('Arial',12, 'bold'), bg='white', fg='green')

    # creating a entry for elements and returning values to the databse function
    name_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#FBB13C')
    name_entry.bind("<Return>", database)
    email_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    email_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#FBB13C')
    password_entry.bind("<Return>",database)
    confirm_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#FBB13C')
    confirm_entry.bind("<Return>",database)
    key_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#FBB13C')
    key_entry.bind("<Return>",database)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#4018f2', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    name.pack()
    name_entry.focus_set()
    name_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    email.pack()
    email_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    username.pack() 
    username_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    confirm.pack()
    confirm_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    key.pack()
    key_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
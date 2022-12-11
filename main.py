from cryptography.fernet import Fernet
import tkinter
import pyperclip

def show_help():
    helpWin = tkinter.Tk()
    helpWin.geometry("650x220")
    helpWin.title("helpWin")
    
    helpText = '''
    Everything works around keys. Think of keys as the password to the message. 
    === Anyone with the key can unlock the message ===
    
    Message encryption:
    1. To encrypt ("lock") a message, you need a key. To get one, press "generate key". This will copy it to your clipboard.
    2. paste that key into the "key" box.
    3. put the message you wish to encrypt / lock in the "token" box.
    4. press encrypt.
    
    Message decryption:
    1. To decrypt a message ("Unlock"), you need the key it was encrypted ("locked") with.
    2. paste the correct key into the "key" box.
    3. put the encrypted ("locked") message into the "token" box.
    4. press decrypt.
    '''
    
    help_text = tkinter.Label(helpWin, text=helpText)
    help_text.pack(anchor="w")
    
    helpWin.mainloop()

def generate_key():
    output_key = str(Fernet.generate_key())
    output_key = output_key[2:]
    output_key = output_key[:-1]
    pyperclip.copy(output_key)
    print("(Copied to clipboard)")
    print(output_key)
    
def get_key():
    global key
    try:
        key = Fernet(key_ent.get())
    except ValueError:
        print("Invalid key.")
        


def encryptFunc():
    get_key()
    try:
        encrypted_token = key.encrypt(bytes(str(token_ent.get()), encoding="utf-8"))
        encrypted_token = str(encrypted_token)[2:]
        encrypted_token = encrypted_token[:-1]
        print("Encrypted text:")
        print("=========================")
        print(encrypted_token)
        print("=========================")
    except NameError:
        print("No key given")

    
def decodeFunc():
    get_key()
    try:
        decoded_token = key.decrypt(bytes(str(token_ent.get()), encoding="utf-8"))
        decoded_token = str(decoded_token)[2:]
        decoded_token = decoded_token[:-1]
        print("Decrypted text:")
        print("=========================")
        print(decoded_token)
        print("=========================")
    except NameError:
        print("No key given")
        
def mainWin():
    global key_ent
    global token_ent
    
    main = tkinter.Tk()
    main.geometry("300x300")
    main.title("EDV4.1")
    key_status = tkinter.IntVar()
    # 0 = unchecked
    # 1 = checked

    key_ent = tkinter.Entry(main, bg="#E0E5F7", show="*")
    key_lab = tkinter.Label(main, text="Key:")
    
    def key_hide():
        if key_status.get() == 0:
            key_ent.config(show="*")
        else:
            key_ent.config(show="")
            
    key_visable = tkinter.Checkbutton(main, text="show key", variable=key_status, onvalue=1, offvalue=0, command=key_hide)
    
    
    
    gen_button = tkinter.Button(main, text="Generate key", command=generate_key)
    
    token_ent = tkinter.Entry(main, bg="#E0E5F7")
    token_lab = tkinter.Label(main, text="Token:")
    
    encrypt_button = tkinter.Button(main, text="Encrypt", command=encryptFunc)
    decode_button = tkinter.Button(main, text="decode", command=decodeFunc)
    
    help_button = tkinter.Button(main, text="Help", command=show_help)
    
    key_lab.place(x=1,y=1)
    key_ent.place(x=30,y=3)
    key_visable.place(x=150,y=1)
    
    token_lab.place(x=1,y=28)
    token_ent.place(x=43,y=30, width=180)
    
    encrypt_button.place(x=1,y=55)
    decode_button.place(x=53,y=55)
    gen_button.place(x=1, y=85)
    help_button.place(x=80, y=85)
        
    main.mainloop()
    
mainWin()
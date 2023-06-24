from tkinter import *
import random
 
root = Tk() 
root.title("SPYDER DEBERIA DE TENER VIRUS") 
root.geometry("800x400") 
root.configure(background = "dark gray");

label_name=Label(root,text="juicy farts")
label_primera_letra=Label(root, fg="black", padx="20", pady="15")
label_ultima_letra=Label(root, fg="black", padx="20", pady="15")

def obtenerLetras():
    word=label_name["text"]
    label_primera_letra["text"]="primera letra "+ word[0]  
    word=label_name["text"]
    label_ultima_letra["text"]="ultima letra "+ word[-1] 
    
btn = Button(root,text="jijijija",command=obtenerLetras,bg="gray")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)    

label_name.place(relx=0.5,rely=0.3,anchor=CENTER)
label_primera_letra.place(relx=0.5,rely=0.6,anchor=CENTER)
label_ultima_letra.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()

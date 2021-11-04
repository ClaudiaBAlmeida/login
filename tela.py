#criando uma janela de login.
#importando a tkinter toda para criar nossa janela...
from tkinter import *

tela = Tk() #instanciando a classe Tk(), tela agora é uma instância de Tk(), abrindo o programa.
lb1 = Label(tela, text="Login:")
lb2 = Label(tela, text="Senha:")

#tela.geometry("")
tela.title("Login")

edit1 = Entry(tela,) #entry é semelhante ao input do html e js.
edit2 = Entry(tela,)

but1 = Button(tela, text = "Confirmar")

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
edit1.grid(row=0,column=1)
edit2.grid(row=1,column=1)
but1.grid(row=2,column=1)

tela.geometry("200x100+100+100")

#encerra o programa.
tela.mainloop()



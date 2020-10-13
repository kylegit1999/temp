from tkinter import*




#calulations

def calculate():
    celc_Temp = celTempVar.get()
    fahr_Temp = fahTempVar.get()

    if celTempVar.get() !=0.0:
        celc_To_fahr = float((float(celc_Temp) * 9 / 5) + 32)
        print(celc_To_fahr)
        fahTempVar.set(celc_To_fahr)

    elif fahTempVar.get()!=0.0:
            fahr_To_celc = float((float(fahr_Temp) - 32) * 5 / 9)
            print(fahr_To_celc)
            celTempVar.set(fahr_To_celc)

#clear button

def clear():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    clear_message = Label(top, text = "Cleared")
    clear_button = Button(top, text="OK", command=top.destroy)
    clear_message.grid(row = 0, padx = 5, pady = 5)
    clear_button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)
    fahTempVar.set(int(0))
    celTempVar.set(int(0))

#adding a title

temp = Tk()
temp.title("Temperature Converter by the one and only KYLE SASHIN PHILLIPS")
temp.geometry("1500x750")
temp.configure(background="cyan")


#declarings
celTempVar = IntVar()
celTempVar.set(int(0))
fahTempVar = IntVar()
fahTempVar.set(int(0))

#adding labels,entries and grid
celLabel = Label (temp, text = "Celcius: ", fg = "red",)
celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)
celLabel.configure(background="cyan")

fahLabel = Label (temp, text = "Fahrenheit: ", fg = "blue")
fahLabel.grid(row = 2, column = 2, pady = 10, sticky = NW)
fahLabel.configure(background="cyan")

celEntry = Entry (temp, width = 10, bd = 5, textvariable = celTempVar, state=DISABLED)
celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


fahEntry = Entry (temp, width = 10, bd = 5, textvariable = fahTempVar, state=DISABLED)
fahEntry.grid(row = 2, column = 2, pady = 10, sticky = NW, padx = 125 )

calcButton=Button (temp, text = "Calculate Conversion", justify = CENTER, command = calculate)
calcButton.grid(row = 4, column = 1)


clearButton = Button (temp, text = "Clear", justify = CENTER,command = clear)
clearButton.grid(row = 5, column = 1)

#exit button

def exit():
    temp = Tk()


def exit_window():
    temp.destroy()

#active buttons

def act_cel():
    celEntry.configure(state=NORMAL)
button = Button (text= "exit" , command= exit_window)
button.grid(row=7 ,column=1)



B1=Button(temp, text="activate celcius",command=act_cel)
B1.grid(row= 11,column=10, pady=10)

def act_fah():
    fahEntry.configure(state=NORMAL)
B2= Button(temp , text="activate fahrenheit", command= act_fah)
B2.grid(row=10 ,column=10, pady=10)


temp.mainloop()
# the end

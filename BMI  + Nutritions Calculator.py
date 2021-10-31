from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk



root = Tk()
root.geometry("1750x790+0+0")
root.resizable(0,0)
root.title("BMI + NUTRITIONS CALCULATOR")

global BMI

def BMI_Cal():
    Bheight = float(var2.get())
    Bweight = float(var1.get())
    BMI = str('%.2f' %(Bweight / (Bheight * Bheight)))
    labelBMIResult.config(text = BMI)
    
    
var1 = DoubleVar()
var2 = DoubleVar()

Tops = Frame(root, width = 1350, height = 50, bd = 8, relief = "raise")
Tops.pack(side = TOP)

f1 = Frame(root, width = 600, height = 600, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, bd = 8, relief = "raise")
f2.pack(side = RIGHT)

f1a = Frame(f1, width = 600, height = 200, bd = 20, relief = "raise")
f1a.pack(side = TOP)

f1b = Frame(f1, width = 600, height = 600, bd = 20, relief = 'raise')
f1b.pack(side=TOP)

label1Title = Label(Tops, text = "          BODY MASS INDEX + NUTRITION CALCULATOR          ", padx = 16, pady = 16, bd = 16, fg = '#000000', font = ("times new roman", 54, 'bold'), bg = "powder blue", relief = 'raise', width = 42, height = 1)
label1Title.pack()

labelweight = Label(f1a, text = "Select Weight in Kilograms", font =('times new roman', 20, 'bold'), bd = 20).grid(row = 0, column = 0)
Bodyweight = Scale(f1a, variable = var1, from_ = 1, to = 500, length = 880, tickinterval = 30, orient = HORIZONTAL)
Bodyweight.grid(row = 1, column = 0)

labelheight = Label(f1b, text = "Enter Height in Meters", font =('times new roman', 20, 'bold'), bd = 20).grid(row = 0, column = 0)
textheight = Entry(f1b, textvariable = var2, font = ('times new roman', 16, 'bold'), bd = 16, width = 22, justify = 'center')
textheight.grid(row = 1, column = 0)

labelBMIResult = Label(f1b, padx = 16, pady = 16, bd = 16, fg = '#000000', font = ('times new roman', 30, 'bold'), bg = 'sky blue', relief = 'sunk', width = 34, height = 1)
labelBMIResult.grid(row = 2, column = 0)

labelBMITable = Label(f2, font  = ("times new roman", 20, 'bold'), text = 'BMI Table').grid(row = 0, column = 0)
txtlabelBMITable = Text(f2, height = 13, width = 38, bd = 16, font = ("times new roman", 12, 'bold'))
txtlabelBMITable.grid(row = 1, column = 0)

txtlabelBMITable.insert(END, 'Meaning \t\t' + "BMI \n\n")
txtlabelBMITable.insert(END, 'Normal weight \t\t' + "19 - 24.9 \n\n")
txtlabelBMITable.insert(END, 'Overwight \t\t' + "25 - 29.9 \n\n")
txtlabelBMITable.insert(END, 'Obesity level I \t\t' + "30 - 34.9 \n\n")
txtlabelBMITable.insert(END, 'Obesity level II \t\t' + "35 - 39.9\n\n")
txtlabelBMITable.insert(END, 'Obesity level III \t\t' + ">= 40\n\n")

def popup():
    messagebox.showinfo("NUTRITIONS TAKEN DEPENDING ON BMI RESULTS", "\n ....THIS IS FOR ONLY TEST PURPOUSE....\n############################# \n         If BMI is Between 19 - 24.9 \n                     BREAKFAST\n6 Eggs + Black Coffee + 3Date(Khajur)\n                        LUNCH\n6 Eggs + Black Coffee + 3Date(Khajur)\n                       DINNER\n6 Eggs + Black Coffee + 3Date(Khajur)\n\n         If BMI is Between 25 - 29.9 \n                     BREAKFAST\n6 Eggs + Black Coffee + 3Date(Khajur)\n                        LUNCH\n6 Eggs + Black Coffee + 3Date(Khajur)\n                       DINNER\n6 Eggs + Black Coffee + 3Date(Khajur)\n\n         If BMI is Between 30 - 35.9 \n                     BREAKFAST\n6 Eggs + Black Coffee + 3Date(Khajur)\n                        LUNCH\n6 Eggs + Black Coffee + 3Date(Khajur)\n                       DINNER\n6 Eggs + Black Coffee + 3Date(Khajur)\n\n         If BMI is Between 36 - 39.9 \n                     BREAKFAST\n6 Eggs + Black Coffee + 3Date(Khajur)\n                        LUNCH\n6 Eggs + Black Coffee + 3Date(Khajur)\n                       DINNER\n6 Eggs + Black Coffee + 3Date(Khajur)\n\n                   If BMI is =>40 \n                     BREAKFAST\n6 Eggs + Black Coffee + 3Date(Khajur)\n                        LUNCH\n6 Eggs + Black Coffee + 3Date(Khajur)\n                       DINNER\n6 Eggs + Black Coffee + 3Date(Khajur)\n#############################\n ....THIS IS FOR ONLY TEST PURPOUSE....")   
button = Button(root, text="NUTRITIONS NEEDED",padx = 8, pady = 8, bd = 12, width = 21,font = ("times new roman", 20, 'bold'), command=popup)
button.place(x=600, y=710)

btnBMI = Button(f2, text = "Click to \nCheck Your \nBMI", padx = 8, pady = 8, bd = 12, width = 21, font = ("times new roman", 20, 'bold'), height = 3, command = BMI_Cal)
btnBMI.grid(row = 2, column = 0)

root.mainloop()
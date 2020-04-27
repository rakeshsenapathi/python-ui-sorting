from tkinter import *
from sortingFunctions import sortData

root = Tk()
root.resizable(False, False)

# Create canvas
canvas = Canvas(root,  height = 400, width = 400 , bg = "#263D42")
canvas.pack()

# Create frame
inputFrame = Frame(root, bg = "white")
inputFrame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

# Input data
lblInputData = Label(inputFrame,
                    text = "Enter Numbers: ",
                    padx = 20,
                    pady = 20,
                    bg = "white"
                    ).grid(row = 1)
inputData = Entry(inputFrame)
inputData.grid(row = 1, column = 1)

# Create Tkinter variable
tk_var = StringVar(root)

#Dictionary with options
options = { 'Bubble Sort', 'Insertion Sort','Merge Sort', 'Quick Sort', 'Radix Sort','Heap Sort'}
tk_var.set('Choose Sorting Type')

dropDownList = OptionMenu(inputFrame, tk_var, *options).place(relx = 0.25, rely = 0.2)

lblOutputData = Label(inputFrame,
                    text = "Output : ",
                    padx = 20,
                    pady = 20,
                    bg = "white"
                    )
lblOutputData.place(relx = 0.2, rely = 0.6)

def handleBtnClick():
    outputData = sortData(inputData.get(), tk_var.get())
    lblOutputData.config(text = outputData)

submitButton = Button(inputFrame, text = "Sort", command = handleBtnClick).place(relx = 0.4, rely = 0.4)


if(__name__ == "__main__"):
    root.mainloop()




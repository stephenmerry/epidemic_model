#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 13:09:19 2020

@author: stephen
"""

import tkinter


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tkinter.Frame(root)
        lab = tkinter.Label(row, width=15, text=field, anchor='w')
        ent = tkinter.Entry(row)
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        lab.pack(side=tkinter.LEFT)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
        entries.append((field, ent))
    return entries



root = tkinter.Tk()
root.title('Epidemic simulation')

inputs_frame = tkinter.LabelFrame(root, text='Inputs', padx=50, pady=50)
inputs_frame.grid(row=0, column=0, padx=10, pady=10)

input_fields = 'Exposure rate', 'Incubation rate', 'Removal rate'

input_entries = makeform(inputs_frame, input_fields)
run_button = tkinter.Button(inputs_frame, text='Run simulation')
run_button.pack(padx=5, pady=5)

outputs_frame = tkinter.LabelFrame(root, text='List of events', padx=50, pady=50)
outputs_frame.grid(row=0, column=1, padx=10, pady=10)

event_string = 'Start\nAt time 0.0632688629034041, 0 became infectious\nAt time 0.3092424212188679, 8 became infectious\nAt time 0.5491598985077621, 17 was exposed to the disease by 0\nAt time 0.5664804673306401, 19 was exposed to the disease by 8\nAt time 0.5764497573908832, 18 was exposed to the disease by 0\nAt time 0.8020626926437653, 36 was exposed to the disease by 8\nAt time 1.0393284954254716, 35 was exposed to the disease by 0\nAt time 1.286754977676229, 18 became infectious\nAt time 1.6218414470739906, 25 was exposed to the disease by 18\nAt time 1.6761945675345253, 8 was removed\nAt time 2.3661681332706106, 35 became infectious\nAt time 2.527410040859951, 22 was exposed to the disease by 18\nAt time 2.6265014141317464, 31 was exposed to the disease by 0\nAt time 2.635962197416795, 18 was removed\nAt time 2.7847578041915466, 6 became infectious\nAt time 3.5152775341751155, 6 was removed\nAt time 3.5865322968070115, 25 became infectious\nAt time 4.279627255753461, 7 was exposed to the disease by 25\nAt time 4.346988952697706, 14 was exposed to the disease by 25\nAt time 5.258114366370176, 19 became infectious\nAt time 5.532719219133595, 27 was exposed to the disease by 0\nAt time 5.725158574864219, 20 was exposed to the disease by 35\nAt time 6.454010747766796, 14 became infectious\nAt time 6.960400874110934, 5 was exposed to the disease by 35\nAt time 7.533771650726041, 36 became infectious\nAt time 8.360919105504792, 22 became infectious\nAt time 10.860635124374499, 20 became infectious\nAt time 12.50571523552862, 13 was exposed to the disease by 14\nAt time 12.622197094630632, 19 was removed\nAt time 13.4894420382596, 32 was exposed to the disease by 22\nAt time 14.070357548834075, 33 was exposed to the disease by 22\nAt time 15.023988484631547, 37 was exposed to the disease by 22\nAt time 15.596537489603106, 20 was removed\nAt time 16.33765563519461, 37 became infectious\nAt time 16.49779805172774, 37 was removed\nAt time 17.782290737255284, 4 was exposed to the disease by 25\nAt time 17.915503302355635, 13 became infectious\nAt time 18.184261067792193, 14 was removed\nAt time 18.505368912702487, 7 became infectious\nAt time 19.831125193632534, 35 was removed\nAt time 20.62400414733926, 24 was exposed to the disease by 22\nAt time 20.81679788754102, 39 was exposed to the disease by 36\nAt time 21.2982596535806, 4 became infectious\nAt time 21.808490232443866, 7 was removed\nAt time 21.93080713311244, 27 became infectious\nAt time 22.25837464058676, 29 was exposed to the disease by 25\nAt time 22.56867166120905, 25 was removed\nAt time 23.088686592162013, 0 was removed\nAt time 23.440291599638655, 21 was exposed to the disease by 27\nAt time 24.875298125804726, 13 was removed\nAt time 25.233181438356503, 10 was exposed to the disease by 27\nAt time 25.440110868267325, 1 was exposed to the disease by 27\nAt time 25.582423829740627, 16 was exposed to the disease by 22\nAt time 25.697364577805992, 5 became infectious\nAt time 25.93347460079911, 2 was exposed to the disease by 27\nAt time 26.145811239701395, 32 became infectious\nAt time 26.27368920764694, 5 was removed\nAt time 26.79947788976163, 16 became infectious\nAt time 26.979292117413916, 34 was exposed to the disease by 32\nAt time 27.03342089510004, 2 became infectious\nAt time 27.042924097617014, 33 became infectious\nAt time 27.056244417301336, 33 was removed\nAt time 28.04462421789214, 17 became infectious\nAt time 29.042626343298604, 10 became infectious\nAt time 29.96695571025963, 17 was removed\nAt time 30.306973884393745, 29 became infectious\nAt time 30.807782114369076, 29 was removed\nAt time 31.849171611600696, 1 became infectious\nAt time 32.45744297087493, 11 was exposed to the disease by 32\nAt time 32.838458133673385, 27 was removed\nAt time 32.86690871089729, 4 was removed\nAt time 34.04002923179267, 15 was exposed to the disease by 32\nAt time 34.33255479674488, 28 was exposed to the disease by 1\nAt time 34.5673782399575, 31 became infectious\nAt time 34.933243266505386, 23 was exposed to the disease by 10\nAt time 35.0820273962255, 39 became infectious\nAt time 35.399349437409, 9 was exposed to the disease by 39\nAt time 35.444984618059934, 23 became infectious\nAt time 35.489077729636165, 10 was removed\nAt time 35.72390727359397, 2 was removed\nAt time 35.91721209583213, 22 was removed\nAt time 36.19551468066174, 36 was removed\nAt time 36.24686052970759, 34 became infectious\nAt time 36.63563432578068, 38 was exposed to the disease by 31\nAt time 37.31051389321278, 9 became infectious\nAt time 37.63479716029849, 38 became infectious\nAt time 37.76906731035308, 28 became infectious\nAt time 37.80667366486299, 39 was removed\nAt time 37.93846882847709, 12 was exposed to the disease by 23\nAt time 38.322137459227285, 24 became infectious\nAt time 38.39545326071746, 24 was removed\nAt time 38.70886136790855, 3 became infectious\nAt time 38.712981437638874, 21 became infectious\nAt time 39.14074415365438, 3 was removed\nAt time 39.18417427123124, 31 was removed\nAt time 39.26630741988434, 26 was exposed to the disease by 21\nAt time 39.890496257936775, 26 became infectious\nAt time 40.01766751997006, 16 was removed\nAt time 40.465552001103504, 32 was removed\nAt time 41.03921057711116, 28 was removed\nAt time 41.10836711922776, 1 was removed\nAt time 41.11956134643466, 26 was removed\nAt time 41.22685419048661, 15 became infectious\nAt time 41.49201245468974, 23 was removed\nAt time 41.51990631600972, 15 was removed\nAt time 41.61944841627967, 38 was removed\nAt time 41.725872331042275, 12 became infectious\nAt time 41.90670897720324, 34 was removed\nAt time 42.09191059924763, 30 was exposed to the disease by 12\nAt time 42.1665172527128, 30 became infectious\nAt time 42.18230961877441, 30 was removed\nAt time 42.25709124731351, 21 was removed\nAt time 42.26639387558013, 11 became infectious\nAt time 42.2771282206791, 12 was removed\nAt time 42.30210304532519, 11 was removed\nAt time 42.30998000987667, 9 was removed\nEnd'
scroll_bar = tkinter.Scrollbar(outputs_frame)
text_block = tkinter.Text(outputs_frame, height=20, width=75)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text_block.pack(side=tkinter.LEFT, fill=tkinter.Y)
scroll_bar.config(command=text_block.yview)
text_block.config(yscrollcommand=scroll_bar.set)
text_block.insert(tkinter.END, event_string)



#b = tkinter.Button(inputs_frame, text="Don't Click Here!")
#b2 = tkinter.Button(inputs_frame, text="Run simulation")
#b.grid(row=0, column=0)
#b2.grid(row=1, column=1)

#b = tkinter.Button(outputs_frame, text="Don't Click Here!")
#b2 = tkinter.Button(outputs_frame, text="Run simulation")
#b.grid(row=0, column=0)
#b2.grid(row=1, column=1)


root.mainloop()

"""
from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="Enter Your Stock Quote", command=myClick)
myButton.pack()



root.mainloop()
"""


"""
import tkinter as tk



def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


root = tk.Tk()
input_entries = makeform(root, input_fields)
run_button = tk.Button(root, text='Run simulation')
run_button.pack(padx=5, pady=5)
root.mainloop()
"""
'''Python Program - Dice Rolling by DJ Harshit'''

#Importing the modules
import tkinter as t
import random as r

#The dice numbers
a = [1,2,3,4,5,6]

#Colors
brwn = '#c88141'
grn = '#52d017'
prpl = '#c12283'
bl = '#6698ff'

wind = t.Tk()

#It gives a random number from list
def no():
        n = r.choice(a)
        l3.config(text=n)

#Main program
wind.title('Dice Rolling')	
wind.geometry('400x400')
wind.resizable(0,0)
wind.config(bg=brwn)

l1 = t.Label(wind, text='Dice Rolling', font=('Bodoni MT', 40, 'bold'), fg=bl, bg=prpl)
l1.pack(pady=10)

l2 = t.Label(wind, text='By Harshit', font=('Arial', 20, 'bold'), fg=grn, bg=prpl)
l2.pack()

b1 = t.Button(wind, text='Click', font=('Arial Black', 20), bg='grey', command=no)
b1.pack(pady=10)

l3 = t.Label(wind, font=('Eras Bold ITC', 50), width=5, fg=bl, bg=prpl)
l3.pack(pady=10)

wind.mainloop()

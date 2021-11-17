from tkinter import *
import random
from tkinter import font
import matplotlib.pyplot as plt
import time
import math
import threading

Bitcoin = 70000000
Ethereum = 5000000
Ripple = 1500
Qtum = 18000
Stellar = 420
Dodge = 300

b_count = 0
e_count = 0
r_count = 0
q_count = 0
s_count = 0
d_count = 0

own_money = 10000


#Use random functions to change the price of coins
def coin(coins1, coins2):
    a = random.randint(1, 4)
    if a == 1:
        coins1 = coins1 - coins2 * random.random() * 0.5
    elif a == 2:
        coins1 = coins1 + coins2 * random.random() * 0.5
    elif a == 3:
        coins1 = coins1 - coins2 * random.random() * 0.8
    else:
        coins1 = coins1 + coins2 * random.random() * 0.8
    return coins1

def cal(coins1, coins2):
    coins = coin(coins1, coins2)
    coins = round(coins)
    return coins

def b1events():
    global b_count, own_money
    if (own_money - cal(Bitcoin, Bitcoin) > 0):
        button1['text'] = "매수"
        button1['fg'] = 'black'
        b_count = b_count + 1
        own_money = own_money - cal(Bitcoin, Bitcoin)
    else :
        button1['text'] = "불가"
        button1['fg'] = 'red'

def b1eventd():
    global b_count, own_money
    if (b_count <= 0):
        button2['text'] = "불가"
        button2['fg'] = 'red'
    else :
        button2['text'] = "매도"
        button2['fg'] = 'black'
        b_count = b_count - 1
        own_money = own_money + cal(Bitcoin, Bitcoin)

def b3events():
    global e_count, own_money
    if (own_money - cal(Ethereum, Ethereum) > 0):
        button3['text'] = "매수"
        button3['fg'] = 'black'
        e_count = e_count + 1
        own_money = own_money - cal(Ethereum, Ethereum)
    else :
        button3['text'] = "불가"
        button3['fg'] = 'red'

def b3eventd():
    global e_count, own_money
    if (e_count <= 0):
        button4['text'] = "불가"
        button4['fg'] = 'red'
    else :
        button4['text'] = "매도"
        button4['fg'] = 'black'
        e_count = e_count - 1
        own_money = own_money + cal(Ethereum, Ethereum)

def b5events():
    global r_count, own_money
    if (own_money - cal(Ripple, Ripple) > 0):
        button5['text'] = "매수"
        button5['fg'] = 'black'
        r_count = r_count + 1
        own_money = own_money - cal(Ripple, Ripple)
    else :
        button5['text'] = "불가"
        button5['fg'] = 'red'

def b5eventd():
    global r_count, own_money
    if (r_count <= 0):
        button6['text'] = "불가"
        button6['fg'] = 'red'
    else :
        button6['text'] = "매도"
        button6['fg'] = 'black'
        r_count = r_count - 1
        own_money = own_money + cal(Ripple, Ripple)

def b7events():
    global q_count, own_money
    if (own_money - cal(Qtum, Qtum) > 0):
        button7['text'] = "매수"
        button7['fg'] = 'black'
        q_count = q_count + 1
        own_money = own_money - cal(Qtum, Qtum)
    else :
        button7['text'] = "불가"
        button7['fg'] = 'red'

def b7eventd():
    global q_count, own_money
    if (q_count <= 0):
        button8['text'] = "불가"
        button8['fg'] = 'red'
    else :
        button8['text'] = "매도"
        button8['fg'] = 'black'
        q_count = q_count - 1
        own_money = own_money + cal(Qtum, Qtum)

def b9events():
    global s_count, own_money
    if (own_money - cal(Bitcoin, Bitcoin) > 0):
        button9['text'] = "매수"
        button9['fg'] = 'black'
        s_count = s_count + 1
        own_money = own_money - cal(Stellar, Stellar)
    else :
        button9['text'] = "불가"
        button9['fg'] = 'red'

def b9eventd():
    global s_count, own_money
    if (s_count <= 0):
        button10['text'] = "불가"
        button10['fg'] = 'red'
    else :
        button10['text'] = "매도"
        button10['fg'] = 'black'
        s_count = s_count - 1
        own_money = own_money + cal(Stellar, Stellar)

def b11events():
    global d_count, own_money
    if (own_money - cal(Dodge, Dodge) > 0):
        button11['text'] = "매수"
        button11['fg'] = 'black'
        d_count = d_count + 1
        own_money = own_money - cal(Dodge, Dodge)
    else :
        button11['text'] = "불가"
        button11['fg'] = 'red'

def b11eventd():
    global d_count, own_money
    if (d_count <= 0):
        button12['text'] = "불가"
        button12['fg'] = 'red'
    else :
        button12['text'] = "매도"
        button12['fg'] = 'black'
        d_count = d_count - 1
        own_money = own_money + cal(Dodge, Dodge)

root = Tk()
root.title("Stoct Game")
root.geometry("1000x500")

#####################label#########################

label = Label(root, text= "Stock Game")
label.pack()

label = Label(root, text= "Bitcoin", font = (30))
label.place(x=70, y=50)

label1 = Label(root, text= "{}".format(Bitcoin), font = (30))   
label1.place(x=50, y=70)

label = Label(root, text= "Ethereum", font = (30))
label.place(x=460, y=50)

label2 = Label(root, text= "{}".format(Ethereum), font = (30))   
label2.place(x=455, y=70)

label = Label(root, text= "Ripple", font = (30))
label.place(x=800, y=50)

label3 = Label(root, text= "{}".format(Ripple), font = (30))   
label3.place(x=793, y=70)

label = Label(root, text= "Qtum", font = (30))
label.place(x=70, y=250)

label4 = Label(root, text= "{}".format(Qtum), font = (30))   
label4.place(x=62, y=270)

label = Label(root, text= "Stellar", font = (30))
label.place(x=470, y=250)

label5 = Label(root, text= "{}".format(Stellar), font = (30))   
label5.place(x=470, y=270)

label = Label(root, text= "Dodge", font = (30))
label.place(x=800, y=250)

label6 = Label(root, text= "{}".format(Dodge), font = (30))   
label6.place(x=800, y=270)

label = Label(root, text = "잔고", font = (30))
label.place(x = 710, y = 370)

label7 = Label(root, text = "{}".format(own_money), font = (30))
label7.place(x = 685, y = 400)

label = Label(root, text = "총 잔액", font = (30))
label.place(x = 190, y = 370)

label8 = Label(root, text = "{}".format(own_money + (Bitcoin * b_count) + (Ethereum * e_count) + (Ripple * r_count) + (Qtum * q_count) + (Stellar * s_count) + (Dodge * d_count)), font = (30))
label8.place(x = 170, y = 400)

############################button#####################################

button1 = Button(root, command= b1events, text="매수", font = 30)
button1.place(x= 40, y=90)

button2 = Button(root, command= b1eventd, text="매도", font = 30)
button2.place(x= 100, y=90)

button3 = Button(root, command= b3events, text="매수", font = 30)
button3.place(x= 445, y=90)

button4 = Button(root, command= b3eventd, text="매도", font = 30)
button4.place(x= 505, y=90)

button5 = Button(root, command= b5events, text="매수", font = 30)
button5.place(x= 770, y=90)

button6 = Button(root, command= b5eventd, text="매도", font = 30)
button6.place(x= 830, y=90)

button7 = Button(root, command= b7events, text="매수", font = 30)
button7.place(x= 40, y=290)

button8 = Button(root, command= b7eventd, text="매도", font = 30)
button8.place(x= 100, y=290)

button9 = Button(root, command= b9events, text="매수", font = 30)
button9.place(x= 445, y=290)

button10 = Button(root, command= b9eventd, text="매도", font = 30)
button10.place(x= 505, y=290)

button11 = Button(root, command= b11events, text="매수", font = 30)
button11.place(x= 770, y=290)

button12 = Button(root, command= b11eventd, text="매도", font = 30)
button12.place(x= 830, y=290)


def upd():
    global Bitcoin, Ethereum, Ripple, Qtum, Stellar, Dodge, own_money, b_count, e_count, r_count, q_count, s_count, d_count
    label1.config(text="{0:,} 원".format(cal(Bitcoin, Bitcoin)))
    label2.config(text="{0:,} 원".format(cal(Ethereum, Ethereum)))
    label3.config(text="{0:,} 원".format(cal(Ripple ,Ripple)))
    label4.config(text="{0:,} 원".format(cal(Qtum, Qtum)))
    label5.config(text="{0:,} 원".format(cal(Stellar, Stellar)))
    label6.config(text="{0:,} 원".format(cal(Dodge, Dodge)))
    label7.config(text="{0:,} 원".format(own_money))
    label8.config(text="{0:,} 원".format(own_money + (cal(Bitcoin, Bitcoin) * b_count) + (cal(Ethereum, Ethereum) * e_count) + (cal(Ripple, Ripple) * r_count) + (cal(Qtum, Qtum) * q_count) + (cal(Stellar, Stellar) * s_count) + (cal(Dodge, Dodge) * d_count)))

    threading.Timer(1, upd).start()
upd()

root.mainloop()

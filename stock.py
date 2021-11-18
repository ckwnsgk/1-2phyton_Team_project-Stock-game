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

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

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

def upd():
    global a, b, c, d, e, f, own_money, b_count, e_count, r_count, q_count, s_count, d_count
    a = cal(Bitcoin, Bitcoin)
    b = cal(Ethereum, Ethereum)
    c = cal(Ripple ,Ripple)
    d = cal(Qtum, Qtum)
    e = cal(Stellar, Stellar)
    f = cal(Dodge, Dodge)
    label1.config(text="{0:,} 원".format(a))
    label2.config(text="{0:,} 원".format(b))
    label3.config(text="{0:,} 원".format(c))
    label4.config(text="{0:,} 원".format(d))
    label5.config(text="{0:,} 원".format(e))
    label6.config(text="{0:,} 원".format(f))
    label7.config(text="{0:,} 원".format(own_money))
    label8.config(text="{0:,} 원".format(own_money + (a * b_count) + (b * e_count) + (c * r_count) + (d * q_count) + (e * s_count) + (f * d_count)))
    label9.config(text="    {}           {}             {}        {}         {}        {}".format(b_count, e_count, r_count, q_count, s_count, d_count))

    threading.Timer(1, upd).start()

def b1events():
    global b_count, own_money
    if (own_money - a) > 0:
        button1['text'] = "매수"
        button1['fg'] = 'black'
        b_count = b_count + 1
        own_money = own_money - a
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
        own_money = own_money + a

def b3events():
    global e_count, own_money
    if (own_money - b > 0):
        button3['text'] = "매수"
        button3['fg'] = 'black'
        e_count = e_count + 1
        own_money = own_money - b
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
        own_money = own_money + b

def b5events():
    global r_count, own_money
    if (own_money - c > 0):
        button5['text'] = "매수"
        button5['fg'] = 'black'
        r_count = r_count + 1
        own_money = own_money - c
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
        own_money = own_money + c

def b7events():
    global q_count, own_money
    if (own_money - d > 0):
        button7['text'] = "매수"
        button7['fg'] = 'black'
        q_count = q_count + 1
        own_money = own_money - d
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
        own_money = own_money + d

def b9events():
    global s_count, own_money
    if (own_money - e > 0):
        button9['text'] = "매수"
        button9['fg'] = 'black'
        s_count = s_count + 1
        own_money = own_money - e
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
        own_money = own_money + e

def b11events():
    global d_count, own_money
    if (own_money - f > 0):
        button11['text'] = "매수"
        button11['fg'] = 'black'
        d_count = d_count + 1
        own_money = own_money - f
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
        own_money = own_money + f




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

label8 = Label(root, text = "{}".format(own_money), font = (30))
label8.place(x = 185, y = 400)

label = Label(root, text = "Bitcoin  Ethereum  Ripple  Qtum  Stellar  Dodge", font = (30))
label.place(x = 310, y = 430)

label9 = Label(root, text = "    {}             {}              {}                 {}              {}               {}" .format(b_count, e_count, r_count, q_count, r_count, q_count), font = (30))
label9.place(x = 310, y = 450)

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
    
upd()

root.mainloop()

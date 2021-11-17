# -*- coding: utf-8 -*-
import sys
import random
from tkinter import *


tried = 0
number_length = 3
target_number = ''


# define functions
def procInput(event):
    global tried

    user_input = entry.get()
    entry.delete(0, END)
    if len(user_input) != number_length or not user_input.isdigit():
        listbox.insert(END, '%d개의 숫자를 입력해 주세요' % number_length)
        return
    if len(set(user_input)) < number_length:
        listbox.insert(END, '중복되지 않은 %d개의 숫자를 입력해 주세요' % number_length)
        return

    tried += 1
    strike, ball = 0, 0
    for i in range(number_length):
        if user_input[i] == target_number[i]:
            strike += 1
        elif user_input[i] in target_number:
            ball += 1
    gameMsg = '%d : %s >> Strike[%d] Ball[%d]' % (tried, user_input, strike, ball)
    listbox.insert(END, gameMsg)
    if strike == number_length:
        listbox.insert(END, '축하합니다. %d번만에 맞추셨네요' % tried)
        entry.config(state=DISABLED)


# make the random number
def makeNumber():
    numbers = []
    while len(numbers) < number_length:
        number = str(random.randint(1, 9))
        if number not in numbers:
            numbers.append(number)
    return ''.join(numbers)


# start game
def startGame():
    global tried, target_number

    tried = 0
    target_number = makeNumber()
#    print target_number

    entry.delete(0, END)
    listbox.delete(0, END)
    listbox.insert(END, '%d개의 숫자를 입력후 enter를 눌러 주세요' % number_length)


if __name__ == '__main__':
    # declare object
    root = Tk()
    label = Label(root, text='<< 숫자 야구 게임 >>')
    frame1 = Frame(root)
    entryLabel = Label(frame1, text='● 숫자(%d개) ' % number_length)
    entry = Entry(frame1, width=number_length, bg='white')
    initButton = Button(frame1, text='Restart', command=startGame)
    quitButton = Button(frame1, text='Quit', command=root.quit)
    scrbar = Scrollbar(root, orient=VERTICAL)
    listbox = Listbox(root, width=30, height=15, yscrollcommand=scrbar.set)

    # display windows
    label.pack()
    frame1.pack(anchor=W)
    entryLabel.pack(side=LEFT)
    entry.pack(side=LEFT, padx=5)
    initButton.pack(side=LEFT)
    quitButton.pack(side=LEFT)
    listbox.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
    scrbar.pack(side=LEFT, fill=Y, pady=5)
    scrbar.config(command=listbox.yview)
    entry.config(state=NORMAL)
    entry.focus_set()
    entry.bind('<Key-Return>', procInput)

    # main procedure
    startGame()
    root.mainloop()
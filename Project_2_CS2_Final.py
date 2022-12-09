#from tkinter import *

from tkinter import *
import random

def main() -> None:
    '''
    Funtion to run th main program
    :return: None
    '''
    window = Tk()
    window.title('Rock, Paper, Scissors Game')
    window.geometry('600x450')
    window.resizable(False, False)
    frame_title = Frame(window)
    label_title = Label(frame_title, text='Rock Paper Scissors Game')
    label_title.pack()
    frame_title.pack(side='top')

    # competitors identity
    frame_competitors = Frame(window)
    label_title = Label(frame_competitors, text='Player vs Python')
    label_title.pack()
    frame_competitors.pack(side='top')

    tool = Entry(window, font=('times new roman', 25))
    tool.pack()
    def rock() -> None:
        '''
        Funtion for rock selection
        :return: None
        '''
        global selection
        selection = 'rock'
        tool.delete(0, END)
        tool.insert(0, 'rock')

    def paper() -> None:
        '''
        Funcion for paper selection
        :return: None
        '''
        global selection
        selection = 'paper'
        tool.delete(0, END)
        tool.insert(0, 'paper')

    def scissors() -> None:
        '''
        Function for scissors selection
        :return: None
        '''
        global selection
        selection = 'scissors'
        tool.delete(0, END)
        tool.insert(0, 'scissors')

    def battle() -> None:
        '''
        Function for deciding game result
        :return: game results
        '''
        #global player_score
        #player_score = 0
        #global python_score
        #python_score = 0
        weapons = ['rock', 'paper', 'scissors']
        options = random.choice(weapons)
        if selection == 'rock' and options == 'scissors' or selection == 'scissors' and options == 'paper' or selection == 'paper' and options == 'rock':
            tool.delete(0, END)
            tool.insert(0, 'Player wins, Python loses')
        elif selection == 'rock' and options == 'paper' or selection == 'paper' and options == 'scissors' or selection == 'scissors' and options == 'rock':
            tool.delete(0, END)
            tool.insert(0, 'Python loses , Player wins')
        elif selection == options:
            tool.delete(0, END)
            tool.insert(0, 'Game tied')
        print(options)
        #return player_score
        #return python_score


    frame_weapons = Frame(window)
    frame_weapons.pack()
    button_rock = Button(frame_weapons, text='Rock', font=('times new roman', 20), command=rock)
    button_rock.pack(side='left', pady = 30, padx=30)
    button_paper = Button(frame_weapons, text='Paper', font=('times new roman', 20), command=paper)
    button_paper.pack(side='left', pady = 30, padx=30)
    button_scissors = Button(frame_weapons, text='Scissors', font=('times new roman', 18), command=scissors)
    button_scissors.pack(side='left', pady = 30, padx=30)
    button_battle = Button(window, text='Start Battle', font=('times new roman', 16), command=battle)
    button_battle.pack(pady= 20)
    button_endprogram = Button(window, text='End program', font=('times new roman', 0), command=exit)
    button_endprogram.pack()
    #frame_results = Frame(window)
    #frame_results.pack()
    #player_score = Label(frame_results)
    #player_score.pack()
    #python_score = Label(frame_results)
    #python_score.pack()
    window.mainloop()

    # test
    #player_score = 0
    #python_score = 0
    #if selection == rock and options == scissors:
    #    player_score = player_score + 1
    #elif selection == rock and options == paper:
    #    python_score = python_score + 1


if __name__ == '__main__':
    main()
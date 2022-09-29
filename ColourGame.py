import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Orange','Black', 'Yellow', 'Purple', 'White', 'Brown']


score = 0

time_remaining = 30


def start_game(event):
    if time_remaining == 30:
        countdown()
    nextcolour()


def nextcolour():
    global score
    global time_remaining

    if time_remaining > 0:

        i.focus_set()

        if i.get().lower() == colours[1].lower():
            score += 1

        i.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score: " + str(score))


def countdown():

    global time_remaining

    if time_remaining > 0:

        time_remaining -= 1

        timeLabel.config(text="Remaining time: " + str(time_remaining))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLOUR GAME")

root.geometry("700x450")

instruction = tkinter.Label(
    root, text="\n Type the colours of the word, not the word text \n", font=('TimesNewRoman', 20))
instruction.pack()

scoreLabel = tkinter.Label(
    root, text="Press Enter to Play \n", font=('TimesNewRoman', 20))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time remaining: " +
                          str(time_remaining), font=('TimesNewRoman', 20))
timeLabel.pack()

label = tkinter.Label(root, borderwidth=3, font=('TimesNewRoman', 20, "bold"))
label.pack()

i = tkinter.Entry(root)

root.bind('<Return>', start_game)
i.pack()

i.focus_set()

root.mainloop()

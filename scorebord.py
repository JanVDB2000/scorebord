from tkinter import *
import random

window = Tk()
window.title("Score Bord")
window.geometry('600x900')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Theme Window
Theme_Colour = "FFFFFF"
Theme_Colour_Secondary = ""
Theme_Colour_Text = "Black"


def SwitchThemeToLight():
    SwitchTheme("#F0F0F0", "White", "Black")


def SwitchThemeToDark():
    SwitchTheme("#2B2B2B", "#3C3F41", "White")


def SwitchTheme(Theme_Color, Theme_Color_Secondary, Theme_Color_Text):
    window.config(bg=Theme_Color)
    btn4.config(bg=Theme_Color_Secondary, foreground=Theme_Colour_Text)
    lbl1.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    entry_1.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    btn2.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    lbl2.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    entry_2.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    btn3.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    lbl3.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    entry_3.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    btn1.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)
    out.config(bg=Theme_Color_Secondary, foreground=Theme_Color_Text)


Menu_Main = Menu(window)
window.config(menu=Menu_Main)

Menu_File = Menu(Menu_Main)

Menu_Theme = Menu(Menu_File)

Menu_Main.add_cascade(label="File", menu=Menu_File)

Menu_File.add_cascade(label="Theme", menu=Menu_Theme)

Menu_Theme.add_command(label="Light", command=SwitchThemeToLight)
Menu_Theme.add_command(label="Dark", command=SwitchThemeToDark)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ----------------------------------------------------------------------------------------------------------------

out = Text(window, width=50, height=48, wrap=WORD, bg="white")
out.grid(column=0, row=25, )
out.delete(1.1, END)

# ----------------------------------------------------------------------------------------------------------------
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Team1Score = 0
Team2Score = 0
Team3Score = 0

DoelpuntenvoorT1 = 0
DoelpuntenvoorT2 = 0
DoelpuntenvoorT3 = 0

DoelpuntentegenT1 = 0
DoelpuntentegenT2 = 0
DoelpuntentegenT3 = 0

DoelpuntensaldoT1 = 0
DoelpuntensaldoT2 = 0
DoelpuntensaldoT3 = 0

T1 = 0
T2 = 0
T3 = 0

VS = ("VS")
HG = ("heeft gewonnen")
ST = ("-")
DP = ("Doelpuntensaldo ->")
PN = ("punten ->")



# --------------------------------------------
# Team 1--------------------------------------
entry_1 = Entry(window, width=10)
entry_1.grid(column=2, row=1)
def clicked():
    global T1
    T1 = entry_1.get()
    string_to_display1 = "Team 1 " + T1
    out.insert(END, "Oke Team 1 werd Geregistreerd als ")  # 1
    out.insert(END, [T1])
    out.insert(END, "\n")
    out.insert(END, "Laden .....\n")  # 2
    lbl1_1 = Label(window)
    lbl1_1["text"] = string_to_display1
    lbl1_1.grid(column=1, row=1)
btn1 = Button(window, text="Button", command=clicked)
lbl1 = Label(window, text="Team 1")
lbl1.grid(column=1, row=1)
btn1.grid(column=3, row=1)

# Team 2--------------------------------------
entry_2 = Entry(window, width=10)
entry_2.grid(column=2, row=2)
def clicked2():
    global T2
    T2 = entry_2.get()
    string_to_display2 = "Team 2 " + T2
    out.insert(END, "Oke Team 2 werd Geregistreerd als ")  # 3
    out.insert(END, [T2])
    out.insert(END, "\n")
    out.insert(END, "Laden .....\n")  # 4

    lbl1_2 = Label(window)
    lbl1_2["text"] = string_to_display2
    lbl1_2.grid(column=1, row=2)
btn2 = Button(window, text="Button", command=clicked2)
lbl2 = Label(window, text="Team 2")
lbl2.grid(column=1, row=2)
btn2.grid(column=3, row=2)

# Team 3--------------------------------------
entry_3 = Entry(window, width=10)
entry_3.grid(column=2, row=3)

def clicked3():
    global T3
    T3 = entry_3.get()
    string_to_display3 = "Team 3 " + T3
    out.insert(END, "Oke Team 3 werd Geregistreerd als ")  # 5
    out.insert(END, [T3])
    out.insert(END, "\n")
    out.insert(END, "Laden .....\n")  # 6

    lbl1_3 = Label(window)
    lbl1_3["text"] = string_to_display3
    lbl1_3.grid(column=1, row=3)

btn3 = Button(window, text="Button", command=clicked3)
lbl3 = Label(window, text="Team 3")
btn3.grid(column=3, row=3)
lbl3.grid(column=1, row=3)
# Start--------------------------------------
def clicked4():
    global Team1Score
    global Team2Score
    global Team3Score

    global DoelpuntenvoorT1
    global DoelpuntenvoorT2
    global DoelpuntenvoorT3

    global DoelpuntentegenT1
    global DoelpuntentegenT2
    global DoelpuntentegenT3

    global DoelpuntensaldoT1
    global DoelpuntensaldoT2
    global DoelpuntensaldoT3

    string_to_display3 = "Start"
    out.insert(END, "START\n")  # 7
    out.insert(END, "Laden .....\n")# 8
    # Score Bord + Tussens Stand + Wedstrijd Volgorden
    # Match 1
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END,  "--==Voebal-Match==--")  # 18
    out.insert(END, "\n")
    out.insert(END, "-------Match 1------\n")  # 9
    out.insert(END, [T1] + [VS] + [T2], END)  # 10
    out.insert(END, "\n")
    DoelpuntenT1 = (random.randint(0, 3))
    DoelpuntenT2 = (random.randint(0, 3))
    out.insert(END, [T1] + [DoelpuntenT1] + [ST] + [DoelpuntenT2] + [T2], )  # 13
    out.insert(END, "\n")
    if DoelpuntenT1 > DoelpuntenT2:
        out.insert(END, [T1] + [HG])  # 14
        out.insert(END, "\n")
        Team1Score = Team1Score + 3
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT2 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT2
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT1
    elif DoelpuntenT1 == DoelpuntenT2:
        out.insert(END, " Draw")  # 15
        out.insert(END, "\n")
        Team1Score = Team1Score + 1
        Team2Score = Team2Score + 1
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT2 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT2
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT1
    else:
        out.insert(END, [T2] + [HG])  # 16
        out.insert(END, "\n")
        Team2Score = Team2Score + 3
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT2 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT2
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT1

    # -------------------------------------------------
    # Match 2
    out.insert(END, "-------Match 2------\n")  # 919
    out.insert(END, [T1] + [VS] + [T3], END)  # 20
    out.insert(END, "\n")
    DoelpuntenT1 = (random.randint(0, 3))
    DoelpuntenT3 = (random.randint(0, 3))
    out.insert(END, [T1] + [DoelpuntenT1] + [ST] + [DoelpuntenT3] + [T3], )  # 13
    out.insert(END, "\n")
    if DoelpuntenT1 > DoelpuntenT3:
        out.insert(END, [T1] + [HG])  # 14
        out.insert(END, "\n")
        Team1Score = Team1Score + 3
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT1
    elif DoelpuntenT1 == DoelpuntenT3:
        out.insert(END, " Draw")  # 15
        out.insert(END, "\n")
        Team1Score = Team1Score + 1
        Team3Score = Team3Score + 1
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT1
    else:
        out.insert(END, [T3] + [HG])  # 14
        out.insert(END, "\n")
        Team3Score = Team3Score + 3
        DoelpuntenvoorT1 = DoelpuntenvoorT1 + DoelpuntenT1
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT1 = DoelpuntentegenT1 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT1
    out.insert(END, "--------------------")  # 18)
    # Match 3
    out.insert(END, "-------Match 3------\n")  # 919
    out.insert(END, [T2] + [VS] + [T3], END)  # 20
    out.insert(END, "\n")
    DoelpuntenT2 = (random.randint(0, 3))
    DoelpuntenT3 = (random.randint(0, 3))
    out.insert(END, [T2] + [DoelpuntenT2] + [ST] + [DoelpuntenT3] + [T3], )  # 13
    out.insert(END, "\n")
    if DoelpuntenT2 > DoelpuntenT3:
        out.insert(END, [T2] + [HG])  # 14
        out.insert(END, "\n")
        Team2Score = Team2Score + 3
        DoelpuntenvoorT2 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT2
    elif DoelpuntenT2 == DoelpuntenT3:
        out.insert(END, " Draw")  # 15
        out.insert(END, "\n")
        Team2Score = Team2Score + 1
        Team3Score = Team3Score + 1
        DoelpuntenvoorT2 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT2
    else:
        out.insert(END, [T3] + [HG])  # 14
        out.insert(END, "\n")
        Team3Score = Team3Score + 3
        DoelpuntenvoorT3 = DoelpuntenvoorT2 + DoelpuntenT2
        DoelpuntenvoorT3 = DoelpuntenvoorT3 + DoelpuntenT3
        DoelpuntentegenT2 = DoelpuntentegenT2 - DoelpuntenT3
        DoelpuntentegenT3 = DoelpuntentegenT3 - DoelpuntenT2
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END, "-+-+-+-+-+-+-+-+-+-+")
    out.insert(END, "\n")
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END, "Laden .....\n")
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END,  "-=De-score--Punten=-")  # 18
    out.insert(END, "\n")


    # Bereken Uitslag
    DoelpuntensaldoT1 = DoelpuntensaldoT1 + DoelpuntenvoorT1 + DoelpuntentegenT1
    DoelpuntensaldoT2 = DoelpuntensaldoT2 + DoelpuntenvoorT2 + DoelpuntentegenT2
    DoelpuntensaldoT3 = DoelpuntensaldoT3 + DoelpuntenvoorT3 + DoelpuntentegenT3

    # Uitslag

    out.insert(END, "--------Team 1------")  # 18
    out.insert(END, "\n")
    out.insert(END, [T1], )  # 13
    out.insert(END, "\n")
    out.insert(END, [PN] + [Team1Score], )  # 13
    out.insert(END, "\n")
    out.insert(END, [DP] + [DoelpuntensaldoT1], )  # 13
    # ---------------------------------------------
    out.insert(END, "\n")
    out.insert(END, "--------Team 2------")  # 18
    out.insert(END, "\n")
    out.insert(END, [T2], )  # 13
    out.insert(END, "\n")
    out.insert(END, [PN] + [Team2Score], )  # 13
    out.insert(END, "\n")
    out.insert(END, [DP] + [DoelpuntensaldoT2], )  # 13
    # ---------------------------------------------
    out.insert(END, "\n")
    out.insert(END, "-------Team 3-------") # 18
    out.insert(END, "\n")
    out.insert(END, [T3], )  # 13
    out.insert(END, "\n")
    out.insert(END, [PN] + [Team3Score], )  # 13
    out.insert(END, "\n")
    out.insert(END, [DP] + [DoelpuntensaldoT3], )  # 13
    out.insert(END, "\n")
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END, "-+-+-+-+-+-+-+-+-+-+")
    out.insert(END, "\n")
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END, "Laden .....\n")
    # uitslag |1 Naar de volgende ronde |2 Moet de Wedstrijd opnieuw doen |3 Gaat naar huis met leggen handen |
    # ScoreBoard
    out.insert(END, "--------------------")  # 18
    out.insert(END, "\n")
    out.insert(END, "---==ScoreBoard==---")  # 18
    out.insert(END, "\n")
    out.insert(END, "-----------------------------------------------")
    out.insert(END, "\n")
    score = [(Team1Score, T1), (Team2Score, T2), (Team3Score, T3)]
    score.sort(reverse=True)
    S1 = (score[0], (" *1* Hij mag naar de volgenden ronden"))
    S2 = (score[1], (" *2* Moet de Wedstrijd opnieuw doen"))
    S3 = (score[2], (" *3* Gaat naar huis met lege handen"))
    out.insert(END, [S1], )  # 13
    out.insert(END, "\n")
    out.insert(END, [S2], )  # 13
    out.insert(END, "\n")
    out.insert(END, [S3], )  # 13
    out.insert(END, "\n")
    out.insert(END, "-----------------------------------------------")  # 18
    out.insert(END, "\n")
    out.update()

btn4 = Button(window, text="Start", command=clicked4)
btn4.grid(column=3, row=4)
# --------------------------------------------
# --------------------------------------------
window.mainloop()


######################
######################
######################
# Gemaakt Door Jan VDB#
#########2019#########
######################
######################

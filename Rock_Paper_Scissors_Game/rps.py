#here i have installed all these libraries 

from tkinter import *
from PIL import Image,ImageTk
from random import randint


window=Tk()
window.title("Rock Paper Scissors Game")
window.config(bg="black")

image_rock1=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\Rock.JPG"))
image_rock2=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\Rock2.JPG"))
image_paper1=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\Paper.JPG"))
image_paper2=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\Paper2.JPG"))
image_scissors1=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\scissors.JPG"))
image_scissors2=ImageTk.PhotoImage(Image.open("C:\\Users\\UNAIB COMPUTERS\\Desktop\\scissors2.JPG"))

label_player=Label(window, image=image_scissors1)
label_computer=Label(window, image=image_scissors2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score=Label(window,text=0,font=("arial",60,"bold"),fg="red")
player_score=Label(window,text=0,font=("arial",60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indicator=Label(window,font=("arial",40,"bold"),
                      text="PLAYER",bg="orange",fg="blue")
computer_indicator=Label(window,font=("arial",40,"bold"),
                      text="COMPUTER",bg="orange",fg="blue")

computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

def update_message(a):
  final_message['text']=a

def computer_update():
  final=int(computer_score['text'])
  final+=1
  computer_score['text']=str(final)

def player_update():
  final=int(player_score['text'])
  final+=1
  player_score['text']=str(final)

def winner_check(p,c):
  if p==c:
    update_message("Its a tie !")

  elif p=="rock":
    if c=="paper":
      update_message("Computer Wins !")
      computer_update()
    else:
      update_message("Player Win !")
      player_update()

  elif p=="paper":
    if c=="scissors":
      update_message("Computer Wins !")
      computer_update()
    else:
      update_message("Player Win !")
      player_update()

  elif p=="scissors":
    if c=="rock":
      update_message("Computer Wins !")
      computer_update()
    else:
      update_message("Player Win !")
      player_update()

  else:
    pass

to_select=['rock','paper','scissors']

def choice_update(a):
  choice_computer=to_select[randint(0,2)]

  if choice_computer=="rock":
    label_computer.config(image=image_rock2)
  elif choice_computer=="paper":
    label_computer.config(image=image_paper2)
  else:
    label_computer.config(image=image_scissors2)
  
  if a=="rock":
    label_player.config(image=image_rock1)
  elif a=="paper":
    label_player.config(image=image_paper1)
  else:
    label_player.config(image=image_scissors1)
  
  winner_check(a,choice_computer)


final_message=Label(window,font=('arial',40,'bold'),bg='red',fg='white')
final_message.grid(row=3,column=2)

button_rock=Button(window,width=16,height=3,text="Rock",
                   font=('arial',20,'bold'), bg='yellow', fg='red', command=lambda:choice_update('rock')).grid(row=2,column=1)

button_paper=Button(window,width=16,height=3,text="Paper",
                   font=('arial',20,'bold'), bg='yellow', fg='red', command=lambda:choice_update('paper')).grid(row=2,column=2)

button_scissors=Button(window,width=16,height=3,text="Scissors",
                   font=('arial',20,'bold'), bg='yellow', fg='red', command=lambda:choice_update('scissors')).grid(row=2,column=3)


window.mainloop()



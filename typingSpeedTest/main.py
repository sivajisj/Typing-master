from tkinter import Tk, Label, PhotoImage, Entry, messagebox
import random

words=['HTML', 'CSS', 'JavaScript', 'Python', 'PHP', 'Ruby', 'Java', 'SQL', 'API', 'Framework',
         'Backend', 'Frontend', 'Database', 'Server', 'Client', 'Browser', 'Node.js', 'Angular',
         'React', 'Vue', 'Bootstrap', 'jQuery', 'Ajax', 'JSON', 'REST', 'GraphQL', 'Django',
         'Flask', 'Express', 'MongoDB', 'MySQL', 'PostgreSQL', 'SQLite', 'Firebase', 'AWS', 'Azure',
         'funny', 'humor', 'general', 'words',
         'apple', 'banana', 'car', 'house', 'tree', 'sun', 'moon', 'star', 'ocean', 'mountain',
         'dog', 'cat', 'bird', 'fish', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'kangaroo']

sliderWords = ""
count = 0
time_left = 60
correct_word = 0
wrong_word = 0
i = 0



# Functionality part

def timer():
    global time_left, i


    if time_left > 0 :
        time_left -= 1
        timer_count_label.config( text=time_left)
        root.after( 1000, timer)
    else:
        wordEntry.config(state="disabled")
        result = correct_word - wrong_word
        instruction_label.config(text=f"Correct words {correct_word}\nWrong_word {wrong_word}\n Final Score {result}")
        if result < 13:
            emoji_label_1.config(image=poor_pic)
            emoji_label_2.config(image=poor_pic)
        elif 13 <= result < 16:
            emoji_label_1.config( image=good_pic)
            emoji_label_2.config( image=good_pic)
        else :
            emoji_label_1.config( image=pro_pic)
            emoji_label_2.config( image=pro_pic)
        res = messagebox.askyesno("Confirm", "Do you want to play again? 😊 ")
        if res:
            i = 0
            time_left = 60
            score_count_label.config(text="0")
            timer_count_label.config(text="60")
            wordEntry.config(state="normal")
            instruction_label.config( text='Type Word And Hit Enter')
            emoji_label_2.config(image="")
            emoji_label_1.config(image="")



def play_game(event):
    if wordEntry.get()!="":
        global i, correct_word, wrong_word
        # print("Entered")
        i += 1
        score_count_label.config( text=i )
        instruction_label.config( text="" )
        if time_left == 60:
            timer()
        if wordEntry.get() == word_list_label["text"]:
            correct_word += 1
        else:
            wrong_word += 1
        random.shuffle( words )
        word_list_label.config( text=words[0] )
        wordEntry.delete( 0, "end" )



def slider():
    global sliderWords, count
    text = "Welcome to Typing Speed Game"
    if count >= len(text):
        count = 0
        sliderWords = ""
    sliderWords = sliderWords+text[count]
    count+=1
    moving_label.configure(text=sliderWords)
    moving_label.after(200,slider)


# UI part
root = Tk()

# Setting title and icon
root.title("Typing Game")
root.iconbitmap("typing.ico")

# Setting width and height of the window
width = 800
height = 600
root.geometry(f"{width}x{height}+250+100")
root.resizable(False, False)

# setting background color
bg_color = "#FFC436"  # Specify your desired background color
root.configure(bg=bg_color)

# Adding image
logoImage = PhotoImage(file="./logo.png")
logoLabel = Label(root, image=logoImage,bg=bg_color)

# arranging place of image
logoLabel.place(x=256, y=50)

# Adding moving Title
moving_label = Label(root, bg=bg_color, font=("arial",25,"bold italic"),
                     width=40, fg="brown")
moving_label.place(x=0, y=10)


# Creating word labe0
word_list_label = Label(root, text=random.choice(words), font=("Impact", 38), bg=bg_color)
word_list_label.place(x=370, y=350, anchor="center")

score_label=Label(root,text='WORDS',font=('Times New Roman',28,'bold'),bg=bg_color)
score_label.place(x=30,y=100)

score_count_label=Label(root,text=0,font=('Times New Roman',28,'bold'),bg=bg_color)
score_count_label.place(x=70,y=180)

time_label=Label(root,text='TIMER',font=('Times New Roman',28,'bold'),bg=bg_color)
time_label.place(x=550,y=100)

timer_count_label=Label(root,text=time_left,font=('Times New Roman',28,'bold'),bg=bg_color)
timer_count_label.place(x=600,y=180)

wordEntry = Entry(root, font=("arial",25, "bold"),bd=8, justify="center")
wordEntry.place(x=200,y=390)
wordEntry.focus_set()

instruction_label = Label(root, text='Type Word And Hit Enter',font=('Garamond',28,'bold'),
                    fg="red",bg=bg_color)
instruction_label.place(x=200,y=450)


# Creating Emojis
poor_pic = PhotoImage(file="poor.png")
good_pic = PhotoImage(file="good.png")
pro_pic = PhotoImage(file="pro.png")
emoji_label_1 = Label(root,bg = bg_color)
emoji_label_1.place(x=100, y=490)
emoji_label_2 = Label(root,bg = bg_color)
emoji_label_2.place(x=620, y=490)
# root.after(1000, timer
root.bind('<Return>', play_game)

slider()
root.mainloop()
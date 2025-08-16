import tkinter as tk
import math
from tkinter import messagebox

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_marks.config(text="")

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="pink")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="green")

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        messagebox.showinfo("Session Complete", "Time is up! Take a break 😊")



window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="white")

title_label = tk.Label(text="Timer", fg="green", bg="white", font=("Arial", 30, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="white", highlightthickness=0)
tomato_img = tk.PhotoImage(file="")

canvas.create_oval(10, 10, 190, 190, outline="red", width=3)
timer_text = canvas.create_text(100, 110, text="00:00", fill="black", font=("Arial", 28, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="white", font=("Arial", 14, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()

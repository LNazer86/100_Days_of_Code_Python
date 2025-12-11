import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"
counter = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(counter)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_seconds)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global counter
    count_minutes = math.floor(count / 60) # floor vrati nejvyssi cele cislo - minuty
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        counter = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        sessions = math.floor(reps/2)
        mark = ""
        for _ in range(sessions):
            mark += checkmark
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro App")

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #highlightthickness odstrani frame
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0, sticky="E") #sticky - zarovnani v gridu, E - east, W - west atd.

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2, sticky="W")

checkmark_label = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)

window.mainloop()
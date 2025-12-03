from time import *
import random as r
import tkinter as tk
from tkinter import messagebox

time_1 = 0
time_2 = 0
testinput = ""

def mistake(paratest, usertest):
    error = 0
    for i in range(min(len(paratest), len(usertest))):
        if paratest[i] != usertest[i]:
            error += 1
    error += abs(len(paratest) - len(usertest))
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    if time_delay == 0:
        return 0
    speed = len(userinput) / time_delay
    return round(speed)

def start_test():
    global test1, time_1
    result_label.config(text="")  
    typing_box.delete("1.0", tk.END)

    test1 = r.choice(test)
    paragraph_label.config(text=test1)

    time_1 = time()
    typing_box.config(state='normal')

def submit_test():
    global testinput, time_2
    time_2 = time()
    testinput = typing_box.get("1.0", tk.END).strip()

    if not testinput:
        messagebox.showwarning("Warning", "Please type the paragraph before submitting.")
        return

    speed = speed_time(time_1, time_2, testinput)
    errors = mistake(test1, testinput)

    result_label.config(
        text=f"Speed: {speed} chars/sec   |   Errors: {errors}",
        fg="blue"
    )

    typing_box.config(state='disabled')

# ----------------- Paragraph Data -----------------
test = [
    "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
    "Life is not a race everyone grows in their own time with their own journey.",
    "Consistency beats talent when talent does not work hard enough.",
    "Success is the result of continuous effort and not a one day miracle.",
    "Discipline is more powerful than motivation because it keeps you moving every day.",
    "Technology is evolving quickly and learning continuously keeps us ahead.",
    "Never compare your life with others everyone is fighting battles you cannot see.",
    "Small progress every day adds up to big results over time.",
    "In this digital world data has become more valuable than oil shaping the future of businesses.",
    "Failure is not the opposite of success it is a part of success that teaches us valuable lessons.",
    "Hard work gives success but smart work gives success faster which is why both are important.",
    "Your comfort zone may feel safe but nothing ever grows there take risks and explore more.",
    "Emotional intelligence helps you understand people and build better relationships.",
    "Opportunities do not happen you create them with dedication and effort.",
    "Time is the most valuable resource once wasted it never comes back.",
    "Dream big work hard stay humble and success will follow you naturally.",
    "Every expert was once a beginner practice consistency and patience always win.",
    "Believe in yourself even when nobody else does that is true confidence."
]

# ----------------- UI Design (Tkinter) -----------------
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("900x500")
root.config(bg="#E9E9E9")

title = tk.Label(root, text="Typing Speed Test", font=("Arial", 22, "bold"), bg="#E9E9E9")
title.pack(pady=10)

paragraph_label = tk.Label(root, text="", font=("Arial", 14), wraplength=850, bg="#E9E9E9")
paragraph_label.pack(pady=20)

typing_box = tk.Text(root, width=90, height=8, font=("Arial", 13), state='disabled')
typing_box.pack(pady=10)

start_btn = tk.Button(root, text="Start Test", font=("Arial", 12), command=start_test)
start_btn.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_test)
submit_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#E9E9E9")
result_label.pack(pady=20)

root.mainloop()

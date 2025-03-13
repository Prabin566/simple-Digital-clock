import time
import threading
from tkinter import Label, Tk, Button, Entry, StringVar, messagebox
import pyttsx3  # To speak the countdown numbers
from time import strftime  # Import strftime function from time module

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# ======= Configuring window =========
window = Tk()
window.title("Enhanced Digital Clock")
window.geometry("800x500")  # Increased window size
window.configure(bg="black")
window.resizable(False, False)

# ======= Time Label =========
time_label = Label(
    window, bg="black", fg="cyan", font=("Arial", 50, "bold"), relief="ridge", width=15, height=2
)
time_label.pack(anchor="center", pady=10)

# ======= Date Label =========
date_label = Label(
    window, bg="black", fg="white", font=("Arial", 20), relief="ridge", width=20, height=2
)
date_label.pack(anchor="center", pady=5)

# ======= Countdown Timer Feature =========
countdown_time = StringVar()

def start_countdown():
    try:
        total_seconds = int(countdown_time.get())
        threading.Thread(target=run_countdown, args=(total_seconds,)).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def run_countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_label.config(text=f"{mins:02d}:{secs:02d}")

        # Speak the remaining seconds
        engine.say(str(secs))  # Speak the number of seconds remaining
        engine.runAndWait()

        time.sleep(1)
        seconds -= 1
        
    messagebox.showinfo("Countdown", "Time's up!")

countdown_label = Label(window, text="Countdown Timer (secs):", bg="black", fg="white", font=("Arial", 15))
countdown_label.pack()

countdown_entry = Entry(window, textvariable=countdown_time, font=("Arial", 15))
countdown_entry.pack()

Button(window, text="Start Countdown", command=start_countdown, font=("Arial", 12)).pack(pady=10)

# ======= Real-time Clock Update =========
def update_label():
    current_time = strftime("%H:%M:%S")  # Get current time in hours:minutes:seconds format
    current_date = strftime("%d-%m-%Y")  # Get current date in day-month-year format
    time_label.configure(text=current_time)
    date_label.configure(text=current_date)
    window.after(1000, update_label)

update_label()
window.mainloop()
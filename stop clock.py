import tkinter as tk

class StopwatchClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch Clock")
        
        self.elapsed_time = 0
        self.running = False

        self.stopwatch_label = tk.Label(master, text="00:00:00", font=("Helvetica", 30))
        self.stopwatch_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def update_time(self):
        if self.running:
            self.elapsed_time += 1
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.master.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
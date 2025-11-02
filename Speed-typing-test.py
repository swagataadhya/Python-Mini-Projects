import tkinter as tk
from timeit import default_timer as timer
import random

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("600x350")
        
        self.sentences = [
            "The sky is blue today",
            "Cats sleep most of the day",
            "Practice makes a man perfect"
        ]
        
        self.start_time = None
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the UI components."""
        self.sentence = random.choice(self.sentences)
        
        self.label_sentence = tk.Label(self.root, text=self.sentence, font=("Arial", 14), wraplength=500)
        self.label_sentence.pack(pady=20)
        
        self.label_prompt = tk.Label(self.root, text="Type the above sentence:", font=("Arial", 12))
        self.label_prompt.pack()
        
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_result())  # Allow Enter key to submit
        
        self.button_done = tk.Button(self.root, text="Done", command=self.check_result, width=12, bg="lightblue")
        self.button_done.pack(pady=5)
        
        self.button_retry = tk.Button(self.root, text="Try Again", command=self.reset_test, width=12, bg="lightgrey")
        self.button_retry.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        
        self.start_time = timer()  # Start the timer when UI loads

    def check_result(self):
        """Check if the typed sentence matches the displayed one and show the result."""
        typed_text = self.entry.get()
        if typed_text == self.sentence:
            end_time = timer()
            time_taken = round(end_time - self.start_time, 2)
            words = len(self.sentence.split())
            wpm = round((words / time_taken) * 60, 2)  # Words per minute calculation
            self.result_label.config(text=f"Time: {time_taken} sec | WPM: {wpm}", fg="green")
        else:
            self.result_label.config(text="Incorrect typing. Try again!", fg="red")

    def reset_test(self):
        """Reset the test with a new sentence and restart the timer."""
        self.sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.sentence)
        self.entry.delete(0, tk.END)  # Clear input field
        self.result_label.config(text="")
        self.start_time = timer()  # Restart timer

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
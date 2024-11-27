import tkinter as tk
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analyzer")
        master.geometry("500x400")

        # Input Text Area
        self.input_label = tk.Label(master, text="Enter Text to Analyze:")
        self.input_label.pack(pady=(10, 5))

        self.input_text = tk.Text(master, height=6, width=60)
        self.input_text.pack(pady=5)

        # Analyze Button
        self.analyze_button = tk.Button(master, text="Analyze Sentiment", command=self.analyze_sentiment)
        self.analyze_button.pack(pady=10)

        # Results Display
        self.results_label = tk.Label(master, text="Sentiment Results:", font=("Arial", 12, "bold"))
        self.results_label.pack(pady=(10, 5))

        self.sentiment_var = tk.StringVar()
        self.sentiment_display = tk.Label(master, textvariable=self.sentiment_var, font=("Arial", 10))
        self.sentiment_display.pack()

        self.polarity_var = tk.StringVar()
        self.polarity_display = tk.Label(master, textvariable=self.polarity_var)
        self.polarity_display.pack()

        self.subjectivity_var = tk.StringVar()
        self.subjectivity_display = tk.Label(master, textvariable=self.subjectivity_var)
        self.subjectivity_display.pack()

    def analyze_sentiment(self):
        # Get input text
        text = self.input_text.get("1.0", tk.END).strip()

        if not text:
            self.sentiment_var.set("Please enter some text.")
            self.polarity_var.set("")
            self.subjectivity_var.set("")
            return

        # Perform sentiment analysis
        blob = TextBlob(text)
        
        # Determine sentiment category
        polarity = blob.sentiment.polarity
        if polarity > 0.05:
            sentiment = "Positive"
        elif polarity < -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Update display
        self.sentiment_var.set(f"Sentiment: {sentiment}")
        self.polarity_var.set(f"Polarity Score: {polarity:.2f}")
        self.subjectivity_var.set(f"Subjectivity Score: {blob.sentiment.subjectivity:.2f}")

def main():
    root = tk.Tk()
    app = SentimentAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
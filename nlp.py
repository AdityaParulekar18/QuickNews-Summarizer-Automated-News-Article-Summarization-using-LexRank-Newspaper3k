from tkinter import *
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_article():
    url = url_entry.get()
    try:
        # Download and parse article
        article = Article(url)
        article.download()
        article.parse()

        text = article.text

        # Summarization using LexRank (similar to TextRank)
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_sentences = summarizer(parser.document, 5)  # 5 sentences summary

        summary = " ".join(str(sentence) for sentence in summary_sentences)

        result_text.delete(1.0, END)
        result_text.insert(END, summary if summary else "Summary cannot be generated.")
    except Exception as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"Error: {str(e)}")

# GUI Setup
root = Tk()
root.title("News Article Summarizer")
root.geometry("800x600")

Label(root, text="Enter News Article URL:", font=("Arial", 14)).pack(pady=10)
url_entry = Entry(root, width=80, font=("Arial", 12))
url_entry.pack(pady=5)

Button(root, text="Summarize", command=summarize_article, font=("Arial", 14), bg="blue", fg="white").pack(pady=10)

result_text = Text(root, wrap=WORD, font=("Arial", 12), width=90, height=25)
result_text.pack(pady=10)

root.mainloop()

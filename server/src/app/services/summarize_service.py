from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str):
    if len(text.split()) < 20:
        return "Text too short for summarization."
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']
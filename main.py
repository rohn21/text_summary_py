import argparse
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

def summarize_from_file(file_path, language="english", sentences_count=5):
  """Summarizes the text content from a file."""
  try:
    with open(file_path, "r") as f:
      text = f.read()
      summary_result = summarize_from_input(text, language, sentences_count)
      #to store result of summarization
      #file_of_summary(summary_result, "summary_result.txt")
      return summary_result
  except FileNotFoundError:
    print(f"Error: File not found - {file_path}. Using text input instead.")
    # return None
    return summarize_from_input(input("Enter the text to summarize :"), language, sentences_count)

def summarize_from_input(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])  
  
"""for creating text summarization output file"""
def file_of_summary(summary_result, output_file):
  with open(output_file, "w") as f:
    f.write(summary_result)

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description="Text Summarization")
  parser.add_argument("file_path", help="Summarize from a file or a text.")
  parser.add_argument("-l", "--language", default="english", help="Default language for text summary (English)")
  parser.add_argument("-s", "--sentences", type=int, default=5, help="Number of sentences in the summary (default: 5)")
  args = parser.parse_args()
  
  summary = summarize_from_file(args.file_path, args.language, args.sentences)
  
  print(f"\nText Summary :\n ")
  # print(summary)
  print(f"\"{summary}\"")
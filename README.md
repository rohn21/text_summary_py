
# Text Summarization using Python

Its a simple command-line based python programm that returns summary of inputed file or text.

A user can take a file or a text as an input.I have used `Sumy` library which uses command-line utility for Text Summarization. As a sub module it uses `LexRankSummarizer` class that implements LexRank algorithm, a popular text summarization technique.

The LexRank algorithm analyzes the relationships between words in a text to identify the most important sentences that capture the essence of the document.

The sumy module also imports `Tokenizer` class from the `tokenizers` submodule.it imports from `sumy.nlp`
package which uses `Natural Language Processing`.
## Installation

Install with git

```bash
  git clone https://github.com/rohn21/text_summary_py.git
  cd text_summary_py
```

additional package installation

```bash
pip install sumy numpy

```
## Usage/Examples

```
python main.py summary.txt
```

For additional arguments pass the parameters

```
python main.py summary.txt -s <number_of_summary_sentences>
```
By default it summarize into 5 sentences, for example I want to summarize into 7 sentences
``` 
python main.py summary.txt -s 7
```
Additionaly, default language it takes as input is English, for change pass parameter -l <language code or name>
Supported languages : 

- Arabic (ar)
- Chinese (Simplified) (zh_CN)
- Czech (cz)
- English (en) (default)
- French (fr)
- German (de)
- Greek (el)
- Hebrew (he)
- Italian (it)
- Japanese (ja)
- Portuguese (pt)
- Slovak (sk)
- Spanish (es)
- Ukrainian (uk)

``` 
python main.py summary.txt -l fr
```
With combined parameters

``` 
python main.py summary.txt -l fr -s 10
```

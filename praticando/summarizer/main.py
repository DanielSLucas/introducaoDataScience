import sys
import nltk
import string

# nltk.download('punkt')
# nltk.download('stopwords')

from GooseWebScrapper import GooseWebScrapper
from TextSerializer import TextSerializer
from TextFrequencyCalculator import TextFrequencyCalculator
from SentenceScorer import SentenceScorer
from TextSummarizer import TextSummarizer

stopwords = nltk.corpus.stopwords.words('portuguese')
pontuation = string.punctuation

# "https://www.boatos.org/politica/arthur-lira-fraudou-votacao-sobre-voto-impresso-camara.html"
def main(url):
  webScrapper = GooseWebScrapper()
  webScrapper.extractDataFrom(url)

  originalText = webScrapper.getTitleAndContentString()  
  
  serializedText = TextSerializer(originalText, nltk).serializeText(stopwords, pontuation)

  wordsScores = TextFrequencyCalculator(serializedText, nltk).getWordsProportionalFrequency()

  sentencesScores = SentenceScorer(originalText, nltk).getSentencesScores(wordsScores)

  summary = TextSummarizer(sentencesScores).summarize()

  return summary


if __name__ == '__main__':
  url = sys.argv[1]
  print(main(url))

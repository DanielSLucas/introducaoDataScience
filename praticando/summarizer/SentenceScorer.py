class SentenceScorer:
  tokenizer = None
  text = None

  def __init__(self, text, tokenizer):
    self.text = text
    self.tokenizer = tokenizer
  
  def getSentencesScores(self, wordsScores):
    sentences = self.__getSentences()
    sentencesScores = {}

    for sentence in sentences:
      sentenceWasNotRated = (sentence not in sentencesScores.keys())

      if sentenceWasNotRated:
        sentencesScores[sentence] = self.__getSetenceScore(sentence, wordsScores)
      else:
        sentencesScores[sentence] += self.__getSetenceScore(sentence, wordsScores)
    
    return sentencesScores
  
  def __getSentences(self):
    return self.tokenizer.sent_tokenize(self.text)
  
  def __getSetenceScore(self, sentence, wordsScores):
    sentenceWords = self.tokenizer.word_tokenize(sentence.lower())
    sentenceScore = 0

    for word in sentenceWords:
      wordWasRated = (word in wordsScores.keys())

      if wordWasRated:
        sentenceScore += wordsScores[word]
    
    return sentenceScore
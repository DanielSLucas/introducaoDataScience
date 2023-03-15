class TextSummarizer:
  sentencesScores = None

  def __init__(self, sentencesScores):
    self.sentencesScores = sentencesScores

  def summarize(self):    
    self.__sortByHighestsScores()        
    sentences = self.__getSentences()
    numberOfSentencesLimiter = int(len(sentences)/10)

    summary = '\n'.join(sentences[:numberOfSentencesLimiter])

    return summary
        
  def __sortByHighestsScores(self):
    sentencesList = list(self.sentencesScores.items())

    sentencesList.sort(key=lambda item: item[1], reverse=True)

    self.sentencesScores = sentencesList
      

  def __getSentences(self):
    sentences = []

    for sentence, score in self.sentencesScores:
      sentences.append(sentence)

    return sentences
    

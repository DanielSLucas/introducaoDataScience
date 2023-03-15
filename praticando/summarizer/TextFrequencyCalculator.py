class TextFrequencyCalculator:
  tokenizer = None
  text = None

  def __init__(self, text, tokenizer):
    self.text = text
    self.tokenizer = tokenizer

  def getWordsProportionalFrequency(self):
    wordsFrequencies = self.__getWordsFrequency()    

    wordsProportinalFrequencies = self.__calculateWordsProportinalFrequencies(
      wordsFrequencies
    )

    return wordsProportinalFrequencies

  def __getWordsFrequency(self):
    return self.tokenizer.FreqDist(
      self.tokenizer.word_tokenize(self.text)
    )

  def __calculateWordsProportinalFrequencies(self, wordsFrequencies):
    wordsProportinalFrequencies = {}
    
    words = wordsFrequencies.keys()
    highestFrequency = self.__getHighestFrequency(wordsFrequencies)

    for word in words:
      wordsProportinalFrequencies[word] = self.__calculatePrortionalFrequency(
        wordsFrequencies[word], highestFrequency
      )
    
    return wordsProportinalFrequencies
  
  def __getHighestFrequency(self, wordsFrequencies):
    frequencies = wordsFrequencies.values()
    return max(frequencies)

  def __calculatePrortionalFrequency(self, frequency, highestFrequency):
    return frequency/highestFrequency

    
  

      
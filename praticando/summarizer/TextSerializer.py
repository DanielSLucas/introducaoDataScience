class TextSerializerFluentAPI:
  tokenizer = None
  serializedText = None

  def __init__(self, text, tokenizer):
    self.serializedText = text
    self.tokenizer = tokenizer
  
  def toLowercase(self):
    self.serializedText = self.serializedText.lower()
    return self
  
  def tokenize(self):
    self.serializedText = self.tokenizer.word_tokenize(self.serializedText)
    return self
  
  def remove(self, charList):
    self.serializedText = [
      word for word in self.serializedText if word not in charList
    ]
    return self
  
  def removeDigits(self):
    self.serializedText = [
      str(word) for word in self.serializedText if not word.isdigit()
    ]
    return self
  
  def join(self, joinChar):
    self.serializedText = joinChar.join(self.serializedText)
    return self

  def build(self):
    return self.serializedText
    

class TextSerializer:
  text = None

  def __init__(self, text, tokenizer):
    self.text = TextSerializerFluentAPI(text, tokenizer)    

  def serializeText(self, stopwords, pontuation):
    return self.text\
      .toLowercase()\
      .tokenize()\
      .remove(stopwords)\
      .remove(pontuation)\
      .removeDigits()\
      .join(" ")\
      .build()

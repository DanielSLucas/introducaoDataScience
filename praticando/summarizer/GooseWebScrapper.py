from goose3 import Goose

class GooseWebScrapper:
  goose = Goose()
  pageData = None

  def extractDataFrom(self, url):
    self.pageData = self.goose.extract(url)

  def getTitleAndContentString(self):
    if not self.pageData:
      raise Exception("You need to extract data from an url first")
    
    return self.pageData.title + ".\n\n" + self.pageData.cleaned_text
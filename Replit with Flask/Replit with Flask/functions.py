import re  
import pickle

def preprocesText(Text):
      # Remove all the special characters
      processedText = re.sub(r'\W', ' ', str(Text))

      # remove all single characters
      processedText = re.sub(r'\s+[a-zA-Z]\s+', ' ', processedText)
  
      # Remove single characters from the start
      processedText = re.sub(r'\^[a-zA-Z]\s+', ' ', processedText) 
  
      # Substituting multiple spaces with single space
      processedText= re.sub(r'\s+', ' ', processedText, flags=re.I)
  
      # Removing prefixed 'b'
      processedText = re.sub(r'^b\s+', '', processedText)
  
      # Converting to Lowercase
      processedText = processedText.lower()
      
      return processedText

def predict(cleaned_text):
  filename = 'Vaccine_sentiment_anaylsiser.sav'
  loaded_model = pickle.load(open(filename, 'rb'))
  return loaded_model.predict([cleaned_text])[0]



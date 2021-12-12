from flask import Flask, request
from functions import preprocesText,predict
app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  
  req = request.get_json(silent=True, force=True)
  # sum = 0
  query_result = req.get('queryResult')
  text = query_result.get('parameters')
  cleaned_text=preprocesText(text)
  result=predict(cleaned_text)
  print('here is the text and result is :'+result)

  return {
        "fulfillmentText": 'The user have : '+result+' feeling about vaccine',
        "source": "webhookdata"
    }
if __name__ == '__main__':
  app.run(host='0.0.0.0',port='8080') # This line is required to run Flask on repl.it
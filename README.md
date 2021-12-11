# Final_nlp_project_Vaccine_analysis

## Project descripltion:
This project aims to extract information about COVID-19 vaccines from Twitter using Clustering, Sentiment analysis, and Classification, in order to encourage people to take the vaccine.


## Methodology:
1. Data Collection: At the first step, data is fetched from Twitter by using `Tweepy library` after creating a tweeter developer account. Target vaccine hashtags are: #Pfizer, #Moderna, and #Johnson, but we only extracted the text data and sorted them in CSV files.

2. Preprocessing dataset: Very important step is to clean the collected data and preprocess them before being used in the models to get the best possible results. This can done through: text lower casing, remove stop words, replace emojes with plain text, remove THML tages, tokenization, normalization, and lemmatization.

3. Used models: 

| Clustering      | Sentiment analysis | Classification     |
|   :----:    |    :----:   |     :----:    |
|  To separate between opinion related and non-opinion related, and then use the opinion related only| To label the obtained data|To predict the opinion about each vaccine whether it is positive, negative, or neutral.|
| K-means   | `TextBlob` library | SVM, KNN, DT      |



### Integration with Chatbot:

[COVID-19 Vaccine Chatbot](https://sites.google.com/view/vaccineprotection/home)
[<img src="https://github.com/AlshimaaGamalAlsaied/Final_nlp_project_Vaccine_analysis/blob/main/1.PNG">](https://sites.google.com/view/vaccineprotection/home)

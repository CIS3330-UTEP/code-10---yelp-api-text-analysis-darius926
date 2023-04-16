import nltk
nltk.download('stopwords','punkt')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import pandas as pd
from yelpapi import YelpAPI
import urllib.parse 
import matplotlib.pyplot as plt
import json

api_key = "tHPiduiiZM5Y4qKS4RArC0lFDYEpyQqXk2QdySV0e_zC2A4MvJEoEfMiV18ssw8gdVhdVydSW2TDQijNRtG74tMqqbnsIuQsIUF67jWMLovr8cgefOmnZ9FBvUA0ZHYx"

with YelpAPI(api_key) as yelp_api:
    yelp_api=YelpAPI(api_key)
search_term="pizza"
search_location="Dallas, TX"
search_sort_by="rating"#best_match, rating, distance, review_count
search_limit= 10
search_results=yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort_by, limit=search_limit,)
# search_results = yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)
print(search_results)

for business in search_results['businesses']:
    print(business['name'])
    print(business['alias'])
    print("\n")


result_df= pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])

id_for_reviews="neony-pizza-works-dallas"
reviews_result=yelp_api.reviews_query(id=id_for_reviews)
print(reviews_result)

for review in reviews_result['reviews']:
    print(review['text'])
    print("\n\n")

reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df)
reviews_df.to_csv(f"{id_for_reviews}_reviews_")

analyzer= SentimentIntensityAnalyzer()
stop_words= set(stopwords.words('english'))
reviews=open('neony-pizza-works-dallas')



for review in reviews_result:
     print(review)
     tokens=nltk.word_tokenize(review)
     pos_tokens=nltk.pos_tag(tokens)
     new_text=[]
     for tag in pos_tokens:
          if tag[0] not in stop_words:
               print(tag[0])
               print(tag)
               new_text.append
for token in pos_tokens:
        if token[1]=='NN' or token[1]=="JJS" or token[1]=="VBD":
            print(token[0])
            print(token)
            print("\nOriginal")
            print(review)
            print("\nNew")
            print(" ".join(new_text))



pos_tags=nltk.pos_tag(tokens)

for review in reviews_result:
    sentiment_score=analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

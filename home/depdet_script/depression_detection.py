import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from ntscraper import Nitter
#import static

#initialize the library
scraper=Nitter(log_level=1, skip_instance_check=False)


def down_tweets(username=str):
    # user_data = pd.read_csv('static/user_tweets.csv')
    print('scraping tweets...')
    tweets = scraper.get_tweets("iamsrk", mode='user', number=100)
    user_dataset=[]
    for tweet in tweets['tweets']:
        user_dataset.append(tweet['text'])

    user_df=pd.DataFrame(user_dataset, columns=['tweet'])
    return user_df


def text_cliner(tweet):
    tweet = re.sub('@[^\s]+','',tweet)
    tweet = re.sub('http[^\s]+','',tweet)
    tweet = re.sub('#','',tweet)
    tweet = re.sub("[^a-zA-Z0-9#]",' ',tweet)
    tweet = " ".join([w for w in str(tweet).split() if len(w)>3])
    return tweet

def df_cleaner(user_data):
    user_data['clean_tweet'] = user_data['tweet'].apply(text_cliner) 
    user_data['clean_tweet'] = user_data['clean_tweet'].apply(lambda x: ' '.join([word for word in x.lower().split() if word not in (stop_words)]))
    tokenized_tweet = user_data['clean_tweet'].apply(lambda x: x.split())

    lemmatizer = WordNetLemmatizer()
    tokenized_tweet = tokenized_tweet.apply(lambda sentence: [lemmatizer.lemmatize(word) for word in sentence])
    user_data['clean_tweet'] = tokenized_tweet.apply(lambda x: " ".join(x))
    user_data['clean_tweet'].dropna()
    
    return user_data

def predict(cleaned_data):


    tf1=pickle.load(open('static/tfidf.pkl', 'rb'))
    tfnew=TfidfVectorizer( stop_words = "english", max_features = 1000, vocabulary = tf1)
    X_tf1 = tfnew.fit_transform(cleaned_data['clean_tweet'])


    
    with open("static/LG_model.pkl", 'rb') as file:  
        LR_model = pickle.load(file)

    
    pred = LR_model.predict(X_tf1)
    return pred


'''
user_data=down_tweets("asdf")
cleaned_data=df_cleaner(user_data)
predict=predict(cleaned_data)
print(predict)
'''
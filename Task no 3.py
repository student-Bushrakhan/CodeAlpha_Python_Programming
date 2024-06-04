  ##-----------  TASK NO. 3----------##
                     ## ---------- Basic Chatbot ---------##
    
import nltk
import numpy as np
import random
import string  # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample text corpus
text_corpus = """
Hello! How can I help you today?
I can assist you with various tasks, including answering questions and providing information.
What would you like to know?
Feel free to ask me anything.
"""

# Tokenization and preprocessing
sent_tokens = nltk.sent_tokenize(text_corpus)  # Converts to list of sentences
word_tokens = nltk.word_tokenize(text_corpus)  # Converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English included in NLTK.

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad you're talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Response generation
def response(user_response):
    chatbot_response = ''
    sent_tokens.append(user_response)
    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if req_tfidf == 0:
        chatbot_response = chatbot_response + "I am sorry! I don't understand you"
    else:
        chatbot_response = chatbot_response + sent_tokens[idx]
    
    sent_tokens.pop()
    return chatbot_response

def chatbot():
    print("Chatbot: Hi! I'm a chatbot. You can type 'bye' to exit.")
    while True:
        user_response = input("You: ").lower()
        if user_response != 'bye':
            if user_response in ('thanks', 'thank you'):
                print("Chatbot: You're welcome!")
                break
            else:
                if greeting(user_response) is not None:
                    print("Chatbot: " + greeting(user_response))
                else:
                    print("Chatbot: " + response(user_response))
        else:
            print("Chatbot: Bye! Take care.")
            break

if __name__ == "__main__":
    chatbot()

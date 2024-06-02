                        ##-----------  TASK NO. 1 ----------##
                         ## -------- Hangman Game -----------##
import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'random', 'word', 'guess', 'player']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        '''
    ]
    return stages[tries]

def play_game():
    word = get_random_word()
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats! You guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
    play_game()



                ##-----------  TASK NO. 2----------##
                ## ---------- Stock Portfolio Tracker ---------##
    

import yfinance as yf
import pandas as pd

# Initialize an empty portfolio
portfolio = {}

def add_stock(ticker, shares):
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares
    print(f"Added {shares} shares of {ticker} to the portfolio.")

def remove_stock(ticker, shares):
    if ticker in portfolio:
        if shares >= portfolio[ticker]:
            del portfolio[ticker]
            print(f"Removed all shares of {ticker} from the portfolio.")
        else:
            portfolio[ticker] -= shares
            print(f"Removed {shares} shares of {ticker} from the portfolio.")
    else:
        print(f"{ticker} is not in the portfolio.")

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")

def track_portfolio():
    total_value = 0
    portfolio_data = []

    for ticker, shares in portfolio.items():
        stock_data = get_stock_data(ticker)
        current_price = stock_data['Close'].iloc[-1]
        stock_value = current_price * shares
        total_value += stock_value
        portfolio_data.append({
            'Ticker': ticker,
            'Shares': shares,
            'Current Price': current_price,
            'Total Value': stock_value
        })

    portfolio_df = pd.DataFrame(portfolio_data)
    print("\nPortfolio Summary:")
    print(portfolio_df)
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\nStock Portfolio Tracking Tool")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares: "))
            add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            remove_stock(ticker, shares)
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



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




                      ##-----------  TASK NO. 4----------##
                     ## --Task Automation with Python Scripts --##
    
import os
import shutil

# Define the directory to organize
directory_to_organize = 'path/to/your/directory'

# Define the file type categories and corresponding folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

# Create folders if they do not exist
for folder in file_types.keys():
    folder_path = os.path.join(directory_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file type and move it to the corresponding folder
        file_moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, folder, filename))
                file_moved = True
                break

        # If the file type is not recognized, move it to the 'Others' folder
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, 'Others', filename))

if __name__ == "__main__":
    organize_files(directory_to_organize)
    print("Files have been organized successfully.")

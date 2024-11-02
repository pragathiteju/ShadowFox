#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4


# In[2]:


import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all quote containers
    quotes = soup.find_all('div', class_='quote')

    # Extract and print each quote and its author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        print(f'Quote: {text}\nAuthor: {author}\n')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# In[1]:


import random

# List of words to choose from
words = ["python", "hangman", "programming", "visual", "code", "computer", "developer", "function", "variable"]

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |  
           -
        """,
        """
           -----
           |   |
           |   O
           |  
           |  
           -
        """,
        """
           -----
           |   |
           |   
           |  
           |  
           -
        """,
        """
           -----
           |   |
           |  
           |  
           |  
           -
        """
    ]
    return stages[attempts]

def hangman():
    word = random.choice(words)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    hints = f"The word is {len(word)} letters long."

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print(hints)
    print()

    while not guessed and attempts > 0:
        guess = input("Please enter a letter or guess the word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Sorry, that's not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please enter a single letter or a valid word.")

        print(display_hangman(attempts))
        print(word_completion)
        print()

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

# Run the game
hangman()


# In[1]:


import random

# List of words to choose from
words = [
    "python", "hangman", "programming", "visual",
    "code", "computer", "developer", "function", "variable"
]

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """
    ]
    return stages[attempts]

def hangman():
    word = random.choice(words)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    hints = f"The word is {len(word)} letters long."
    
    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print(hints)
    print()

    while not guessed and attempts > 0:
        guess = input("Please enter a letter or guess the word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Sorry, that's not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Invalid input. Please enter a single letter or a valid word.")

        print(display_hangman(attempts))
        print(word_completion)
        print()

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

# Run the game
hangman()


# In[2]:


import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extract all the headings (h1, h2, h3, etc.) from the webpage
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Print the headings
for heading in headings:
    print(heading.get_text())

# Example: Extract all the links (anchor tags) from the webpage
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))


# In[1]:


import random

# List of words to choose from
words = [
    "python", "hangman", "programming", "visual", "code", "computer", "developer", "function", "variable"
]

def display_hangman(attempts):
    stages = [
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / 
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |   |
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |  
         |  
         -
        """,
        """
         -----
         |   |
         |   
         |  
         |  
         -
        """
    ]
    return stages[attempts]

def hangman():
    word = random.choice(words)
    word_completion = "_" * len(word)  # Visual progress of the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    hints = f"The word is {len(word)} letters long."

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print(hints)
    print()

    while not guessed and attempts > 0:
        guess = input("Please enter a letter or guess the word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"Sorry, {guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"Sorry, {guess} is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Invalid input. Please enter a single letter or a valid word.")

        print(display_hangman(attempts))
        print(word_completion)
        print()

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

# Run the game
hangman()


# In[5]:


import random

# List of words to choose from
words = [
    "python", "hangman", "programming", "visual", "code", "computer", "developer", "function", "variable"
]

def display_hangman(attempts):
    stages = [
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / 
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |   |
         |  
         -
        """,
        """
         -----
         |   |
         |   O
         |  
         |  
         -
        """,
        """
         -----
         |   |
         |   
         |  
         |  
         -
        """
    ]
    return stages[attempts]

def hangman():
    word = random.choice(words)
    word_completion = "_" * len(word)  # Visual progress of the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    hints = f"The word is {len(word)} letters long."

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print("Progress: ", word_completion)
    print(hints)
    print()

    while not guessed and attempts > 0:
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        guess = input("Please enter a letter or guess the word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"Sorry, {guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"Sorry, {guess} is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Invalid input. Please enter a single letter or a valid word.")

        print(display_hangman(attempts))
        print("Progress: ", word_completion)
        print()

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

# Run the game
hangman()


# In[ ]:





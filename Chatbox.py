
import csv # Provides functionality for reading and writing CSV Files
import random # Random variable generators.
from sklearn.feature_extraction.text import CountVectorizer
'''
The sklearn.feature_extraction module deals with feature extraction from raw data.
It currently includes methods to extract features from text and images.

CountVectorizer: Convert a collection of text documents to a matrix of token counts.
'''
from sklearn.svm import SVC
'''
The sklearn.svm module includes Support Vector Machine algorithms
The implementation is based on libsvm. The fit time scales at least quadratically with the 
number of samples and may be impractical beyond tens of thousands of samples
'''
# Load English and Italian data from CSV file
def load_data(): # Reads the file and return the as a list that can be use to load vocab 
    data = [] # create a empty list

    '''    
    Open the file that contains the data needed to train the AI model
    with : ensures that the file is close automatically 
    r : specifies that the file needs to be read
    '''
    with open('vocabulary_data.csv', 'r') as file: 
        reader = csv.reader(file) # creates an object called "reader" allows us to read the contents of the csv file 
        data = list(reader) # Reads the contents from reader object(Representing the CSV File) and converts it into a list.. using list() function 

    return data # This line returns the data list, which contains the contents of the CSV file. 

# Train the AI model
def train_model(data): 

    italian_words = [item[0] for item in data] 
    '''
        1. Creates a list called "italian_words" ...
        2. Specifying to focus on the first column of this list Iterates over the data passed to the function ...
        3. Retrieve the words from the first column and stores it into the created list
    '''
    english_translations = [item[1] for item in data]
    '''
        1. Creates a list called "english_translations" ...
        2. Specifying to focus on the second column of this list Iterates over the data passed to the function ...
        3. Retrieve the words from the second column and stores it into the created list
    '''
    vectorizer = CountVectorizer() 
    '''
        Creates a instance of the function ..
        This function is from scikit-learn...
        used to convert text data into numerical feature vectors
        '''
    X = vectorizer.fit_transform(italian_words) 
    ''' 
        Applies the function to the list containing italian words
        Resulting in a matrix 'X' represents the Italian words as numerical features.
   
    ''' 
    model = SVC(kernel='linear')
    '''
        Creates a SVC instance with a Linear Kernel
        The SVC is a classification algo that can be used to train AI Model
    '''

    model.fit(X, english_translations)
    '''
    Trains the model using:
        1. the matrix 'X' numerically representing the Italian words
        2. The english translations list
    Then associating the feautre matrix 'X' with corresponding English Translations
    '''
    return vectorizer, model

# Generate a random word or phrase
def generate_word(data):
    random_item = random.choice(data) # Randomly selects an item from the 'data' list and assign it to the variable
    return random_item[0] # Return the first column, being the italian word

# Translate the Italian word using the AI model
def translate_word(italian_word, vectorizer, model):
    '''
    Takes in 3 parameters
        1. The italian word to be translated
        2. The trained vectorizer
        3. The trained AI model
    '''
    X = vectorizer.transform([italian_word])
    '''
    Transforms the italian_word into a feature vector...
    The word is then wrapped in a list because the ... transform() method expects an iterable
    '''
    english_translation = model.predict(X)
    '''
    uses predict() method from 'model' to predict the English Translation 
    For the given feature vector 'X'
    '''
    return english_translation[0] #Returns english translation .. the first and only element

# Check user's translation
def check_translation(user_translation, correct_translation):
    if user_translation.lower() == correct_translation.lower(): #Converts characters to lowercase
        return "Correct!"
    else:
        return "Incorrect. Try again."

# Chatbot with loop to iterate through words
def chatbot():
    data = load_data()
    vectorizer, model = train_model(data)

    print("Welcome to the Italian Vocabulary Practice Chatbot!")
    print("You will be prompted with an Italian word or phrase, and you need to provide its English translation.")
    print("Enter 'quit' at any time to exit.")

    while True:
        # Prompt user for options
        category = input("Choose a category (e.g., 'animals', 'food', 'colors'): ")
        difficulty = input("Choose a difficulty level (e.g., 'easy', 'medium', 'hard'): ")
        generate = input("Type 'generate' to generate a word or phrase: ")

        if generate.lower() == 'quit':
            break

        # Filter data based on user's options
        # item[3] = column 4 and item[5] = column 5
        filtered_data = [item for item in data if item[3] == category and item[4] == difficulty]

        if len(filtered_data) == 0:
            print("No matching words found. Please try different options.")
            continue

        # Generate a random word or phrase
        word = generate_word(filtered_data)

        print("Italian: " + word)
        user_translation = input("Enter the English translation: ")

        if user_translation.lower() == 'quit':
            break

        # Translate the Italian word
        translated_word = translate_word(word, vectorizer, model)

        # Check the user's translation
        result = check_translation(user_translation, translated_word)
        print(result)

# Starts the chatbot
chatbot()


# LanguageLearningChatBox

## Scope 
The scope of the language learning chatbot for Italian would be to provide vocabulary practice exercises to users. The chatbot will present Italian words or phrases and ask users to provide translations or definitions in their native language (EN). The focus will be on building users' vocabulary and improving their understanding of Italian words and their meanings.

## Key Features
1. Vocabulary Exercises: The chatbot will present Italian words or phrases and ask users to provide their translations or definitions.
2. Randomization: The chatbot will randomize the selection of vocabulary items for each exercise to provide variety and prevent predictability.
3. Difficulty Levels: The chatbot can offer different difficulty levels (e.g., beginner, intermediate, advanced) to cater to users with varying language proficiency.
4. Feedback and Evaluation: The chatbot will provide feedback on the user's responses, indicating whether they are correct or incorrect.***
5. Progress Tracking: The chatbot can keep track of the user's progress, such as the number of exercises completed and their success rate.***

## User Interface
The user interface of the chatbot will be a text-based interface where users can interact by typing their responses. It can be a console or a web-based interface. 

## Interaction flow
“ The interaction flow refers to the sequence and structure of interactions between the user and the system.”

1. The chatbot starts by greeting the user and providing a brief introduction to the Italian Vocabulary Chatbot.

### How to Start/Exit Chatbox:
2. The chatbot prompts the user to enter 'start' to begin the exercise or 'quit' to exit.

### How Language Learning interaction works:
3. If the user enters 'start', the chatbot presents the first word or phrase in Italian along with a textbox for the user to provide the translation.
4. The user enters their translation in the textbox.
5. The chatbot evaluates the user's response and provides feedback, indicating whether the translation is correct or incorrect. It may also provide the correct translation if the user's response is incorrect.

### How to create re-iteration
6. The chatbot prompts the user to enter 'next' for the next word or 'quit' to exit.
7. If the user enters 'next', the chatbot presents the next word or phrase for translation.
8. Steps 4-7 are repeated until the user chooses to exit by entering 'quit'.

### Exit Message
9. Upon exiting, the chatbot thanks the user for practicing and encourages them to come back for more exercises.


## Dataset 

**Italian_Word:** This column contains the Italian word or phrase.
**English_Translation:** This column contains the corresponding English translation of the Italian word or phrase.
**Type:** This column specifies whether the entry is a word or a phrase.
**Category:** This column categorizes the vocabulary entry into different categories such as:
1. Basic Phrases **
2. Numbers **
3. Colors **
4. Animals **
5. Food and Drinks *
6. Family
7. Clothing
8. Weather
9. Transportation
10. Body Parts
11. Jobs and Professions
12. Countries and Nationalities
13. Time and Dates
14. Sports and Hobbies
15. Places and Locations
16. Emotions **
17. Daily Activities
18. Technology
19. Music and Arts
20. Nature and Environment
21. Shopping
22. Education
23. Home 
24. Travel



**Difficulty_Level:** This column indicates the difficulty level of the vocabulary entry, such as "Beginner", "Intermediate", or "Advanced".


## Functions

'''
This code utilizes scikit-learn is used for training the AI model.
    `load_data()` function loads the vocabulary data from the CSV file. 
    `train_model()` function trains the AI model using the Italian words as input features and the corresponding English translations as the target variable. 
    `generate_word()` function selects a random word or phrase based on the user's chosen options. 
    `translate_word()` function translates the Italian word using the trained model. 
    `check_translation()` function checks the user's translation and provides feedback. 
    `chatbot()` loop handles user interactions and prompts.
'''

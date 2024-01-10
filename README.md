# Hangman-Game

The Hangman Game is a Python console-based application that allows users to play the classic Hangman word-guessing game.

**Key Features:**

•	Linked List to manage and manipulate the words used in the game.  
•	Lists are used to represent the ‘display’ attribute.  
•	Sets are used to store guessed letters.  
•	Dictionaries are used to store the hangman stages.  
•	Random shuffling of words for variety.  
•	Interactive user input for letter guessing.  
•	Visual display of the current state of the word.  

**Rules for the game:**

•	The program randomly picks a word from the imported ‘word_file’ list.  
•	The player begins with 6 lives.  
•	For each guessed letter, the game checks if it is in the ‘chosen_word’.  
•	If the letter is not in the word, one life is deducted.  
•	If the same letter is guessed again, the player is informed that the letter has already been guessed without further life deduction.  
•	If 0 lives are remaining, the game ends by revealing the chosen word.  
•	If all letters are guessed correctly before running out of lives, the user wins.  


**Linked List Structure:**

1.	Node Class:  
•	Each node represents a word in the linked list.  
•	It contains a ‘value’ attribute to store the word and a ‘next’ attribute to reference the next node in the list.  

2.	LinkedList Class:  
•	Manages the overall linked list.  
•	Contains a ‘head’ attribute pointing to the first node in the list.  
•	Includes methods to add words to the list, shuffle the words, and retrieve the next word.  

**Role of Linked List in Hangman Game**

1.	Word List Management:  
•	The linked list is used to store a list of words for the Hangman game.  
•	Words are added to the linked list using the ‘add_word’ method of the ‘Linked List’ class.  

2.	Shuffling Words:  
•	The ‘shuffle_words’ method of the ‘LinkedList’ class shuffles the words in the linked list.    
•	It converts the linked list into a regular list(‘words’), shuffle the list using ‘random.shuffle()’, and then reconstructs the linked list with the shuffled order.   

3.	Getting Next Word:   
•	The ‘get_next_word’ method of the ‘LinkedList’ class retrieves the next word for the game.    
•	It returns the value of the current head node and moves the ‘head’ reference to the next node in the list.

**Code Structure**

hangman.py:Contains the Python code for the Hangman game.  
hangman_stages.py:Provides ASCII art representations of the hangman stages.  
word_file.py:Includes a sample list of words used in the game.  
  

**Conclusion:**

In conclusion, the Hangman game provides a fun and interactive way for users to enjoy the classic game of guessing words. The use of a linked list for word management demonstrates the advantages of efficient insertion, deletion, and shuffling. Looking ahead, the plan to develop a website for the game opens up exciting possibilities for enhancing user interaction and enjoyment.



Credits for the word_file.py goes to VanshShandilya GitHub

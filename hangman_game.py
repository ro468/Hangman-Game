import random
import hangman_stages
import word_file
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_word(self, word):
        new_node = Node(word)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def shuffle_words(self):
        words = []
        current = self.head
        while current:
            words.append(current.value)
            current = current.next
        random.shuffle(words)
        self.head = None
        for word in words:
            self.add_word(word)
    def get_next_word(self):
        if not self.head:
            return None
        current = self.head
        self.head = self.head.next
        return current.value
class HangmanGame:
    def __init__(self):
        self.lives = 6
        self.word_list = LinkedList()
        self.guessed_letters = set()
        self.chosen_word = ""
        self.display = []
    def initialize_game(self):
        self.word_list.shuffle_words()
        self.chosen_word = self.word_list.get_next_word().lower()
        self.display = ['_' for _ in self.chosen_word]
        self.guessed_letters.clear()
        self.lives = 6
    def display_word(self):
        print(" ".join(self.display))
    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter. Try again.")
            return
        self.guessed_letters.add(letter)

        if letter in self.chosen_word:
            for position in range(len(self.chosen_word)):
                if self.chosen_word[position] == letter:
                    self.display[position] = letter
            self.display_word()
        else:
            print("Oops!Sorry. It's a wrong letter")
            self.lives -= 1
            print(hangman_stages.stages[self.lives])
        print("Already guessed letters:", sorted(self.guessed_letters))
    def play_game(self):
        while self.lives > 0 and '_' in self.display:
            self.guess_letter(input("Guess a letter: ").lower())

        if '_' not in self.display:
            print("YAY! you guessed the word", self.chosen_word, "!!")
        else:
            print("You lose, sorry. The word was", self.chosen_word)
if __name__ == "__main__":
    hangman_game = HangmanGame()

    # Add words to the word list
    for word in word_file.words:
        hangman_game.word_list.add_word(word)

    # Play the game
    hangman_game.initialize_game()
    hangman_game.display_word()
    hangman_game.play_game()





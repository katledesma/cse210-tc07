import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """The responsibility of Word is to display words. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self._segments = ["apple"]
        self.fill_list()
        i = random.randint(0, len(self._segments) - 1)
        self.set_text(self._segments[i])
        self.reset()

    def fill_list(self):
        """Populates the word list into _segments.
        
        Args:
            self ("word"): an instance of "word".
        """
        with open("words.txt") as wordlist:
            words = wordlist.read()
            words = words.splitlines()
            for word in words:
                self._segments.append(random.choice(words))
    
    def get_points(self):
        """Gets the points this "word" is worth.
        
        Args:
            self ("word"): an instance of "word".

        Returns:
            integer: The points this "word" is worth.
        """
        return self._points
    
    def move_word(self, direction):
            """Moves the words downward each frame.

            Args:
                self (Word): An instance of word.
                direction (Point): The direction to move, which is downward.
            """
            count = len(self._segments) - 1
            for n in range(count, -1, -1):
                segment = self._segments[n]
                segment.set_velocity(direction)
                segment.move_next()

    def reset(self):
        """Resets the word by moving it to a random position 
        at the top of the screen and appoints a number of points
        depending on word length.
        
        Args:
            self ("word"): an instance of "word".
        """
        self._points = len(self.get_text()) * 10
        x = random.randint(1, constants.MAX_X - len(get_text()))
        y = 1
        position = Point(x, y)
        self.set_position(position)
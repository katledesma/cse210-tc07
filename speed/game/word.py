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
        self.set_text("jazz")
        self.reset()

        # with open("words.txt") as wordlist:
        #     words = wordlist.read()
        #     words = words.splitlines()
        #     for word in words:
        #         answer = random.choice(words)
        #         # get word
    
    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.

        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def reset(self):
        """Resets the food by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Food): an instance of Food.
        """
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)
        

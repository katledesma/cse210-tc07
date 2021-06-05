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
        self._segments = []
        self.fill_list()
        # i = random.randint(0, len(self._segments) - 1)
        # self.set_text(self._segments[i])
        self.reset()

    def fill_list(self):
        """Populates the word list into _segments.
        
        Args:
            self ("word"): an instance of "word".
        """
        for i in range(0, constants.STARTING_WORDS):
            random_word = constants.LIBRARY[random.randint(0, len(constants.LIBRARY) - 1)]
            x = random.randint(1, constants.MAX_X - len(self.get_text()))
            y = random.randint(1, constants.MAX_Y - len(self.get_text()))
            position = Point(x, y)
            self.set_position(position)
            velocity = Point(0, 1)
            self._add_segment(random_word, position, velocity)
            print()
    
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
        

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Word): An instance of word.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments
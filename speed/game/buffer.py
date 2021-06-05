from game import constants
from game.actor import Actor
from game.point import Point

class Buffer:
    """The responsibility of Buffer is keep track of (?). It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._buffer = 0
        position = Point(20, 0)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")
    
    def buffer_input(self, user_input):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        self._buffer += user_input
        self.set_text(f"Buffer: {self._buffer}")
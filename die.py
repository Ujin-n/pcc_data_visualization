from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self._num_sides = num_sides

    def num_sides(self):
        """Getter for sef._num_sides"""
        return self._num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides())

class Item:
    def __init__(self, description: str, calories: str):
        self.description = description
        self.calories = calories

    def __eq__(self, other):
        """Equals between Items. If the other is not a Product - raise an error"""
        if type(other) != Item:
            raise TypeError("Argument of __eq__ must be of type Item")
        if self.description == other.description and self.calories == other.calories:
            return True
        else:
            return False

    def __hash__(self):
        # Combine the hash of all fields used in equality check
        return hash((self.description, self.calories))

    def __str__(self):
        return f"description: {self.description}, {self.calories} calories"

    def __repr__(self):
        return f"description: {self.description}, {self.calories} calories"

from item import Item


class Reminder(Item):
    def __init__(self, name: str, description: str, comment: str, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, description, comment)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


    def get_type(self):
        return Item.ItemType_E.REMINDER.value


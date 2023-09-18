from datetime import timedelta, datetime

from item import Item


class Task(Item):
    def __init__(self, name: str, description: str, comment: str, deadline: datetime):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, description, comment)

        # Run validations to the received arguments
        assert deadline >= datetime.now(), f"Deadline {deadline} is overdue!"

        # Assign to self object
        self.deadline = deadline


    def get_type(self):
        return Item.ItemType_E.TASK.value

    def __repr__(self):
        return f"{super().__repr__()} + 'deadline', {self.deadline}"
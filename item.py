import csv
from enum import Enum


class Item:
 
    class ItemType_E(Enum):
        TODO = 1
        TASK = 2
        REMINDER = 3
        MEETING = 4

    # list to hold all items
    todo_list = []

    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, description: str, comment: str, quantity=0):
        # run validations to the received arguments
        assert len(description) < 100, f"Description '{description}' is to long!"
        assert Item.is_integer(quantity), f"Quantity {quantity} is not an integer!!!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # assign to self object
        self.__name = name
        self.__description = description
        self.comment = comment
        self.quantity = quantity

        # actions to execute
        Item.todo_list.append(self)

    @property
    def description(self):
        return self.__description

    def apply_discount(self):
        # self.__price = self.__price * self.pay_rate
        pass

    def apply_increment(self, increment_value):
        # self.__price = self.__price + self.__price * increment_value
        pass

    # getter
    @property
    def name(self):
        # property Decorator = Read-Only Attribute
        return self.__name

    # setter
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value


    def item_to_csv_row(self):
        csv_row = []
        csv_row.append(self.name)
        csv_row.append(self.description)
        csv_row.append(self.comment)
        csv_row.append(self.quantity)
        return csv_row


    def get_type(self):
        return Item.ItemType_E.TASK.value
    

    def calculate_total_price(self):
        # return self.__price * self.quantity
        return 0


    @classmethod
    def read_from_csv(cls):
        with open('items.csv', 'r') as f:
            csvreader = csv.DictReader(f)
            items = list(csvreader)

        for item in items:
            print(item)
            Item(
                name=item.get('Name'),
                description=item.get('Description'),
                comment=item.get('Comment'),
                quantity=int(item.get('quantity')),
            )

    @classmethod
    def write_to_csv(cls):

        # field names
        fields = ['Name', 'Description', 'Comment', 'quantity']

        # data rows of csv file
        rows2 = [ ['Nikhil', 'COE', '2', '9.0'],
                ['Sanchit', 'COE', '2', '9.1'],
                ['Aditya', 'IT', '2', '9.3'],
                ['Sagar', 'SE', '1', '9.5'],
                ['Prateek', 'MCE', '3', '7.8'],
                ['Sahil', 'EP', '2', '9.1']]
            
        rows = []

        for item in Item.todo_list:
            row = item.item_to_csv_row()
            print('row:', row)
            rows.append(row)

        print('rows:', rows)

        # name of csv file
        filename = "items_2.csv"
            
        # writing to csv file
        # with open(filename, 'w') as csvfile:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
                
            # writing the fields
            csvwriter.writerow(fields)
                
            # writing the data rows
            csvwriter.writerows(rows)


    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero, i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__description}', '{self.comment}', {self.quantity})"


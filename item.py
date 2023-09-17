import csv
from enum import Enum
from datetime import timedelta, datetime
# from dateutil import tz

# from item_factory import create_reminder


class Item:
 
    class ItemType_E(Enum):
        TODO = 1
        TASK = 2
        REMINDER = 3
        MEETING = 4

    # list to hold all items
    todo_list: list = []

    modified: bool = False

    def __init__(self, name: str, description: str, comment: str):
        # run validations to the received arguments
        assert len(description) < 100, f"Description '{description}' is to long!"
        # assert Item.is_integer(quantity), f"Quantity {quantity} is not an integer!!!"

        # assign to self object
        self.__name: str = name
        self.__description: str = description
        self.comment: str = comment
        # self.create_date: datetime = datetime.now(tz=tz.tzlocal())
        self.create_date: datetime = datetime.now()
        self.expiry_date: datetime = None

        # actions to execute
        Item.todo_list.append(self)

    @property
    def description(self):
        return self.__description

    def comment_update(self, s: str):
        self.comment = self.comment + ', ' + s
        pass

    def comment_replace(self, s: str):
        self.comment = s
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
        csv_row.append(self.get_type())
        csv_row.append(self.name)
        csv_row.append(self.description)
        csv_row.append(self.comment)
        return csv_row


    def get_type(self):
        return Item.ItemType_E.TODO.value
    

    def calculate_total_price(self):
        # return self.__price * self.quantity
        return 0


    @classmethod
    def read_from_csv(cls):
        with open('items.csv', 'r') as f:
            csvreader = csv.DictReader(f)
            items = list(csvreader)

        for item in items:
            print('item:', item)
            if int(item.get('Type')) == 1:
                Item(
                    name=item.get('Name'),
                    description=item.get('Description'),
                    comment=item.get('Comment'),
                )
            elif int(item.get('Type')) == 2:
                # create_reminder(
                Item(
                    name=item.get('Name'),
                    description=item.get('Description'),
                    comment=item.get('Comment'),
                )

    @classmethod
    def write_to_csv(cls):

        # field names
        fields = ['Type', 'Name', 'Description', 'Comment']

        # data rows of csv file
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
        return f"{self.__class__.__name__}('type:', '{self.get_type()}', 'name:', '{self.name}', 'description:', '{self.__description}', 'comment:', '{self.comment}', 'created:', '{self.create_date}', 'expiry:', '{self.expiry_date}', )"


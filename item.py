import os
import csv
from enum import Enum
from datetime import timedelta, datetime
# from dateutil import tz

# from reminder import Reminder
# Can't imprt Reminder here due to the following error:
# ImportError: cannot import name 'Item' from partially initialized module 'item' (most likely due to a circular import) (d:\Users\haimk-2\Software2\Python\Python-Examples\MiscHK\MyGitProjects\todo_list\item.py)

# from item_factory import create_reminder

# move the read_from_csv function to nutral file!!!


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
        csv_row.append(self.create_date.strftime('%Y-%m-%d %H:%M:%S'))
        return csv_row


    def get_type(self):
        return Item.ItemType_E.TODO.value
    

    def calculate_total_price(self):
        # return self.__price * self.quantity
        return 0


    @classmethod
    def qqq_read_from_csv(cls):
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
                # Item(
                Reminder(
                    name=item.get('Name'),
                    description=item.get('Description'),
                    comment=item.get('Comment'),
                )

    @classmethod
    def write_to_csv(cls):

        # save current file as backup
        # note: rename gets error on windows, hence use replace
        # os.rename('items.csv', 'items_backup.csv')
        os.replace('items.csv', 'items_backup.csv')

        # field names
        fields = ['Type', 'Name', 'Description', 'Comment', 'Created']

        # data rows of csv file
        rows = []

        for item in Item.todo_list:
            row = item.item_to_csv_row()
            print('row:', row)
            rows.append(row)

        print('rows:', rows)

        # name of csv file
        filename = "items.csv"
            
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


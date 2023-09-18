import csv

from item import Item
from reminder import Reminder


def qqq_create_reminder(name: str, description: str, comment: str, broken_phones=0):
    return Reminder(name, description, comment)


def read_from_csv():
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

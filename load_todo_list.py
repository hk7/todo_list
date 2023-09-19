import csv
from datetime import timedelta, datetime

from item import Item
from reminder import Reminder
from task import Task


def qqq_create_reminder(name: str, description: str, comment: str, broken_phones=0):
    return Reminder(name, description, comment)


def read_from_csv():
    date_format = '%Y-%m-%d %H:%M:%S'

    with open('items.csv', 'r') as f:
        csvreader = csv.DictReader(f)
        items = list(csvreader)

    for item in items:
        print('item:', item)
        if int(item.get('Type')) == 1:
            item2 = Item(
                name=item.get('Name'),
                description=item.get('Description'),
                comment=item.get('Comment'),
            )
            date_str = item.get('Created')
            item2.create_date = datetime.strptime(date_str, date_format)
        elif int(item.get('Type')) == 2:
            task = Task(
                name=item.get('Name'),
                description=item.get('Description'),
                comment=item.get('Comment'),
                deadline=datetime.now() + timedelta(days=2, hours=7)
            )
            date_str = item.get('Created')
            task.create_date = datetime.strptime(date_str, date_format)
        elif int(item.get('Type')) == 3:
            reminder = Reminder(
                name=item.get('Name'),
                description=item.get('Description'),
                comment=item.get('Comment'),
            )
            date_str = item.get('Created')
            reminder.create_date = datetime.strptime(date_str, date_format)


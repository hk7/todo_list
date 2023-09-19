from datetime import timedelta, datetime

from item import Item
from task import Task
from reminder import Reminder

from load_todo_list import read_from_csv

def main():

    # load todo-list from csv file
    # Item.read_from_csv()
    read_from_csv()

    print('hk0:', Item.todo_list)


    '''
    item1 = Item("car", "10000 $", "qwerty...")
    print(item1.description)
    print(item1.comment)
    print(item1.get_type())

    item2 = Reminder("water the plants", "every other day", "very important...don't forget...")
    print(item2.description)
    print(item2.comment)
    print(item2.get_type())

    item3 = Task("task-qqq", "do qqq", "do also qqq2", datetime.now() + timedelta(days=2, hours=7))
    print(item3.description)
    print(item3.comment)
    print(item3.get_type())
    print(item3.deadline)
    '''


    print('hk1:', Item.todo_list)


    # save todo-list to csv file
    Item.write_to_csv()


if __name__ == "__main__":
	main()

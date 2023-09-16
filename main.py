
from item import Item
from reminder import Reminder


def main():

    # load todo-list from csv file
    Item.read_from_csv()


    item1 = Item("car", "10000 $", "qwerty...", 3)
    item1.apply_discount()
    print(item1.description)
    print(item1.comment)
    print(item1.get_type())

    item2 = Reminder("water the plants", "every other day", "very important...don't forget...", 3)
    item2.apply_discount()
    print(item2.description)
    print(item2.comment)
    print(item2.get_type())


    print('hk1:', Item.todo_list)


    # save todo-list to csv file
    Item.write_to_csv()


if __name__ == "__main__":
	main()

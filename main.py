
from item import Item
from reminder import Reminder


def main():

    # load todo-list from csv file
    Item.read_from_csv()


    item1 = Item("car", 1000, 3)
    item1.apply_discount()
    print(item1.price)


    print(Item.todo_list)


if __name__ == "__main__":
	main()

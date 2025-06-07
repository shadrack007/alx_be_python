def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input('Enter item to add: ')
            shopping_list.append(new_item)
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input('Enter the item name to remove: ')

            try:
                shopping_list.remove(item_to_remove)
            except ValueError:
                print('No such item')
            pass
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print('Your shopping list is empty')
            else:
                print('Here is a shopping list')
                for i in range(0, len(shopping_list)):
                    print(f'{i+1}. {shopping_list[i]}')
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
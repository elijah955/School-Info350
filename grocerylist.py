print("Welcome to your grocery list!\n")
grocery_item = {}
grocery_history = []

while True:
    try:
        ch = int(input("Enter the number 1 to view your saved list, enter the number 2 to skip and start your new list."))
    except ValueError:
        print("\nERROR: Please choose 1 or 2.\n")
        continue
    else:
        if ch == 1:
            import csv
            with open("itemsPrices.csv", newline='') as csvfile:
                items = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in items:
                    print(', '.join(row))

            back = int(input("Enter the number 1 to go back."))
            if back != 1:
                print("There's nothing left to do here.")

        elif ch == 2:
            stop = False
            while not stop:
                name = input("\nItem name:\n")
                quantity = int(input("\nQuantity Purchased:\n"))
                cost = input("\nPrice per item:\n")
                grocery_item = {'item_name':name, 'quantity':int(quantity), 'cost':float(cost)}
                grocery_history.append(grocery_item)
                response = input("\nWould you like to enter another item?\nType 'Y' to add another item, or 'N' to quit.")

                if response == 'y':
                    continue

                else:
                    stop = True
                    break
grand_total = 0

for item in grocery_history:
    item_total= item['quantity'] * item['cost']
    grand_total += item_total
    print("%d %s at $%.2f each $%.2f" %(item['quantity'], item['item_name'], item['cost'], item_total))
    item_total = 0
print("\nGrand total: $%.2f" % grand_total)

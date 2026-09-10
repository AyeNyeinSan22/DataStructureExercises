"""
========================================
1. Display all stock quantities
2. Access stock using index
3. Add a new stock quantity
4. Insert stock at a specific position
5. Update stock quantity
6. Delete stock by position
7. Delete a specific stock quantity
8. Search for a stock quantity
9. Sort stocks in ascending order
10. Sort stocks in descending order
11. Reverse stock records
12. Find highest stock quantity
13. Find lowest stock quantity
14. Calculate total number of stocks
15. Calculate average stock quantity
16. Count occurrence of a stock quantity
17. Display number of inventory records
18. Display low-stock and sufficient-stock items
19. Restock all low-stock items
20. Display inventory statistics
21. Clear inventory
22. Exit
"""

stocks = [50, 20, 90, 16, 60, 30, 100]
LOW_STOCK_LIMIT = 30
print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
print("1.  Display all stock quantities")
print("2.  Access stock using index")
print("3.  Add a new stock quantity")
print("4.  Insert stock at a specific position")
print("5.  Update stock quantity")
print("6.  Delete stock by position")
print("7.  Delete a specific stock quantity")
print("8.  Search for a stock quantity")
print("9.  Sort stocks in ascending order")
print("10. Sort stocks in descending order")
print("11. Reverse stock records")
print("12. Find highest stock quantity")
print("13. Find lowest stock quantity")
print("14. Calculate total number of stocks")
print("15. Calculate average stock quantity")
print("16. Count occurrence of a stock quantity")
print("17. Display number of inventory records")
print("18. Display low-stock and sufficient-stock items")
print("19. Restock all low-stock items")
print("20. Display inventory statistics")
print("21. Clear inventory")
print("22. Exit")

while True:
    choice = input("\nEnter your choice (1-22): ")

    match choice:
        case "1":
            # Display all stock quantities
            if not stocks:
                print("Inventory is empty.")
            else:
                print("Stock quantities in inventory:")
                for index, quantity in enumerate(stocks):
                    print(f"  Index {index} : {quantity}")

        case "2":
            # Access stock using index
            if not stocks:
                print("Inventory is empty.")
            else:
                index = int(input(f"Enter index (0 to {len(stocks)-1}): "))
                if 0 <= index < len(stocks):
                    print(f"Stock quantity at index {index} : {stocks[index]}")
                else:
                    print("Invalid index.")

        case "3":
            # Add a new stock quantity
            qty = int(input("Enter the new stock quantity to add: "))
            if qty > 0:
                stocks.append(qty)
                print(f"Stock quantity {qty} added to the inventory.")
            else:
                print("Stock quantity must be positive.")

        case "4":
            # Insert stock at a specific position
            if not stocks:
                print("Inventory is empty.")
            else:
                position = int(input(f"Enter position to insert (0 to {len(stocks)}): "))
                if 0 <= position <= len(stocks):
                    quantity = int(input("Enter the stock quantity to insert: "))
                    if quantity > 0:
                        stocks.insert(position, quantity)
                        print(f"Inserted {quantity} at position {position}")
                    else:
                        print("Stock quantity must be positive.")
                else:
                    print("Invalid position.")

        case "5":
            # Update stock quantity
            if not stocks:
                print("Inventory is empty.")
            else:
                index = int(input(f"Enter index to update (0 to {len(stocks)-1}): "))
                if 0 <= index < len(stocks):
                    new_stock = int(input("Enter the new stock quantity: "))
                    if new_stock > 0:
                        stocks[index] = new_stock
                        print(f"Stock at index {index} updated to {new_stock}.")
                    else:
                        print("Stock quantity must be positive.")
                else:
                    print("Invalid index.")

        case "6":
            # Delete stock by position
            if not stocks:
                print("Inventory is empty.")
            else:
                index = int(input(f"Enter index to delete (0 to {len(stocks)-1}): "))
                if 0 <= index < len(stocks):
                    remove_item = stocks.pop(index)
                    print(f"Stock quantity {remove_item} removed at index {index}.")
                else:
                    print("Invalid index.")

        case "7":
            # Delete a specific stock quantity
            if not stocks:
                print("Inventory is empty.")
            else:
                quantity_to_delete = int(input("Enter the stock quantity to delete: "))
                if quantity_to_delete in stocks:
                    stocks.remove(quantity_to_delete)
                    print(f"Deleted {quantity_to_delete} from the list.")
                else:
                    print(f"Stock quantity {quantity_to_delete} not found.")

        case "8":
            # Search for a stock quantity
            if not stocks:
                print("Inventory is empty.")
            else:
                qty_to_search = int(input("Enter the stock quantity to search: "))
                if qty_to_search in stocks:
                    index = stocks.index(qty_to_search)
                    print(f"Stock quantity {qty_to_search} found at index {index}.")
                else:
                    print(f"Stock quantity {qty_to_search} not found.")

        case "9":
            # Sort ascending
            if not stocks:
                print("Inventory is empty.")
            else:
                stocks.sort()
                print("Sorted stocks in ascending order:", stocks)

        case "10":
            # Sort descending
            if not stocks:
                print("Inventory is empty.")
            else:
                stocks.sort(reverse=True)
                print("Sorted stocks in descending order:", stocks)

        case "11":
            # Reverse stock records
            if not stocks:
                print("Inventory is empty.")
            else:
                stocks.reverse()
                print("Reversed stock records:", stocks)

        case "12":
            # Find highest
            if not stocks:
                print("Inventory is empty.")
            else:
                max_qty = max(stocks)
                index = stocks.index(max_qty)
                print(f"Highest stock: {max_qty} at index {index}")

        case "13":
            # Find lowest
            if not stocks:
                print("Inventory is empty.")
            else:
                min_qty = min(stocks)
                index = stocks.index(min_qty)
                print(f"Lowest stock: {min_qty} at index {index}")

        case "14":
            # Total
            if not stocks:
                print("Inventory is empty. Total: 0.")
            else:
                total_qty = sum(stocks)
                print(f"Total: {total_qty} quantities across {len(stocks)} records.")

        case "15":
            # Average
            if not stocks:
                print("Inventory is empty. Average: N/A.")
            else:
                average_qty = sum(stocks) / len(stocks)
                print(f"Average stock quantity: {average_qty:.2f}")

        case "16":
            # Count occurrence
            if not stocks:
                print("Inventory is empty.")
            else:
                qty_to_count = int(input("Enter the stock quantity to count: "))
                count = stocks.count(qty_to_count)
                print(f"Occurrence of {qty_to_count} is {count} times.")

        case "17":
            # Number of records
            print(f"Number of inventory records: {len(stocks)}")

        case "18":
            # Low-stock and sufficient-stock
            if not stocks:
                print("Inventory is empty.")
            else:
                low = [(i, qty) for i, qty in enumerate(stocks) if qty < LOW_STOCK_LIMIT]
                sufficient = [(i, qty) for i, qty in enumerate(stocks) if qty >= LOW_STOCK_LIMIT]

                print(f"\nLow stock items (below {LOW_STOCK_LIMIT}):")
                if low:
                    for i, qty in low:
                        print(f"  Index {i} : stock {qty}")
                else:
                    print("  None.")

                print(f"\nSufficient stock items ({LOW_STOCK_LIMIT}+):")
                if sufficient:
                    for i, qty in sufficient:
                        print(f"  Index {i} : stock {qty}")
                else:
                    print("  None.")

        case "19":
            # Restock low-stock items
            if not stocks:
                print("Inventory is empty.")
            else:
                restock_qty = int(input("Enter quantity to restock each low-stock item to: "))
                if restock_qty <= 0:
                    print("Restock quantity must be positive.")
                else:
                    count = 0
                    for i in range(len(stocks)):
                        if stocks[i] < LOW_STOCK_LIMIT:
                            stocks[i] = restock_qty
                            count += 1
                    if count > 0:
                        if restock_qty < LOW_STOCK_LIMIT:
                            print(f"Warning: {restock_qty} is still below limit ({LOW_STOCK_LIMIT}).")
                        print(f"Restocked {count} item(s) to {restock_qty} units.")
                    else:
                        print("No low-stock items to restock.")

        case "20":
            # Inventory statistics
            print("\n===== INVENTORY STATISTICS =====")
            print(f"Number of records: {len(stocks)}")
            if stocks:
                print(f"Total stock quantity: {sum(stocks)}")
                print(f"Average stock quantity: {sum(stocks) / len(stocks):.2f}")
                print(f"Highest stock quantity: {max(stocks)}")
                print(f"Lowest stock quantity: {min(stocks)}")
                print(f"Low-stock records: {sum(1 for q in stocks if q < LOW_STOCK_LIMIT)}")
                print(f"Sufficient-stock records: {sum(1 for q in stocks if q >= LOW_STOCK_LIMIT)}")
            else:
                print("Total stock quantity: 0")
                print("Average stock quantity: N/A")
                print("Highest stock quantity: N/A")
                print("Lowest stock quantity: N/A")
                print("Low-stock records: 0")
                print("Sufficient-stock records: 0")

        case "21":
            # Clear inventory
            stocks.clear()
            print("Inventory cleared.")

        case "22":
            # Exit
            print("Exiting inventory system. Goodbye!")
            break

        case _:
            print("Invalid choice. Please enter a number between 1 and 22.")
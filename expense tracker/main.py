from Expense import Expense

def main():

    all_expenses = "expense tracker/expenses.csv"
    # get user input    
    expense = get_user_input()
    print(expense)

    # save into file
    save_input(expense, all_expenses)
    # read and provide summary

def get_user_input():
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))

    product_categories = [
        "Utilities & Essentials",
        "Grocery & Food",
        "Transportation",
        "Entertainment",
        "Savings & Investments"
    ]

    while True:
        print("Choose category: ")
        for i, cat in enumerate(product_categories):
            print(f"{i + 1}. {cat}")
        
        category_range = f"[1 - {len(product_categories)}]"
        product_category = int((input("->"))) - 1
        break

    if product_category in range(len(product_categories)):
        selected_category = product_categories[product_category]
        new_expense = Expense(name = product_name, price = product_price, category = selected_category)
        return new_expense
    
    else:
        print("invalid choice")

def save_input(expense: Expense, all_expenses):
    with open(all_expenses, "a") as f:
        f.write(f"{expense.name}, {expense.price}, {expense.category}\n")

if __name__ == "__main__":
    main()

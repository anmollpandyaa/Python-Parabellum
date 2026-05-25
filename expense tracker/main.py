import locale
from Expense import Expense



def main():

    budget = 20000

    all_expenses = "expense tracker/expenses.csv"
    # get user input    
    # expense = get_user_input()
    # print(expense)

    # # save into file
    # save_input(expense, all_expenses)

    # read and provide summary
    analyse_expenses(all_expenses, budget)

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

def analyse_expenses(all_expenses, budget):
    expenses = []
    with open(all_expenses, "r") as f:
        lines = f.readlines()

        for line in lines:
            name, price, category = line.strip().split(",")
            line_expense = Expense(name = name, price = float(price), category = category)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        cat = expense.category

        if cat in amount_by_category:
            amount_by_category[cat] += expense.price
        
        else:
            amount_by_category[cat] = expense.price
    
    for cat, price in amount_by_category.items():
        print(f"   •{cat}: ₹{price}")
    
    total_spent = sum([x.price for x in expenses])
    print(red_text(f"Total spent: {format_inr(total_spent)}"))

    remaining_budget = budget - total_spent
    print(green_text(f"Remaining: {format_inr(remaining_budget)}"))

locale.setlocale(locale.LC_MONETARY, 'en_IN')
def format_inr(amount):
    formatted = locale.currency(amount, grouping=True)
    return formatted.replace("₹ ", "₹")

def red_text(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    return f"{RED}{text}{RESET}"

def green_text(text):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    return f"{GREEN}{text}{RESET}"

if __name__ == "__main__":
    main()

class Category:

    ledger = []
    balance = 0
    name = ""

    def __init__(self, categories):
        self.name = categories.lower()
        self.balance = 0
        self.ledger = []

    def __repr__(self):
        tempCat = self.name.capitalize().rjust(15+len(self.get_name())//2, "*")
        tempCat = tempCat.ljust(30, "*")
        for i in self.ledger:
            lenForDesc = 30 - len('%.2f' % i["amount"]) - 1
            k = f'{i["description"][:lenForDesc]:<{lenForDesc}}'
            tempCat += '\n' + k + " " + '%.2f' % i["amount"]
        tempCat += "\nTotal: " + str(self.balance)
        return tempCat

    def get_name(self):
        return self.name

    def deposit(self, amount, desc=""):
        self.balance += amount
        self.ledger.append({"amount":amount, "description":desc})

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return True
        else:
            return False

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":desc})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":f"Transfer to {category.get_name().capitalize()}"})
            category.balance += amount
            category.ledger.append({"amount":amount, "description":f"Transfer from {self.name.capitalize()}"})
            return True
        else:
            return False

def print_o(percentage, balances):
    chartData = str(percentage).rjust(3, " ") + "|"
    for _, balance in balances:
        if percentage <= balance:
            chartData += " o "
        else:
            chartData += "   "
    return chartData + " \n"

def get_deduction(transactions):
    sum_deductions = 0
    for i in transactions:
        if i['amount'] < 0:
            sum_deductions -= i['amount']
    return abs(sum_deductions)

def create_spend_chart(categories):
    balances = []
    totalSpent = 0
    for i in categories:
        totalSpent += get_deduction(i.ledger)
    longest = 0
    for i in categories:
        balances.append([i.get_name().capitalize(), int(get_deduction(i.ledger)/totalSpent*100)])
        if longest < len(i.get_name()):
            longest = len(i.get_name())
    chart = [i for i in range(100, -1, -10)]
    returnString = "Percentage spent by category\n"
    for i in chart:
        returnString += print_o(i, balances)
    lineString = "    ".ljust(14, "-")
    names = "\n"
    for i in range(0,longest):
        names += "    "
        for a, _ in balances:
            try:
                names += " " + a[i] + " "
            except:
                names += "   "
        names += ' \n'
    returnString += lineString + names[:-1]
    return returnString

food = Category("Food")
entertainment = Category("entertainment")
business = Category("business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(business)
print(entertainment)
# print(food.ledger[food.get_name()]['transactions'])
print(create_spend_chart([business, food, entertainment]))

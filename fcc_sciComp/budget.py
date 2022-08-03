class Category:

    cat = dict()
    name = ""

    def __init__(self, categories):
        self.name = categories.lower()
        self.cat[self.name] = {"balance":0, "transactions":[]}
        #print(self.cat)

    def __repr__(self):
        tempCat = self.name.capitalize().rjust(15+len(self.cat)//2, "*")
        tempCat = tempCat.ljust(30, "*")
        #print(self.cat[self.name]["transactions"])
        for i in self.cat[self.name]["transactions"]:
            lenForDesc = 30 - len('%.2f' % i["amount"]) - 1
            k = f'{i["description"][:lenForDesc]:<{lenForDesc}}'
            tempCat += '\n' + k + " " + '%.2f' % i["amount"]
        tempCat += "\nTotal: " + str(self.cat[self.name]["balance"])
        return tempCat

    def get_name(self):
        return self.name

    def deposit(self, amount, desc=""):
        self.cat[self.name]["balance"] += amount
        self.cat[self.name]["transactions"].append({"amount":amount, "description":desc})
        #print(self.cat)

    def check_funds(self, amount):
        if self.cat[self.name]["balance"] - amount >= 0:
            self.cat[self.name]["balance"] -= amount
            return True
        else:
            return False

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.cat[self.name]["transactions"].append({"amount":-amount, "description":desc})
            #print(self.cat)
            return True
        else:
            return False

    def get_balance(self):
        return self.cat[self.name]["balance"]

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.cat[self.name]["transactions"].append({"amount":-amount, "description":f"Transfer to {category.get_name().capitalize()}"})
            self.cat[category.get_name()]["balance"] += amount
            self.cat[category.get_name()]["transactions"].append({"amount":amount, "description":f"Transfer from {self.name.capitalize()}"})
            #print(self.cat)
            return True
        else:
            return False

def print_o(percentage, balances):
    chartData = str(percentage).rjust(3, " ") + "|"
    for _, balance in balances:
        # #print(balance)
        if percentage <= balance:
            chartData += " o "
        else:
            chartData += "   "
    return chartData + "\n"


def create_spend_chart(categories):
    balances = []
    totalBalance = 0
    for i in categories:
        totalBalance += i.get_balance()
    longest = 0
    for i in categories:
        balances.append([i.get_name().capitalize(), int(round(i.get_balance()/totalBalance, 1)*100)])
        if longest < len(i.get_name()):
            longest = len(i.get_name())
    #print(balances)
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
        names += '\n'
    returnString += lineString + names
    return returnString



# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# #print(food.get_balance())
# clothing = Category("Clothing")
# clothing.deposit(500, "initial deposit")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)
# print(auto)
# print(food.cat)
# print(create_spend_chart([food, clothing, auto]))

# k = int(round(10/100, 1)*100)
# s = '%.2f' % 10.12999
# print(s)

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
print(create_spend_chart([business, food, entertainment]))

import sys

def round_total_cost(meal_cost, tip_percent, tax_percent):
    tip = ((meal_cost * tip_percent) / 100)
    tax = ((meal_cost * tax_percent) / 100)
    totalcost = meal_cost + tip + tax
    print(totalcost)
    #print("The total meal cost is %d dollars." % int(totalcost))
    print("The total meal cost is {} dollars.\n".format(round(totalcost)))

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    round_total_cost(meal_cost, tip_percent, tax_percent)
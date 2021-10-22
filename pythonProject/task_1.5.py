
def check_input(num):
    if num < 0:
        raise RecursionError("You put a negative number.")
    else:
        return num


while True:
    try:
        revenue = int(input("Please, enter the revenue: "))
        result = check_input(revenue)
    except RecursionError:
        print("You put a negative number.")
        continue
    except ValueError:
        print("You entered not a number.")
        continue
    else:
        while True:
            try:
                costs = int(input("Please, enter the costs: "))
                result = check_input(costs)
            except RecursionError:
                print("You put a negative number.")
                continue
            except ValueError:
                print("You entered not a number.")
                continue
            else:
                profit_loss = revenue - costs

                if profit_loss > 0:
                    profitability = (profit_loss / revenue) * 100
                    print(f"Your company's profit is {profit_loss} USD.")
                    staff = int(input("Please, enter a number of employees to calculate the profit per employee: "))
                    profit_per_employee = round(profit_loss / staff, 2)
                    print(f"Your company's profit per employees is {profit_per_employee} USD.")

                elif profit_loss == 0:
                    print("Your company has no profit.")

                else:
                    print(f"Your company's loss is {profit_loss} USD.")
                break
    break

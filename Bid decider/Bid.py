import logo

print(logo)
def highest_number(biddest_number):
    score = 0
    winner = ""

    for high in biddest_number:
        number = biddest_number[high]

        if number > score:
            score = number
            winner = high
    print(f"Okay! The winner is {winner} and the bid is {score} $ 😀")

bid = {}
Programme_end = True

while Programme_end:

    user_name = input("What is your name: ").title()
    user_bide = int(input("What is your bid $: "))
    bid[user_name] = user_bide
    any_biders = input("If there is any biders type 'yes' or 'no': ").capitalize()

    if any_biders == 'Yes':
        print("\n"*100)
    if any_biders == 'No':
        Programme_end = False
        highest_number(biddest_number = bid)


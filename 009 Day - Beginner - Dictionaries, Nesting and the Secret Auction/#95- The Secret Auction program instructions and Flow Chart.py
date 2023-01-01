from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.

auctioneers = []
end = False
print(logo)


def reveal_winner(arr):
    name = ""
    bid = 0
    for i in arr:
        if i["bid"] > bid:
            name = i["name"]
            bid = i["bid"]
    print(f"The winner is {name} with a bid of ${bid}")


def add_item():
    auctioneer = {
        "name": input("What is your name?: "),
        "bid": int(input("What is your bid?: $")),
    }
    auctioneers.append(auctioneer)


add_item()

while not end:
    new_auctioneer = input("Are there any other bidders? Type 'yes' or 'no'. \n")

    if new_auctioneer == "yes":
        clear()
        add_item()
    else:
        end = True
        reveal_winner(auctioneers)

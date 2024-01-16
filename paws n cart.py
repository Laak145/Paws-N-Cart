# This is a Python program for an online shopping cart for pet products
# The program is designed to enable user be able to amend their shopping list.
# as well as calculates the total cost of items.
# The shopping cart also provides info on pet adoption centres and care advice.

# background codes
line = "-"*40
shopping_cart = []
total = []
welcome_msg = "         Welcome to Paws n Cart!    "
appreciate_msg = "Thank you for your custom at Paws n Cart!"
goodbye_msg = "Goodbye!"

# main menu
shop = "shop - to start shopping"
services = "services - for info on pet care and adoption centres"

# print outputs
print()
print(welcome_msg)

# Menu for pet services
pet_care = "Pet Care - pet care information"
pet_adoption = "Pet Adoption - pet adoption centres"

# print outputs
print(line, " * Our offerings are * : Shop and Services !", line, sep="\n")
print("           *     Menu:       *")
print(shop)
print(services)
print(line)

# Menu for pet supplies
menu_cart = {"chicken": 1.99, "turkey": 2.99, "lamb-mix": 3.70,
             "duck-toy": 0.99, "pig-toy": 1.00, "collar": 2.50,
             "jumper": 4.99, "bed": 10.00, "blanket": 3.82, "shampoo": 1.00,
             "towel": 3.00, "brush": 3.50}
try:
    while True:
        # This asks the user for choice; shop or services.
        welcome_question = input("To continue, enter either shop or services"
                                 " (enter stop to exit) : \n").lower()
        if welcome_question == "stop":

            print(line, appreciate_msg, line, sep="\n")
            print(goodbye_msg)
            break

        # Block of codes to manage user's choice to shop
        if welcome_question == "shop":
            print("You're about to shop!", "Enter:", "1 to add items & view "
                                                     "cart", "2 to remove "
                                                     "items & view cart", "3 "
                                                     "to checkout", sep="\n")

            shop_question = int(input("(For other options or to exit, enter "
                                      "done) :  \n"))
            if shop_question == 4:
                print(line, appreciate_msg, line, sep="\n")

            elif shop_question <= 0 or shop_question >= 5:
                print("just numbers 1 to 4 please!")

            # Block of codes to manage user's choice to add items to cart
            elif shop_question == 1:
                print("**  **  **        Menu        **  **  **")
                for key, value in menu_cart.items():
                    print(f"{key:20} : £{value:.2f}")
                print("**  **  **  **  **  **  **  **  **")
                while True:

                    print(line, "Your shopping cart: ", shopping_cart, line,
                          sep="\n")

                    print("You're about to add an item to your cart. ")

                    item_added = input("To continue, add an item from the menu"
                                       " (to stop adding, enter done): ").lower()
                    price_added = float(input("Enter the item price e.g. 2.15"
                                        " (for other options or to exit, "
                                              "enter 5050): "))
                    if item_added == "done":
                        print(line, "This is your shopping cart:",
                              shopping_cart, line, sep="\n")
                    if price_added == 5050:
                        print()
                        break

                    if not menu_cart.get(item_added or price_added) is None:
                        shopping_cart.append(item_added)
                        shopping_cart.append(price_added)
                        print("------------------------------------")
                        print(f"** The item: *{item_added} at price: £"
                              f"{price_added} is added!")

                    else:
                        print()
                        print(f" The item: *{item_added} at price £:"
                              f"{price_added} has NOT been added. ")
                        print(" * * Item or price not in the menu! * * ")

            # Block of codes to manage user's choice to remove items from cart
            elif shop_question == 2:
                print("Your cart: ", shopping_cart)
                while not shopping_cart == []:
                    print("You're about to remove an item from your cart.")
                    item_removed = input("Enter an item you'd like to remove "
                                         "(terminate to exit): ").lower()
                    price_removed = float(input("Enter the item price e.g 1.23"
                                          " (for other options or to exit,"
                                                "enter 2020): "))

                    if item_removed == "finished":
                        print(line, "Your shopping cart:",
                              shopping_cart, line, sep="\n")
                    if price_removed == 2020:
                        print()
                        break

                    if item_removed or price_removed in shopping_cart:
                        shopping_cart.remove(item_removed)
                        shopping_cart.remove(price_removed)

                        print(f"** The item: {item_removed} at price: £"
                              f"{price_removed} is removed!")
                        print(line, "Your updated shopping cart is :",
                              shopping_cart, line, sep="\n")

                    else:
                        print(f" The item: *{item_removed} at price £: "
                              f"{price_removed} has NOT been taken off. ")
                        print(" * * Item or price not in the menu! * * ")
                        print(line, "Your shopping_cart is :",
                              shopping_cart, line, sep="\n")

            # Block of codes to manage user's choice to checkout cart items
            elif shop_question == 3:
                print(line, "Your Checkout!", line, sep="\n")
                print("Here is your final shopping cart: ", shopping_cart)

                for item_added in shopping_cart:
                    total += menu_cart.get(item_added)
                print(item_added, "£", end=" ")

                # the order total
                print("-------------------------------")
                print(f"Your total order is: £{total}")

                print(line)
                print(appreciate_msg)
                print(goodbye_msg, line, sep="\n")

        # Block of codes to manage user's choice for pets services
        elif welcome_question == "services":
            print("You're onto the pet services!")
            print("Here is the menu: ")
            print(line)
            print("* *    Services Menu   * *")
            print(line)

            # Block of codes to print pet services menu
            print(pet_care)
            print(pet_adoption)
            print(line)

            # These ask user for choice; care advice or adoption info.
            print("For care advice, enter C.", "For adoption info, enter "
                  "A.", sep="\n")
            service_question = input("For other options or to exit"
                                     ", enter Q): ").lower()
            print(line)

            # Block of codes to manage user's choice for pet care advice.
            if service_question == "c":
                print("You're at the right place for your pet care"
                      " advice!", "Enter the type of pet care you require e.g,"
                      " cat dog fish or other.", sep="\n")

                care_question = input("(For other options or to exit, enter"
                                      " Z): ").lower()

                # Block of codes to manage user's choice for cat care advice.
                if care_question == "cat":
                    print(line)
                    print("* Cats are cute!", "Below is an easy download pack "
                          "for cat care", "Download: Essential Fact Sheet for "
                          "your cat.", "We hope you find it useful!", sep="\n")
                    print(line)
                    print(appreciate_msg)
                    print(goodbye_msg, line, sep="\n")

                # Block of codes to manage user's choice for dog care advice.
                elif care_question == "dog":
                    print()
                    print("* Dogs are the best!", "Below is an easy download "
                          "pack for dog care!", "Download: Essential "
                          "Fact Sheet for your dog.", "We hope you find it "
                          "useful!", sep="\n")
                    print(line)
                    print(appreciate_msg)
                    print(goodbye_msg, line, sep="\n")

                # Block of codes to manage user's choice for fish care advice.
                elif care_question == "fish":
                    print()
                    print("* Fish are cool!", "Below is an easy download for "
                          "fish care", "Download: Essential Fact Sheet for you"
                          "r fish.", "We hope you find it useful!", sep="\n")

                    print(line)
                    print(appreciate_msg)
                    print(goodbye_msg, line, sep="\n")

                # Block of codes to manage user's choice for other animals care
                elif care_question == "other":
                    print()
                    print("* We understand why you love them!", "Below is an  "
                          "easy download:", "Essential Fact Sheet for "
                          "your pet.", "We hope you find it useful!", sep="\n")
                    print(line)
                    print(appreciate_msg)
                    print(goodbye_msg, line, sep="\n")

                else:
                    print(line, appreciate_msg, line, sep="\n")

            # code manages user's choice for adoption information
            elif service_question == "a":
                print()
                print("* We are happy to help!")
                print("For friendly & custom adoption info relevant to you,",
                      "please contact: Kat at Pets n Me Adoption Centre",
                      "Telephone - 0102031234", sep="\n")

                print(line)
                print(appreciate_msg)
                print(goodbye_msg, line, sep="\n")

        # Code manages errors from misspelt words or type errors.
        elif welcome_question != "shop" or "services":
            print("You have made wrong entries, look again!")

# Codes further handle error from other wrong inputs.
except ValueError as e:
    print(e)
    print("Wrong entry or null input entered :( ")
except AttributeError as e:
    print(e)
    print("Wrong entry")
except KeyError as e:
    print(e)
    print("Ah! I couldn't find your request")
except ZeroDivisionError as e:
    print(e)
    print("Division by zero has occurred!")
except RuntimeError as e:
    print(e)
    print("A runtime error, very exceptional!")

# End of program
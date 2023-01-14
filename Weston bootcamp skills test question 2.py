class product:
    #Set up a new product, VAT set at 20%. Takes cost per unit in pence
    VAT_rate = 20
    def __init__(self,product_name,amount,price_per_unit):
        self.product_name = product_name
        self.total_bought = amount
        self.price = round((amount * price_per_unit)/100,2)
        self.VAT = 0
        self.total_cost = 0
    # Functions to calculate different outputs (might have been easier and tidier to set calculation/
    # in the attributes above!)
    def calculate_vat(self):
        self.VAT = round((self.price * (product.VAT_rate/100)),2)
    def total(self):
        self.total_cost = round((self.price + self.VAT),2)
    def display_invoice(self):
        print (f"Amount of {self.product_name} bought : {self.total_bought}\n"
                f"Cost of {self.product_name} before tax : £{self.price:.2f}\n"
                f"Cost of VAT added : £{self.VAT:.2f}\n"
                f"Total cost of gummies : £{self.total_cost:.2f}")
def GummyAmount():
    while True:
        amount = input("Please enter how many you would like: ")
        if amount.isdigit():
            return int(amount)
        else:
            print("Please enter a number")
            continue
def continue_choice():
    # Check that the input is valid, it must be either Y,N,y,n
    valid = "YNyn"
    while True:
        play =input("Would you like to make another purchase? Y/N ? ")
        if play in (valid):
            return play
        else:
            print("Please enter Y or N")
            continue
running = True
while running == True:
    #Ask how many gummies the customer wants to purchas
    gummy_quantity = GummyAmount()

    #Create new gummies object and print results

    gummies = product("gummies",gummy_quantity,50)
    gummies.calculate_vat()
    gummies.total()
    gummies.display_invoice()
    # Ask user if the would like to make another purchase
    another_purchase = continue_choice()

    if another_purchase.upper() == "Y":
        continue
    else:
        print("Thank you for shopping with Yummy Gummies")
        running = False



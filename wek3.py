def calculate_discount(price, discount_percent):
    """
    Calculates the discounted price based on a percentage.
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

def get_user_input():
    """
    Prompts the user for the original price and discount percentage.
    """
    while True:
        try:
            original_price = float(input("Enter the original price of the item: "))
            discount_percentage = float(input("Enter the discount percentage (0-100): "))
            
            if original_price < 0 or not (0 <= discount_percentage <= 100):
                print("Please enter a non-negative price and a discount percentage between 0 and 100.")
                continue
            
            return original_price, discount_percentage
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to handle the user interaction and price calculation.
    """
    price, discount_percent = get_user_input()

    if discount_percent >20:
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${price:.2f}")

if __name__ == "__main__":
    main()
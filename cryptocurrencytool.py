# crypto_calculator.py
def crypto_calculator(amount, price_per_coin):
    try:
        total_value = amount * price_per_coin
        return f"Your cryptocurrency value is: ${total_value:,.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount of cryptocurrency you own: "))
        price_per_coin = float(input("Enter the current price per coin: "))
        result = crypto_calculator(amount, price_per_coin)
        print(result)
    except ValueError:
        print("Please enter valid numbers.")

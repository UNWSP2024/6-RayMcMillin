def calculate_tax(total_sales):
   
    state_tax_rate = 0.05
    county_tax_rate = 0.025

    county_tax = total_sales * county_tax_rate
    state_tax = total_sales * state_tax_rate
    total_tax = county_tax + state_tax

    return county_tax, state_tax, total_tax

def main():
    try:
        total_sales = float(input("Please enter the total sales for the month: "))
        
        county_tax, state_tax, total_tax = calculate_tax(total_sales)
        
        print(f"Total Sales: ${total_sales:.2f}")
        print(f"County Sales Tax: ${county_tax:.2f}")
        print(f"State Sales Tax: ${state_tax:.2f}")
        print(f"Total Sales Tax: ${total_tax:.2f}")
        
    except ValueError:
        print("This number is invalid. Please enter a numerical value. (ex. 10000)")


if __name__ == "__main__":
    main()

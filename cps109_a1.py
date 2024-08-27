# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 22:34:20 2023

@author: 2004f
"""
''' This is a python program for managing stocks right from the command prompt.
It allows the users to load stocks from a file. Users can purchase,sell or view
available stocks. If there are no stocks available to sell, it will start with an
empty list. It has a function called log_and_print which outputs onto the screen
as well as onto an external text file. It's a simple program without any complication.User can buy upto 10 shares'''

def log_and_print(message, file):
    print(message)  # Print message to console
    file.write(message + '\n')  # Write message to file with a newline

# Load portfolio from the file
def load_portfolio(file_name, output_file):
    portfolio = {}  # Initialize an empty dictionary for the portfolio
    try:
        with open(file_name, 'r') as file:  
            for line in file:  
                stock, shares = line.strip().split(',')
                portfolio[stock] = float(shares)  # Add stock and its shares to the portfolio
    except FileNotFoundError:  # Handle case where file does not exist
        log_and_print(f"{file_name} not found. Start with an empty porfolio.", output_file)
    return portfolio  # Return the loaded or empty portfolio

# Saving portfolio
def save_portfolio(portfolio, file_name):
    with open(file_name, 'w') as file:  # Opening the file in write mode
        for stock, shares in portfolio.items():  
            file.write(f'{stock},{shares}\n')  
# Manage purchase of stocks
def purchase(portfolio, stock_name, shares_to_buy, output_file):
    portfolio[stock_name] = portfolio.get(stock_name, 0) + shares_to_buy  
    log_and_print(f"Purchased {shares_to_buy} shares of {stock_name}.", output_file)  # Log the purchase

# Managing the selling of stocks
def sell_stock(portfolio, stock_name, shares_to_sell, output_file):
    if portfolio.get(stock_name, 0) >= shares_to_sell:  # Check if enough shares are available to sell
        portfolio[stock_name] -= shares_to_sell  # Subtract the sold shares from the portfolio
        log_and_print(f"Sold {shares_to_sell} shares of {stock_name}.", output_file)  # Log the sale
    else:
        log_and_print(f"Not enough shares of {stock_name} to sell.", output_file)  # Log if not enough shares

# Displaying what's in the portfolio after buying or selling or before that
def show_portfolio(portfolio, output_file):
    if portfolio:  # Check if portfolio is not empty
        log_and_print("Current portfolio:", output_file)  # Log the portfolio header
        for stock, shares in portfolio.items():  # Iterate through each stock in the portfolio
            log_and_print(f"{stock}: {shares} shares", output_file)  # Log each stock and its share count
    else:
        log_and_print("Your portfolio is empty.", output_file)  # Log if portfolio is empty

# 
def work():
    file_name = 'stocks.txt'  # Name of the file to load/save the portfolio
    output_file_name = 'cps109_a1_output.txt'  # Name of the output file to log actions
    
    with open(output_file_name, 'w') as output_file: 
        portfolio = load_portfolio(file_name, output_file) 
        
        while True:  
            log_and_print("\nAvailable actions: [P]urchase, [S]ell, [D]isplay portfolio, [Q]uit", output_file)
            action = input("What would you like to do? ")  # Prompt user for an action

            if action.lower() == 'p':  # User chooses to purchase stocks
                stock_name = input("Enter the stock symbol to buy: ")  # Get stock symbol from user
                shares = float(input(f"How many shares of {stock_name} would you like to buy? "))
                if shares > 10:
                    print("Max shares limit reached for buying")
                    
                else:# Get number of shares
                 purchase(portfolio, stock_name, shares, output_file)  # Call purchase function
            elif action.lower() == 's':  # User chooses to sell stocks
                stock_name = input("Enter the stock symbol to sell: ")  # Get stock symbol from user
                shares = float(input(f"How many shares of {stock_name} would you like to sell? "))  # Get number of shares
                sell_stock(portfolio, stock_name, shares, output_file)  
            elif action.lower() == 'd':  # User chooses to display portfolio
                show_portfolio(portfolio, output_file)  
            elif action.lower() == 'q':  # User chooses to quit
                save_portfolio(portfolio, file_name)  
                log_and_print("Portfolio saved.", output_file) 
                break 
            else:
                log_and_print("Invalid action. Please choose a valid action.", output_file)  

if __name__ == '__main__':
    work()  # Run the interact function if the script is executed directly
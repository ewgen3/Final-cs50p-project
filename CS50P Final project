from tabulate import tabulate
import pyfiglet
from pyfiglet import Figlet
import csv
import sys
import re
import yfinance as yf
from datetime import date
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
import warnings
# Set logging level for yfinance to suppress warnings
warnings.filterwarnings("ignore", message="Series.__getitem__ treating keys as positions is deprecated.*")

def main():
    introduction = pyfiglet.figlet_format("PORTFOLIO SIMULATOR", font="small")
    print(introduction)
    create_portfolio()

def create_portfolio():
    while True:
        options = [
            ["Options", "Action"],
            ["L", "Login"],
            ["S", "Signup"],
            ["E", "Exit"],
        ]
        print(tabulate(options, headers="firstrow", tablefmt="psql"))
        choice = input(Fore.BLUE + "Please input L/S/E : ").upper()
        if choice not in ["L","S","E"]:
            print_color(Fore.RED, "!!! Invalid input, please try again !!!")
            continue

        elif choice == "E":
            print_color(Fore.YELLOW, "Goodbye! See you soon :)")
            sys.exit()

        elif choice == "L":
            username = input("Portfolio name?: ").lower()
            if check_login(username):
                print_color(Fore.GREEN , "Login successful!")
                display_portfolio(username)
            else:
                print_color(Fore.RED , "Portfolio does not exist, signup to create a portfolio")

        else:
            username = input("Portfolio name?: ")
            if check_create_new(username):
                print_color(Fore.GREEN , "Signup successful")

            else:
                print_color(Font.RED , "Profile already exists")

def check_login(username):
    with open("usernames.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and username == row[0].strip().lower():
                return True
        return False

def check_create_new(username):
    with open("usernames.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and username == row[0]:
                return False

                # If username is new, add username and password to the login_database.csv
    with open("usernames.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([username])
    return True
  
def display_portfolio(username):
    portfolio = load_portfolio(username)

    while True:

        displayscreen =[
            ["Options","Description"],
            ["1.", "View portfolio"],
            ["2.", "Add stock:Percentage"],
            ["3.", "Remove stock:Percentage"],
            ["4.", "Analyse returns"],
            ["5.", "Exit and save"],
        ]

        print(tabulate(displayscreen, headers="firstrow", tablefmt="grid"))
        second_choice = input(Fore.BLUE + "👉 Enter your choice (1/2/3/4/5): ")

        if second_choice == "1":
            if not portfolio:
                print_color(Fore.RED , "Your portfolio is empty!")

            else:
                print_color(Fore.CYAN , "YOUR PORTFOLIO")
                for i,stock in enumerate(sorted(portfolio)):
                    print(Fore.YELLOW + str(i+1), Fore.MAGENTA + str(stock))

        elif second_choice == "2":
            stock = input(f"Please {Fore.GREEN}ADD{Fore.BLUE} a stock with its portfolio percentage {Fore.GREEN}(e.g. AAPL:10%): ").upper()
            if correct_format := re.search(r"^([A-Z]+\.[A-Z]+|[A-Z]{1,4}):([0-9]{1,3})%$",stock):
                pieces = correct_format.groups()
                stock_symbol = pieces[0]
                percent = pieces[1]

                if stock in portfolio:
                    print_color(Fore.RED ,"Stock already exists")

                elif check_stock_exists(stock_symbol):
                    portfolio.append(stock)

                    print_color(Fore.GREEN , f"{get_name(stock_symbol)} is now {percent}% of your portfolio")

                else:
                    print_color(Fore.RED, "Stock is not in yahoo finance")

            else:
                print_color(Fore.RED,"Invalid format")

        elif second_choice == "3":
            stock = input(f"{Fore.GREEN}REMOVE{Fore.BLUE} a stock and its portfolio percentage {Fore.GREEN}(e.g. AAPL:10%): ").upper()
            if portfolio:
                if correct_format := re.search(r"^([A-Z]+\.[A-Z]+|[A-Z]{1,4}):([0-9]{1,3})%$",stock):
                    pieces = correct_format.groups()
                    stock_symbol = pieces[0]
                    if stock in portfolio:
                        portfolio.remove(stock)
                        print_color(Fore.RED, f"{get_name(stock_symbol)} has been removed")
                    else:
                        print_color(Fore.RED,"Stock and percentage not in portfolio")

                else:
                    print_color(Fore.RED,"Invalid format")
            else:
                print_color(Fore.RED,"PORTFOLIO IS EMPTY")

        elif second_choice == "4":
            if portfolio:
                allocation = []
                ticker_list = []
                for stocks in portfolio:
                    ticker, percentage = stocks.split(":")
                    percentage = float(percentage.rstrip("%"))
                    allocation.append(percentage/100)
                    ticker_list.append(ticker)

                if sum(allocation) == 1:
                    print_color(Fore.YELLOW,"Timeframe of investment")
                    start_date = check_date(f"Enter {Fore.CYAN}START{Fore.RESET} date (YYYY-MM-DD): ")
                    end_date = check_date(f"Enter {Fore.CYAN}END{Fore.RESET} date (YYYY-MM-DD): ")
                    if end_date > start_date:
                        # Calculate the total investment amount
                        stock_returns = []
                        for stock in ticker_list:
                            stock_data = get_stock_data(stock, start_date, end_date)
                            stock_return = calculate_returns(stock_data)
                            stock_returns.append(stock_return)

                        # Calculate portfolio return
                        portfolio_return = sum(stock_return * alloc for stock_return, alloc in zip(stock_returns, allocation))


                        sp500_data = yf.download("^GSPC", start=start_date, end=end_date)
                        sp500_returns = calculate_returns(sp500_data['Close'])

                        # Print portfolio and S&P 500 returns
                        print(Fore.CYAN + f"Portfolio Returns: {portfolio_return:.2%}")
                        print(Fore.CYAN + f"S&P 500 Returns: {sp500_returns:.2%}")
                        if portfolio_return > sp500_returns:
                            print_color(Fore.GREEN,"CONGRATS! Your portfolio has beaten the S&P500")
                        elif portfolio_return < sp500_returns:
                            print_color(Fore.RED,"Unfortunately your portfolio lost :(")
                    else:
                        print_color(Fore.RED,"INVALID TIMEFRAME")

                else:
                    print_color(Fore.RED,"Percentages do not add up to 100%")


            else:
                print_color(Fore.RED,"Empty portfolio")

        elif second_choice == "5":
            print_color(Fore.GREEN,"Exiting the Stock Portfolio Tracker. \nBack to Login Interface.")
            save_portfolio_to_csv(username,portfolio)
            print_color(Fore.YELLOW,"Goodbye! See you soon :)")
            break

        else:
            print_color(Fore.RED,"Invalid choice! Please select a valid option (1/2/3/4/5)")

def check_date(prompt):
    while True:
        try:
            date_input = input(prompt)
            stock_date = date.fromisoformat(date_input)
        except ValueError:
            print_color(Fore.RED,"INVALID DATE")
        else:
            return date_input

def get_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock['Adj Close']

def get_portfolio_value(ticker_list, allocation):
    portfolio_value = 0
    for stock, allocation in zip(ticker_list, allocation):
        portfolio_value += stock * allocation
    return portfolio_value

def calculate_returns(stock_data):
    return (stock_data[-1] / stock_data[0]) - 1


def check_stock_exists(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        # Fetch summary information for the stock
        name = stock.info["longName"]
        return True
    except KeyError:
        return False

def get_name(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        return(stock.info["longName"])
    except Exception:
        raise ValueError

def load_portfolio(username):
    with open("portfolios.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == username:
                return row[1].split(",") if row[1] else []
    return []

def save_portfolio_to_csv(username,portfolio):
    data=[]
    with open("portfolios.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Update or add the user's portfolio to portfolio.csv
    user_found = False
    for row in data:
        if row and row[0] == username:
            if len(row) > 1:
                row[1] = ",".join(portfolio) # Update the portfolio
            else:
                row.append(",".join(portfolio)) # If row[1] is empty, create a new portfolio
            user_found = True # Update user founded

    # If the user's data is not found, create a new entry
    if not user_found:
        new_entry = [username, ",".join(portfolio)]
        data.append(new_entry)

    # Write the updated data back to portfolio.csv
    with open("portfolios.csv", "w", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def get_portfolio_value(investment, allocation):
    portfolio_value = 0
    for invest_amount, allocation in zip(investment, allocation):
        portfolio_value += invest_amount * allocation
    return portfolio_value

def print_color(color_code, text):
    print()
    print("======================================")
    print(color_code + text)
    print("======================================")
    print()

if __name__ == "__main__":
    main()

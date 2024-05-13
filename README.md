# YOUR PROJECT TITLE : Portfolio Backtester
# Video Demo: https://youtu.be/xJfW-0ZWejg
# Description:
My main goal of learning python is to integrate it with finance for better past, present and future analysis. Thus, this project is for users to customise and analyse their own portfolio of stocks which are in the s&p 500. They will give each stock they choose a specific percentage weightage in their portfolio. The user then can choose the timeframe that they will hold this portfolio. The project will then show and compare the average yearly return of their portfolio against the average yearly return of the s&p500.

Firstly, Users will be brought to a main page to either login/signin/exit.
This is functional as their login/signin data will be stored in a csv file so that they do not need to rebuild their portfolio/user info from scratch in future logins

Secondly, Users will be brought to a second page with 5 options. View portfolio, ADD/REMOVE stocks, Evaluate portfolio or Exit.

When viewing their portfolio, i have used the for loop, enumerate and sorted to display their numbered portfolio clearly in alphabetical order.

If user is adding a stock, I use regex to ensure user is inputting in the correct format. I also verify the stock is in yahoo finance through my check_stock_exists function. Similarly, when a user is removing a stock I also use the same regex and use a for loop to check if the stock they want to remove is in their portfolio.

When users want to evaluate their portfolio, I ask them for the starta and end date in a YYYY-MM-DD format and use datetime to verify their input. I will forst make sure that the percentages of each stock they have add up to 100%. Then ill use the dates to find the adjusted close price of these stocks on these dates and find their percentage returns by dividing start date adjusted close price by end date adjusted close price and minus one to get a deicimal return. I will then multiply their percentage returns with their percentange allocation in order to get the total portfolio return. I then find the returns of SPY using the same methods. I compare the portfolios returns againsts the SPY and feedback to the users the outcomes.

Lastly, if a user exits, i store their information in a temporary data file then check if they have an existing data in their portfolio, if they do i will join them together. Otherwise, i append the portfolio list with their stocks and save them.

Some aesthetics i have added are colors and tabulating tables. I have done these as i found it quite hard to find information without it being color coded.

This portfolio backtester is useful as it allows for users to assign each stock its percentage which is something i am unable to find online. In the future, futher refinements i would hope to make are accounting for dividends, etc in order to improve its accuracy.

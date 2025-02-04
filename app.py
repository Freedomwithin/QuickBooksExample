from flask import Flask, render_template
from src.quickbooks_api import get_quickbooks_data
from src.data_processing import format_customer_data, calculate_total_balance

app = Flask(__name__)

@app.route('/')
def index():
    customer_data = get_quickbooks_data("select * from Customer")

    if customer_data:
        formatted_data = format_customer_data(customer_data)
        total_balance = calculate_total_balance(customer_data)
        return render_template('index.html', customers=formatted_data, total_balance=total_balance)
    else:
        return "Error retrieving customer data (mock)."  # Simpler error message for the web

if __name__ == '__main__':
    app.run(debug=True)  # debug=True for automatic reloading during development

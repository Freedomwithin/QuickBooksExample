def format_customer_data(customer_data):
    """Formats customer data for display or further use."""
    formatted_customers = []
    for customer in customer_data['QueryResponse']['Customer']:
        formatted_customer = {
            "Name": customer['DisplayName'],
            "ID": customer['Id'],
            "Balance": customer['Balance']
        }
        formatted_customers.append(formatted_customer)
    return formatted_customers


def calculate_total_balance(customer_data):
    """Calculates the total balance of all customers."""

    total_balance = 0
    for customer in customer_data['QueryResponse']['Customer']:
        balance = float(customer['Balance'])  # Assuming 'Balance' is a string
        total_balance += balance
    return total_balance

# Example usage:
# formatted_data = format_customer_data(customer_data)
# total = calculate_total_balance(customer_data)
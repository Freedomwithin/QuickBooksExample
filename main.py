from src.quickbooks_api import get_quickbooks_data
from src.data_processing import format_customer_data, calculate_total_balance
from src.utils import setup_logging

def main():
    logger = setup_logging()
    customer_data = get_quickbooks_data("select * from Customer")  # Query doesn't matter in mock mode

    if customer_data:
        formatted_data = format_customer_data(customer_data)
        total_balance = calculate_total_balance(customer_data)

        print("Formatted Customer Data:")
        for customer in formatted_data:
            print(customer)
        print(f"\nTotal Customer Balance: {total_balance}")
        logger.info("Customer data retrieved and processed successfully (mock).")
    else:
        logger.error("Failed to retrieve customer data (mock).")

if __name__ == "__main__":
    main()
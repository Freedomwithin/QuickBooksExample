import logging

def setup_logging(log_file="quickbooks_app.log"):
    """Sets up logging for the application."""
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)  # Return a logger instance

# Example usage:
# logger = setup_logging()
# logger.info("Application started.")

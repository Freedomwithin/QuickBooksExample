# QuickBooks Customer Data Visualization (Mock Data)

This project demonstrates how to build a web application to display and visualize QuickBooks customer data. It uses Python with the Flask framework to create a user-friendly interface.  Currently, the project utilizes mock data stored in JSON format, allowing for development and testing without requiring a live connection to the QuickBooks Online API. The architecture is designed to facilitate seamless integration with the actual QuickBooks API when ready. Key features include a sortable table for displaying customer information and a bar chart to visually represent customer balances.
This project implements a Python web application using the Flask framework to display and visualize QuickBooks customer data. The application follows a modular design, separating API interaction logic, data processing, and presentation. Currently, mock data is used for testing and demonstration. The project utilizes Chart.js for creating charts and Bootstrap for styling. The next phase will involve integrating with the QuickBooks Online API using OAuth 2.0 for authentication and the QuickBooks Query API for data retrieval.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Mock Data](#mock-data)
- [Future API Integration](#future-api-integration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a client-friendly demonstration of a web application designed to visualize QuickBooks customer data.  It showcases the user interface and data presentation capabilities.  While this version uses mock data, the final application will integrate with the QuickBooks Online API to display real-time data.  The interface includes a table for detailed customer information and a chart for balance visualization.

## Features

*   **Customer Data Table:** Displays customer names, IDs, and balances in a sortable and well-formatted table.
*   **Balance Chart:**  Presents customer balances visually using a bar chart for easy understanding.
*   **Responsive Design:**  The web application is designed to be responsive, adapting to different screen sizes.
*   **Mock Data Driven:** Uses mock data for development and demonstration purposes, eliminating the need for live API connections during initial development.
*   **Modular Design:**  The project follows a modular structure, separating API interaction, data processing, and presentation logic for maintainability and scalability.

## Getting Started

### Prerequisites

Before running the application, ensure that you have the following installed:

*   Python 3.6+
*   pip (Python package manager)

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/your-username/QuickBooksExample.git](https://github.com/your-username/QuickBooksExample.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd QuickBooksExample
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv.venv
    ```

4.  Activate the virtual environment:

    ```bash
    source.venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
    ```

5.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Ensure your virtual environment is activated.
2.  Run the Flask app:

    ```bash
    python app.py
    ```

3.  Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Project Structure

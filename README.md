# Website Data Engineering Project

## Overview

This project is a **Data Engineering** application that allows users to submit their details through a web interface. It involves the following key components:

- **Flask web application** to create and serve an interactive website.
- **AWS Lambda** function to push data to an S3 bucket when a user submits their details.
- **AWS Glue** to clean and transform the data in S3 (removing null values and duplicate emails) and store the cleaned data in a separate S3 folder.
- **AWS DynamoDB** to store contact details for later processing.

This is a full-stack project demonstrating how different AWS services work together in a data engineering pipeline.

## Features

- **Flask Web Application**: A user-friendly web interface to capture user details.
- **AWS Lambda Function**: Automatically triggered when user data is submitted, stores data in S3.
- **AWS Glue Job**: Cleans and processes the data by removing null values and duplicate emails.
- **Data Storage**: Raw and processed data are stored in separate S3 folders.
- **DynamoDB**: Stores user contact information for further processing.

## Architecture

- **Frontend**: HTML, CSS (for the user interface).
- **Backend**: Flask for routing and handling user input.
- **AWS Services**:
  - **Lambda**: To trigger the data storage in S3.
  - **S3**: For raw and processed data storage.
  - **Glue**: For data transformation and cleaning.
  - **DynamoDB**: To store user contact information.
  - **SNS**: Sends notifications in case of failures.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- AWS account with the following services:
  - Lambda
  - S3
  - Glue
  - DynamoDB
  - SNS

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/Website_data_Engineering.git
   cd Website_data_Engineering

2.**Install the Dependencies:**

Create a virtual environment and install required libraries:
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
pip install -r requirements.txt

3.**Run the Flask Application:**

To start the Flask web application locally:
python app.py

The web application will be accessible at http://127.0.0.1:5000/.

4. **AWS Setup:**

Set up Lambda function and Glue job in your AWS account.

Create an S3 bucket to store raw and cleaned data.

Set up DynamoDB to store user contact information.

Create an SNS topic for failure notifications.

5. **Test the Application:**

Open the website in your browser and fill in the contact form.

After submitting, check your S3 bucket to confirm that the raw data is stored.

Verify that the Lambda function is working properly by testing it with the S3 data.

Check the AWS Glue logs to ensure the data is processed correctly and stored in the clean data folder.

**Project Structure**
Website_data_Engineering/
│
├── app.py              # Flask application
├── templates/          # Contains HTML files (index.html, contact.html)
├── static/             # Contains CSS, images
│   ├── style.css
│   └── images/
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file to exclude unnecessary files


**Troubleshooting**
Lambda Function Permissions: Ensure that the Lambda execution role has the necessary permissions to access S3 and DynamoDB.

Glue Job: Make sure your Glue job has the correct script and access to the S3 buckets.

CORS Issues: If you’re hosting the web app publicly, ensure that CORS settings in your S3 bucket are properly configured.

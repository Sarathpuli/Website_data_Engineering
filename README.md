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

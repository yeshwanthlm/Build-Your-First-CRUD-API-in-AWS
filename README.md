# Step-by-Step Guide to Build Your First CURD API in AWS

### Project Description:

Your goal in this workshop is to build a very simple CRUD (Create, read, update, delete) API. To accomplish this you will be guided through a few steps. Starting with creating a DynamoDB table using the DynamoDB console, to creating a Lambda function in the AWS Lambda console. Next you will configure an HTTP API using the API Gateway console and last, after launching an AWS Cloud9 IDE you will use it to test your API!

If you have little experience with AWS but know your way around at typing commands in a terminal, this workshop is for you! (Copy/Paste allowed!) 

When you invoke your HTTP API, API Gateway routes the request to your Lambda function. The Lambda function interacts with DynamoDB, and returns a response to the API Gateway. The API Gateway then returns a response to you.

### Project Architecture:

![image](https://github.com/user-attachments/assets/500b1e1f-1f41-4ea8-a401-ba778fbe6204)


### Steps to Build the Project:

## Prerequisites

1. AWS Account with appropriate permissions to create Lambda functions, API Gateway, and S3 buckets.
2. Passion to Learn!

## Steps to Deploy

* Step 1: Create a DynamoDB table: \
  For Table name, enter: http-crud-tutorial-items \
  For Primary key, enter id

* Step 2: Create a lambda function: \
  Name: http-crud-tutorial-function \
  Runtime: Python 3.x \
  Execution role: IAM role with DynamoDB and API permissions \
  Code: Use the UploadFunction Python code.

* Step 3: Create the Lambda function to handle file downloads (DownloadFunction): \
  Name: DownloadFunction \
  Runtime: Python 3.x \
  Execution role: IAM role with S3 write permissions \
  Code: Use the CURD.py Python code.

* Step 4: Create an HTTP API \
  Name: http-crud-tutorial-api

* Step 5: Create routes: \
  
  ```bash
  GET /items/{id}

  GET /items

  PUT /items

  DELETE /items/{id}
  ```
  
* Step 6: Create an integration: \

  Choose your API (http-crud-tutorial-api) \
  Choose Integrations \
  Choose Manage integrations and then choose Create  Skip Attach this integration to a route. You complete that in a later step. \
  For Integration type, choose Lambda function \
  For Lambda function, enter http-crud-tutorial-function \

  ```bash
  {
    "body" : "$input.body",
    "queryStringParameters" : {
        "fileName" : "$input.params('fileName')"
    }
  }
  ```
* Step 7: Attach your integration to routes: \
  Choose your API (http-crud-tutorial-api) \
  Choose Integrations \
  Choose a route \
  Under Choose an existing integration, choose http-crud-tutorial-function \
  Choose Attach integration \
  Repeat steps 4-6 for all routes. All routes show that an AWS Lambda integration is attached. \
  Note your API's invoke URL. It appears under Invoke URL on the Details page.

* Step 8: Create Cloud9 Environment

* Step 9: Testing: 
  
  1) Export API Invoke URL: \

  ```bash
  export INVOKE_URL="https://**abcdef123**.execute-api.eu-west-1.amazonaws.com"
  ```
  2) Create or update an item. The command includes a request body with the item's ID, price, and name. \

  ```bash
  curl -X "PUT" -H "Content-Type: application/json" -d "{
    \"id\": \"abcdef234\",
    \"price\": 12345,
    \"name\": \"myitem\"
  }" $INVOKE_URL/items
  ```

  3) Use the following command to list all items.

  ```bash
  curl -s $INVOKE_URL/items | js-beautify 
  ```
  
  4) Use the following command to get an item by its ID.

  ```bash
  curl -s $INVOKE_URL/items/abcdef234 | js-beautify
  ```

  5) Use the following command to delete an item.
  ```bash
  curl -X "DELETE" $INVOKE_URL/items/abcdef234
  ```
  
  6) Use the following command to list all items.

  ```bash
  curl -s $INVOKE_URL/items | js-beautify 
  ```


Link to the video tutorial: 

Follow our tutorials here: https://www.youtube.com/@amonkincloud/videos \
Follow my personal blog here:https://dev.to/yeshwanthlm/ \
Follow us on Instagram: https://www.instagram.com/amonkincloud/ \
For queries write to us at: amonkincloud@gmail.com 


from flask import Flask, render_template, request, redirect, url_for
import uuid
import boto3

app = Flask(__name__)

#route to display home page
@app.route("/")

def home():
    return render_template('index.html')

#route to display contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission and store data in DynamoDB
@app.route('/contact/submit', methods=['POST'])
def contact_submit():
    # Fetch form data
    data = {
        'contact_id': str(uuid.uuid4()),  # Unique ID for each submission
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'country': request.form['country'],
        'budget': request.form['budget'],
        'start_date': request.form['start_date'],
        'end_date': request.form['end_date'],
        'description': request.form['description']
    }

    #Create DynamoDB resource
    dynamodb = boto3.resource('dynamodb')

    # Save into DynamoDB table 'SarathContactRequests'
    contact_table = dynamodb.Table('SarathContactRequests')
    contact_table.put_item(Item=data)

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug =True)

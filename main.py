from flask import Flask, render_template
app = Flask(__name__)
import dynamodb_handler
import boto3
from decouple import config

AWS_ACCESS_KEY_ID     = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = config("REGION_NAME")

client = boto3.client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)
resource = boto3.resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)
 #aws stuff
table = resource.Table('employeecrud')
@app.route('/')
def hello_world(table=table):
   response = table.scan()
   data = response['Items']
   return render_template('index.html')
   print(data)

if __name__ == '__main__':
   app.run(debug=True)

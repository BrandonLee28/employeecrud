from flask import Flask, render_template
app = Flask(__name__)
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
response = table.scan()
data = response['Items']
@app.route('/')
def hello_world(data=data):
   return render_template('index.html', data=data)

if __name__ == '__main__':
   app.jinja_env.auto_reload = True
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run(debug=True, port=3000)

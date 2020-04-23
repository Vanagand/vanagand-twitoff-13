# web_app/services/basilica_service.py
# C:\Users\Michel\Desktop\lambda_ds13\vanagand-twitoff-13\web_app\services\basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>
    return connection

if __name__ == "__main__":
    
    print("---------")
    connection = basilica_api_client()
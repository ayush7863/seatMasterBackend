import mongoengine
from dotenv import load_dotenv
import os

load_dotenv('.env')

mongo=os.getenv('MONGO_URL')

# Establish a connection to MongoDB
mongoengine.connect('seatMaster', host=mongo)

# Access the desired database
db = mongoengine.connection.get_db()

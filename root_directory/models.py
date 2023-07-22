import uuid
from mongoengine import Document, StringField, BooleanField, DateTimeField, ReferenceField, UUIDField   


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    user_status = BooleanField(default=True)
    gender = StringField(choices=('Male', 'Female', 'Other'))
    membership_type = StringField(choices=('Regular', 'Premium', 'VIP'))
    bio = StringField()
    date_of_birth = DateTimeField()
    # role = StringField(required=True, choices=('user', 'Admin'), default='user')  # Updated role field

    meta = {'collection': 'users'}


class Movie(Document):
    title = StringField(required=True)
    genre = StringField()
    uuid = UUIDField(binary=False, default=uuid.uuid4)
    image_url = StringField()


class Show(Document):
    time = StringField(required=True)
    location = StringField(required=True)
    movie = ReferenceField(Movie, reverse_delete_rule=2)

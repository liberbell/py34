import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

# Use a service account
cred = credentials.Certificate('firebase_secret.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# print(db)

users_ref = db.collection('users')
docs = users_ref.stream()

users = []
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


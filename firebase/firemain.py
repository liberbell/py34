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
indexes = []
for doc in docs:
    indexes.append(doc.id)
    users.append(doc.to_dict())
    print(f'{doc.id} => {doc.to_dict()}')

# print(users)
df = pd.DataFrame(data=users, index=indexes)
print(df)

# db.collection('users').add({
#     'first_name': 'Elton',
#     'last_name': 'Jhon',
#     'nickname': 'both',
#     'age': 72
# })

# city_ref = db.collection('users').document('elton')
# city_ref.update({
#     'age': 74,
#     'nickname': "pianist"
#     })

user_ref = db.collection('cities').document(u'BJ')
user_ref.update({
    'capital': firestore.DELETE_FIELD
})
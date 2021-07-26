import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
import json
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

with open("faceapi_secret.json") as f:
    face_api_key = json.load(f)
KEY = face_api_key["key"]
ENDPOINT = face_api_key["URL"]

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

single_face_image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
single_image_name = os.path.basename(single_face_image_url)
# detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')

image = Image.open("single.jpg")
single_image_name = os.path.basename(image)
detected_faces = face_client.face.detect_with_stream(image, detection_model='detection_03')

if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    
    return ((left, top), (right, bottom))

response = requests.get(single_face_image_url)
img = Image.open(BytesIO(response.content))
print('Drawing rectangle around face... see popup for results.')
draw = ImageDraw.Draw(img)
for face in detected_faces:
    draw.rectangle(getRectangle(face), outline='green')

img.show()

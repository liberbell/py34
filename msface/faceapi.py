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

with open("faceapi_end.json") as f:
    url = json.load(f)

ENDPOINT = url["URL"]
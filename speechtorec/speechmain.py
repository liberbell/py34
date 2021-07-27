import os
import io
from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "speech_secret.json"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
with io.open("english.wav", "rb") as f:
    wav_data = f.read()

audio = speech.RecognitionAudio(content=wav_data)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)
print(response)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
import os
import io
from google.cloud import speech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "speech_secret.json"
wav_file = "english.wav"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
with io.open(wav_file, "rb") as f:
    wav_data = f.read()

sourceAudio = AudioSegment.from_file(wav_file)
rates = sourceAudio.frame_rate


audio = speech.RecognitionAudio(content=wav_data)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=rates,
    language_code="ja-JP",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)
print(response)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
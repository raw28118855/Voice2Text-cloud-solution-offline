import time
import os
import json
import wave
import io
from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
def transcribe_streaming(stream_file):
    f = open('google_streaming.txt', 'w+')
    index=1
    credentials = service_account.Credentials.from_service_account_file('D:\Tool\google speech2text\My First Project-91cee1041c4b.json')
    client = speech.SpeechClient(credentials=credentials)
    with io.open(stream_file,'rb') as audio_file:
        content=audio_file.read()
        stream=[content]
        requests=(types.StreamingRecognizeRequest(audio_content=chunk)
                  for chunk in stream)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US')
        streaming_config=types.StreamingRecognitionConfig(config=config)
        responses=client.streaming_recognize(streaming_config,requests)
        for response in responses:
            for result in response.results:
                print('Finished: {}'.format(result.is_final))
                print('Stability: {}'.format(result.stability))
                alternatives = result.alternatives
                # The alternatives are ordered from most likely to least.
                for alternative in alternatives:
                    print('Confidence: {}'.format(alternative.confidence))
                    print(u'Transcript: {}'.format(alternative.transcript))
                    f.write(str(index) + " " +alternative.transcript+"\n")
                    index=index+1
        f.close()
def main():

    os.chdir("D:\Report\Voice2text\Python\google_multi_wav_en")
    audioname="test.wav"
    transcribe_streaming(audioname)

#if __name__=='__main__':
main()
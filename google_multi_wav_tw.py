import time
import os
import json
import wave
from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
def main():
    credentials = service_account.Credentials.from_service_account_file('D:\Tool\google speech2text\My First Project-91cee1041c4b.json')
    os.chdir("D:\Report\Voice2text\Python\google_multi_wav_en")
    f=open('google.txt','w+')
    audioPath="D:\Report\Voice2text\Python\google_multi_wav_en"    #     ./sample.wav
    files = os.listdir(audioPath)
    client = speech.SpeechClient(credentials=credentials)

    for wav in files:
        if ".wav" in wav:
            wavPath=audioPath+"\\"+wav
            test_wav = wave.open(wavPath, "rb")
            params = test_wav.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            content = test_wav.readframes(nframes)
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,sample_rate_hertz=16000,language_code='zh-TW')
            '''starting sending file for vioce recognition'''
            print("\n-------Testing Speech API-------\n")
            print("\nsending audio file......\n")
            response = client.recognize(config, audio)
            for result in response.results:
                #print('Transcript: {}'.format(result.alternatives[0].transcript))
                print(result.alternatives[0].transcript)
                f.write(wav + " " +result.alternatives[0].transcript+"\n")
    f.close()
#if __name__=='__main__':
main()




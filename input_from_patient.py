#step1 : Set up Audio recorder(ffmpeg & portaudio) portaudio=>used for micrphone 
import logging
import speech_recognition as sr

from io import BytesIO
from pydub import AudioSegment
#ffmpeg is used convert the wav file to mp3 file
# Point pydub to ffmpeg in our project
AudioSegment.converter = r"C:\Users\home\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
from pydub.utils import which
AudioSegment.converter = r"C:\Users\home\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffmpeg = which(AudioSegment.converter)

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path,timeout=20,phrase_time_limit=None):
    """Simplified function to record audio from the microphone and save it in mp3 format

    Args:
        file_path (str): Path to save the recorded audio file
        timeout (int, optional): Maximum time to wait for a phrase to start (in seconds).
        phrase_time_limit (int, optional): Maximum time for the phrase to be recorded(in seconds).
    """
    recogniser=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise")
            recogniser.adjust_for_ambient_noise(source,duration=1)
            logging.info("Start Speaking Now")
            
            #Record the audio
            audio_data=recogniser.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("Recording Compelte")
            
            #convert audio to mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment=AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path,format="mp3",bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
        
    except Exception as e:
        logging.error(f"error occured:{e}")
file_path="voice_test.mp3"
#record_audio(file_path="voice_test.mp3")


#step2: Setup speech to text-STT-model for transcription
import os
from groq import Groq
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
# transcription_model="whisper-large-v3"

def speech_2_text(transcription_model,file_path):
    client=Groq(api_key=GROQ_API_KEY)
    audio_file=open(file_path,'rb')
    transcription=client.audio.transcriptions.create(
        model=transcription_model,
        file=audio_file,
        language="en"
    )
    return transcription.text

    
    
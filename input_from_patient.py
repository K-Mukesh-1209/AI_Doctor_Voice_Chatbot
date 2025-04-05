#step1 : Set up Audio recorder(ffmpeg & portaudio) portaudio=>used for micrphone 
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path,time_out=20,phrase_time_limit=None):
    recogniser=sr.Recogniser()
    try:
        with sr.Microphone() as source:
            logging.info
    
    
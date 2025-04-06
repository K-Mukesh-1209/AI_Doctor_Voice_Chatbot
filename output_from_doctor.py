#step1: Set up Text to speech - TTS model (gTTS & ElevenLabs)
import os
from gtts import gTTS
import platform
import subprocess
from dotenv import load_dotenv
from pydub import AudioSegment
load_dotenv()
def text_to_speech_gtts_old(text,output_filepath):
    language="en"
    audioobj=gTTS(
        text=text,
        lang=language,
        slow=False
        )
    audioobj.save(output_filepath)
    
input_text="Hii , I am Mukesh!"
#text_to_speech_gtts(input_text,output_filepath="t2s.mp3")

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
        

ELEVEN_LABS_API_KEY=os.environ.get("ELEVEN_LABS_API_KEY")
## with ElevenLabs

import elevenlabs
from elevenlabs.client import ElevenLabs
output_filepath="elven_t2s.mp3"
output_wavpath = "elven_t2s.wav"
def text_to_speech_elevenlabs(text,output_filepath):
    client=ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio=client.generate(
        text=text,
        voice= "Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(output_wavpath, format="wav")
    os_name = platform.system()
    
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_wavpath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
    
text_to_speech_elevenlabs(input_text,output_filepath)

#step2: use model for text output to speech
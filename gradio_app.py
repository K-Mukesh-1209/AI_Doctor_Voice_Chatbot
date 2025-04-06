from brain import encode_image,analyze_with_query
from input_from_patient import speech_2_text,record_audio
from output_from_doctor import text_to_speech_elevenlabs,text_to_speech_with_gtts
import gradio as gr

system_prompts="""
            You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath,image_filepath):
    speech_to_text_output=speech_2_text(transcription_model="whisper-large-v3",file_path=audio_filepath)
    
    if image_filepath:
        doctor_response=analyze_with_query(query=system_prompts+speech_to_text_output,encoded_image=encode_image(image_path=image_filepath),model="llama-3.2-90b-vision-preview")
    else:
        doctor_response="Please provide an image for giving good response"
    doctors_suggestion=text_to_speech_elevenlabs(text=doctor_response,output_filepath="final.mp3")
    return speech_2_text,doctor_response,doctors_suggestion

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"],type="filepath"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="speech to Text"),
        gr.Textbox(label="Doctor's Respose"),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor With vision and Voice"
)

iface.launch(debug=True)

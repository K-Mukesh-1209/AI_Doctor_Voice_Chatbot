#step1: Setup GRoq Api key
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#step2: Convert image to required format
import base64

def encode_image(image_path): 
    image_file=open(image_path,'rb')
    return base64.b64encode(image_file.read()).decode('utf-8')

#step3: Set up Multi llm
# model="llama-3.2-90b-vision-preview"
# query="What does it sense?"

from groq import Groq
def analyze_with_query(query,encoded_image,model):
    client=Groq()
    messages=[
        {   
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    },
                },
            ],
        }
    ]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content
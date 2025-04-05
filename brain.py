#step1: Setup GRoq Api key
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#step2: Convert image to required format
import base64

image_path="./image.jpg"
image_file=open(image_path,'rb')
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')

#step3: Set up Multi llm
from groq import Groq

client=Groq()
query="What does it sense?"
model="llama-3.2-90b-vision-preview"
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
print(chat_completion.choices[0].message.content)
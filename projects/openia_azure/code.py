
import os
from openai import AzureOpenAI
    
from dotenv import load_dotenv

import json 

load_dotenv()

def generate_minuta_text(prompt_content):

    client = AzureOpenAI(
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
        api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )
    
    deployment_name=os.getenv('DEPLOYED_MODEL_NAME') 
    prompt_content_to_json = json.dumps(prompt_content)
    userPrompt = f"Genera una minuta con un formato para un archivo markdown: {prompt_content_to_json}, y no generes al principio esto ```markdown"
    completion  = client.chat.completions.create(
    messages=[        
        {"role": "user", "content": userPrompt},
    ],
    model=deployment_name,
    )

    

    print(f'content -> {completion.choices[0].message.content}')

    content = completion.choices[0].message.content
    print(type(content))
    return content

    

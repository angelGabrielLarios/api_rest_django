
import os
from openai import AzureOpenAI
    
from dotenv import load_dotenv


load_dotenv()

def generate_minuta(prompt_content):

    client = AzureOpenAI(
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
        api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )
    
    deployment_name=os.getenv('DEPLOYED_MODEL_NAME') 
    
    userPrompt = f"Genera una minuta de la siguiente información: {prompt_content}"
    completion  = client.chat.completions.create(
    messages=[        
        {"role": "user", "content": userPrompt},
    ],
    model=deployment_name,
    )

    

    print(f'content -> {completion.choices[0].message.content}')

    

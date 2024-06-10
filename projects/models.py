
from pprint import pprint
from .videoindexer.Consts import Consts
from .videoindexer.VideoIndexerClient import VideoIndexerClient
from dotenv import load_dotenv


import os
load_dotenv()
def ModelVideoIndexer():
    AccountName = os.getenv('AccountName')
    ResourceGroup = os.getenv('ResourceGroup')
    SubscriptionId = os.getenv('SubscriptionId')

    ApiVersion = os.getenv('ApiVersion')
    ApiEndpoint = os.getenv('ApiEndpoint')
    AzureResourceManager = os.getenv('AzureResourceManager')

    # create and validate consts
    consts = Consts(ApiVersion, ApiEndpoint, AzureResourceManager, AccountName, ResourceGroup, SubscriptionId)# Authenticate

    # create Video Indexer Client
    client = VideoIndexerClient()

    # Get access tokens (arm and Video Indexer account)
    client.authenticate_async(consts)

    client.get_account_async()

    video_id = os.getenv('video_id')

    prompt_content = client.get_prompt_content(video_id)

    
    return prompt_content




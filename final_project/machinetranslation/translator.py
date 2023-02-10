import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    temp = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    #print(json.dumps(temp))
    frenchText= json.dumps(temp)
    print(frenchText)
    t = json.loads(frenchText)['translations'][0]['translation']
    print(t)
    return t

def frenchToEnglish(frenchText):
    temp = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText= json.dumps(temp)
    print(frenchText)
    t = json.loads(englishText)['translations'][0]['translation']
    print(t)
    return t
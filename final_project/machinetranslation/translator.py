"""import"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def english_to_french(english_text):
    """"Ciao"""
    temp = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print(json.dumps(temp))
    french_text= json.dumps(temp)
    print(french_text)
    t = json.loads(french_text)['translations'][0]['translation']
    print(t)
    return t

def french_to_english(french_text):
    """ciao"""
    temp = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text= json.dumps(temp)
    print(french_text)
    t = json.loads(english_text)['translations'][0]['translation']
    print(t)
    return t

'''modules to translate en to fr and fr to en'''
import os
import sys
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
VERSION="2018-05-01"
authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

'''translate english to french'''
def english_to_french(english_text):
    '''pass the params'''
    french_text=language_translator.translate(
    text=english_text,
    source='en',
    target='fr'
    ).get_result()
    return french_text["translations"][0]["translation"]

'''translate french to english'''
def french_to_english(french_text):
    '''pass the params'''
    english_text=language_translator.translate(
    text=french_text,
    source='fr',
    target='en'
    ).get_result()
    return english_text["translations"][0]["translation"]

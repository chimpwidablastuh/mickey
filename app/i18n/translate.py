import os
import json

def load_translations(locale):
    localedir = './app/i18n/locales'
    filepath = os.path.join(localedir, f'{locale}.json')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def i18n(text):
    locale = os.getenv('LANG', 'en_US').split('.')[0]
    translations = load_translations(locale)
    return translations.get(text, text)
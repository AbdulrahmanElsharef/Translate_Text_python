# import Translator class from googletrans
from googletrans import Translator
# import input and out put from pywebio library
from pywebio.input import *
from pywebio.output import *


def translate_text():
    while True:
        translator = Translator()  # create translator object from Translator class
        #
        translation_text = input_group("welcome to translate program".title(), [
            textarea('please enter your text for translate'.title(),
                     rows=5, name='text'),
            select('choice translate language'.title(), {'English': "en", 'French': "fr", 'German': "de", 'Italian': "it", 'Japanese': "ja", 'Arabic': 'ar', 'Hindi': "hi"}, name='language')])
        # function for translate from user input to select language
        translation = translator.translate(
            text=translation_text['text'], dest=translation_text['language'])

        # output translation for user
        put_table([
            ['your text'.title(), 'translation'.title()],
            [translation_text['text'], translation.text],
        ]).style('color: yellow; font-size: 25px')


translate_text()

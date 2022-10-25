from googletrans import Translator
from translate import Translator


# init translator
translator = Translator(to_lang="ja")

try:
    with open('C:\\Users\\bala_\\Desktop\\Fast\\teste.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Check file path.')

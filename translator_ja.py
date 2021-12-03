#offline translator from english to japanese
#translate the txt file saved on the desktop
#save traslated file in a new file on the desktop
#remider ~ pip translate need to be installed
#reminder ~ PWD in terminal have to be cd desktop
from translate import Translator
translator = Translator(to_lang="ja")
#file testP.txt created and saved on the desktop
#add some text to the testP.txt file and save it
try:
  with open('./testP.txt', mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    #new file test-ja.txt created and saved on the desktop
    #with open('./test-ja.txt', mode = 'w') as my_file2:
    #  my_file2.write(translation)
    print ( translation )
except FileNotFoundError as e:
    print('check your file path!')
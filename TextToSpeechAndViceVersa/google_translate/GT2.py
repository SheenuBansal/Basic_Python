# Translating More than a phrase

from googletrans import Translator
translator = Translator()

sentences = ["Hello Beautiful", "How are you doing?",
             "How's the weather", "God bless you"]

translations= translator.translate(sentences,dest="hi")
for i in translations :
    print(f'{i.origin}({i.src}) --> {i.text}({i.dest})')
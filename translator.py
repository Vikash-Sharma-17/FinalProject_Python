from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source="english", target="french").translate(englishText)
    return translator

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='french', target='english')
    translation = translator.translate(frenchText)
    return translation



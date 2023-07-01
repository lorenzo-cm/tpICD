from googletrans import Translator as GoogleTranslator
from time import sleep
from threading import Thread
import pandas as pd
from tqdm import tqdm

class Translator:

    def __init__(self) -> None:
        self.translator = GoogleTranslator()
    
    
    def translate(self, text: str):
        try:
            translated_text = self.translator.translate(text, dest='en').text
            return translated_text
        except:
            return ''


    def translate_list(self, texts: list):
        translated_texts = []
        for text in tqdm(texts):
            translated_text = self.translate(text)
            translated_texts.append(translated_text)
        return translated_texts


    def translate_list_parallel(self, texts: list):

        translated_texts = []

        def execute_translation(text: str):
            translated_text = self.translate(text)
            translated_texts.append(translated_text)

        threads = []

        for text in tqdm(texts):
            # A API CALL NÃO SUPORTA MUITAS CHAMADAS POR SEGUNDO
            sleep(0.01) # tentativa de suavizar o problema
            t = Thread(target=execute_translation, args=[text])
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return translated_texts


    def translate_df(self, df: pd.DataFrame, column_name: str):
        df[column_name] = self.translate_list(df[column_name].tolist())
        return df
    

    def translate_df_parallel(self, df: pd.DataFrame, column_name: str):
        df[column_name] = self.translate_list_parallel(df[column_name].tolist())
        return df
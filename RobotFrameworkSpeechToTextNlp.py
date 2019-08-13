import speech_recognition as sr

import spacy

__author__ = 'Mreddy'
import requests
__version__ = '1.0'
def get_version():
    return __version__
def test_run():
   print(get_version())


class RobotFrameworkSpeechToTextNlp(object):
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')



    def Voice_Conv(self,audioFile):
        r = sr.Recognizer()
        with sr.AudioFile(audioFile) as source:
            AudioContent = r.record(source)
        try:
            #s = r.recognize_google(AudioContent)
            s = r.recognize_sphinx(AudioContent)
            #print(s)
        except Exception as e:
            print("Exception : "+str(e))
        return s

    def Extract_Info_Noun_Chunks(self, audioFile):
        Resultval = []
        resp = self.Voice_Conv(audioFile)
        doc = self.nlp(resp)
        for token in doc.noun_chunks:
            Resultval.append(token)
        return Resultval

    def Parts_Of_Speech(self, audioFile):
        Resultval = []
        resp = self.Voice_Conv(audioFile)
        doc = self.nlp(resp)
        #p_stemmer = PorterStemmer()
        for words in doc:
            Resultval.append(words.pos_)
        return Resultval



    def Lemma(self, audioFile):
        Resultval = []
        resp = self.Voice_Conv(audioFile)
        doc = self.nlp(resp)


        for words in doc:
            Resultval.append(words.lemma_)
        return Resultval

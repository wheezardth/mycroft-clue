from os.path import join, abspath, dirname
import os.path
import random
from adapt.tools.text.tokenizer import EnglishTokenizer
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
from mycroft.util.parse import fuzzy_match
from mycroft.util.parse import match_one
from mycroft.audio import wait_while_speaking
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.context import *

class ClueEngine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        
        #Register list of search history entries that are held in a padatious entity
        #self.register_entity_file("title.entity")
        #self.process = None
        
        #Build search history list
        self.play_list = {
            'anonymitaet': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'anonymitaet.mp3'),    
            'daten': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'daten.mp3'),
            'koerperverletzung': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'koerperverletzung.mp3'),
            'kreuzstich': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'kreuzstich.mp3'),
            'lichter': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'lichter.mp3'),
            'linz': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'linz.mp3'),
            'mindestlohn': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'mindestlohn.mp3'),
            'osteoporose': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'osteoporose.mp3'),
            'palatschinken': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'palatschinken.mp3'),
            'putzplaylist': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'putzplaylist.mp3'),
            'sms': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'sms.mp3'),
            'wetter': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'wetter.mp3'),
            'whistleblowing': join(abspath(dirname(__file__)), 'soundfiles', 'history', 'whistleblowing.mp3')
        }

    #Search history
    @intent_file_handler('question.history.intent')
    def handle_question_history(self, message):
        self.speak_dialog('question.history')
        wait_while_speaking()
        story_file = list(self.play_list.values())
        story_file = random.choice(story_file)
        print(story_file)
        #if os.path.isfile(story_file):
        wait_while_speaking()
        self.process = play_mp3(story_file)

    #What have you heard
    @intent_file_handler('recent.heard.intent')
    def handle_overheard(self, message):
        self.speak_dialog('recent.heard')
        wait_while_speaking()
        # need to replace with actual story
        self.process = play_mp3(self.play_list('whistleblowing'))

    #What can you do
    @intent_file_handler('what.capabilities.intent')
    def handle_capabilities(self, message):
        self.speak_dialog('what.capabilities')
        wait_while_speaking()

    #Who are you
    @intent_file_handler('whoare.you.intent')
    def handle_whoisyou(self, message):
        self.speak_dialog('whoare.you')
        wait_while_speaking()

    #Who's Laura
    @intent_file_handler('whois.laura.intent')
    def handle_whois_laura(self, message):
        self.speak_dialog('whois.laura')
        wait_while_speaking()

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return ClueEngine()

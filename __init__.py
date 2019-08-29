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

class BedtimeStories(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        
        #Register list of search history entries that are held in a padatious entity
        #self.register_entity_file("title.entity")
        #self.process = None
        
        #Build search history list
        self.play_list = {
            'twas the night before christmas': join(abspath(dirname(__file__)), 'stories', 'twas_the_night_before_christmas.mp3'),    
            'little red riding hood': join(abspath(dirname(__file__)), 'stories', 'little_red_riding_hood.mp3'),
            'the three bears': join(abspath(dirname(__file__)), 'stories', 'the_three_bears.mp3'),
            'hansel and gretel': join(abspath(dirname(__file__)), 'stories', 'hansel_and_gretel.mp3'),
            'the velveteen rabbit': join(abspath(dirname(__file__)), 'stories', 'the_velveteen_rabbit.mp3'),
            'rumplestiltskin': join(abspath(dirname(__file__)), 'stories', 'rumplestiltskin.mp3'),
            'the emporers new clothes': join(abspath(dirname(__file__)), 'stories', 'the_emporers_new_clothes.mp3'),
            'the princess on the pea': join(abspath(dirname(__file__)), 'stories', 'the_princess_on_the_pea.mp3'),
            'the elves and the shoemaker': join(abspath(dirname(__file__)), 'stories', 'the_elves_and_the_shoemaker.mp3'),
            'the three billy goats gruff': join(abspath(dirname(__file__)), 'stories', 'the_three_billy_goats_gruff.mp3'),
            'peter rabbit': join(abspath(dirname(__file__)), 'stories', 'peter_rabbit.mp3'),
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
    def handle_pick_story(self, message):
        self.speak_dialog('recent.heard')
        wait_while_speaking()
        # not sure about story file here
        self.process = play_mp3(peter rabbit)

    #What can you do
    @intent_file_handler('what.capabilities.intent')
    def handle_pick_story(self, message):
        self.speak_dialog('what.capabilities')
        wait_while_speaking()

    #Who are you
    @intent_file_handler('whoare.you.intent')
    def handle_pick_story(self, message):
        self.speak_dialog('whoare.you')
        wait_while_speaking()

    #Who's Laura
    @intent_file_handler('wwhois.laura.intent')
    def handle_pick_story(self, message):
        self.speak_dialog('whois.laura')
        wait_while_speaking()

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return BedtimeStories()

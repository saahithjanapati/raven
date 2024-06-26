# eleven labs

# from elevenlabs.client import ElevenLabs
from config import *

import pygame
import time


class AudioModule():
    def __init__(self):
        # self.client = ElevenLabs(api_key = ELEVEN_KEY)
        pygame.mixer.init()
        pass


    def play_snippet(self, name: str):
        pygame.init()
        pygame.mixer.init()

        try:
            sound = pygame.mixer.Sound(f'audio/{name}.mp3')
            sound.play()

            while pygame.mixer.get_busy():
                time.sleep(0.1)  # You can adjust the sleep time as needed
        except Exception as e:
            print(e)
            print(f"Error playing {name}.mp3")
        
        pygame.quit()


# audio = AudioModule()
# audio.play_snippet("turn_right")
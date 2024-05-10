import pygame
from exceptions import GUTNException

class Speaker:
    def __init__(self):
        pygame.mixer.init()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def play_sound(self, sound_file):
        try:
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
        except Exception as e:
            raise GUTNException(f"Failed to play sound: {str(e)}")

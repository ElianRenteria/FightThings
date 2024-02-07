import pygame
import os

sprites = {}
for file in os.listdir("characters"):
    if file != ".DS_Store":
        sprites[file] = {}
        try:
            for action in os.listdir(f"characters/{file}"):
                if action != ".DS_Store":
                    sprites[file][action] = []
                    for image in os.listdir(f"characters/{file}/{action}"):
                        sprites[file][action].append(pygame.image.load(f"characters/{file}/{action}/{image}"))
        except NotADirectoryError:
            if action != ".DS_Store":
                sprites[file] = []
                for image in os.listdir(f"characters/{file}"):
                    sprites[file].append(pygame.image.load(f"characters/{file}/{image}"))

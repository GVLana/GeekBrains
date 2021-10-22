import json
import pickle

with open('group.json', 'r') as f:
    music_fav = json.load(f)

print(music_fav)

with open('group.pickle', 'rb') as f:
    music = pickle.load(f)

print(music)
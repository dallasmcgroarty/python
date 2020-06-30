playlist = {
    "title": 'Cool Playlist',
    'author': 'Dallas McGroarty',
    'songs': [
        {'title': 'song1', 'artist': ['Black Keys'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['Jones Bros', 'DJ Ruff'], 'duration': 4.30},
        {'title': 'song3', 'artist': ['We the People'], 'duration': 3.0},
    ]
}

total_length = 0
for song in playlist['songs']:
    print(song['title'])
    print(song['duration'])
    total_length += song['duration']

print()
print(f"Total playlist duration is {total_length}")
print()
print(playlist)
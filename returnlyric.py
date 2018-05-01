import random

# return a list of lyrics that belong to a random song in the `Lyrics_Death.txt` file
def return_song(songs, length):
    song_number = random.randint(1, length)
    count = 0
    for lyric in songs:
        if lyric[0] == ' ':
            count += 1
            if count == song_number:
               subcount = songs.index(lyric) + 1
               song = []
               song.append(lyric)
               while subcount <= len(songs)-1:
                   if songs[subcount][0] == ' ':
                       break 
                   else:
                       song.append(songs[subcount])
                       subcount += 1
                   
               return(song)

# return a random lyric from a list of lyrics
def random_lyrics(song):
    song = [s + '.\n' for s in ' '.join(song).split('.\n')[:-1]]
    i = random.randint(1,len(song)-1)
    if song[i] != '\n': 
        return(song[i])
    else:
        random_lyrics(song)


def main():
    file = open('/Users/andrewvlouis/Documents/GitHub/lyricsbot_death/Lyrics_Death.txt', mode = 'r')
    file = list(file)
    song = return_song(file, 64)
    return random_lyrics(song)


if __name__ == '__main__':
    main()
import tweepy
import random
import returnlyric
from secrets import consumer_key, consumer_secret, access_token, access_secret
from time import sleep 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
        
file = open('/Users/andrewvlouis/Documents/GitHub/lyricsbot_death/Lyrics_Death.txt', mode = 'r')
file = list(file)

def main():
    while True:
        song = returnlyric.return_song(file, 55)
        lyric = returnlyric.random_lyrics(song)
        try:
            api.update_status(lyric)
        except tweepy.TweepError as error:
            print(error.reason)
        sleep(900)


if __name__ == '__main__':
    main() 
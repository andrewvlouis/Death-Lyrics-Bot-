import lyricsgenius as genius

# access Genius API
access = ''
api = genius.Genius(access)
artist = api.search_artist('Death (metal band)')

scream_bloody_gore = ['Infernal Death', 'Zombie Ritual', 'Denial of LIfe', 'Sacrificial', \
                       'Mutilation', 'Regurgitated Guts', 'Baptized in Blood', 'Torn to Pieces', \
                       'Evil Dead', 'Scream Bloody Gore', 'Beyond the Unholy Grave', 'Land of No Return']

leprosy = ['Leprosy', 'Born Dead', 'Forgotten Past', 'Left to Die', 'Pull the Plug', \
           'Open Casket', 'Primitive Ways', 'Choke on It']


spiritual_healing = ['Living Monstrosity', 'Altering the Future', 'Defensive Personalities', \
                    'Within the Mind', 'Spiritual Healing', 'Low Life', 'Genetic Reconstruction', \
                    'Killing Spree']

human = ['Flattening of Emotions', 'Suicide Machine', 'Together as One', 'Secret Face', \
         'Lack of Comprehension', 'See Through Dreams', 'Cosmic Sea', 'Vacant Planets']

individual_thought_patterns = ['Overactive Imagination', 'In Human Form', 'Jealousy', \
                                'Trapped in a Corner', 'Nothing Is Everything', 'Mentally Blind', \
                                'Individual Thought Patterns', 'Destiny', 'Out of Touch', \
                                'The Philosopher']
 
symbolic = ['Symbolic', 'Zero Tolerance', 'Empty Words', 'Sacred Serenity', '1,000 Eyes', \
            'Without Judgement', 'Crystal Mountain', 'Misanthrope', 'Perennial Quest']

the_sound_of_perserverance = ['Scavenger of Human Sorrow', 'Bite the Pain', 'Spirit Crusher', \
                              'Story to Tell', 'The Flesh and the Power It Holds', 'Voice of the Soul', \
                              'To Forgive Is to Suffer', 'A Moment of Clarity']

albums = [scream_bloody_gore, leprosy, spiritual_healing, human, individual_thought_patterns, \
          symbolic, the_sound_of_perserverance]


def main():
    for album in albums:
        for song in album:
            song = api.search_song(song, artist.name)
            artist.add_song(song)

    artist.save_lyrics(format = 'txt')

if __name__ == '__main__':
    main()


    
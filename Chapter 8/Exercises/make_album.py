def make_album(artist, title, number_of_songs=''):
    """Simple way to build an album."""
    album = {'artist': artist, 'title': title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    print('\nCreating an album. Press \'q\' if you want to quit.')
    artist = input('Artist: ')
    if artist == 'q':
        break
    title = input('Title: ')
    if title == 'q':
        break
    number_of_songs = input('Number of songs in the album (Optional - leave blank): ')
    if number_of_songs == 'q':
        break
    print(make_album(artist, title, number_of_songs))

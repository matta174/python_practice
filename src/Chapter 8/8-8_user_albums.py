def make_album(artist_name,album_title):
    album = {'Artist Name': artist_name,'Album Title': album_title}
    return album

while True:
    album = input('Please provide an album\n')
    if album == 'q':
        break
    artist_name = input('Please provide an artist\n')
    if artist_name== 'q':
        break
    print(make_album(artist_name,album))



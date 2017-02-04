def make_album(artist_name,album_title):
    album = {'Artist Name': artist_name,'Album Title': album_title}
    return album

sams_town = make_album('Brandon Flowers',"Sam's Town")
print(sams_town)

macklemore = make_album('Macklemore','wooohoo')
print(macklemore)
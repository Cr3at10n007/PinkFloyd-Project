FILEPATH="Pink_Floyd_DB.txt"
def get_parsed_data():
    """
    parses and returns the database
    :return: the parsed data
    :rtype: dict
    """
    file=open(FILEPATH,"r")
    data=file.read()
    data = data.split("#")[1:]  # Removing a blank spot from the beginning
    album_dict = {}
    for i in data:
        i = i.split("*")
        album_name = i[0].split("::")[0]
        songs = i[1:]
        album_dict[album_name] = {}
        for song in songs:
            song_info = song.split("::")
            song_name = song_info[0]
            writer = song_info[1]
            length = song_info[2]
            lyrics = song_info[3]
            album_dict[album_name][song_name] = [writer, length, lyrics]
    return album_dict

def get_albums(database):
    """
    returns a list of all the albums from a database
    :param database: a parsed database
    :type database: dict
    :return: all the albums
    :rtype: str
    """
    return ", ".join(database.keys()) 

def get_album_songs(database,album_name):
    """
    gets all songs from an album
    :param database: a parsed database
    :type database: dict
    :param album_name: the name of the album
    :type album_name: str
    :return: all the songs in the album or an error
    :rtype: str
    """
    try:
        return ", ".join(database[album_name].keys())
    except:
        return "ERROR:album not found"
        
def get_song_album(database,song_name):
    """
    Gets the album in which a song is in
    :param database: a parsed database
    :type database: dict
    :param song_name: the name of the song
    :type song_name: str
    :return: the album in which the song is in
    :rtype: str
    """
    for i in database.keys():
        if song_name in database[i].keys():
            return i
    return "Error: song doesn't exist" 

def get_song_length(database, song_name):
    """
    Gets the length of a song
    :param database: a parsed database
    :type database: dict
    :param song_name: the name of the song
    :type song_name: str
    :return: the length of the song
    :rtype: str
    """
    try:
        length=database[get_song_album(database,song_name)][song_name][1]
        return length
    except:
        return "ERROR:song not found"
    
def get_song_lyrics(database, song_name):
    """
    Gets the lyrics of a song
    :param database: a parsed database
    :type database: dict
    :param song_name: the name of the song
    :type song_name: str
    :return: the lyrics of the song
    :rtype: str
    """
    try:
        lyrics=database[get_song_album(database,song_name)][song_name][2]
        return lyrics
    except:
        return "ERROR:song not found"

def search_song_by_name(database,song_name):
    """
    Searches song by name
    :param database: a parsed database
    :type database: dict
    :param song_name: the name of the song
    :type song_name: str
    :return: the name of the song or an error
    :rtype: str
    """
    songs=[]
    for i in database.keys():
        for j in database[i].keys():
            if j.lower().find(song_name)!=-1:
                songs.append(j)
    if len(songs)==0:
        return "No songs containing "+song_name
    return ", ".join(songs)
    
def search_song_by_lyrics(database,lyrics):
    """
    Searches song by lyrics
    :param database: a parsed database
    :type database: dict
    :param lyrics: some lyrics of the song
    :type lyrics: str
    :return: the name of the song or an error
    :rtype: str
    """
    songs=[]
    for i in database.keys():
        for j in database[i].keys():
            if database[i][j][2].find(lyrics) != -1:
                songs.append(j)
    if len(songs)==0:
        return "No songs containing "+lyrics
    return ", ".join(songs)

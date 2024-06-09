class Song:
    count =0
    genres=[]
    artists=[]
    genre_count={}
   
     
    def __init__(self, name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
    
    @classmethod
    def add_song_to_count(cls):
        cls.count+=1
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls,artist): 
        cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
     cls.genre_count[cls.genre]=cls.genre_count.get(genre,0)+1
    @classmethod
    def add_to_artist_count(cls,artist):
     cls.artist_count[artist]=cls.artist_count.get(artist,0)+1
    
     def __repr__(self):
        return f"{self.name} by {self.artist} in {self.genre}"
     

     
       

import pandas as pd

music_df = pd.read_csv("data/music_recommender.csv")
def get_songs():
    df = pd.read_csv("data/music_recommender.csv")
    songs = []
    artists = []
    ids = []
    for song in df.name:
        songs.append(song)
    for artist in df.primary_artist:
        artists.append(artist)
    for id in df.id:
        ids.append(id)
    return songs,artists,ids

def get_recommendations(title_id,valence,energy,df=music_df):
    topic = df[df['id']==title_id]['dominant_topic']
    print(topic.item())
    genre = df[df['id']==title_id]['genre']
    genres=[]
    nongenre = []
    df = df[df['valence'] >= valence-0.05]
    df = df[df['valence'] <= valence+0.05]
    df = df[df['energy'] >= energy-0.05]
    df = df[df['energy'] <= energy+0.05]
    df = df[df['dominant_topic'] == topic.item()]
    df.reset_index(drop=True,inplace=True)
    for ix,g in enumerate(df.genre):
        if g == genre.item():
            genres.append(ix)
        else:
            nongenre.append(ix)

    ids_in_genre = list(df.loc[genres]['id'])


    ids_non_genre = list(df.loc[nongenre]['id'])

    if len(genres) >= 15:
        return ids_in_genre[:11]
    elif len(genres) > 0 and len(nongenre)>0:
        ids = ids_in_genre + ids_non_genre
        return ids[:11]
    elif len(genres) > 0 :
        return ids_in_genre
    else:
        return ids_in_genre

import re 
import urllib.request 
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator,MyMemoryTranslator
"""
    Title: Extractlyrics
    By: Cuadernin
    Task: extract the song lyrics searched in azlyrics with the possibility of translation 
"""

def lyrics(cancion,artista,trans): 
    artista=artista.lower() 
    cancion=cancion.lower() 
    artista=re.sub('[^A-Za-z0-9]+',"",artista) 
    cancion=re.sub('[^A-Za-z0-9]+',"",cancion) 
    url=f"http://azlyrics.com/lyrics/{artista}/{cancion}.html"    
    try: 
        content=urllib.request.urlopen(url).read() 
        soup=BeautifulSoup(content,'html.parser') 
        lyrics=str(soup) 
        inicio='<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->' 
        fin='<!-- MxM banner -->' 
        lyrics=lyrics.split(inicio)[1] 
        lyrics=lyrics.split(fin)[0] 
        lyrics=re.sub('(<.*?>)',"",lyrics)
        if trans==0:
            return lyrics
        elif trans==1:
            ln='es' # <-----------------------------Assign the language using its abbreviation
            lyrics=GoogleTranslator(source='auto',target=ln).translate(text=lyrics)
            return lyrics
        else:
            return 'Error: You got the wrong number'
    except Exception as error: 
        return "Exception occurre: "+str(error)
fn=lyrics('pásame un bote','banda ms',0)
archivo=open("song.txt","w") 
archivo.write(fn)
print("################@@@@@@@@@@@@@@@@ D O N E @@@@@@@@@@@@@@@@################")



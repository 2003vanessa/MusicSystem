# import music_tag

# f = music_tag.load_file("Thriller.mp3")
# title_item = f['title']
from tinytag import TinyTag 

def music(metadata):
    f=TinyTag.get("Thriller.mp3")
    
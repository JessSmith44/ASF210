import random
import itertools

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

playlist = [
    'Dolly Parton, Jolene',
    'Pantera, Walk',
    'The Dirty Heads, Lay Me Down',
    'Spice Girls, Wannabe',
    'Purity Ring, Asido',
    'Chrvrches, Clearest Blue',
    'Carrie Underwood, Before He Cheats'
]
# print(playlist.index('Chrvrches, Clearest Blue')) shows index of 5. 

# playlist = {
#     'artist': 'Dolly Parton', 'song': 'Jolene',
#     'artist':'Pantera', 'song':'Walk',
#     'artist':'The Dirty Heads', 'song':'Lay Me Down',
#     'artist':'Spice Girls', 'song':'Wannabe',
#     'artist':'Purity Ring', 'song':'Asido',
#     'artist':'Chrvrches', 'song':' Clearest Blue',
#     'artist':'Carrie Underwood', 'song':' Before He Cheats'
# }

def quickSort(list):
    playlist.sort()
    
    # sortedSong = sorted(playlist.keys(), key=lambda x:x.lower())
    # for i in sortedSong:
    #     values=playlist[i]
    # print(values)

    # music = playlist(quickSort(playlist))
    # if not list:
    #     return[]
    # return(quickSort([x for x in list[1:] if x < list[0]])
    # + [list[0]] + quickSort(x for x in list[1:] if x >= list[0]))

print(quickSort(playlist))

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

length = 20
currSong = []

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        artist = input("Please give an artist: ")
        song = input('and song title: ')
        Song(artist, song)

        plSong = artist + ", " + song
        playlist.append(plSong)
        print(playlist)

        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        artist = input("Please give an artist: ")
        song = input('and song title:')
        currSel = artist + ", " + song
        # remove song from playlist
        playlist.remove(currSel)
        
        print("Song Removed to Playlist")
        print('Your new playlist is: ', playlist)
    elif choice == 3:
        # Play the playlist from the beginning
        # start at index 0 
        playing = playlist[0]
        currSong.append(playing)
        # print current
        # Display song name that is currently playing
        print("Playing....")        
        print(currSong)
        # index = playlist.index(currSong)
        # print("at index: ", index)
    elif choice == 4:
        # Skip to the next song on the playlist
        # played = []
        for index, elem in enumerate(playlist):
            if (index+1 < len(playlist)):
                currSong = str(elem)
                nextSong = str(playlist[index+1])
                break
            currSong.append(nextSong)
            # print(currSong)
            index = playlist.index(currSong)
            print("at index: ", index)
        # Display song name that is now playing
        print("Skipping....")   
        print(nextSong) 

    elif choice == 5:
        # Go back to the previous song on the playlist

        # played = []

        # for index, elem in enumerate(playlist):
        #     if (index+1 < len(playlist)):
        #         currSong = str(elem)
        #         nextSong = str(playlist[index+1])
        #         played.append(currSong)
        #         print(played)
        #         break

        l_iter = iter(playlist)
        print(next(l_iter))

        # Display song name that is now playing
        print("Replaying....") 
        # print(nextSong) 
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song

        shuffleSong = random.choice(playlist)
        
        # Display song name that is now playing
        print("Shuffling....")          
        print(shuffleSong)

    elif choice == 7:
        # Display the song name and artist of the currently playing song

        print("Currently playing: ", end=" ")    
        print(currSong)
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(playlist)
    elif choice == 0:
        print("Goodbye.")
        break

# Show Currently Playing Song


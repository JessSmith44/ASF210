from random import randint 
import itertools

class Song:
    def __init__(self,artist,title):
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


class Playlist:
    def __init__(self):
        self.songList = []
        self.currSong = 0

    def addSong(self, song):
        self.songList.append(song)

    def remove(self, title):
        variable = None
        for index in range(0, len(self.songList)):
            song = self.songList[index]
            if song.title == title:
                variable = index
        if variable is not None:
            self.songList.pop(variable)

    def shuffleList(self):
        s = len(self.songList)
        for i in range(s):
            rand = randint(i, s -1)
            self.songList[i], self.songList[rand] = self.songList[rand], self.songList[i]
            


playlist = Playlist()

playlist.addSong(Song('Dolly Parton', 'Jolene'))
playlist.addSong(Song('Pantera', 'Walk'))
playlist.addSong(Song('The Dirty Heads', 'Lay Me Down'))
playlist.addSong(Song('Spice Girls', 'Wannabe'))
playlist.addSong(Song('Purity Ring', 'Asido'))
playlist.addSong(Song('Chrvrches', 'Clearest Blue'))
playlist.addSong(Song('Carrie Underwood', 'Before He Cheats'))


size = len(playlist.songList)

def sort(playlist, size):
    for s in range(len(playlist)):
        min_idx = s
        for i in range(s + 1, size):
            if playlist[i] < playlist[min_idx]:
                min_idx = i
        (playlist.songList[s], playlist.songList[min_idx]) = (playlist.songList[min_idx], playlist.songList[s])

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
currSong = 0

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        artist = input("Please give an artist: ")
        title = input('and song title: ')
        song = Song(artist, title)

        playlist.addSong(song)
        # print(playlist)

        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        song = input('Please give a song title: ')
        
        # remove song from playlist
        playlist.remove(song)
        
        print("Song Removed from Playlist")
        print('Your new playlist is: ', playlist)
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")        
        print(playlist.songList[playlist.currSong]) 
        
    elif choice == 4:
        # Skip to the next song on the playlist

        if playlist.currSong+1 < len(playlist.songList):
            playlist.currSong = playlist.currSong +1
        else:
            playlist.currSong = 0

        # Display song name that is now playing
        print("Skipping....")   
        print(playlist.songList[playlist.currSong]) 

    elif choice == 5:
        # Go back to the previous song on the playlist

        if playlist.currSong != 0:
            playlist.currSong = playlist.currSong -1
        else:
            playlist.currSong = len(playlist.songList)-1


        # Display song name that is now playing
        print("Replaying....") 
        print(playlist.songList[playlist.currSong])  

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song    
        # Display song name that is now playing
        print("Shuffling....")          
        playlist.shuffleList()

    elif choice == 7:
        # Display the song name and artist of the currently playing song

        print("Currently playing: ", end=" ")    
        print(playlist.songList[playlist.currSong])

    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        for song in playlist.songList:
            print(song.title,' by ', song.artist)

    elif choice == 0:
        print("Goodbye.")
        break

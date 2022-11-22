class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key,size):
        # Insert your hashing function code
        return key%size 
        # used google to see what the correct was to set this up was

    def rehash(self, oldhash, size):
        # Insert your secondary hashing function code
        return (oldhash+1)% size
        # used google to see what the correct was to set this up was
        # pass

    def put(self,key,data):
        # Insert your code here to store key and data 
        hashvalue = self.hashfunction(key,len(self.slots))
 
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
         
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                 
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                
                else:
                    self.data[nextslot] = data
    # pass

# Had the help of a few websites help get these functions set-up as I could not resolve why my return was coming up 
# as it was. One of the sites was explaning everything about setting up the functions for hashing including a deep dive
# into each step in lamens terms. one site being here : https://docs.python.org/3/library/hashlib.html
# another being here : https://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php
# and I am sure I am forgetting a few as I have been working on this for a while now, however if you would like me to 
# track them all down I can certainly do a history hunt for them, please let me know.
# I also reviewed previous assignments for this class to give me the proper mindset of what all has
# led up to this point to assist me in the correct was of thinking to resolve everything

    def get(self,key):
        # Insert your code here to get data by key

        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and not found and not stop:
             
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                 
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                     
                    stop = True
        return data
        # pass

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H[52])

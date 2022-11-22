class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)
        return(hashVal *len(keystr)) % self.size
        # this return is set to make clustering less
        # prevelent. 

    def rehash(self,key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        counter = 0 
        for ch in str(keystr):
            counter += 1
            hashVal += ord(ch)+counter
        return(hashVal *len(keystr)) % self.size
        # pass

    def put(self,key,data):
        # Insert your code here to store key and data 
        
        pass

    def get(self,key):
        # Insert your code here to get data by key
        return self.get(key)
        # index = self.hash(key)
        # if self.array[index] is None:
        #     raise KeyError()
        # else:
        #     for kvp in self.array[index]:
        #         return kvp[1]
        #     raise KeyError
        # pass

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data

# print the slot values
# print(H.hashfunction())

# print the data values
# print(H.hashfunction())

# print the value for key 52
# print(H.hashfunction())

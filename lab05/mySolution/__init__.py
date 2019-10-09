class HashTable :
    def __init__(self) :
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data) :
        if data == "" :
            return

        if self.checkSize() >= 70 :
            self.size, self.slots, self.data = self.resize()

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None :
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else :
            if self.slots[hashvalue] == key :
                self.data[hashvalue] = data  #replace
            else :
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key :
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None :
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self, key, size) :
        return key % size

    def rehash(self, oldhash, size) :
        return (oldhash + 1 ) % size

    def get(self, key) :
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key :
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
            if position == startslot :
                stop = True
        return data

    def __getitem__(self, key) :
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def checkSize(self) :
        count = 0
        for element in self.slots :
            if element != None :
                count += 1
        return (float(count) / float(self.size)) * 100

    def resize(self) :
        temp = HashTable()
        
        temp.size = self.size * 2
        temp.slots = [None] * temp.size
        temp.data = [None] * temp.size
        count = 0
        
        for element in self.slots :
            if element != None :
                temp.put(element, self.data[count])
                count += 1
        
        return temp.size, temp.slots, temp.data
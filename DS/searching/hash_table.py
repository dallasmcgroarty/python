# hash table class

class HashTable(object):
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hash_val = self.hash_function(key,len(self.slots))

        # if slot is empty
        if self.slots[hash_val] == None:
            self.slots[hash_val] == key
            self.data[hash_val] = data
        # if key exists
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = data
            # handle collisions, find next available slot
            else:
                next_slot = self.re_hash(hash_val, len(self.slots))

                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data   
    def hash_function(self, key, size):
        return key%size

    def re_hash(self, old_hash, size):
        return (old_hash + 1)%size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        pos = start_slot

        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.re_hash(pos, len(self.slots))
                if pos == start_slot:
                    stop = True
        return data
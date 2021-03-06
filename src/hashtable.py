# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        new_node = LinkedPair(key, value) 
        hm_key = self._hash_mod(key)
        head = self.storage[hm_key]
        node = head

        if not head:
            self.storage[self._hash_mod(key)] = new_node # if a no hash is available at that key, create one via a new node
        else:
            if head.key == key: # if the hash exists at that key, override it with new hash value
                new_node.next = head.next # assigning the old head's next to new head
                self.storage[self._hash_mod(key)] = new_node # head becomes new node
            else:
                while node:
                    if not node.next: # if next does not exist, next becomes the new node
                        node.next = new_node
                        break
                    elif node.next.key == key: # if next key is the key node.next becomes node
                        new_node.next = node.next.next
                        node.next = new_node
                        break
                    else: # else move to the next node in LL
                        node = node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        node = self.storage[self._hash_mod(key)]
        count = 0
        while node:
            if count == 0: # if key is first node
                count += 1
                if node.key == key:
                    self.storage[self._hash_mod(key)] = node.next # pointer will look at node.next
                    break
            elif count > 0: # if the key is in the LL, find key and make the prev node point to node.next
                if node.next:
                    if node.next.key == key:
                        node.next = node.next.next
                        break
                    else:
                        node = node.next
                else:
                    return
        return
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        node = self.storage[self._hash_mod(key)]
        while node: # check that key exists in the hash
            if node.key == key: # if key is found return it
                return node.value
            else:
                node = node.next # else move to the next node in LL until key is found
        return None # return None if it does not exist


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2 # multiply size by 2
        new_ht = HashTable(self.capacity) # new hash table with new 2x capacity
        for bucket in self.storage: # loop through all buckets in hash
            while bucket: # while each node exists
                new_ht.insert(bucket.key, bucket.value) # insert each node in the LL at its curr position into new hash
                bucket = bucket.next # move to next node and repeat until we reach end of linked list for this hash
        self.storage = new_ht.storage




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

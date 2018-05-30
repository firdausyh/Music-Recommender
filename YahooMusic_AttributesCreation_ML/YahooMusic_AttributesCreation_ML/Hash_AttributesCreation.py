#############################################  HashMap  #######################################
#Using HashMap to store training data: "trainIdx2.txt"
#Key:UserId,ItemId
#Value:Score
class Hashmap(object):
    """
    character holding hash map
    """
    def __init__(self, hash_fn, length=100):
        assert hasattr(hash_fn, '__call__'), 'You must provide a hash function'

        self._buckets = [None] * length
        self.hash_len = length
        self.hash_fn = hash_fn

        # Max items per bucket
        self.change_len = length / 5

        

    def _hash(self, key):
        return self.hash_fn(key) % self.hash_len

    def put(self, key, val):
        pos = self._hash(key)
        bucket = self._buckets[pos]
    
        if bucket is None:
            self._buckets[pos] = bucket = LinkedList()
            bucket.put(key, val)
        else:
            bucket.put(key, val)
            if len(bucket) >= self.change_len:
                #print 'growing', 'num buckets: ', len(self._buckets)
                self._grow()

    def _grow(self):
        # Double size of buckets
        self.hash_len = self.hash_len * 2

        # New max len for buckets
        self.change_len = self.hash_len / 5

        # new bucket holder
        oldBuckets = self._buckets
        self._buckets = [None] * self.hash_len


        # Iterate through all buckets
        # and reinsert key=>vals
        for bucket in oldBuckets:
            if bucket is None: continue
            for (key, val) in bucket:
                self.put(key, val)


    def get(self, key):
        pos = self._hash(key)
        bucket = self._buckets[pos]

        if bucket is None: return None

        return bucket.get(key)

    def delete(self, key):
        """
        Deletes a value in a hashmap
        returns the value in the map if it exists
        """
        pos = self._hash(key)
        node = self._buckets[pos]

        if node is None: return None

        self._buckets[pos] = None
        self.num_vals -= 1

        return node.val


    def _shrink(self):
        #length = self.hash_len 
        pass
        
    def __repr__(self):
        return '<Hashmap %r>' % self._buckets
    
    def __len__(self):
        n = 0
        for bucket in self._buckets:
            if bucket is None: continue
            n += len(bucket)
        return n

    def get_num_empty_buckets(self):
        n = 0
        for bucket in self._buckets:
            if bucket is None or len(bucket) == 0: n += 1
        return n

    def get_longest_bucket(self):
        longest = 0
        b = None
        for bucket in self._buckets:
            if bucket is None: continue

            l = len(bucket)
            if longest < l:
                longest = l
                b = bucket
        return longest

    def get_shortest_bucket(self):
        shortest = 0
        b = None
        for bucket in self._buckets:

            if bucket is None:
                shortest = 0
                b = None
                break

            l = len(bucket)
            if shortest == 0: shortest = l
            if shortest >= l:
                shortest = l
                b = bucket

        return shortest
    
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __str__(self):
        return "<Node key: %s val: %s>" % (self.key, self.val)

    def __repr__(self):
        return self.__str__()

class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self._cur = None

    def put(self, key, val):
        # Empty list
        node = self.first 
        if node is None:
            # TODO when first is set, set _cur (only happens on delete)
            self.first = Node(key, val)
            self.last = self.first
            self._cur = self.first
            self.length += 1
            return None

        node = self._get_node(key)

        # key for node exists, overwrite val
        if not node is None and node.key == key:
            node.val = val
            return None

        # Set new node to the end
        tmp = self.last
        tmp.next = Node(key, val)
        self.last = tmp.next
        self.length += 1

    def _get_node(self, key):
        node = self.first

        while not node is None:
            if node.key == key:
                return node
            node = node.next
        else:
            return None

    def get_key_and_val(self, key):
        node = self._get_node(key)
        if node is None:
            return None
        else:
            return (node.key, node.val)

    def get(self, key):
        tup = self.get_key_and_val(key)
        if not tup is None:
            return tup[1]

    def delete(self, key):
        pass

    def __str__(self):
        return '<LinkedList: %d nodes>' % self.length

    def __repr__(self):
        arr = []
        node = self.first
        while not node is None:
            arr.append(str(node))
            node = node.next

        return 'LinkedList: Nodes: %r' % arr

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur is None:
            self._cur = self.first
            raise StopIteration
        else:
            node = self._cur
            self._cur = self._cur.next
            return (node.key, node.val)

    def __len__(self):
        return self.length



def string_hash(string): return hash(string)

############################## Reading training file and Creating HashMap objective################
hashmap = Hashmap(string_hash)
i=0
for word in open('D:/627/Project/Python/DataProcess/trainIdx2_matrix.txt', 'r'):
    arr=word.strip().split('|')
    value=float(arr[2])
    key=str(arr[0]+','+arr[1])
    hashmap.put(key, value)
    
############################# Creating Attributes###########################################
exec(open('D:/627/Project/Python/YahooMusic_Attributes&ML/FinalSubmission/AttributesCreation_train.py').read())
exec(open('D:/627/Project/Python/YahooMusic_Attributes&ML/FinalSubmission/AttributesCreation_test.py').read())

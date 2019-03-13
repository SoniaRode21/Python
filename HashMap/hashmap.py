__author__ = 'Soniya Rode'
from collections import namedtuple
import re

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    __slots__ = 'table', 'numkeys', 'cap', 'maxload', 'hashfunction', 'collisions', 'probes'

    def __init__(self, hashf, initsz=100, maxload=0.7):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param hashf : The hashfunction to use
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.hashfunction = hashf
        self.collisions = 0
        self.probes = 0

    def put(self, key, value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        index = self.hashfunction(key) % self.cap

        if self.table[index] is not None:

            # To calculate the number of collisions
            if self.table[index].key != key:
                self.collisions += 1
            # To add  1 to the value count of an already present key
            if self.table[index].key == key:
                self.table[index] = Entry(key, self.table[index].value + 1)
                self.probes += 1
                return

        # Finding the index value to add to the hash table
        while self.table[index] is not None and \
                self.table[index] != DELETED and \
                self.table[index].key != key:

            index += 1

            self.probes += 1

            # To wrap around the hash table to find an empty slot
            if index == len(self.table):
                index = 0
            if self.table[index] is not None:

                if self.table[index].key == key:
                    self.table[index] = Entry(key, self.table[index].value + 1)
                    return

        self.probes += 1

        # Adding key,value to the table
        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key, value)

        # For rehashing
        if self.numkeys / self.cap > self.maxload:
            print("rehashing")
            # rehashing
            self.probes = 0
            self.collisions = 0
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None and entry != DELETED:
                    self.put(entry.key, entry.value)

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hashfunction(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hashfunction(key) % self.cap

        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1

            index += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            self.probes += 1
            return self.table[index].value
        else:
            self.probes += 1
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hashfunction(key) % self.cap

        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1

            index += 1
            if index == self.cap:
                index = 0
        self.probes += 1
        return self.table[index] is not None

def getProbes(self):
        '''
        Returns Number of probes
            :return: probes
        '''

        return self.probes


def getCollisions(self):
    '''
    Returns Number of collisions

    :return: collisions
    '''
    return self.collisions


def getNumberKeys(self):
    '''
    Returns Number of keys present in the hashmap

    :return: probes
    '''
    return self.numkeys


def getMaxValue(self):
    '''
    Returns the key with max no of values

    :return: key
    :return: maxValue
    '''

    index = 0
    maxIndex = 0
    maxValue = 0

    # Parses through the hash map to find max Value
    while index < self.cap:

        if self.table[index] is not None and \
                self.table[index] != DELETED:

            if (self.table[index].value > maxValue):
                maxValue = self.table[index].value
                maxIndex = index
        index += 1

    return self.table[maxIndex].key, maxValue


def hash_func1(key):
    '''
        Returns the hash value for the given key

        :param : key  key to be hashed
        :return: hashVal hashed value
    '''
    hashval = 0
    i = 0
    while i < len(key):

        if (i % 2 == 0):
            hashval += ord(key[i]) * 5 ** i
        i += 1
    return hashval


def hash_func2(key):
    '''
          Returns the hash value for the given key

          :param : key  key to be hashed
          :return: hashVal hashed value
      '''
    hashval = 0
    i = 0
    while i < len(key):
        hashval += ord(key[len(key) - i - 1]) * i ** 5
        i += 1
    return hashval


def hash_funcPython(key):
    '''
        Returns the hash value for the given key

        :param : key  key to be hashed
        :return: hashVal hashed value
    '''

    # Python's hash function


    return hash(key)


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def testMap():
    # Hashing hashmap map using hash map function 2
    map = Hashmap(hash_func2, 5, 0.7)
    map.put('apple', 1)
    map.put('banana', 2)
    map.put('orange', 15)
    printMap(map)
    print("Number of probes : ", map.getProbes())
    print("Number of collisions : ", map.getCollisions())
    print("Number of keys Present : ", map.getNumberKeys())
    print(map.contains('apple'))

    print(map.contains('grape'))

    print(map.get('orange'))
    print("Probes after contains and get : ", map.getProbes())

    print('--------- adding one more to force table resize ')
    map.put('grape', 7)

    printMap(map)
    print("Number of probes after resizing ", map.getProbes())
    print("Number of collisions after resizing : ", map.getCollisions())
    print("Number of keys Present : ", map.getNumberKeys())

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach', 16)
    printMap(map)
    print(map.get('grape'))


def main():
    # Take file input and process it
    filename = input("Enter File name ")
    load = {0.5, 0.7, 0.9}
    print()
    print()
    print()
    for i in load:
        print("----Max load value : ", i)

        my_file = open(filename, "r")
        map2 = Hashmap(hash_func2, 1000, i)
        map1 = Hashmap(hash_func1, 1000, i)
        map3 = Hashmap(hash_funcPython, 1000, i)
        for line in my_file:

            line = line.lower()
            # Remove the punctuatuions from each line
            line = re.split('\W+', line)
            i = 0
            while i < len(line):

                if (line[i] != ""):
                    map2.put(line[i], 1)
                    map1.put(line[i], 1)
                    map3.put(line[i], 1)

                i += 1

        print('--------- HASHMAP using hash function 1 --------')
        printMap(map1)
        print("Word occured maximum number of times ", map1.getMaxValue())
        print("Number of probes : ", map1.getProbes())
        print("Number of collisions : ", map1.getCollisions())

        print('--------- HASHMAP using hash function 2 --------')
        printMap(map2)
        print("Word occured maximum number of times ", map2.getMaxValue())
        print("Number of probes : ", map2.getProbes())
        print("Number of collisions : ", map2.getCollisions())

        print('--------- HASHMAP using python inbuilt hash function --------')
        printMap(map3)
        print("Word occured maximum number of times ", map3.getMaxValue())
        print("Number of probes : ", map3.getProbes())
        print("Number of collisions : ", map3.getCollisions())
        print()
        print()
        print()
        my_file.close()


if __name__ == '__main__':
    testMap()
    main()
__author__ = 'Soniya Rode'
from collections import namedtuple
import re

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    __slots__ = 'table', 'numkeys', 'cap', 'maxload', 'hashfunction', 'collisions', 'probes'

    def __init__(self, hashf, initsz=100, maxload=0.7):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param hashf : The hashfunction to use
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.hashfunction = hashf
        self.collisions = 0
        self.probes = 0

    def put(self, key, value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        index = self.hashfunction(key) % self.cap

        if self.table[index] is not None:

            # To calculate the number of collisions
            if self.table[index].key != key:
                self.collisions += 1
            # To add  1 to the value count of an already present key
            if self.table[index].key == key:
                self.table[index] = Entry(key, self.table[index].value + 1)
                self.probes += 1
                return

        # Finding the index value to add to the hash table
        while self.table[index] is not None and \
                self.table[index] != DELETED and \
                self.table[index].key != key:

            index += 1

            self.probes += 1

            # To wrap around the hash table to find an empty slot
            if index == len(self.table):
                index = 0
            if self.table[index] is not None:

                if self.table[index].key == key:
                    self.table[index] = Entry(key, self.table[index].value + 1)
                    return

        self.probes += 1

        # Adding key,value to the table
        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key, value)

        # For rehashing
        if self.numkeys / self.cap > self.maxload:
            print("rehashing")
            # rehashing
            self.probes = 0
            self.collisions = 0
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None and entry != DELETED:
                    self.put(entry.key, entry.value)

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hashfunction(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hashfunction(key) % self.cap

        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1

            index += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            self.probes += 1
            return self.table[index].value
        else:
            self.probes += 1
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hashfunction(key) % self.cap

        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1

            index += 1
            if index == self.cap:
                index = 0
        self.probes += 1
        return self.table[index] is not None

    def getProbes(self):
        '''
            Returns Number of probes

            :return: probes
        '''

        return self.probes


def getCollisions(self):
    '''
    Returns Number of collisions

    :return: collisions
    '''
    return self.collisions


def getNumberKeys(self):
    '''
    Returns Number of keys present in the hashmap

    :return: probes
    '''
    return self.numkeys


def getMaxValue(self):
    '''
    Returns the key with max no of values

    :return: key
    :return: maxValue
    '''

    index = 0
    maxIndex = 0
    maxValue = 0

    # Parses through the hash map to find max Value
    while index < self.cap:

        if self.table[index] is not None and \
                self.table[index] != DELETED:

            if (self.table[index].value > maxValue):
                maxValue = self.table[index].value
                maxIndex = index
        index += 1

    return self.table[maxIndex].key, maxValue


def hash_func1(key):
    '''
        Returns the hash value for the given key

        :param : key  key to be hashed
        :return: hashVal hashed value
    '''
    hashval = 0
    i = 0
    while i < len(key):

        if (i % 2 == 0):
            hashval += ord(key[i]) * 5 ** i
        i += 1
    return hashval


def hash_func2(key):
    '''
          Returns the hash value for the given key

          :param : key  key to be hashed
          :return: hashVal hashed value
      '''
    hashval = 0
    i = 0
    while i < len(key):
        hashval += ord(key[len(key) - i - 1]) * i ** 5
        i += 1
    return hashval


def hash_funcPython(key):
    '''
        Returns the hash value for the given key

        :param : key  key to be hashed
        :return: hashVal hashed value
    '''

    # Python's hash function
    return hash(key)


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def testMap():
    # Hashing hashmap map using hash map function 2
    map = Hashmap(hash_func2, 5, 0.7)
    map.put('apple', 1)
    map.put('banana', 2)
    map.put('orange', 15)
    printMap(map)
    print("Number of probes : ", map.getProbes())
    print("Number of collisions : ", map.getCollisions())
    print("Number of keys Present : ", map.getNumberKeys())
    print(map.contains('apple'))

    print(map.contains('grape'))

    print(map.get('orange'))
    print("Probes after contains and get : ", map.getProbes())

    print('--------- adding one more to force table resize ')
    map.put('grape', 7)

    printMap(map)
    print("Number of probes after resizing ", map.getProbes())
    print("Number of collisions after resizing : ", map.getCollisions())
    print("Number of keys Present : ", map.getNumberKeys())

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach', 16)
    printMap(map)
    print(map.get('grape'))


def main():
    # Take file input and process it
    filename = input("Enter File name ")
    load = {0.5, 0.7, 0.9}
    print()
    print()
    print()
    for i in load:
        print("----Max load value : ", i)

        my_file = open(filename, "r")
        map2 = Hashmap(hash_func2, 1000, i)
        map1 = Hashmap(hash_func1, 1000, i)
        map3 = Hashmap(hash_funcPython, 1000, i)
        for line in my_file:

            line = line.lower()
            # Remove the punctuatuions from each line
            line = re.split('\W+', line)
            i = 0
            while i < len(line):

                if (line[i] != ""):
                    map2.put(line[i], 1)
                    map1.put(line[i], 1)
                    map3.put(line[i], 1)

                i += 1

        print('--------- HASHMAP using hash function 1 --------')
        printMap(map1)
        print("Word occured maximum number of times ", map1.getMaxValue())
        print("Number of probes : ", map1.getProbes())
        print("Number of collisions : ", map1.getCollisions())

        print('--------- HASHMAP using hash function 2 --------')
        printMap(map2)
        print("Word occured maximum number of times ", map2.getMaxValue())
        print("Number of probes : ", map2.getProbes())
        print("Number of collisions : ", map2.getCollisions())

        print('--------- HASHMAP using python inbuilt hash function --------')
        printMap(map3)
        print("Word occured maximum number of times ", map3.getMaxValue())
        print("Number of probes : ", map3.getProbes())
        print("Number of collisions : ", map3.getCollisions())
        print()
        print()
        print()
        my_file.close()


if __name__ == '__main__':
    testMap()
    main()

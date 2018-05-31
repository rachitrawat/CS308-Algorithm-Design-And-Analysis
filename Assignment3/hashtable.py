def hash_function(key_str, m):
    i = 0
    sum = 0
    for c in key_str:
        sum += ord(c) * (263 ** i)
        i += 1
    return (sum % 1000000007) % m


class HashTable:
    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m + 1)]

    def ifIndexEmpty(self, index):
        # if list at index is empty, return false
        if not self.table[index]:
            return False
        return True

    def addElement(self, val):
        # only add if element does not exist in list
        if not self.ifElementExists(val):
            index = hash_function(val, self.m)
            # if index is occupied, do list chaining
            if self.ifIndexEmpty(index):
                self.table[index] = [val] + self.table[index]
            else:
                self.table[index] = [val]

    def deleteElement(self, val):
        index = hash_function(val, self.m)
        for element in self.table[index]:
            if element == val:
                self.table[index].remove(element)

    def findElement(self, val):
        if self.ifElementExists(val):
            print("yes")
        else:
            print("no")

    def ifElementExists(self, val):
        index = hash_function(val, self.m)
        for element in self.table[index]:
            if element == val:
                return True
        return False

    def printTable(self):
        print(self.table)

    def printListAtIndex(self, i):
        for element in self.table[int(i)]:
            print(element, end=' ')
        print()


test_case_file = open('test.txt', 'r')
content = [x.strip() for x in test_case_file]

# read m and N
m = int(content[0])
N = int(content[1])

# make HastTable
ht = HashTable(m)

for line in range(2, N + 2):
    query = content[line].split()
    if (query[0] == "add"):
        ht.addElement(query[1])
    elif (query[0] == "check"):
        ht.printListAtIndex(query[1])
    elif (query[0] == "find"):
        ht.findElement(query[1])
    elif (query[0] == "del"):
        ht.deleteElement(query[1])

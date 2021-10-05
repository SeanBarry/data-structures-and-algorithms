class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
        
    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        # iterate through the input string
        for i in range(0, len(string)):
            # call helper method to create the suffix trie
            self.insertSubStringStartingAt(i, string)


    def insertSubStringStartingAt(self, i, string):
        # set the current node to the root node
        node = self.root
        # iterate through the input string from the input index onwards
        for j in range(i, len(string)):
            # grab the letter from the string
            letter = string[j]
            # if the letter is not in the node, insert it, if it is, do nothing
            if letter not in node:
                node[letter] = {}
            
            # update the current node to the letter you just processed
            node = node[letter]
        
        # once the for loop has executed, add a endSymbol to the node and set the value
        # to something arbitrary. True is fine
        node[self.endSymbol] = True
                
    # O(m) time | O(1) space where m in length of input string
    def contains(self, string):
        # set the current node to the root node
        node = self.root
        # iterate through each letter in the string
        for letter in string:
            # if the letter is not in the node, return false
            if letter not in node:
                return False
            # otherwise update the node to the letter so the next letter can be searched
            node = node[letter]
        # once you've found all letters, assert that the endSymbol is in the node.
        # if it is, the method returns True, otherwise if it isn't, it means that the string
        # is not a suffix - instead it's a prefix and the method will return False.
        return self.endSymbol in node
            

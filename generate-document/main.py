# O(n + m) time | O(c) space
# where n is the number of characters, m is the length of the document and c is the number
# of unique characters in the characters string
def generateDocument(characters, document):
    # create a cache
    characterCounts = {}

    # for each character, if not in the cache add it and then increment its count by 1
    for char in characters:
        if char not in characterCounts:
            characterCounts[char] = 0
        
        characterCounts[char] += 1

    # for each char in the document, if it's not in the cache or it's already at count zero
    # then return false because the document cannot be made using the given characters
    for char in document:
        if char not in characterCounts or characterCounts[char] == 0:
            return False

        # once a character has been used, decrement its count in the cache
        characterCounts[char] -= 1

    # if it gets this far, all characters are present in cache with enough count to generate the doc
    return True
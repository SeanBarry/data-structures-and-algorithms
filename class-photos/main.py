# O(nlog(n)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] == blueShirtHeights[0]:
        return False

    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(0, len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False

    if blueShirtHeights[0] < redShirtHeights[0]:
        for i in range(0, len(blueShirtHeights)):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False

    return True



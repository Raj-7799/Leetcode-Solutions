from collections import defaultdict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charLookup = defaultdict(int)
        finalSum = 0
        for c in list(chars):
            charLookup[c] += 1

        for word in words:
            wordDict = defaultdict(int)
            good = True
            for w in list(word):
                wordDict[w] += 1

                if not (w in charLookup and wordDict[w] <= charLookup[w]):
                    good = False
                    break

            if good:
                finalSum += len(word)

        return finalSum

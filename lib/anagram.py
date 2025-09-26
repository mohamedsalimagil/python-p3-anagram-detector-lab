# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)  # we can reuse this

        for candidate in candidates:
            cand_lower = candidate.lower()

            # skip identical words
            if cand_lower == self.word:
                continue

            # check if anagram
            if sorted(cand_lower) == sorted_word:
                matches.append(candidate)

        return matches


# test run
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))



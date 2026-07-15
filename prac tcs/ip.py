class Neel:
    def vowel(self, word, left, right):
        ref = "aeiouAEIOU"
        c = 0

        for i in range(left, right + 1):
            if word[i][0] in ref and word[i][-1] in ref:
                c += 1

        return c

w=Neel()
print(w.vowel())
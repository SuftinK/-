class Tablo():

    def __int__(self, word: str):
        self._word = word

    def __str__(self):
        """ this method will print the word itself"""
        return f"The word is {self._word}"


w = Tablo("Hello")
print(w)

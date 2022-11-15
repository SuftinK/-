class Tablo:
    def __init__(self, word : str) -> None:
        self._word = word
        self._unick_letters = list(set(word))
        self._letter = ""

    def __str__(self):
        return f'{self._word} have unick letters {self._unick_letters}, the letter is {self._letter}'

    def unick_let_setter(self, let:str):
        #self._unick_letters = list(set(let))
        let_dict = dict()
        word_copy = list(self._word)[:]
        for i in range(0, len(self._word) + 1):
            print(i, word_copy[i])
            let_dict[word_copy[i]] = let_dict.get(word_copy[i], list())
            let_dict[word_copy[i]].append(i)

            print(let_dict)

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, let) -> None:
        self._word = let

    @property
    def letter(self) -> str:
        return self._letter

    @letter.setter
    def letter(self, l) -> None:
        if isinstance(l, str) and l.isalpha() and len(l) == 1:
            self._letter = l
        else:
            raise TypeError('The letter should be typed in letters and lenght should be 1 ch ')

Tablo = Tablo('hello')
print(Tablo)
# Tablo.letter = "h"
# Tablo.word = "red"
Tablo.unick_let_setter("reddick")
print(Tablo)
class Tablo:
    def __init__(self, word : str) -> None:
        self._word = word.upper()
        self._letter = ""
        self._hidden = "*" * len(self._word)
        let_dict = dict()
        word_copy = list(self._word)[:]
        for i in range(0, len(self._word)):
            print(i, word_copy[i])
            let_dict[word_copy[i]] = let_dict.get(word_copy[i], list())
            let_dict[word_copy[i]].append(i)
        print(let_dict)

    def __str__(self):
        return f'{self._word} The hidden word is: {self._hidden}, the letter is {self._letter}'

    # def letters_and_indexs(self):
    #
    #     let_dict = dict()
    #     word_copy = list(self._word)[:]
    #     for i in range(0, len(self._word)):
    #         print(i, word_copy[i])
    #         let_dict[word_copy[i]] = let_dict.get(word_copy[i], list())
    #         let_dict[word_copy[i]].append(i)
    #
    #         print(let_dict)

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

T = Tablo('hello')
print(T)
T2 = Tablo('Carshearing')
print(T2)
# Tablo.letter = "h"
# Tablo.word = "red"
# Tablo.letters_and_indexs()

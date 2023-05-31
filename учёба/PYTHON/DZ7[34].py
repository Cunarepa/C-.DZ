vowel_letters = set("аяуюоеёэиы")

def count_Puh_rithm(sentence, isfullinf="Пам парам"):
    counters = set()
    fullinf = []
    for idx, phrase in enumerate(sentence.split()):
        vowel_letters_count = 0
        fullinf.append({})
        for letter in phrase:
            if letter in vowel_letters:
                vowel_letters_count += 1
                if letter in fullinf[idx]:
                    fullinf[idx][letter] += 1
                else:
                    fullinf[idx][letter] = 1
        counters.add(vowel_letters_count)
        if len(counters) != 1:
            if isfullinf:
                return "Пам парам", fullinf
            else:
                return "Пам парам"
    if isfullinf:
        return "Парам пам-пам", fullinf
    else:
        return "Парам пам-пам"

print(count_Puh_rithm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(count_Puh_rithm("пара-ра-рам рам-пум-пупам па-ре-по-дам", True))
print(count_Puh_rithm("пара-ра-рам рам-пуум-пупам па-ре-по-дам", True))

print(count_Puh_rithm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па", True))
print(count_Puh_rithm("Пам-парам-пурум Пум-пурум-карам", True))


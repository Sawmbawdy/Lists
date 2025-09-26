def match_words(words):
    counter = 0
    output = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            counter += 1
            output.append(word) 

    print("List of words that match the criteria where the first and last character are the same:", output)
match_words(['abc', 'xyz', 'aba', '1221'])    
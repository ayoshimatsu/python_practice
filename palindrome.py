from collections import defaultdict
from collections import Counter

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    print(sorted(w1))
    print(sorted(w2))
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf123", "tree123"))

def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)
    return count_dict

result = count_characters("Dynasty")
print(result.get("D"))

print(Counter("Dynasty"))
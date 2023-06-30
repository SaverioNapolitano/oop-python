# Comprehension

**[filter_odd.py]** Use a list comprehension to filter odd numbers in a list. 

Suppose the following input is supplied to the program: [1,2,3,4,5,6,7,8,9]. Then, the output should be: [1,3,5,7,9].

---

**[list_to_tuple.py]** Write a program to generate a list whose values are the first 50 even numbers. Then, transform the list into a tuple using tuple().

---

**[strings_to_integers.py]** Write a program to get a list of strings and create a list of integers. Each self represents the length of each initial string.

---

**[random_from_list.py]** Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 200 inclusive using random module and list comprehension. Use random.choice() to a random element from a list.

---

**[remove_numbers.py]** By using list comprehension, please write a program to print a given list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

---

**[sort_words_no_dup.py]** Write a program that accepts a sequence of white space separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program: 'hello world and practice makes perfect and hello world again'

Then, the output should be: 'again and hello makes perfect practice world'

---

**[lengths.py]** Rewrite the following code using list comprehension.
```Python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)
```

---

**[remove_indexes.py]** By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th, 6th numbers in [12,24,35,70,88,120,155]. Use list comprehension to delete a bunch of elements from a list. Use enumerate() to get (index, value) tuple.
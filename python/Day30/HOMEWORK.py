# Python
# List Comprehension Practice Questions Solutions

# 1. Create a list of squares of numbers from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print("1. Squares of numbers from 1 to 10:", squares)


#====================================================================================================

# 2. From the list nums = [3, 7, 10, 15, 22, 8, 13], create a new list containing only even numbers.
nums_2 = [3, 7, 10, 15, 22, 8, 13]
even_num = [num for num in nums_2 if num % 2 == 0]
print("2. Even numbers:", even_num)


#=====================================================================================================

# 3. Convert all words in the list words = ['python', 'data', 'science', 'ai'] to uppercase.
words_3 = ['python', 'data', 'science', 'ai']
uppercase_words = [word.upper() for word in words_3]
print("3. Uppercase words:", uppercase_words)


#=======================================================================================================

# 4. Create a list containing the length of each word in words = ['apple', 'banana', 'mango', 'kiwi'].
words_4 = ['apple', 'banana', 'mango', 'kiwi']
word_lengths = [len(word) for word in words_4]
print("4. Length of each word:", word_lengths)


#========================================================================================================

# 5. From the list nums = [5, 12, 7, 18, 3, 25, 10], create a new list containing numbers greater than 10.
nums_5 = [5, 12, 7, 18, 3, 25, 10]
greater_than_10 = [num for num in nums_5 if num > 10]
print("5. Numbers greater than 10:", greater_than_10)


#=========================================================================================================

# 6. Create a list containing the first letter of each word in words = ['machine', 'learning', 'deep', 'python'].
words_6 = ['machine', 'learning', 'deep', 'python']
first_letters = [word[0] for word in words_6]
print("6. First letter of each word:", first_letters)


#=============================================================================================================

# 7. From the list nums = [1,2,3,4,5,6], create a new list that stores 'Even' or 'Odd' for each number.
nums_7 = [1, 2, 3, 4, 5, 6]
even_odd_list = ['Even' if num % 2 == 0 else 'Odd' for num in nums_7]
print("7. Even or Odd list:", even_odd_list)

#=============================================================================================================


# 8. From the string 'datascience', create a list of characters excluding vowels.
string_8 = 'datascience'
consonants = [char for char in string_8 if char not in 'aeiou']
print("8. Characters excluding vowels:", consonants)

#============================================================================================================


# 9. Create a list of multiples of 3 from 1 to 30.
multiples_of_3 = [i for i in range(1, 31) if i % 3 == 0]
print("9. Multiples of 3:", multiples_of_3)

#============================================================================================================

# 10. Create all possible pairs using list1 = [1,2,3] and list2 = ['a','b'].
list1_10 = [1, 2, 3]
list2_10 = ['a', 'b']
all_pairs = [(x, y) for x in list1_10 for y in list2_10]
print("10. All possible pairs:", all_pairs)













# VS Code Terminal Output
# bhartii@LAPTOP-XYZ:~/python_projects$ python list_comprehension_answers.py
# 1. Squares of numbers from 1 to 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 2. Even numbers: [10, 22, 8]
# 3. Uppercase words: ['PYTHON', 'DATA', 'SCIENCE', 'AI']
# 4. Length of each word: [5, 6, 5, 4]
# 5. Numbers greater than 10: [12, 18, 25]
# 6. First letter of each word: ['m', 'l', 'd', 'p']
# 7. Even or Odd list: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
# 8. Characters excluding vowels: ['d', 't', 's', 'c', 'n', 'c']
# 9. Multiples of 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 10. All possible pairs: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
# bhartii@LAPTOP-XYZ:~/python_projects$
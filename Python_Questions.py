# # type_of_currency = {
# #     'BTC': [{'asset': 'bitcoin', 'usd': '30000'}]
# # }

# # key_of_crypto = 'BTC'
# # asset_of_crypto = 'bitcoin'
# # required_value = 'usd'

# # type_rate = [{'symbol': 'USDINR', 'rate': '83.2'}]
# # symbol_rate = 'USDINR'
# # required_rate = 'rate'

# class amount_calculations:
#     @staticmethod
#     def crypto_exchange_value(type_of_currency,key_of_crypto,asset_of_crypto,required_value,type_rate,symbol_rate,required_rate):
#         for i in type_of_currency[key_of_crypto]:
#             if i['asset']== asset_of_crypto:
#                 result1=(i[required_value])
#                 print(result1)
#         for i in type_rate:
#             if i['symbol']==symbol_rate:
#                 result2 = i[required_rate]
#                 print(result2)

# #         result3 = float(result1)*float(result2)
# #         print(result3, "amount")
# #         return result3
    
# # amount_calculations.crypto_exchange_value(
# #     type_of_currency,
# #     key_of_crypto,
# #     asset_of_crypto,
# #     required_value,
# #     type_rate,
# #     symbol_rate,

# # def word_count(paragraph_words):
# #     output = dict()
# #     words_list = paragraph_words.split()
# #     for i in words_list:
# #         if i in output:
# #             output[i] +=1

# #         else:
# #             output[i] = 1
# #         print(output)

# #     return output

# # print(word_count('the quick brown box python for jumps over python the lazy dog ans python'))

# # def word_count(paragraph_words):
# #     output = dict()
# #     words_list = paragraph_words.split()
# #     for i in words_list:
# #         if i in output:
# #            output[i] += 1
# #         else:
# #             output[i] = 1
# #         print(output)

# #     return(output)

# # print(word_count('the quick fix'))


# # def find_largest_number(numbers):
# #     largest_number = max(numbers, default=None)
# #     return largest_number

# # number_list = [3,8,1,5,9,303, 5]
# # result = find_largest_number(number_list)
# # print("The largesr_number is:", result)


# # def reverse_string(input_string):
# #     reversed_string = input_string[::-1]
# #     return reverse_string


# # def reverse_string(input_string):
# #     words = list(input_string)
# #     i, j = 0, len(words) - 1
# #     while i < j:
# #         words[i], words[j] = words[j], words[i]
# #         i +=1 
# #         j -=1

# #     reverse_string= ''.join(words)

# #     return reverse_string

# # original_string = "Hello, Terence"
# # reverse_result = reverse_string(original_string)
# # print("Original_String:", original_string)
# # print("Reversed_ String:", reverse_result)


# import decimal
# integer = 10
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

# import decimal
# string = '12345'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))

# string = "python Programming"
# print(string[::-1])

# vowel = ['a', 'e','i', 'o','u']
# word = "programming"
# count = 0
# for character in word:
#     if character in vowel:
#         count +=1
# print(count)
      
# vowel = ['a', 'e', 'i, 'o', 'i', 'u']
# words = "programming"
# count = 0
# for word in words:
#     if word not in vowel:
# #         count += 1
# # print(count)

# word = "programming"
# character = 'g'
# count = 0
# for i in word:
#     if i == character:
#         count+=1
# print(count, 'g is this time')

# fib = [0,1]
# n=5
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])

# print( ','.join(str(e) for e in fib))



# numberList = [12,3,35,23,6,78,33,4]
# max = numberlist[0]
# for num in numberList:
#     if max < num:
#         max = num
# print(max)



# numList= [12,3,66,23,7,78,33,5]
# m = int(len(numList)/2)
# print(numList[m])



# list = ["P","Y", "T", "H", "O", "N"]
# string = "".join(list)
# print(string)
# print(type(string))

# list = [1,2,3]
# list2 = [4,5,6]
# margeList = []
# for i in range(0, len(list)):
#     margeList.append(list[i]+list2[i])
# print(margeList)

# str1 = "listen"
# str2 = "Silent"
# str1 = str1.replace("","").upper()
# str2 = str2.replace("","").upper()
# if sorted(str1) == sorted(str2):
#     print("True")
# else:
#     print("False")


# str1 = "kayak".lower()
# if str1 == str1[::-1]
#      print("True")
# else:
#      print("False")

# string = "P  r  ogram  in  g"
# print(string.count(" "))
                    
#counting digits, letters, and spaces in a String

# import re
# name = 'Python is 1'
# digitcount = re.sub("[^0-9","",name)
# lettercount = re.sub("[^a-zA-z]","",name)
# spacecount= re.findall("[\s", name)

# print(len(digitcount))
# print(len(lettercount))
# print(len(spacecount))


# def count_sp_char(string):
#     sp_char = "!@#$%6&*()<>?/\[]{};:~`"
#     count = 0
#     for i in string:
#         if i in sp_char:
#             count+=1
#     return count


# string = 'Hello! How are you? #specialchars! 123'
# result = count_sp_char(string)
# print(result)

#removing all the whitespaces in a string
# import re
# string = "C O D E"
# spaces = re.compile(r'\s+')
# result = re.sub(spaces, "", string)
# print(result)


# string = "C O D E"
# string2 = "".join(char for char in string if char !=" ")
# print(string2)



# string = 'C O D E'
# string2 = string.replace(" ","")
# print(string2)


#Randomizing the items of a list in python
# from random import shuffle
# lst = ['Python', 'is', 'fuckimg', 'good']
# shuffle(lst)
# print(lst)

#create generator to product first n prime numbers

# def isprime(num):
#      for i in range(2, num):
#           if num%1 == 0:
#                return False
#      return True

# def prime_generator(n):
#      num = 2
#      while n:
#           if isprime(n):
#                '''
#                #yield keyword used to return a value and then the code is resumed'''

#                yield num
#                n-=1
#           num+=1

# x =int(input("Enter no of prime numbers required"))
# it = prime_generator(x)
# for e in it:
#      print(e, end=" ")

# def prime(n):
#     Flag = False
#     if n< 2:
#         return Flag
#     else:
#         for i in range(2, n):
#             if n%i==0:
#                 return Flag
#             else:
#                 Flag = True
#                 return Flag
    
# num = int(input("Enter a number:"))
# prime(num)

# def average(*t):
#     avg = sum(t)/len(t)
#     return avg
# result1 = average(32,5,65,22,87,34,2,57)
# result2 = average(5,10,15,20,25,30,35,40,45,50)

# print("Average is:", result1)
# print("Average is:", result2)



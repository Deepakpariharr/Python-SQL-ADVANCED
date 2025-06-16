# type_of_currency = {
#     'BTC': [{'asset': 'bitcoin', 'usd': '30000'}]
# }

# key_of_crypto = 'BTC'
# asset_of_crypto = 'bitcoin'
# required_value = 'usd'

# type_rate = [{'symbol': 'USDINR', 'rate': '83.2'}]
# symbol_rate = 'USDINR'
# required_rate = 'rate'

class amount_calculations:
    @staticmethod
    def crypto_exchange_value(type_of_currency,key_of_crypto,asset_of_crypto,required_value,type_rate,symbol_rate,required_rate):
        for i in type_of_currency[key_of_crypto]:
            if i['asset']== asset_of_crypto:
                result1=(i[required_value])
                print(result1)
        for i in type_rate:
            if i['symbol']==symbol_rate:
                result2 = i[required_rate]
                print(result2)

#         result3 = float(result1)*float(result2)
#         print(result3, "amount")
#         return result3
    
# amount_calculations.crypto_exchange_value(
#     type_of_currency,
#     key_of_crypto,
#     asset_of_crypto,
#     required_value,
#     type_rate,
#     symbol_rate,

# def word_count(paragraph_words):
#     output = dict()
#     words_list = paragraph_words.split()
#     for i in words_list:
#         if i in output:
#             output[i] +=1

#         else:
#             output[i] = 1
#         print(output)

#     return output

# print(word_count('the quick brown box python for jumps over python the lazy dog ans python'))

# def word_count(paragraph_words):
#     output = dict()
#     words_list = paragraph_words.split()
#     for i in words_list:
#         if i in output:
#            output[i] += 1
#         else:
#             output[i] = 1
#         print(output)

#     return(output)

# print(word_count('the quick fix'))


# def find_largest_number(numbers):
#     largest_number = max(numbers, default=None)
#     return largest_number

# number_list = [3,8,1,5,9,303, 5]
# result = find_largest_number(number_list)
# print("The largesr_number is:", result)


# def reverse_string(input_string):
#     reversed_string = input_string[::-1]
#     return reverse_string


def reverse_string(input_string):
    words = list(input_string)
    i, j = 0, len(words) - 1
    while i < j:
        words[i], words[j] = words[j], words[i]
        i +=1 
        j -=1

    reverse_string= ''.join(words)

    return reverse_string

original_string = "Hello, Terence"
reverse_result = reverse_string(original_string)
print("Original_String:", original_string)
print("Reversed_ String:", reverse_result)




















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

def word_count(paragraph_words):
    output = dict()
    words_list = paragraph_words.split()
    for i in words_list:
        if i in output:
           output[i] += 1
        else:
            output[i] = 1
        print(output)

    return(output)

print(word_count('the quick fix'))


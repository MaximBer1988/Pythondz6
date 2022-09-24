
text_1 = 'Мы неабв очень любим Питон иабв Джавуабв!'
# output_text = []
  
# input_text = text_1.split()
# print(input_text)
# for i in range(0, len(input_text)):
#     if 'абв' not in input_text[i]:
#         print(input_text[i], end=" ")
# print()        
        
       
print (' '.join(filter(lambda x: not 'абв' in x,text_1.split())))

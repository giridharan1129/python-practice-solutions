jewel=input('enter jewel :')
stones=input('enter stones :')
def count_jewels_in_stones(jewel, stones):
    count_jewels_in_collection = 0

    for element in jewel:
        for item in stones:
            if element == item:
                count_jewels_in_collection += 1
    return count_jewels_in_collection

print(count_jewels_in_stones(jewel, stones))
# def jewelStones(jewel,stones):
#     count=0
#     for i in stones:
#         if i in jewel:
#             count+=1
#     return count
  
# print(jewelStones(jewel,stones))        
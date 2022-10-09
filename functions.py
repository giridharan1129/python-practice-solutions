#wirte a program that returns fizz when divisible by 3 and buzz when divisible by 5 and fizzbuzz when divisibe by both and the same number when divisible by none
def fizz_buzz(input):
    if input%3 == 0 and input%5 !=0:
        return 'fizz'
    elif input%5 ==0 and input%3 !=0:
        return 'buzz'
    elif input%15==0:
        return 'fizzbuzz'
    return input        
print(fizz_buzz(11))

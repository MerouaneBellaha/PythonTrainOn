class FizzBuzzUtils(object):

    def isMultipleOf(n1, n2):
        return n2 % n1 == 0

    def parse(input):
        inputList = input.read().splitlines() 
        return list(map(int, inputList))
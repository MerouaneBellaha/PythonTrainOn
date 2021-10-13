import fizzBuzzUtils

class FizzBuzz(object):
    
    utils = fizzBuzzUtils.FizzBuzzUtils

    @classmethod
    def exec(self, res, list):

        for n in list:
            if self.utils.isMultipleOf(3, n) and self.utils.isMultipleOf(5, n):
                res.write('fizzBuzz\n')
            elif self.utils.isMultipleOf(3, n):
                res.write('fizz\n')
            elif self.utils.isMultipleOf(5, n):
                res.write('buzz\n')
            else:
                res.write(str(n)+'\n')

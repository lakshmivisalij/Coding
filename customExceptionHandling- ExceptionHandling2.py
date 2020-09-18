class ZeroDenominatorError(Exception):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError('This goes into message of init method of the exception class inherited in above class ZeroDenominatorError') 
    c = a/b
except ZeroDivisionError:
    print('Zero Division Error occured')
except ZeroDenominatorError:
    print('Zero as denominator, so custom exception raised!')
    
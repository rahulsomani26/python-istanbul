# def test(*a):
#     print(len(a))


# test('rahul', 'somani', 'ali', 'mohammad')


'''
  Key word argument   
'''


def myFirstKeywordArgFun(fruit1, fruit2, fruit3):
    print(fruit1, fruit2, fruit3)


myFirstKeywordArgFun(fruit2='apple', fruit1='orange', fruit3='banana')


'''
  Arbitrary number of keyword argument
  **kwargs
'''


def keywordFuntion(**kwargs):
    print(kwargs)
    print(*kwargs)
    print(kwargs["lname"])


keywordFuntion(fname='Ali', lname='mohammand')

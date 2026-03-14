# вариант 1
def repeat_me1(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)
        print("finished 1 test")

    return wrapper


@repeat_me1
def example(text):
    print(text)


example('print me', count=2)


# 2й вариант
def repeat_me2(**kwargs):
    count = kwargs["count"]

    def decoration(fun):
        def wrapper(text):
            for i in range(count):
                fun(text)
            print("finished 2 test")

        return wrapper

    return decoration


@repeat_me2(count=2)
def example(text):
    print(text)


example('print me')

something = "Hello World!"
iterable_obj = iter(something)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration as error:
        print(error)
        break

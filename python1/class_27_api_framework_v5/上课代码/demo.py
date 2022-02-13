a = "yuz"
a = a.replace('u','z')
print(a)


print("a + b = {}".format('c'))
print("xioafeng is {}".format({"name":"xiaofeng"}))
print(f"a + b = {a}")

class DemoA:
    def __str__(self):
        return "demo aaaa"
print("demo a :{}".format(DemoA()))
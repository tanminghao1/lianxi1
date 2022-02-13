def make_pizza(size,*args):
    print(f"制作一个{size}寸的披萨，需要加以下配料：")
    for arg in args:
        print(arg)
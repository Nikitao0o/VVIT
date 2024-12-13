class D():
    def __init__(self, *args):
        for i in range(len(args)):
            exec(f'self.f{i} = args[{i}]')

d = D(100, 200, 300)

print(d.f0, d.f1, d.f2)

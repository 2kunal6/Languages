class parent:
    def __init__(self):
        pass

    def show(self):
        print('parent')

class child(parent):
    def __init__(self):
        pass

    def show(self):
        print('child')

parent_obj = parent()
child_obj = child()

print(parent_obj.show())
print(child_obj.show())

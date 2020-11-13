class Button:
    def __init__(self, name=None, func = None):
        self.name = name
        self.clicked_num = 0
        if type(func).__name__ != 'function':
            raise TypeError("parameter `func` has to be type function")
        else:
            self.func = func

    def __call__(self):
        return {"name": self.name, "clicked": self.clicked_num}

    def click(self):
        print("Click!")
        self.func()
        self.clicked += 1

    def clicked(self):
        return "Click! " * self.clicked_num


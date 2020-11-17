class Button:
    def __init__(self, name='Button', func=None):
        self.name = name
        self.clicked_num = 0
        if type(func).__name__ == 'function' or func is None:  # workaround bc func is optional
            self.func = func
        else:
            self.func = func
            raise TypeError("parameter `func` has to be type function")

    def __call__(self, output=True):  # prints or returns info about itself when called
        data = {"name": self.name, "clicked": self.clicked_num}
        if output:
            print('\n'.join([f"{x} = {data[x]}" for x in data]))
        else:
            return data

    def click(self):
        print("Click!")
        if self.func is not None:  # executes passed in function
            self.func()
        self.clicked_num += 1

    def clicked(self):
        return "Click! " * self.clicked_num


class Slider:
    def __init__(self, name='Slider', s_min: int = 0, s_max: int = 100, starting_value: int = 50):
        self.name = name
        self.value = starting_value
        self.s_max = s_max
        self.s_min = s_min

    def __add__(self, other):
        self.value += other

    def __sub__(self, other):
        self.value -= other

    def slide_to(self, value: int):
        self.value = value

    def slide(self, value):
        self.value += value

    def __call__(self, output=True):
        data = {"min": self.s_min,
                "max": self.s_max,
                "value": self.value,
                "name": self.name}
        if output:
            print('\n'.join([f"{x} = {data[x]}" for x in data]))
        else:
            return data


def on_click():
    print("This is a function")  # we can specify which functions to use onclick!


button = Button(func=on_click)
for _ in range(3):
    button.click()

print("Calling button!")
button()


print("\n\n\n------Starting slider section-------\n\n\n\n")

myslider = Slider(s_min=-50,
                  s_max=50,
                  starting_value=0
                  )

myslider.slide_to(int(input("What would you like to set the value to?")))
print(myslider.value)





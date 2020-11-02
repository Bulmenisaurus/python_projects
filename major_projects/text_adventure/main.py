from time import sleep as wait
import random                        # for everything random and unexpected
import pickle                        # loading, and saving game data


class Player:
    def __init__(self, name: str = 'xX Ashius Ketchumuni Xx', money_dict=None,
                 xp: float = 0, lvl: int = 1, luck: int = 50, age: float = -100):
        if money_dict is None:
            money_dict = {'coins': 0}
        self.name = name
        self.money = money_dict
        self.xp = xp
        self.lvl = lvl
        self.luck = luck
        self.age = age

    def pickle_save(self, hide: bool = True) -> None:
        """Save data to save_data[0]. Pickle is so useful!"""
        variables = ['self.name', 'self.money', 'self.xp', 'self.lvl', 'self.luck', 'self.age']
        to_pickle = {}
        for var in variables:
            to_pickle[var] = eval(var)

        with open("save_data[0]", "wb") as pickle_save:
            pickle.dump(to_pickle, pickle_save)
        if not hide:
            print("Succesfully saved!")

    def pickle_load(self, hide: bool = True) -> None:
        """Load saved file, (save_data[0])"""
        with open("save_data[0]", "rb") as pickle_load:
            un_pickle = pickle.load(pickle_load)

        variables = [x + " = " + repr(un_pickle[x]) for x in un_pickle]
        exec('\n'.join(variables))
        if not hide:
            print("Loading done!")

    def give_xp(self, amount: float, display: bool = False) -> None:
        if self.lvl == 100:
            return
        lvl_requirements = [round(lvl**1.5, 1) for lvl in range(100)]
        self.xp += amount
        while self.xp > lvl_requirements[self.lvl]:
            self.xp -= lvl_requirements[self.lvl]
            self.lvl += 1
            print("Congrats! You lvled up to level ", self.lvl)
            print(f"{self.xp=}")

            if self.lvl == 100:
                return


class Game:
    def __init__(self, map_len: int = 10_000, progress: int = 0,
                 curr_city: str = ''):
        self.map_len = map_len
        self.all_cities = ()
        self.progress = progress
        self.curr_city = curr_city

    def pickle_save(self, hide: bool = True) -> None:
        """Save data to save_data[1]. Pickle is so useful!"""
        variables = ['self.map_len', 'self.all_cities',
                     'self.progress', 'self.curr_city',
                     'self.all_cities', ]
        to_pickle = {}
        for var in variables:
            to_pickle[var] = eval(var)

        with open("save_data[1]", "wb") as pickle_save:
            pickle.dump(to_pickle, pickle_save)
        if not hide:
            print("Succesfully saved!")

    def pickle_load(self, hide: bool = True) -> None:
        """Load saved file, (save_data[0])"""
        with open("save_data[1]", "rb") as pickle_load:
            un_pickle = pickle.load(pickle_load)

        variables = [x + " = " + repr(un_pickle[x]) for x in un_pickle]
        exec('\n'.join(variables))
        if not hide:
            print("Loading done!")

    def travel(self, amount: int, encounters: bool) -> None:
        self.progress += amount
        if encounters and random.randint(1, 6) != 6:
            print("encounter")
            self._encounter()

    def _encounter(self):
        encounter_types = {'battle': 10, 'village': 3, 'landform': 5, 'treasure': 4}
        encounter_type = random.choice(list(encounter_types))
        encounter = encounter_type, random.randint(0, encounter_types[encounter_type])
        print(encounter)

    def create_map(self):
        self.all_cities = ['' for _ in range(random.randint(3, 6))]





def create_player() -> Player:
    print("Would you like to bother fiddling with selections? [Y/N]")
    if input().upper() == 'Y':
        play = Player(
            input("Ho ho ho. What is your name?\n"),
            lvl=1,
            luck=random.randint(35, 100),
            age=int(input("How old are you?"))
        )
        print("kthbai")
        return play
    else:
        print("Wow, lazybones.")
        return Player()


user = create_player()
print(user.name)
adventure = Game()
adventure.travel(100, True)

print(Exception)


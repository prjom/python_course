print('Задание№4')

class Apple:
    STAGES = ["цветение", "зеленое", "красное"]

    def __init__(self, index):
        self.index = index
        self.stage = self.STAGES[0]

    def ripen(self):
        current_stage_index = self.STAGES.index(self.stage)
        if current_stage_index < len(self.STAGES) - 1:
            self.stage = self.STAGES[current_stage_index + 1]

    def is_ripe(self):
        return self.stage == self.STAGES[-1]

class Tree:
    def __init__(self, *apples):
        self.apples = list(apples)

    def grow(self):
        for apple in self.apples:
            apple.ripen()

    def all_apples_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def harvest(self):
        if self.all_apples_ripe():
            self.apples = []
            print("Урожай собран.")
        else:
            print("Не все яблоки созрели. Урожай не может быть собран.")

class Gardener:
    def __init__(self, name, *trees):
        self.name = name
        self.trees = list(trees)

    def take_care(self):
        for tree in self.trees:
            tree.grow()

    def harvest_all(self):
        if all(tree.all_apples_ripe() for tree in self.trees):
            for tree in self.trees:
                tree.harvest()
        else:
            print("Не все яблоки созрели. Урожай не может быть собран.")

apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)

tree = Tree(apple1, apple2, apple3, apple4, apple5)

gardener = Gardener("Олег", tree)

gardener.take_care()

gardener.harvest_all()

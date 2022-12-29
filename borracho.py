import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

class Drogado(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return (
            random.choice([
                (random.random(), random.random() * -1),
                (random.random() * -1, random.random()),
                (random.random() * -1, random.random() * -1),
                (random.random(), random.random()),
            ])
        )

        
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        # return random.choice([(9, 33), (55, 77), (75, 47), (3, 55)])
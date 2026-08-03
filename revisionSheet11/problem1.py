class TwoVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"This is for 2D having dimenssion {self.i} + {self.j}")


class ThreeVector(TwoVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"This is for 3D having dimenssion {self.i} + {self.j} + {self.k}")


a = TwoVector(1, 2)
a.show()
b = ThreeVector(5, 2, 3)
b.show()
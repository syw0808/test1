class C:
    def __init__(self):
        print("class C의 인스턴스가 생성됨")
        self.name="ccc"
        self.age=0
    def say_hi(self):
        print("hi")


    def add_age(self, n:int):
        self.age+=n
    def __str__(self):
        return "__str__ 호출됨"
    def __repr__(self):
        return "__repr__호출됨"
    def __abs__(self):
        return "__abs___호출됨"

    def __len__(self):
        return "__len__호출됨"
    def __add__(self, other):
        return self.age + other.age

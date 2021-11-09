class Man:
    def __init__(self, id, FIO, birthyear, numGroup):
        self.id = id
        self.FIO = FIO
        self.birthyear = birthyear

class Student(Man)
    def __init__(self, id, FIO, birthyear, numGroup):
        Man.__init__(self, id, FIO, birthyear)
        self.numGroup = numGroup

class Teacher(Man)
    def __init__(self, id, FIO, birthyear, numGroup):
        Man.__init__(self, id, FIO, birthyear)
        self.numGroup = numGroup


class Person(object):
    total = 0

    def __init__(self, name, age):  # 기본 생성자 (self) / 오버로딩
        self.name=name
        self.age=age
    def getAge(self):
        return self.age
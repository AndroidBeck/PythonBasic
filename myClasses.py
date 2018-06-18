# -*- coding: cp1251 -*-
# РУсские комменты вкл
__author__ = 'Evdokimov'

class Monster:
    class_name = ""

    def __init__(self, name, desc):
        self.name=name
        self.desc=desc


class Goblin (Monster):
    class_name = "goblin"
    def __init__(self, name, desc):
        self.name=name
        self.desc=desc
        super.init(name,desc)
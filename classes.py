class pokemon:
    def __init__(self, name, level, health, type1, type2, move1, move2, move3, move4):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.health = health
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
    def lvlUp(self):
        self.level +=1
        print(self.name,"leveled up to level",str(self.level)+"!")
    def fight_intro(self):
        print("You sent out",str(self.name)+"!")
    def retreat(self):
        print("You brought back",str(self.name)+"!")

class move:
    def __init__(self, name, type, damage, pp, effects):
        self.name = name
        self.type = type
        self.damage = damage
        self.pp = pp
        self.effects = effects
    def use(self,enemy):
        print("You used",str(self.name)+"!")
        if self.damage>0:
            print("It dealt",str(self.damage)+" damage to",str(enemy.name)+"!")
            enemy.health -= self.damage
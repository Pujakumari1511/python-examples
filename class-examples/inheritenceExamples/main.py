from enemy import Enemy, Troll, Vampyre, VampyreKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)
brother.take_damage(3)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vampyre("Poo")
print("new_vampyre - {}".format(vamp))

vamp.take_damage(4)
print(vamp)

another_vamp = Vampyre("Akash")
print("another_vamp - {}".format(another_vamp))
another_vamp.take_damage(3)

print("*" * 40)

another_troll.take_damage(35)
print(another_troll)


vamp._live = 0
vamp._hit_points = 1
print(vamp)

king = VampyreKing("Piyush")
print("VampyreKing - {}".format(king))
king.take_damage(12)
print(king)

king.take_damage(15)
print(king)

king.take_damage(700)
print(king)

king.take_damage(15)
print(king)







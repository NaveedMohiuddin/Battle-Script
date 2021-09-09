import random

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Get:
    def __init__(self, hp, mp, shoot, attack, heal):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.shootl = shoot - 10
        self.shooth = shoot + 10
        self.attack = attack
        self.heal = heal
        self.action = ["SHOOT", "SPECIAL ATTACKS","HEAL"]

    def create_dmg(self):
        return random.randrange(self.shootl, self.shooth)

    def create_atk_dmg(self, i):
        atkl = self.attack[i]["dmg"] - 10
        atkh = self.attack[i]["dmg"] + 10
        return random.randrange(atkl, atkh)

    def create_heal(self, i):
        heall = self.heal[i]["points"] - 5
        healh = self.heal[i]["points"] + 5
        return random.randrange(heall, healh)

    def take_dmg(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_heal(self,heal):
        self.hp +=heal
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_max_mp(self):
        return self.max_mp
    def get_mp(self):
        return self.mp

    def get_atk_name(self, i):
        return self.attack[i]["name"]

    def get_action_name(self,i):
        return self.action[i]

    def get_atk_mp(self, i):
        return self.attack[i]["cost"]

    def get_heal_mp(self,i):
        return self.heal[i]["cost"]

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp <= 0:
            self.mp = 0
            return self.mp
        else:
            return self.mp

    def choose_action(self):
        i = 1
        print(bcolors.BOLD + bcolors.OKBLUE + "CHOOSE ACTION" + bcolors.ENDC)
        for items in self.action:
            print("      ",str(i) + ":", items)
            i += 1

    def choose_attack(self):
        i = 1
        print(bcolors.BOLD + bcolors.FAIL + "SPECIAL ATTACKS" + bcolors.ENDC)
        for spell in self.attack:
            print("      ",str(i) + ":", spell["name"], "(cost", str(spell["cost"]) + ")")
            i += 1

    def choose_heal(self):
        i=1
        print(bcolors.BOLD + bcolors.OKGREEN + "HEAL" + bcolors.ENDC)
        for items in self.heal:
            print("      ",str(i) + ":",items["name"], "(cost", str(items["cost"]) + ")","(health",str(items["points"]),")")
            i +=1

    def enemy_choice(self):
        low = 0
        high = 2
        return random.randrange(low, high)

    def get_stats1(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_ticks = ((self.get_hp()/self.get_max_hp())*100)//4
        mp_bar_ticks = ((self.get_mp()/self.get_max_mp())*100)//10
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -=1
        while len(hp_bar) < 25:
            hp_bar += " "
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -=1
        while len(mp_bar) < 10:
            mp_bar += " "
        print(bcolors.BOLD + "                      HEALTH_________________________    MAGIC POINTS__________" + bcolors.ENDC)
        print(bcolors.BOLD + "                    " + str(self.get_hp()) + "/" + str(self.get_max_hp()) + "|" +
              bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|" + bcolors.BOLD + "         " +str(self.get_mp()) + "/" +str(self.get_max_mp()) + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
        return " "

    def get_stats2(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_ticks = ((self.get_hp() / self.get_max_hp()) * 100) // 4
        mp_bar_ticks = ((self.get_mp() / self.get_max_mp()) * 100) // 10
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        print(
            bcolors.BOLD + "                      HEALTH_________________________    MAGIC POINTS__________" + bcolors.ENDC)
        print(bcolors.BOLD + "                    " + str(self.get_hp()) + "/" + str(self.get_max_hp()) + "|" +
              bcolors.FAIL + hp_bar + bcolors.ENDC + "|" + bcolors.BOLD + "         " + str(
            self.get_mp()) + "/" + str(self.get_max_mp()) + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
        return " "

    def enemy_atk_choice(self):
        l = 0
        h = 3
        return random.randrange(l, h)


attack = [{"name":"Bomb","cost":5,"dmg":75},
        {"name":"Laser","cost":15,"dmg":150},
        {"name":"Thunder","cost":10,"dmg":100}]

heal = [{"name":"Bandages","cost":2,"points":40},
      {"name":"Med kit","cost":20,"points":250}]
running=True
print("CHOOSE DIFFICULTY LEVEL")
print("1:EASY")
print("2:MEDIUM")
print("3:HARD")
level = int(input(""))
if level == 1:
    enemy = Get(650, 50, 40, attack, heal)
    player = Get(500, 60, 55, attack, heal)
    print("you have chosen EASY LEVEL")
elif level == 2:
    player = Get(500,60,50,attack,heal)
    enemy = Get(750,50,50,attack,heal)
    print("you have chosen MEDIUM LEVEL")
else:
    player = Get(500,50,50,attack,heal)
    enemy = Get(800,50,60,attack,heal)
    print("you have chosen HARD LEVEL")


print(bcolors.FAIL + bcolors.BOLD + "=============================================" + bcolors.UNDERLINE + "BATTLE STARTS"
      + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "===================================================" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKBLUE +"                            ***************************************"
                                   "*************                                       " + bcolors.ENDC)

print("YOUR:")
print(player.get_stats1())
print("ENEMY:")
print(enemy.get_stats2())

while running:
    print("====================================================================================\n")
    player.choose_action()
    choice=int(input(""))-1
    if choice == -1:
        continue

    if choice == 0:
        dmg=player.create_dmg()
        enemy.take_dmg(dmg)
        print("you shot for",dmg,"points of damage")
        print("YOUR:")
        print(player.get_stats1())
        print("ENEMY:")
        print(enemy.get_stats2())

    elif choice == 1:
        player.choose_attack()
        print("To go back enter 0")
        option = int(input(""))-1
        if option == -1:
            continue
        atk_dmg = player.create_atk_dmg(option)
        cost = player.get_atk_mp(option)
        if player.get_mp() <= cost:
            print(bcolors.FAIL + "you does not have Enough MAGIC POINTS" + bcolors.ENDC)
            continue
        enemy.take_dmg(atk_dmg)
        player.reduce_mp(cost)
        print("you attacked Enemy for",atk_dmg,"points.")
        print("YOUR:")
        print(player.get_stats1())
        print("ENEMY:")
        print(enemy.get_stats2())

    elif choice == 2:
        player.choose_heal()
        print("To go back enter 0")
        option = int(input(""))-1
        if option == -1:
            continue
        heal = player.create_heal(option)
        player_mp=player.get_heal_mp(option)

        if player.get_mp() < player_mp:
            print(bcolors.OKBLUE + "you does not have Enough MAGIC POINTS" + bcolors.ENDC)
            continue
        player.reduce_mp(player_mp)
        player.take_heal(heal)
        print("you have health has increased to" ,player.get_hp())
        print("YOUR:")
        print(player.get_stats1())
        print("ENEMY:")
        print(enemy.get_stats2())

    if enemy.get_hp() == 0:
        print(bcolors.OKBLUE + bcolors.BOLD + "               **********" + bcolors.UNDERLINE + "!!!YOU WON!!!" + bcolors.ENDC + bcolors.OKBLUE + bcolors.BOLD + "**********" + bcolors.ENDC)
        break
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "               **********" + bcolors.UNDERLINE + "$$ENEMY HAS DEFEATED YOU$$" + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "**********" + bcolors.ENDC)
        break

    print("--------------------------------------------------------------------------------------")
    run = True
    while run:
        enemy_choice = enemy.enemy_choice()
        if enemy.get_hp() < 200 and enemy.get_mp() >= 20:
            option = 1
            heal = enemy.create_heal(option)
            cost = enemy.get_heal_mp(option)
            enemy.reduce_mp(cost)
            enemy.take_heal(heal)
            print("Enemy has chosen to heal")
            print("YOUR:")
            print(player.get_stats1())
            print("ENEMY:")
            print(enemy.get_stats2())

        elif enemy_choice == 0:
            enemy_dmg = enemy.create_dmg()
            player.take_dmg(enemy_dmg)
            print("Enemy shot you for", enemy_dmg, "points.")
            print("YOUR:")
            print(player.get_stats1())
            print("ENEMY:")
            print(enemy.get_stats2())

        elif enemy_choice == 1:
            atk_choice = enemy.enemy_atk_choice()
            atk_dmg = enemy.create_atk_dmg(atk_choice)
            cost = enemy.get_atk_mp(atk_choice)
            if enemy.get_mp() <= cost:
                continue
            player.take_dmg(atk_dmg)
            enemy.reduce_mp(cost)
            print("Enemy has attacked you for",atk_dmg,"points")
            print("YOUR:")
            print(player.get_stats1())
            print("ENEMY:")
            print(enemy.get_stats2())
        run = False

    if enemy.get_hp() == 0:
        print(bcolors.OKBLUE + bcolors.BOLD + "               **********" + bcolors.UNDERLINE +"!!!YOU WON!!!" + bcolors.ENDC + bcolors.OKBLUE + bcolors.BOLD + "**********" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "               **********" + bcolors.UNDERLINE + "$$ENEMY HAS DEFEATED YOU$$" + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "**********" + bcolors.ENDC)
        running = False












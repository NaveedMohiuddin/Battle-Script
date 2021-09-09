# BATTLE SCRIPT(GAME)
# PROGRAM:
pink = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'

import random

player_hp=500
player_max_hp=500
enemy_max_hp=800
player_mp=50
player_max_mp=50
enemy_max_mp=50
enemy_mp=50
shoot=60
shootl = shoot-10
shooth=shoot+10
action = ["SHOOT", "SPECIAL ATTACKS", "HEAL"]
attack=[{"name":"Bomb","cost":5,"dmg":75},
        {"name":"Laser","cost":15,"dmg":150},
        {"name":"Thunder","cost":10,"dmg":100}]

heal=[{"name":"Bandages","cost":2,"points":40},
      {"name":"Med kit","cost":20,"points":250}]


def create_dmg():
    return random.randrange(shootl,shooth)


def reduce_player_hp(dmg):
    global player_hp
    player_hp -= dmg


def reduce_enemy_hp(dmg):
    global enemy_hp
    enemy_hp -= dmg


def create_atk_dmg(i):
    global attack
    atkl = attack[i]["dmg"] - 10
    atkh = attack[i]["dmg"] + 10
    return random.randrange(atkl, atkh)


def create_heal(i):
    global heal
    heall = heal[i]["points"] - 5
    healh = heal[i]["points"] + 5
    return random.randrange(heall,healh)


def take_player_dmg(dmg):
    global player_hp
    player_hp -= dmg
    if player_hp < 0:
        player_hp= 0
    return player_hp


def take_enemy_dmg(dmg):
    global enemy_hp
    enemy_hp -= dmg
    if enemy_hp < 0:
        enemy_hp= 0
    return enemy_hp


def take_player_heal(heal):
    global player_hp
    global player_max_hp
    player_hp +=heal
    if player_hp >= player_max_hp:
        player_hp = player_max_hp
    return player_hp


def take_enemy_heal(heal):
    global enemy_hp
    global enemy_max_hp
    enemy_hp +=heal
    if enemy_hp >= enemy_max_hp:
        enemy_hp = enemy_max_hp
    return enemy_hp


def get_atk_name(i):
    global attack
    return attack[i]["name"]


def get_action_name(i):
    global action
    return action[i]["name"]


def get_atk_mp(i):
    global attack
    return attack[i]["cost"]


def get_heal_mp(i):
    global heal
    return heal[i]["cost"]


def reduce_player_mp(cost):
    global player_mp
    player_mp -= cost
    if player_mp <= 0:
        player_mp = 0
        return player_mp
    else:
        return player_mp


def reduce_enemy_mp(cost):
    global enemy_mp
    enemy_mp -= cost
    if enemy_mp <= 0:
        enemy_mp = 0
        return enemy_mp
    else:
        return enemy_mp


def choose_action():
    global action
    i = 1
    print(blue + bold + "CHOOSE ACTION" + end)
    for items in action:
        print("      ",str(i) + ":", items)
        i += 1


def choose_attack():
    global attack
    i = 1
    print(red + bold + " SPECIAL ATTACK" + end)
    for spell in attack:
        print("      ",str(i) + ":", spell["name"], "(cost", str(spell["cost"]) + ")","(gives damage of",str(spell["dmg"])+")")
        i += 1


def choose_heal():
    global heal
    i=1
    print(green + bold +"HEAL" + end)
    for items in heal:
        print("      ",str(i) + ":",items["name"], "(cost", str(items["cost"]) + ")","(health",str(items["points"]),")")
        i +=1


def enemy_option():
    low = 0
    high = 2
    return random.randrange(low, high)


def get_player_stats():
    global player_mp
    global player_max_mp
    global player_hp
    global player_max_hp
    hp_bar = ""
    mp_bar = ""
    hp_bar_ticks = ((player_hp/player_max_hp)*100)//4
    mp_bar_ticks = ((player_mp/player_max_mp)*100)//10
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

    print("                  HEALTH_________________________           MAGIC POINTS__________")
    print("             " + bold + str(player_hp) + "/" + str(player_max_hp) + "   "+ "|" + green + hp_bar + end +"|"  +"              "+ bold + str(player_mp) + "/" +str(player_max_mp) + "  " + "|" + blue + mp_bar + end +"|")
    return " "


def get_enemy_stats():
    global enemy_mp
    global enemy_max_mp
    global enemy_hp
    global enemy_max_hp
    hp_bar = ""
    mp_bar = ""
    hp_bar_ticks = ((enemy_hp/enemy_max_hp)*100)//4
    mp_bar_ticks = ((enemy_mp/enemy_max_mp)*100)//10
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

    print("                  HEALTH_________________________            MAGICPOINTS__________")
    print("             " + bold + str(enemy_hp) + "/" + str(enemy_max_hp) + "   " + "|" + red + hp_bar + end + "|"+ "              " + bold + str(enemy_mp) + "/" +str(enemy_max_mp) + "  " + "|" + blue + mp_bar + end + "|")
    return " "


def enemy_atk_choice():
    l = 0
    h = 3
    return random.randrange(l, h)


print("CHOOSE DIFFICULTY LEVEL")
print("1:EASY")
print("2:MEDIUM")
print("3:HARD")
level = int(input(""))
if level == 1:
    enemy_hp = 650
    enemy_max_hp = 650
    print("you have chosen EASY LEVEL")
elif level == 2:
    enemy_hp = 750
    enemy_max_hp = 750
    print("you have chosen MEDIUM LEVEL")
else :
    enemy_hp = 850
    enemy_max_hp = 850
    print("you have chosen HARD LEVEL")
running=True

print(bold + red + "==========================================="+ underline +" BATTLE STARTS "+ end + bold + red +"======================================================" + end)
print(bold + red + "                           *************************************************                                  "+ end)

print("YOUR:")
print(get_player_stats())
print("ENEMY:")
print(get_enemy_stats())

while running:
    print("=====================================================================================\n")
    choose_action()
    choice=int(input(""))-1
    if choice == -1:
        continue

    if choice == 0:
        dmg=create_dmg()
        take_enemy_dmg(dmg)

        print("you shot for",dmg,"points of damage.")
        print("YOUR:")
        print(get_player_stats())
        print("ENEMY:")
        print(get_enemy_stats())

    elif choice == 1:
        choose_attack()
        print("To go back enter 0")
        option = int(input("Choose Attack: \n"))-1

        if option == -1:
            continue

        atk_dmg = create_atk_dmg(option)
        cost = get_atk_mp(option)

        if player_mp < cost:
            print(red + "you does not have Enough MAGIC POINTS" + end)
            continue
        take_enemy_dmg(atk_dmg)
        reduce_player_mp(cost)
        print("you attacked Enemy for",atk_dmg,"points.")
        print("YOUR:")
        print(get_player_stats())
        print("ENEMY:")
        print(get_enemy_stats())

    elif choice == 2:
        choose_heal()
        print("To go back enter 0")
        selection = int(input("Choose Heal: \n"))-1

        if selection == -1:
            continue

        heal_ = create_heal(selection)
        amount = get_heal_mp(selection)

        if player_mp < amount:
            print("you does not have enough MAGIC POINTS")
            continue
        reduce_player_mp(amount)
        take_player_heal(heal_)
        print("your HEALTH has been increased to" ,player_hp, "/", player_max_hp)
        print("YOUR:")
        print(get_player_stats())
        print("ENEMY:")
        print(get_enemy_stats())

    if enemy_hp == 0:
        print(bold + blue + "               " + "*********"+ underline + "!!!YOU WON!!!" + end + bold + blue +"*********" + end + "               " )
        break
    elif player_hp == 0:
        print(bold + red + "               "+ "*********"+ underline +"$$ENEMY HAS DEFEATED YOU$$"+ end + bold + red +"*********" + end + "              " )
        break


    print("-------------------------------------------------------------------------------------")
    run = True
    while run:
        enemy_choice = enemy_option()
        if enemy_hp < 200 and enemy_mp >= 20:
            option = 1
            heal_enemy = create_heal(option)
            cost = get_heal_mp(option)
            reduce_enemy_mp(cost)
            take_enemy_heal(heal_enemy)
            print("Enemy has chosen to heal")
            print(get_enemy_stats())
        elif enemy_choice == 0:
            enemy_dmg = create_dmg()
            take_player_dmg(enemy_dmg)
            print("Enemy shot you for", enemy_dmg, "points.")
            print("YOUR:")
            print(get_player_stats())
            print("ENEMY:")
            print(get_enemy_stats())


        elif enemy_choice == 1:

            atk_choice = enemy_atk_choice()

            atk_dmg = create_atk_dmg(atk_choice)
            cost = get_atk_mp(atk_choice)
            if enemy_mp <= cost:
                continue
            take_player_dmg(atk_dmg)
            reduce_enemy_mp(cost)
            print("Enemy has attacked you for",atk_dmg,"points.")
            print("YOUR:")
            print(get_player_stats())
            print("ENEMY:")
            print(get_enemy_stats())
        run = False

    if enemy_hp == 0:
        print(bold + blue + "               " + "*********"+ underline + "!!!YOU WON!!!" + end + bold + blue +"*********" + end + "               " )
        break
    elif player_hp == 0:
        print(bold + red + "               "+ "*********"+ underline +"$$ENEMY HAS DEFEATED YOU$$"+ end + bold + red +"*********" + end + "              " )
        break

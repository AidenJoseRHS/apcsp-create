damage = 0
basehealth = 0
name = input(str("Enter username: "))

def brawler(name, kithealth, kitspeed, basedamage):
    basedamage = 3
    kithealth = 20
    print(basedamage)
    return(name, kithealth, kitspeed, basedamage)

def mage(name, kithealth, kitspeed, basedamage):
    basedamage = 2
    kithealth = 15
    return(name, kithealth, kitspeed, basedamage)

def doctor(name, kithealth, kitspeed, basedamage):
    basedamage = 1
    kithealth = 15
    return(name, kithealth, kitspeed, basedamage)

def tank(name, kithealth, kitspeed, basedamage):
    basedamage = 3
    kithealth = 30
    return(name, kithealth, kitspeed, basedamage)

def kits(brawler,mage,doctor,tank)

brawler(name, kithealth, kitspeed, basedamage)

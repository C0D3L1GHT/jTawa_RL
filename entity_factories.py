from components.ai import HostileEnemy
from components.ai import Barker
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="jan Tawa",
    ai_cls=HostileEnemy, # the Actor class needs an AI, but player obviously isn't going to use it
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

#TODO: add friendly NPC that you can talk with
# an Elder who gives quests,
# a Trader who gives items,
# a Farmer who just barks
farmer = Actor(
    char="i",
    color=(39, 217, 98),
    name="jan kili",
    ai_cls=Barker,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="monsuta lili",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="monsuta suli",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="lipu pi lawa nasa",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="lipu pi kon seli",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="telo pi sijelo pona",
    consumable=consumable.HealingConsumable(amount=4),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="lipu pi suno ike",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)
dagger = Item(
    char="/", color=(0, 191, 255), name="ilo kipisi lili", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="ilo kipisi", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="len kiwen",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="len kiwen wawa", equippable=equippable.ChainMail()
)

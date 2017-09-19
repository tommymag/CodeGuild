from random import randint


# Items are made up of a name, currency value, and weight. Some items have their own special attributes as well.
class Items:
    def __init__(self, name=None, currency_value=None, weight=None):
        self.item_name = name
        self.gold_value = currency_value
        self.item_weight = weight

    def __str__(self):
        return '{}'.format(self.item_name)


# Weapons, special attributes are attack power and attack speed. Attack function can be removed if necessary.
class Weapons(Items):
    def __init__(self, key=None):
        super().__init__(name=None, currency_value=None, weight=None)
        available_weapons = {
            1: {'name': 'Laser', 'currency_value': 80, 'weight': 90, 'hit_points': 100, 'attack_power': 4,
                'attack_speed': 6},
            2: {'name': 'Energy Cannon', 'currency_value': 90, 'weight': 100, 'hit_points': 110, 'attack_power': 6,
                'attack_speed': 5},
            3: {'name': 'Plasma Ray', 'currency_value': 100, 'weight': 110, 'hit_points': 120, 'attack_power': 8,
                'attack_speed': 4},
            4: {'name': 'Rail Gun', 'currency_value': 110, 'weight': 120, 'hit_points': 130, 'attack_power': 10,
                'attack_speed': 3},
            5: {'name': 'Photon Torpedo', 'currency_value': 120, 'weight': 130, 'hit_points': 140, 'attack_power': 12,
                'attack_speed': 2}
        }
        self.key = key
        if self.key is None:
            self.key = randint(1, 5)
        self.item_name = available_weapons[self.key]['name']
        self.gold_value = available_weapons[self.key]['currency_value']
        self.item_weight = available_weapons[self.key]['weight']
        self.hit_points = available_weapons[self.key]['hit_points']
        self.attack_power = available_weapons[self.key]['attack_power']
        self.attack_speed = available_weapons[self.key]['attack_speed']

    def attack(self, enemy_hp):
        enemy_hp -= self.attack_power
        return enemy_hp


# Shields, special attribute is defensive power.
class Shields(Items):
    def __init__(self, key=None):
        super().__init__(name=None, currency_value=None, weight=None)
        available_shields = {
            1: {'name': 'Force Field', 'currency_value': 100, 'weight': 100, 'hit_points': 75, 'defensive_power': 100},
            2: {'name': 'Defense Shield', 'currency_value': 120, 'weight': 200, 'hit_points': 100,
                'defensive_power': 125},
            3: {'name': 'Energy Shield', 'currency_value': 140, 'weight': 400, 'hit_points': 125,
                'defensive_power': 150},
            4: {'name': 'Deflector Shield', 'currency_value': 160, 'weight': 600, 'hit_points': 150,
                'defensive_power': 175}
        }
        self.key = key
        if self.key is None:
            self.key = randint(1, 4)
        self.item_name = available_shields[self.key]['name']
        self.gold_value = available_shields[self.key]['currency_value']
        self.item_weight = available_shields[self.key]['weight']
        self.hit_points = available_shields[self.key]['hit_points']
        self.defensive_power = available_shields[self.key]['defensive_power']


# Engines. Special attribute is speed boost.
class Drive(Items):
    def __init__(self, key=None):
        super().__init__(name=None, currency_value=None, weight=None)
        available_engines = {
            1: {'name': 'Sub-light Drive', 'currency_value': 100, 'weight': 150, 'hit_points': 200,
                'speed_boost': 2},
            2: {'name': 'Alcubierre Drive', 'currency_value': 200, 'weight': 200, 'hit_points': 300,
                'speed_boost': 4},
            3: {'name': 'Warp Drive', 'currency_value': 300, 'weight': 250, 'hit_points': 400,
                'speed_boost': 6},
            4: {'name': 'Improbability Drive', 'currency_value': 400, 'weight': 300, 'hit_points': 500,
                'speed_boost': 8},
            5: {'name': 'Ludicrous Drive', 'currency_value': 500, 'weight': 350, 'hit_points': 600,
                'speed_boost': 10}
        }
        self.key = key
        if self.key is None:
            self.key = randint(1, 5)
        self.item_name = available_engines[self.key]['name']
        self.gold_value = available_engines[self.key]['currency_value']
        self.item_weight = available_engines[self.key]['weight']
        self.hit_points = available_engines[self.key]['hit_points']
        self.speed_boost = available_engines[self.key]['speed_boost']


# repair items, special attribute is heal value. heal it function can be removed if redundant w/ another team
class Heal(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        self.item_name = 'Universal Repair Module'
        self.gold_value = 50
        self.heal_value = 500

    def heal_it(self, ship_hp):
        ship_hp += self.heal_value
        return ship_hp


# Relics. There will be 3 relics from the 3 different races. If they are discovered and added to inventory,
# the player's reputation is increased.
class Relic(Items):
    def __init__(self, key=None):
        super().__init__(name=None, weight=None)
        available_relics = {
            1: {'name': 'The Aven Statue of Inter-galactic Wisdom', 'weight': 300, 'reputation_value': 3},
            2: {'name': 'The Ulmadi Crown of the Interstellar Priestess', 'weight': 300, 'reputation_value': 3},
            3: {'name': 'The Hadian Sphere of Solar Flares', 'weight': 300, 'reputation_value': 3}
        }
        self.key = key
        if self.key is None:
            key = randint(1, 3)
        self.item_name = available_relics[key]['name']
        self.item_weight = available_relics[key]['weight']
        self.reputation_value = available_relics[key]['reputation_value']


# Keys. All 4 should be collected before one can leave a room/planet.
class Key(Items):
    def __init__(self, key=None):
        super().__init__(name=None, currency_value=None, weight=None)
        available_keys = {
            1: {'name': 'Supernova Key', 'key_code': 5},
            2: {'name': 'Black Hole Key', 'key_code': 5},
            3: {'name': 'Wormhole Key', 'key_code': 5},
            4: {'name': 'Tesseract Key', 'key_code': 5}
        }
        self.key = key
        if self.key is None:
            key = randint(1, 4)
        self.item_name = available_keys[key]['name']
        self.key_code = available_keys[key]['key_code']


# Inventory, which holds items, gold, and heal items, and allows those items to be added or removed.
class Inventory:
    def __init__(self):
        self.inventory = []  # 23 slots
        self.repair_kit = []  # 1 slot stacking
        self.key_chain = []  # so keys don't take up regular inventory space
        self.wallet = 0
        self.max_weight = 5000
        self.current_weight = 0
        self.current_repair_item_count = 0
        self.current_key_count = 0

    # adds weight of each item, and if new item makes inventory exceed 5k, then item cannot be added
    def add_to_inventory(self, new_item):
        if len(self.inventory) <= 23 and self.current_weight + new_item.item_weight <= self.max_weight:
            self.inventory.append(new_item)
            self.current_weight += new_item.item_weight
            return '{} has been added to inventory'.format(new_item.item_name)
        else:
            return '{} cannot be added due to space or weight.'.format(new_item.item_name)

    def display_inventory(self):
        for i, o in enumerate(self.inventory):
            print('{} - {}'.format(i, o))

    # when removing from inventory, should subtract weight of item removed
    def remove_from_inventory(self, item_index):
        removed_item = self.inventory.pop(item_index)
        self.current_weight -= removed_item.item_weight
        return 'You have removed {} from your inventory.'.format(removed_item.item_name)

    def add_gold_to_wallet(self, gold_amount):
        self.wallet += gold_amount
        return '{} gold has been added to your wallet.'.format(gold_amount)

    def display_gold_total(self):
        return str(self.wallet)

    def remove_gold_from_wallet(self, gold_amount):
        self.wallet -= gold_amount
        return 'You have removed {} gold from your wallet.'.format(gold_amount)

    def add_item_to_repair_kit(self, new_module):
        self.repair_kit.append(new_module)
        self.current_repair_item_count += new_module.heal_value
        return '{} has been added to your repair kit.'.format(new_module.item_name)

    def display_healing_items_total(self):
        for i, o in enumerate(self.repair_kit):
            print('{} {}'.format(len(self.repair_kit), o))

    def remove_item_from_repair_kit(self, repair_index):
        removed_module = self.repair_kit.pop(repair_index)
        self.current_repair_item_count -= removed_module.heal_value
        return 'You have removed {} from your repair kit.'.format(removed_module.item_name)

    def add_key_to_keychain(self, new_key):
        self.key_chain.append(new_key)
        self.current_key_count += new_key.key_code
        return '{} has been added to your keychain.'.format(new_key.item_name)

    def display_keychain(self):
        for i, o in enumerate(self.key_chain):
            print('{} {}'.format(len(self.key_chain), o))

    def remove_item_from_keychain(self, key_index):
        removed_key = self.key_chain.pop(key_index)
        self.current_key_count -= removed_key.key_code
        return 'You have removed {} from your keychain.'.format(removed_key.item_name)


wep = Weapons()
engine = Drive()
repair = Heal()
shield = Shields()
key = Key()
inv = Inventory()
print(inv.add_to_inventory(shield))
print(inv.add_to_inventory(engine))
print(inv.add_gold_to_wallet(5))
print('You have {} gold total.'.format(inv.display_gold_total()))
print(inv.add_item_to_repair_kit(repair))
print(inv.add_key_to_keychain(key))
inv.display_healing_items_total()
print(inv.add_to_inventory(wep))
inv.display_inventory()
print(inv.remove_gold_from_wallet(2))
print('You have {} gold total.'.format(inv.display_gold_total()))
print()
print(inv.remove_from_inventory(0))
inv.display_inventory()
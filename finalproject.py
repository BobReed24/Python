# Python Text Adventure Game - Final Project

import sys
import random

class Item:
    def __init__(self, name, description, is_collectible=True, is_usable=False):
        self.name = name
        self.description = description
        self.is_collectible = is_collectible
        self.is_usable = is_usable

    def use(self, player, game):
        # Default use does nothing
        print(f"You can't use the {self.name} right now.")

    def inspect(self):
        print(f"{self.name}: {self.description}")

class Room:
    def __init__(self, name, description, is_locked=False, key_name=None):
        self.name = name
        self.description = description
        self.exits = {}  # direction: Room object
        self.items = []  # list of Item objects
        self.is_locked = is_locked
        self.key_name = key_name  # name of item that unlocks this room

    def describe(self):
        print(f"\n== {self.name} ==")
        print(self.description)
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f" - {item.name}")
        else:
            print("There are no items here.")
        print("Exits:")
        for direction in self.exits:
            print(f" - {direction}")

    def get_exit(self, direction):
        return self.exits.get(direction, None)

    def unlock(self, key_name):
        if self.is_locked and key_name == self.key_name:
            self.is_locked = False
            print(f"You unlocked the {self.name}!")
            return True
        return False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(i)
        return None

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_location = starting_room
        self.inventory = []
        self.health = 100

    def move(self, direction):
        next_room = self.current_location.get_exit(direction)
        if not next_room:
            print("You can't go that way.")
            return False
        if next_room.is_locked:
            print(f"The {next_room.name} is locked.")
            return False
        self.current_location = next_room
        print(f"You move {direction} to the {self.current_location.name}.")
        self.current_location.describe()
        return True

    def pick_up_item(self, item_name):
        item = self.current_location.remove_item(item_name)
        if item:
            if item.is_collectible:
                self.inventory.append(item)
                print(f"You picked up the {item.name}.")
            else:
                print(f"You can't pick up the {item.name}.")
                self.current_location.add_item(item)  # put it back
        else:
            print(f"There is no {item_name} here.")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return
        print("You have the following items:")
        for item in self.inventory:
            print(f" - {item.name}")

    def has_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return True
        return False

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def take_damage(self, amount):
        self.health -= amount
        print(f"You take {amount} damage! Health: {self.health}")
        if self.health <= 0:
            print("You have died!")
            return True
        return False

class Enemy:
    def __init__(self, name, health, strength, location):
        self.name = name
        self.health = health
        self.strength = strength
        self.location = location

    def attack(self, player):
        damage = random.randint(1, self.strength)
        print(f"The {self.name} attacks you for {damage} damage!")
        player_dead = player.take_damage(damage)
        return player_dead

    def take_damage(self, amount):
        self.health -= amount
        print(f"You hit the {self.name} for {amount} damage! Enemy health: {self.health}")
        if self.health <= 0:
            print(f"The {self.name} has been defeated!")
            return True
        return False

class Game:
    def __init__(self):
        self.rooms = {}
        self.player = None
        self.is_running = True
        self.enemies = []
        self.create_world()

    def create_world(self):
        # Create rooms
        foyer = Room("Foyer", "A small foyer with a dusty chandelier. Doors lead north and east.")
        hall = Room("Hall", "A long hall with portraits on the walls. There is a locked door to the north.", is_locked=True, key_name="silver key")
        kitchen = Room("Kitchen", "A kitchen with old pots and pans. There is a door to the west and stairs going down.")
        cellar = Room("Cellar", "A dark, damp cellar. You can barely see. Stairs lead up.")
        library = Room("Library", "A quiet library filled with ancient books. There is a door to the south.")
        secret_room = Room("Secret Room", "A hidden room filled with treasures!", is_locked=True, key_name="golden key")
        garden = Room("Garden", "A beautiful garden with blooming flowers. Paths lead east and south.")
        tower = Room("Tower", "A tall tower with a great view. There is a locked door to the east.", is_locked=True, key_name="tower key")
        armory = Room("Armory", "An armory with weapons and armor. Doors lead west and south.")
        dungeon = Room("Dungeon", "A dark dungeon with chains on the walls. There is a door to the north.")
        throne_room = Room("Throne Room", "The grand throne room. The final challenge awaits here.")
        secret_passage = Room("Secret Passage", "A narrow passage connecting the library and the tower.")

        # Connect rooms
        foyer.exits = {"north": hall, "east": kitchen, "south": garden}
        hall.exits = {"south": foyer, "north": throne_room}
        kitchen.exits = {"west": foyer, "down": cellar}
        cellar.exits = {"up": kitchen}
        library.exits = {"south": garden, "east": secret_passage}
        secret_passage.exits = {"west": library, "east": tower}
        tower.exits = {"west": secret_passage, "east": armory}
        armory.exits = {"west": tower, "south": dungeon}
        dungeon.exits = {"north": armory}
        garden.exits = {"north": foyer, "east": library, "south": secret_room}
        secret_room.exits = {"north": garden}
        throne_room.exits = {"south": hall}

        # Add items to rooms
        foyer.add_item(Item("silver key", "A small silver key. It might open a locked door.", True, True))
        kitchen.add_item(Item("apple", "A fresh red apple. Restores some health.", True, True))
        cellar.add_item(Item("torch", "A wooden torch. Useful to light dark places.", True, True))
        library.add_item(Item("golden key", "A shiny golden key with intricate engravings.", True, True))
        armory.add_item(Item("sword", "A sharp sword. Useful for fighting enemies.", True, True))
        dungeon.add_item(Item("potion", "A mysterious red potion. Restores health.", True, True))
        garden.add_item(Item("map", "A map of the castle grounds.", True, False))
        tower.add_item(Item("tower key", "A heavy iron key labeled 'Tower'.", True, True))

        # Create enemies
        goblin = Enemy("Goblin", 30, 10, dungeon)
        ghost = Enemy("Ghost", 40, 15, throne_room)
        self.enemies = [goblin, ghost]

        # Store rooms
        self.rooms = {
            "Foyer": foyer,
            "Hall": hall,
            "Kitchen": kitchen,
            "Cellar": cellar,
            "Library": library,
            "Secret Room": secret_room,
            "Garden": garden,
            "Tower": tower,
            "Armory": armory,
            "Dungeon": dungeon,
            "Throne Room": throne_room,
            "Secret Passage": secret_passage
        }

        # Create player
        player_name = input("Enter your adventurer's name: ").strip()
        if not player_name:
            player_name = "Hero"
        self.player = Player(player_name, foyer)
        print(f"\nWelcome, {self.player.name}! Your adventure begins...\n")
        self.player.current_location.describe()

    def start(self):
        while self.is_running:
            command = input("\nWhat do you want to do? ").strip().lower()
            if command in ["quit", "exit"]:
                print("Thanks for playing! Goodbye.")
                self.is_running = False
                continue
            self.parse_command(command)
            # Check for enemy encounters
            self.check_for_enemies()
            # Check win/lose conditions
            if self.check_win_condition():
                print("Congratulations! You have won the game!")
                self.is_running = False
            if self.player.health <= 0:
                print("Game Over. You have died.")
                self.is_running = False

    def parse_command(self, command):
        words = command.split()
        if not words:
            print("Please enter a command.")
            return

        verb = words[0]
        if verb == "go" and len(words) > 1:
            direction = words[1]
            self.player.move(direction)
        elif verb == "look":
            self.player.current_location.describe()
        elif verb == "inventory":
            self.player.show_inventory()
        elif verb == "take" and len(words) > 1:
            item_name = " ".join(words[1:])
            self.player.pick_up_item(item_name)
        elif verb == "use" and len(words) > 1:
            item_name = " ".join(words[1:])
            item = self.player.get_item(item_name)
            if item:
                self.use_item(item)
            else:
                print(f"You don't have a {item_name}.")
        elif verb == "inspect" and len(words) > 1:
            item_name = " ".join(words[1:])
            item = self.player.get_item(item_name)
            if item:
                item.inspect()
            else:
                print(f"You don't have a {item_name}.")
        elif verb == "help":
            self.show_help()
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")

    def use_item(self, item):
        # Special use cases
        if item.name.lower() == "apple":
            print("You eat the apple and feel refreshed.")
            self.player.health = min(100, self.player.health + 20)
            print(f"Health: {self.player.health}")
            self.player.inventory.remove(item)
        elif item.name.lower() == "potion":
            print("You drink the potion and feel your wounds heal.")
            self.player.health = min(100, self.player.health + 50)
            print(f"Health: {self.player.health}")
            self.player.inventory.remove(item)
        elif item.name.lower() == "torch":
            # Torch can be used to light cellar or dungeon
            if self.player.current_location.name in ["Cellar", "Dungeon"]:
                print("You light the torch. The room is now illuminated.")
                # Could add more effects here
            else:
                print("You don't need to use the torch here.")
        elif item.name.lower() in ["silver key", "golden key", "tower key"]:
            # Try to unlock adjacent locked rooms
            unlocked_any = False
            for direction, room in self.player.current_location.exits.items():
                if room.is_locked and room.key_name == item.name.lower():
                    room.unlock(item.name.lower())
                    unlocked_any = True
                    # Optionally remove key after use
                    # self.player.inventory.remove(item)
                    break
            if not unlocked_any:
                print(f"You can't use the {item.name} here.")
        elif item.name.lower() == "sword":
            # Sword can be used to attack enemy if present
            enemy = self.get_enemy_in_room()
            if enemy:
                damage = random.randint(10, 25)
                enemy_dead = enemy.take_damage(damage)
                if enemy_dead:
                    self.enemies.remove(enemy)
            else:
                print("There is nothing to attack here.")
        else:
            print(f"You can't use the {item.name} right now.")

    def get_enemy_in_room(self):
        for enemy in self.enemies:
            if enemy.location == self.player.current_location:
                return enemy
        return None

    def check_for_enemies(self):
        enemy = self.get_enemy_in_room()
        if enemy:
            print(f"A {enemy.name} appears!")
            while enemy.health > 0 and self.player.health > 0:
                action = input("Do you want to (attack) or (run)? ").strip().lower()
                if action == "attack":
                    # Player attacks first if has sword
                    sword = self.player.get_item("sword")
                    if sword:
                        damage = random.randint(15, 30)
                        enemy_dead = enemy.take_damage(damage)
                        if enemy_dead:
                            self.enemies.remove(enemy)
                            break
                    else:
                        print("You have no weapon! You punch the enemy.")
                        damage = random.randint(1, 5)
                        enemy_dead = enemy.take_damage(damage)
                        if enemy_dead:
                            self.enemies.remove(enemy)
                            break
                    # Enemy attacks back
                    player_dead = enemy.attack(self.player)
                    if player_dead:
                        self.is_running = False
                        break
                elif action == "run":
                    # Try to run to a random available exit
                    exits = list(self.player.current_location.exits.keys())
                    if exits:
                        run_direction = random.choice(exits)
                        print(f"You run {run_direction} to escape!")
                        self.player.move(run_direction)
                        break
                    else:
                        print("No way to run!")
                else:
                    print("Invalid action. Choose 'attack' or 'run'.")

    def check_win_condition(self):
        # Win if player reaches throne room and no enemies remain
        if self.player.current_location.name == "Throne Room" and not self.enemies:
            return True
        return False

    def show_help(self):
        print("""
Available commands:
 - go [direction] (e.g., go north)
 - look (describe current room)
 - take [item] (pick up an item)
 - use [item] (use an item in your inventory)
 - inspect [item] (read description of an item in your inventory)
 - inventory (show your items)
 - help (show this help message)
 - quit or exit (end the game)
Directions can be: north, south, east, west, up, down
""")

if __name__ == "__main__":
    game = Game()
    game.start()

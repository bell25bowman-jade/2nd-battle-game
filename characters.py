# Base Character class
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.shield = False

    def attack(self, opponent):
       damage = random.randint(self.attack_power - 5, self.attack_power + 5)
       print(f"{self.name} attacks {opponent.name} for {damage} damage!")
       opponent.take_damage(damage)

    def take_damage(self, damage):
        if self.shield:
            damage = max(0, damage - 10)  # Shield reduces damage by 10
            print(f"{self.name}'s shield absorbs some damage! Damage taken: {damage}")
            self.shield = False  # Shield is used up after one attack
        else:
            print(f"{self.name} takes {damage} damage!")
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    
    def heal(self):
        amount = random.randint(10, 20)
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}")
    
    @staticmethod
    def create_choice():
        print("Choose your character class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer") 
        print("4. Paladin")  

        class_choice = input("Enter the number of your class choice: ")
        name = input("Enter your character's name: ")

        if class_choice == '1':
            return Warrior(name)
        elif class_choice == '2':
            return Mage(name)
        elif class_choice == '3':
            return Archer(name)
        elif class_choice == '4':
            return Paladin(name)
        else:
            print("Invalid choice. Defaulting to Warrior.")
            return Warrior(name)
        
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def axe_swing(self, opponent):
        damage = random.randint(self.attack_power + 5, self.attack_power + 15)
        print(f"{self.name} uses Axe Swing on {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)
    
    def mace_strike(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        print(f"{self.name} uses Mace Strike on {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)       

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def arcane_blast(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        print(f"{self.name} uses Arcane Blast on {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)
    
    def elemental_shield(self):
        self.shield = True
        print(f"{self.name} conjures an elemental shield! Incoming damage will be reduced for the next attack.")
        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health = min(self.max_health, self.health + 5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
    
    def cast_spell(self, opponent):
        #randomly choose a spell to cast
        action = random.choice(['fireball', 'ice_shard', 'lightning_bolt', 'summon_minions'])
        if action == 'fireball':
            damage = random.randint(self.attack_power + 5, self.attack_power + 15)
            opponent.take_damage(damage)
            print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
        
        elif action == 'ice_shard':
            damage = random.randint(self.attack_power, self.attack_power + 10)
            opponent.take_damage(damage)
            print(f"{self.name} casts Ice Shard on {opponent.name} for {damage} damage! {opponent.name} is frozen and misses their next turn!")
        
        elif action == 'lightning_bolt':
            damage = random.randint(self.attack_power + 10, self.attack_power + 20)
            opponent.take_damage(damage)
            print(f"{self.name} casts Lightning Bolt on {opponent.name} for {damage} damage! {opponent.name} is stunned and misses their next turn!")
            
        elif action == 'summon_minions':
            print(f"{self.name} summons minions to attack {opponent.name}!")
            for _ in range(3):
                damage = random.randint(5, 10)
                opponent.take_damage(damage)
                print(f"A minion attacks {opponent.name} for {damage} damage!")
        
        else:
            evade_chance = random.random()
            if evade_chance < 0.2:  # 20% chance to evade
                print(f"{self.name} evades the attack!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.invisible = False
        
    def quick_shot(self, opponent):
        damage = random.randint(self.attack_power - 10, self.attack_power + 10)
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)
        
    def become_invisible(self):
        self.invisible = True
        print(f"{self.name} becomes invisible! The next attack against them will miss.")
        if self.invisible:
            print(f"{self.name} is invisible! The attack misses!")
            self.invisible = False  # Reset invisibility after one attack
    
    def evade(self):
        self.evade_chance = random.random()
        if self.evade_chance < 0.3:  # 30% chance to evade
            print(f"{self.name} evades the attack!")
            return True
        else:
            print(f"{self.name} fails to evade the attack!")
        return False
# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        
    def use_shield(self):
        self.shield = True
        print(f"{self.name} raises their shield! Incoming damage will be reduced for the next attack.")
        
    def holy_smite(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        print(f"{self.name} uses Holy Smite on {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)
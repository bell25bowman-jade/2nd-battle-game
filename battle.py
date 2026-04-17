from characters import Character, EvilWizard, Paladin, Warrior, Mage, Archer

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':  # class special abilities
            if isinstance(player, Warrior):
                print("1. Axe Swing")
                print("2. Mace Strike")
                ablility = input("Choose your special ability: ")
                if ablility == '1':
                    player.axe_swing(wizard)
                elif ablility == '2':
                    player.mace_strike(wizard)

            elif isinstance(player, Mage):
                print("1. Arcane Blast")
                print("2. Elemental Shield")
                ability = input("Choose ability: ")

                if ability == '1':
                    player.arcane_blast(wizard)
                elif ability == '2':
                    player.elemental_shield()

            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability = input("Choose ability: ")

                if ability == '1':
                    player.quick_shot(wizard)
                elif ability == '2':
                    player.evade()

            elif isinstance(player, Paladin):
                print("1. Holy Smite")
                print("2. Shield")
                ability = input("Choose ability: ")

                if ability == '1':
                    player.holy_smite(wizard)
                elif ability == '2':
                    player.use_shield()

        elif choice == '3':
            player.heal()

        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue

        else:
            print("Invalid choice.")
            continue
      
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
        else:
            wizard.health <= 0
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = Character.create_choice()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
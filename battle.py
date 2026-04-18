from characters import Character, Warrior, Mage, Archer, Paladin, EvilWizard


# Battle system
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        while True:
            choice = input("Choose your action: ")
            if choice in ['1', '2', '3', '4']:
                break
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':  # class special abilities
            if isinstance(player, Warrior):
                print("1. Axe Swing")
                print("2. Mace Strike")
                while True:
                    ability = input("Choose your special ability: ")
                    if ability == '1':
                        player.axe_swing(wizard)
                        break
                    elif ability == '2':
                        player.mace_strike(wizard)
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")

            elif isinstance(player, Mage):
                print("1. Arcane Blast")
                print("2. Elemental Shield")
                while True:
                    ability = input("Choose ability: ")
                    if ability == '1':
                        player.arcane_blast(wizard)
                        break
                    elif ability == '2':
                        player.elemental_shield()
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")

            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                print("3. Become Invisible")
                while True:
                    ability = input("Choose ability: ")
                    if ability == '1':
                        player.quick_shot(wizard)
                        break
                    elif ability == '2':
                        player.evade()
                        break
                    elif ability == '3':
                        player.become_invisible()
                        break
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")

            elif isinstance(player, Paladin):
                print("1. Holy Smite")
                print("2. Shield")
                while True:
                    ability = input("Choose ability: ")
                    if ability == '1':
                        player.holy_smite(wizard)
                        break
                    elif ability == '2':
                        player.use_shield()
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")

        elif choice == '3':
            player.heal()

        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue
      
        if wizard.health > 0:
            wizard.regenerate()
            wizard.cast_spell(player)

        if player.health <= 0:
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = Character.create_choice()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
import time

class Player:
    def __init__(self):
        self.inventory = []
        self.allies = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def add_ally(self, ally):
        self.allies.append(ally)

class Game:
    def __init__(self):
        self.player = Player()
        self.story_progress = 0

    def display_options(self, options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def make_choice(self, options):
        self.display_options(options)
        choice = int(input("Enter your choice: "))
        return choice

    def start_game(self):
        print("Welcome to Shadows of Destiny!")
        time.sleep(1)

        # Game Introduction
        print("In the city of Eldoria, you, a young mage named Alaric, embark on a quest to save the city.")
        time.sleep(1)

        # Game Loop
        while self.story_progress < 4:  # Increased complexity with more chapters
            if self.story_progress == 0:
                self.chapter_one()
            elif self.story_progress == 1:
                self.chapter_two()
            elif self.story_progress == 2:
                self.chapter_three()
            elif self.story_progress == 3:
                self.chapter_four()

        # Game Ending
        self.show_endings()

    def chapter_one(self):
        print("Chapter One: The Cryptic Message")
        time.sleep(1)

        choice = self.make_choice(["Investigate the message", "Ignore and continue your studies"])
        if choice == 1:
            print("You follow the message's clues, leading you to the Thieves' Guild.")
            self.player.add_ally("Thieves' Guild")
            self.story_progress += 1
        elif choice == 2:
            print("Ignoring the message, you focus on your studies, unaware of the impending danger.")
            self.story_progress += 1

    def chapter_two(self):
        print("Chapter Two: Shadows of Alliance")
        time.sleep(1)

        choice = self.make_choice(["Confront the Thieves' Guild", "Seek help from the mage councils"])
        if choice == 1:
            print("You confront the Thieves' Guild, forming an uneasy alliance.")
            self.player.add_ally("Mage Councils")
            self.story_progress += 1
        elif choice == 2:
            print("You seek help from the mage councils, gaining their support against the looming threat.")
            self.player.add_ally("Thieves' Guild")
            self.story_progress += 1

    def chapter_three(self):
        print("Chapter Three: The Shattered Prophecy")
        time.sleep(1)

        choice = self.make_choice(["Retrieve the ancient prophecy", "Investigate the mysterious disappearances"])
        if choice == 1:
            print("You delve into the ancient archives, retrieving a shattered prophecy.")
            self.player.add_to_inventory("Shattered Prophecy")
            self.story_progress += 1
        elif choice == 2:
            print("Investigating the disappearances, you uncover a dark plot threatening Eldoria.")
            self.story_progress += 1

    def chapter_four(self):
        print("Chapter Four: The Final Confrontation")
        time.sleep(1)

        choice = self.make_choice(["Master the power of the Shadow Crystal", "Unite the factions of Eldoria",
                                   "Choose power over alliances"])
        if choice == 1:
            print("You master the power of the Shadow Crystal, saving Eldoria at a great personal cost.")
        elif choice == 2:
            print("Uniting the factions, you lead a cooperative effort to thwart the impending darkness.")
        elif choice == 3:
            print("Choosing power over alliances, you unleash the ancient force, and Eldoria succumbs to chaos.")

        # End the game
        self.story_progress += 1

    def show_endings(self):
        print("Thanks for playing Shadows of Destiny!")

if __name__ == "__main__":
    game = Game()
    game.start_game()

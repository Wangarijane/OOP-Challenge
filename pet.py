class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at mid-level
        self.energy = 5  # Starting at mid-level
        self.happiness = 5  # Starting at mid-level
        self.tricks = []  # For storing learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")

    def play(self):
        if self.energy >= 2:  # Check if pet has enough energy to play
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play. Try sleeping first.")

    def get_status(self):
        print("\n" + "="*20)
        print(f"{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        print("="*20 + "\n")

    # Bonus methods
    def train(self, trick):
        if self.energy >= 3:  # Training requires energy
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to learn new tricks right now.")

    def show_tricks(self):
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"\n{self.name} hasn't learned any tricks yet.")
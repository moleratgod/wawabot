import random

dice_faces = [
"""
███████
█     █
█  ■  █
█     █
███████""",
"""
███████
█ ■   █
█     █
█   ■ █
███████""",
"""
███████
█ ■   █
█  ■  █
█   ■ █
███████""",
"""
███████
█ ■ ■ █
█     █
█ ■ ■ █
███████""",
"""
███████
█ ■ ■ █
█  ■  █
█ ■ ■ █
███████""",
"""
███████
█ ■ ■ █
█ ■ ■ █
█ ■ ■ █
███████""",
]

def randomroll():
    return random.randint(0, 5)

def diceroll():
    players_role = randomroll()
    return (dice_faces[players_role] + f"\nYou rolled a {players_role+1}.")


if __name__ == "__main__":
    print(diceroll())
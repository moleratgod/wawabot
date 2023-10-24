import random

dice_faces = [
"""
███████
█     █
█  0  █
█     █
███████""",
"""
███████
█ 0   █
█     █
█   0 █
███████""",
"""
███████
█ 0   █
█  0  █
█   0 █
███████""",
"""
███████
█ 0 0 █
█     █
█ 0 0 █
███████""",
"""
███████
█ 0 0 █
█  0  █
█ 0 0 █
███████""",
"""
███████
█ 0 0 █
█ 0 0 █
█ 0 0 █
███████""",
]

def randomroll():
    return random.randint(0, 5)

def diceroll():
    return dice_faces[randomroll()]



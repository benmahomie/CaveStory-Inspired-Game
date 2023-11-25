# Overview

As a software engineer inspired by game development, I embarked on a journey to create a platformer game inspired by the classic "Cave Story" by Daisuke "Pixel" Amaya. I've long admired how Pixel created the game over a five-year period in his free time, as it proves to me that one-man passion projects are possible. This project was an opportunity to dive deeper into the nuances of game mechanics, physics, and player interactions, while honing my skills in Python and game development.

The game I've created is a 2D platformer where players navigate a character through various levels, encountering enemies and obstacles along the way. The core mechanics include running, jumping, shooting, and enemy interactions. The player must strategically navigate through the levels, defeating enemies and avoiding hazards. Currently, only one demo level exists.

The purpose of writing this software was to challenge myself in creating a functional and engaging game from scratch. Basically, I wanted to follow Pixel's ground-up approach in creating his own game engine as closely as I could, but with Python. It was also a means to understand the intricacies of game design and apply my programming skills in a creative and fun way.

See the demo of the game in action here:

[CaveStory-inspired Python Game](https://youtu.be/o3UNKSxGAB8)

# Development Environment

This game was developed in VSCode using a Python Miniconda environment leveraging the following tools:

- **Programming Language:** Python, chosen for its readability, flexibility, and vast array of libraries.
- **Game Library:** Pygame, a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library, allowing for real-time game development. This helped me handle a lot of complicated keyboard events that I would not have had time to build code around in two weeks.
- **Code Editor:** Visual Studio Code, for its robust features and ease of use in handling Python code.
Version Control: Git, for efficient tracking of changes and collaborative development.
- **Environment Management:** Miniconda, used to manage multiple Python environments and dependencies, ensuring consistency across development and production setups.

# Useful Websites

Throughout the development of this game, several resources proved invaluable for learning and troubleshooting:

* [Pygame Documentation](https://www.pygame.org/docs/)
* [Cavestory's Tribute Site](https://www.cavestory.org/)

# Future Work

Future enhancements planned for this game include:

* Add camera following logic so that the player can explore large levels
* Swap hitboxes for sprites, but keep hitbox logic
* Add the ability to interact with objects and NPCs by pressing down while on the ground
* Add textbox functionality for dialogue, including response options
* Swap placeholder sfx for custom-made sfx (I will probably use BFXR for that)
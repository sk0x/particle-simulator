# Physics Simulation Game
This is a simple physics simulation game built using Pygame. The game allows you to interact with particles on the screen by clicking and dragging them.
## How to Run

Ensure you have Python and Pygame installed.
Run the main.py file to start the game.

## Features

Particles with realistic physics behavior, including collision detection and response
Ability to click and drag particles to move them
Customizable particle properties such as size, color, mass, and elasticity
Boundaries that particles bounce off of

## Files
The project consists of two files:

main.py: This file is the main entry point of the game. It sets up the Pygame window, creates the environment, and handles the game loop.
physicsim.py: This file contains the implementation of the Particle and Enviroment classes, which handle the physics simulation and particle behavior.

## Customization
The Enviroment class in physicsim.py has several properties that can be adjusted to customize the simulation:

color: The background color of the environment.
mass_of_air: The "mass" of the air, which affects particle drag.
elasticity: The elasticity of particle collisions.
accelerate: A vector representing the acceleration applied to all particles.
hasBoundaries: A flag indicating whether the particles should bounce off the environment boundaries.

You can modify these properties to create different simulation scenarios.
## Future Improvements

Add support for different particle shapes (e.g., rectangles, polygons)
Implement different interaction methods (e.g., gravity, forces)
Add visualization options (e.g., trails, velocities)
Implement a level or scenario system

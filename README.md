
# Snake Game

This project is a classic implementation of the Snake game using the `pygame` library.

## Files Overview:

1. **main.py**: This is the entry point to initiate and run the Snake game.
2. **snake.py**: Contains the `Snake` class that manages the snake's body, movement, and related game logic.
3. **food.py**: Contains the `Food` class which manages the position and behavior of the food in the game.
4. **variables.py**: Defines several constant values like colors and game dimensions used across the game.

## How to Use:

1. Ensure you have `pygame` installed. If not, you can install it using pip:
```
pip install pygame
```
2. Run the `main.py` script to start the game.
```
python main.py
```
3. Use arrow keys to control the snake's direction. Try to eat the food and grow your snake without colliding into yourself!

## How to Adjust:

1. **Game Dimensions**: You can modify the `WIDTH`, `HEIGHT`, and `CELL_SIZE` in the `variables.py` file to adjust the game's dimensions and the size of each cell.
2. **Colors**: Adjust the RGB color values in `variables.py` to change the color scheme of the game.
3. **Game Speed**: In `main.py`, adjust the value passed to `CLOCK.tick()` to increase or decrease the game's speed.

## Contribution:

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!

## License:

This project is open-source and available under the MIT License.

## Author:

RobertIonutF


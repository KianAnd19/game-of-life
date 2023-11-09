# Conway's Game of Life with Fading Effect

This project is an implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. In this version, we've added a visual fading effect to cells as they die.

## Features

- A grid where cells can live, die or multiply based on Conway's rules.
- Cells fade out gradually as they die, rather than disappearing instantly.
- Ability to pause and resume the game.
- Clicking on the grid toggles the life state of cells.

## Rules of the Game

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Fading Effect

When a cell dies, it doesn't turn to white directly. Instead, it fades to white over several generations, creating a visual effect of dying out.

## Getting Started

### Prerequisites

Make sure you have Python and Pygame installed on your system. You can install Pygame using pip:

```bash
pip install -r requriements.txt
```


### Running the Game

To run the game, execute the following command in your terminal:

```bash
python game_of_life.py
```

### Controls

- Click on the cells to create your initial configuration or to toggle the life state of cells during the game.
- Press `P` to pause or resume the game.
- Close the window to exit the game.

### Customization

You can adjust the size of the grid, the size of the cells, and the fading steps by modifying the constants at the beginning of the script. (Coming soon)

## License

This project is open source and available under the MIT License.

## Acknowledgments

- John Horton Conway, for devising the original Game of Life.
- The Pygame community, for providing the Pygame library which made this project possible.

Enjoy exploring the Game of Life!
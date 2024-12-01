# Tetris Auto Player

This is an advanced AI-powered Tetris auto player implementation that uses sophisticated heuristic evaluation techniques to determine optimal piece placements in real-time.

## Features

- Smart AI decision making using weighted heuristic evaluation
- Multiple visualization options (Tkinter and Pygame)
- Manual play mode with keyboard controls
- Real-time move calculation and execution
- Next piece preview
- Score tracking and level progression
- Evaluates multiple possible moves ahead considering:
    - Number and distribution of holes
    - Aggregate height of the board
    - Surface roughness/bumpiness
    - Complete line opportunities
    - Column transitions
    - Empty column counts
    - Well depths
    - Block density distribution

## How to Run

Make sure you have Python 3.x installed along with the required libraries.

### Autoplay with Tkinter Visualization

To run the autoplayer with the Tkinter visualization, execute:

```bash
python3 visual.py
```

### Autoplay with Pygame Visualization

To run the autoplayer with the Pygame visualization, execute:

```bash
python3 visual-pygame.py
```

### Manual Play Mode

To play the game manually using keyboard controls, run:

```bash
python3 visual.py -m
```

### Controls in Manual Mode

- Arrow keys: Move the piece left or right
- Up arrow: Rotate the piece
- Down arrow: Soft drop
- Space: Hard drop

## Requirements

- Python 3.x
- Tkinter (for default visualization)
- Pygame (for alternate visualization)

Install Pygame using:

```bash
pip install pygame
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per the license terms.

## Acknowledgments

Inspired by the classic Tetris game mechanics.

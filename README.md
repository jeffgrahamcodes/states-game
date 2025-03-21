# US States Learning Game

A simple Python-based game using `turtle` that helps players learn and memorize the 50 U.S. states by guessing their names.

## Features
- Interactive map where users can guess the names of U.S. states
- Real-time feedback on correct and incorrect guesses
- Saves unguessed states for future practice
- Uses `turtle` for visual representation

## Project Structure
```
├── main.py               # Main script that runs the game
├── 50_states.csv         # Data file containing state names and coordinates
├── states_to_learn.csv   # File that stores unguessed states for practice
├── blank_states_img.gif  # Image used as the game background
```

## Requirements
- Python 3.x
- `turtle` (built-in)
- `pandas`

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/jeffgrahamcodes/states-game.git
   cd states-game
   ```
2. Install dependencies:
   ```sh
   pip install pandas
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## How to Play
1. A blank U.S. map appears on the screen.
2. Type the name of a U.S. state in the input prompt.
3. If correct, the state’s name appears on the map.
4. The game continues until all states are correctly guessed or the player exits.
5. After exiting, unguessed states are saved in `states_to_learn.csv` for review.

## License
This project is open-source under the [MIT License](LICENSE).

## Author
Developed by [@jeffgrahamcodes](https://jeffgraham.codes). Contributions and feedback are welcome!


# Psychic-Discord Music Bot

Psychic-Discord is a powerful and flexible music bot for Discord. It supports playback from YouTube and Spotify,
provides playlist management features for individual users, and more!

## Technologies Used:

- **Python**: The primary language for developing the bot.
- **discord.py**: A modern, easy-to-use Python library that allows for interacting with the Discord API.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **MySQL**: The primary relational database used for storing user data and playlists.

## Design Patterns & Code Structure:

- **Command Pattern**: Used to handle different bot commands.
- **Singleton Pattern**: For certain utility classes to ensure a single instance.
- **Repository Pattern**: For database operations, separating the business logic and database logic.

## Project Structure:

- `/cogs`: Contains different functionalities of the bot.
    - `music`: Handles music playback features.
    - `playlist`: Manages user playlists.
- `/integrations`: Contains integration logic for external services like YouTube and Spotify.
- `/database`: Contains all database-related logic, models, and operations.
- `/utils`: Utility functions and classes.
- `/config`: Configuration files for different environments.
- `/tests`: Unit tests to ensure code reliability.

## Setup & Installation:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/shamspias/psychic-discord.git
    cd psychic-discord
    ```

2. **Setup a Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Configuration**:
    - Rename `example.env` to `.env`.
    - Fill in the necessary details in `.env` (Bot Token, Database URL, API Keys).

5. **Initialize the Database**:
    ```bash
    python -m database.create_tables
    ```
6. **Fix Privileged Gateway Intents**
    - Go to [Discord Application Portal](https://discord.com/developers/applications/)
    - Select your bot and go to `Privileged Gateway Intents` enable three Privileged

7. **Run the Bot**:
    ```bash
    python main.py
    ```

## Usage:

- `!play [song_name/song_url]`: Play a song from YouTube or Spotify.
- `!pause`: Pause the current song.
- `...` (Add more commands as per your implementation)

## Contribution:

Feel free to fork this repository and submit pull requests. All contributions are welcome!

## License:

[MIT License](LICENSE) (Provide a link if you have a LICENSE file in your repo)


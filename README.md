# ⚡ Lightning Round

A simple deck tool to facilitate lightning rounds in any game!

## Quick Start

**0. Install Python** (if you don't have it):

```bash
# Check if you have Python installed
python3 --version

# On Mac (if not installed):
brew install python3

# On Windows: Download from python.org
# On Linux: sudo apt install python3
```

**1. Create your config file:**

```bash
cp config.example.json config.json
```

**2. Add your own questions and configure the theme:**

```bash
# Edit config.json in your favorite editor
# - Add your custom question/answer decks
# - Customize colors, fonts, and visual effects
```

**3. Run the app:**

```bash
python3 serve.py
```

**4. Open in browser:**

The server will display URLs like:

```
On this computer: http://localhost:8001
On your phone (same WiFi): http://192.168.1.123:8001
```

**On your computer:** Use `http://localhost:8001`
**On your phone:** Use the IP address shown (make sure you're on the same WiFi)

## Making Changes

**After editing `config.json`:**

1. Stop the server (press `Ctrl+C`)
2. Restart it: `python3 serve.py`
3. Refresh your browser

The app loads the config file when it starts, so you need to restart the server to see changes.

## Configuration

### App Title

Customize the app title shown on the home screen:

```json
{
  "appTitle": "⚡ Lightning Round"
}
```

### Theme Customization

Edit the `theme` section in `config.json` to customize colors, fonts, and effects:

```json
{
  "theme": {
    "fontFamily": "Inter, system-ui, -apple-system, sans-serif",
    "colors": {
      "primary": { "from": "purple-600", "to": "blue-600" },
      "accent": "purple-600",
      "correct": "green-500",
      "wrong": "red-500",
      "void": "gray-400"
    }
  }
}
```

Use any [Tailwind CSS](https://tailwindcss.com/docs/colors) color names (e.g., `blue-500`, `red-600`, `green-400`).

### Adding Your Own Decks

Add decks in the `decks` array:

```json
{
  "decks": [
    {
      "id": 1,
      "name": "My Custom Deck",
      "cards": [
        { "question": "What is your question?", "answer": "The answer" },
        { "question": "Another question?", "answer": "Another answer" }
      ]
    }
  ]
}
```

## How to Play

1. **Select a deck** from the home screen
2. **Set timer** duration (default 30 seconds)
3. **Answer questions** using:
   - ✓ **Correct**: Right Arrow or Swipe Right
   - ✗ **Wrong**: Left Arrow or Swipe Left
   - ○ **Void/Skip**: Up Arrow or Swipe Up
4. **View results** when time expires!

## 📁 Project Structure

- `index.html` - Main HTML file (self-contained React app)
- `config.example.json` - Example configuration with sample decks
- `config.json` - Your custom configuration (create from example)
- `serve.py` - Simple Python HTTP server

## TODO

- look into refacotring html file
- look into websocket
- look into build tool origin

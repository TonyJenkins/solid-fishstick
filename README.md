# Solid Fishstick Model Railway Club Website

A simple two-page website for a model railway club, built with standard HTML and served using Python.

## Features

- Two-page website with Home and About pages
- Clean, accessible HTML structure (no CSS styling)
- Navigation between pages
- Information about club activities, membership, and facilities
- Python web server for local hosting

## Pages

- **index.html** - Main homepage with club overview and latest news
- **about.html** - Detailed information about club history, facilities, and membership

## Running the Website

### Prerequisites

- Python 3.6 or higher (uses standard library only)

### Starting the Server

1. Navigate to the project directory
2. Run the Python server:
   ```bash
   python3 server.py
   ```
   or
   ```bash
   python server.py
   ```

3. Open your web browser and visit:
   - Home page: http://localhost:8000/
   - About page: http://localhost:8000/about.html

4. Press `Ctrl+C` in the terminal to stop the server

### Alternative: Using Python's Built-in Server

You can also use Python's built-in HTTP server:
```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000/ in your browser.

## Project Structure

```
solid-fishstick/
├── index.html          # Main homepage
├── about.html          # About page
├── server.py           # Custom Python web server
├── requirements.txt    # Python dependencies (standard library only)
└── README.md          # This file
```

## Technical Details

- Uses standard HTML5 markup
- No CSS styling (as per requirements)
- Python web server handles routing and serves static files
- Responsive viewport meta tag for mobile compatibility
- Basic security headers included in custom server
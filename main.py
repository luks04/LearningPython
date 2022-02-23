import os
from app import app

if __name__ == "__main__":
    # Gets the app from app.py and runs it
    port = os.environ.get('PORT', 8080) # Heroku will set the PORT environment variable
    app.run(host = '0.0.0.0', port = port, debug = False) # Set debug to False before deployment

    # Run with waitress to execute in production environment
    # from waitress import serve
    # serve(app, host = "0.0.0.0", port = 8080)
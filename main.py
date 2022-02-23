import os
from app import app

# Gets the app from app.py and runs it
app.run(debug = False) # Set debug to False before deployment

# Run with waitress to execute in production environment
# from waitress import serve
# serve(app, host = "0.0.0.0", port = 8080)
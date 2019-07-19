"""
Author: Jay

This is the Main Python file that will run.
In this Python file we will:

    - Import the instance of the app from nexus/__init__.py
    - Call the run function from the instance
"""

from nexus import app
app.run(debug=True)
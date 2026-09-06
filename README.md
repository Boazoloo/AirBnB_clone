# AirBnB Clone - The Console

## Description

This project is the first step toward building a full AirBnB clone.
The goal is to create a command interpreter that can manage AirBnB
objects such as users, places, states, cities, and amenities.

The console will allow users to create, retrieve, update, and destroy
objects and store their data persistently.

## Command Interpreter

The command interpreter is a command-line interface used to manage
objects in the AirBnB clone.

### How to start it

Run:

    ./console.py

Or:

    python3 console.py

### How to use it

Once the console starts, commands can be entered at the `(hbnb)` prompt.

Examples:

    (hbnb) help
    (hbnb) create BaseModel
    (hbnb) show BaseModel <id>
    (hbnb) all
    (hbnb) destroy BaseModel <id>
    (hbnb) quit

To exit the console:

    (hbnb) quit

You can also use EOF (Ctrl-D) to exit.

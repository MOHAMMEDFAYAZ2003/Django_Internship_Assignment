
**Project Overview**
1. Rectangle Management (rectangle_example)
This app allows users to create and list rectangles using Django models, forms, and views. It provides a simple UI for managing rectangles through a web interface.

**Features:**
Users can create rectangles by entering width and height.
The rectangle list page displays all saved rectangles.
The data is stored in an SQLite database.
**Key Components:**
Model (models.py): Defines the Rectangle model with width and height attributes.
Form (forms.py): Implements a Django ModelForm for Rectangle.
Views (views.py):
rectangle_list → Displays all rectangles.
create_rectangle → Handles the form to add a new rectangle.
Templates (templates/rectangle_example/):
rectangle_list.html → Displays rectangles in a list format.
create_rectangle.html → Form for adding new rectangles.
URLs (urls.py): Defines URL patterns for listing and creating rectangles.
2. Django Signals Demonstration (signals_example)
This app demonstrates how Django signals work in handling database events, specifically with post_save signals.

**Features:**
Automatically triggers signals whenever a new object (MyModel) is created.
Simulates delays, threading, and transaction behavior in signal handling.
Provides a test page to create objects and observe signal execution.
Key Components:
Model (models.py): Defines MyModel with a name field.
Signals (signals.py):
sync_signal_handler → Simulates a 2-second delay in processing.
thread_check_signal_handler → Prints the current thread ID.
transaction_check_signal_handler → Logs signal execution for transaction testing.
Views (views.py):
test_signals → Creates a new MyModel object to trigger signals.
Templates (templates/):
test.html → Displays the created object's name.
URLs (urls.py): Maps the /test-signals/ route to trigger signal testing.
Technology Stack
Backend: Django 5.1.4, Python
Database: SQLite
Frontend: HTML, Django Templates
Concepts Used: Django Models, Forms, Views, URL Routing, Signals, Middleware
**Conclusion**
This project is an excellent demonstration of Django’s model handling, form processing, and signal execution.

The rectangle_example app provides CRUD functionality for managing geometric shapes.
The signals_example app showcases how Django signals can be used for event-driven programming.

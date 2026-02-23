# Classroom reservation system

Write a simple program that will serve as a **classroom reservation system** for a school or university.
The program will manage information about classrooms and their reservations and will allow users to keep track of how classrooms are used over time.

The program will be based on data structures representing classrooms and reservations.

### Classroom data

For each classroom, store at least the following information:

- Classroom identifier (e.g. room number)
- Building name
- Capacity
- Equipment (one classroom can have multiple pieces of equipment, e.g. projector, computers, lab equipment)

### Reservation data

For each reservation, store at least the following information:

- Classroom identifier
- Name of the person who made the reservation
- Purpose of the reservation (e.g. lecture, exam, consultation)
- Date of the reservation (date when the classroom is used)
- Start time and end time

### Required operations

The user of the program should be able to perform the following operations:

- Create a new reservation book
- Save the reservation book into a file
- Load a reservation book from a file
- Insert new classrooms
- Insert new reservations
- Display all classrooms
- Display all reservations (optionally filtered by classroom or date)
- Remove a reservation
- Remove all reservations
- Completely delete the reservation book

The program will allow the user to select and execute any of these actions using a simple text-based event loop.
Graphical or web-based user interface is not required 😊

### Conflict checking

When inserting a new reservation, the program must **check for time conflicts**.
If the selected classroom is already reserved for the given time interval,
the program should not allow the reservation to be created and should inform the user.

### Optional operations

Possible extensions for practice:

- Ability to edit an existing reservation (change time, purpose, or person)
- Display daily or weekly schedule for a selected classroom or person
- Calculate and display classroom utilization (e.g. total reserved hours per day or week, percentage of occupied time)
- Support for different reservation types with priorities (e.g. exam > lecture > consultation)
- Suggest an alternative free time slot when a reservation conflict occurs
- Export selected views (e.g. schedule of one classroom) into a separate file

### Technical requirements

- The program must be implemented in one or more files with the `.py` extension (**not .ipynb**).
- Divide the program appropriately into modules and the modules further into functions.
- Use basic elements of object-oriented programming and define at least three custom classes (e.g. Classroom, Reservation, ReservationBook).
- Do not use any external packages. You can use only modules from the Python standard library.
- Propose and use an appropriate file format for saving and loading data (e.g. CSV or JSON).
  Depending on the selected format, you may use the corresponding module from the Python standard library.
- All user inputs must be validated.
- Handle possible error situations (invalid user input, invalid date or time, file system errors) using exceptions.

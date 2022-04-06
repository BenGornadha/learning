##Overview
An elevator responds to call based on where an elevator is currently located and in which direction it is going.

#Example
Assume that the elevator is at level 2 and going to level 5.

If the up button of level 3 is pressed - it will stop at level 3 and then continue to level 5.
If the down button of level 3 is pressed - it will go to level 5 without stopping, then come back to level 3 and stop.
Assumptions
The elevator is for a 5 level building.
The elevator has three movement types: up, down, stopped.
The elevator can be at a specific level at a time, no need to consider that it can be in between two levels.
The elevator can be called only from outside buttons (up/down).
A single elevator is being controlled by the buttons.
No need to consider calls from multiple places.
No need to consider concurrency and multi-threading.

#Tasks
Write an Elevator class.

Write a call method in the elevator class, which takes input a Button, using which it has been called.

The call method should return true if the elevator will stop directly, false if it will first move to its current destination and then accept the call.\n

Feel free to write additional classes that might be required.

#Learning goal
Encapsulation

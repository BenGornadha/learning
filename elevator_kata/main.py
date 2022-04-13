from __future__ import annotations

import time

from elevator_kata.elevator import Elevator
from person import Person

if __name__ == '__main__':
    print('--------------INIT-------------')
    my_elevator = Elevator(current_level=0)
    print(my_elevator)
    print('--------------INIT-------------')
    time.sleep(2)
    first_person = Person(level=0, level_target=4)
    second_person = Person(level=2, level_target=0)
    third_person = Person(level=3, level_target=5)
    persons = [first_person, second_person, third_person]
    my_elevator.add_persons_to_take(list_persons=persons)
    my_elevator.go()

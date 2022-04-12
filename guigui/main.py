from __future__ import annotations

import time
from typing import List, Optional

from guigui.Elevator_exceptions import IncorrectLevelException, CannotGoUpper, \
    CannotGoDowner, NoMovementDetectedException


class Elevator:
    MAX_LEVELS = 5
    MIN_LEVELS = 0
    def __init__(self, current_level: int):
        self.current_level: int = current_level
        self.target_level: List[int] = []
        self.next_target_level: List[Optional[int]] = [0]
        self.direction = "up"
        self._my_positions = []
        self.persons_inside: List[Person] = []
        self.persons_outside: List[Person] = []

    def __str__(self):
        return f'Elevator Position : {self.current_level}\nElevator target level : {self.target_level}\nNext target : {self.next_target_level}\n'

    def add_persons_to_take(self, persons: List[Person]):
        self.persons_outside = persons

    def go(self):
        while len(self.persons_outside) != 0:
            closest_person = self.get_closest_person()
            print(f'Closest person is : {closest_person}')
            self._go_to_closest_person(level_of_person=closest_person.level)
            print(f"Arrived at level {self.current_level} for taking in charge : {closest_person}")
            chemin = self.compute_the_way(person=closest_person)
            print(f"Chemin : {chemin}")
            for next_level in chemin:
                print(f"Going to level... {next_level}")
                self.current_level = next_level
                time.sleep(1)
                for index, person in enumerate(self.persons_outside):
                    self.check_if_open_door(index, person)
                if self.current_level == self.target_level[0]:
                    self.open_doors_for_exit()
                if len(self.persons_inside) == 0:
                    print("No one inside elevator...")
                    break

    def check_if_open_door(self, index: int, person: Person) -> None:
        if self.direction == person.direction and self.current_level == person.level:
            print(f"Opening doors at level {self.current_level} for person : {person}")
            self.open_doors_for_entry(index, person)

    def open_doors_for_entry(self, index, person):
        self.persons_inside.append(person)
        self.persons_outside.pop(index)
        if self.persons_inside[-1].level_target >= max(self.target_level):
            self.target_level.append(self.persons_inside[-1].level_target)
            self.target_level.sort()
            print(f"New target level : {self.target_level}")
        else:
            print(f"Target level unchanged: {self.target_level}")

    def open_doors_for_exit(self):
        for person_to_remove_index in self.get_persons_to_exit():
            print(f"Someone leaves the elevator... Person : {self.persons_inside[person_to_remove_index]} ")
            self.persons_inside.pop(person_to_remove_index)

    def update_new_target_level(self):
        new_target_levels = []
        for person in self.persons_inside:
            new_target_levels.append(person.level_target)
        self.target_level = new_target_levels.sort()

    def get_persons_to_exit(self):
        persons_to_remove_indexes = []
        for index, person in enumerate(self.persons_inside):
            if person.level_target == self.current_level:
                persons_to_remove_indexes.append(index)
        return persons_to_remove_indexes

    def get_closest_person(self):
        distance_min = 5
        person_min_index = 0
        for index, person in enumerate(self.persons_outside):
            distance = self._compute_distance_to(person=person)
            if distance < distance_min:
                distance_min = distance
                person_min_index = index

        return self.persons_outside.pop(person_min_index)

    def compute_the_way(self, person: Person) -> List:
        self.target_level.append(person.level_target)
        if person.direction == "up":
            return [level + 1 for level in range(self.current_level, Elevator.MAX_LEVELS)]
        return [level for level in range(person.level_target, Elevator.MIN_LEVELS, -1)]

    def _compute_distance_to(self, person) -> int:
        return abs(self.current_level - person.level)

    def _get_current_direction(self):
        if self._has_to_go_up():
            self.direction = "up"
        if self._has_to_go_down():
            self.direction = "down"

    def _has_to_go_up(self):
        return self.current_level < self.target_level

    def _has_to_go_down(self):
        return self.current_level > self.target_level

    def _go_up(self) -> None:
        if self.current_level < 5:
            self.current_level += 1
        raise CannotGoUpper()

    def _go_down(self) -> None:
        if self.current_level != 0:
            self.current_level -= 1
        raise CannotGoDowner()

    def _has_to_wait(self) -> bool:
        return self.current_level == self.target_level

    def _go_to_closest_person(self, level_of_person: int):
        self.current_level = level_of_person


class Person:

    def __init__(self, level: int, level_target: int):

        self.level = self._extract_level(level)
        self.level_target = self._extract_level(level_target)
        self.direction = self._extract_direction()

    def _extract_level(self, level):
        if level > 5 or level < 0:
            raise IncorrectLevelException
        return level

    def _extract_direction(self):
        self._require_movement()
        if self.level < self.level_target:
            return "up"
        return "down"

    def _require_movement(self):
        if self.level == self.level_target:
            raise NoMovementDetectedException

    def __str__(self):
        return f"Person at level : {self.level}, going to : {self.level_target}"


if __name__ == '__main__':
    # expected = [0, 2, 4, 5, 1, 0]

    print('--------------INIT-------------')
    my_elevator = Elevator(current_level=0)
    print(my_elevator)
    print('--------------INIT-------------')
    time.sleep(2)
    first_person = Person(level=0, level_target=4)
    second_person = Person(level=1, level_target=0)
    third_person = Person(level=2, level_target=5)
    persons = [first_person, second_person, third_person]
    my_elevator.add_persons_to_take(persons=persons)
    my_elevator.go()

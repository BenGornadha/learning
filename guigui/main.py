from __future__ import annotations

import time
from typing import List, Tuple

from guigui.Elevator_exceptions import IncorrectLevelException, NoMovementDetectedException


class Elevator:
    MAX_LEVELS = 5
    MIN_LEVELS = 0

    def __init__(self, current_level: int):
        self.current_level: int = current_level
        self.target_level: List[int] = []
        self.direction = "up"
        self.persons_inside: List[Person] = []
        self.persons_outside: List[Person] = []

    def __str__(self) -> str:
        return f'Elevator Starting Position : {self.current_level}'

    def add_persons_to_take(self, persons: List[Person]) -> None:
        self.persons_outside = persons

    def go(self):
        while len(self.persons_outside) != 0:
            closest_person, closest_person_index = self.get_closest_person_waiting()
            print(f'Closest person waiting is : {closest_person}')
            self._go_to_closest_person(person=closest_person)
            self._someone_enters(index=closest_person_index, person=closest_person)
            chemin = self._compute_levels_until_extremities(person=closest_person)
            for next_level in chemin:
                print(f"Going to level... {next_level}")
                self.current_level = next_level
                time.sleep(1)
                for index, person in enumerate(self.persons_outside):
                    self._check_if_open_door(index, person)
                if self.current_level == self.target_level[0]:
                    self._open_doors_for_exit()
                if len(self.persons_inside) == 0:
                    print("No one inside elevator...")
                    break

    def _check_if_open_door(self, index: int, person: Person) -> None:
        if self.direction == person.direction and self.current_level == person.level:
            print(f"Opening doors at level {self.current_level} for person : {person}")
            self._someone_enters(index, person)

    def _someone_enters(self, index: int, person: Person) -> None:
        print(f"{person} enters...")
        time.sleep(2)
        self.persons_inside.append(person)
        self.persons_outside.pop(index)
        print("Doors closing...")
        if person.level_target >= max(self.target_level, default=0):
            self.target_level.append(person.level_target)
            self.target_level.sort()
        self.direction = person.direction

    def _open_doors_for_exit(self) -> None:
        for person_to_remove_index in self._get_persons_to_exit():
            print(f"{self.persons_inside[person_to_remove_index]} leaves...")
            self.persons_inside.pop(person_to_remove_index)
            self._update_new_target_level()

    def _update_new_target_level(self) -> None:
        new_target_levels = []
        for person in self.persons_inside:
            new_target_levels.append(person.level_target)
        new_target_levels.sort()
        self.target_level = new_target_levels

    def _get_persons_to_exit(self) -> List[int]:
        persons_to_remove_indexes = []
        for index, person in enumerate(self.persons_inside):
            if person.level_target == self.current_level:
                persons_to_remove_indexes.append(index)
        return persons_to_remove_indexes

    def get_closest_person_waiting(self) -> Tuple[Person, int]:
        distance_min = 5
        person_min_index = 0
        for index, person in enumerate(self.persons_outside):
            distance = self._compute_distance_to(person=person)
            if distance < distance_min:
                distance_min = distance
                person_min_index = index
                person_min = person

        return person_min, person_min_index

    def _compute_levels_until_extremities(self, person: Person) -> List:
        if person.direction == "up":
            return [level + 1 for level in range(self.current_level, Elevator.MAX_LEVELS)]
        return [level - 1 for level in range(self.current_level, Elevator.MIN_LEVELS, -1)]

    def _compute_distance_to(self, person) -> int:
        return abs(self.current_level - person.level)

    def _go_to_closest_person(self, person: Person):
        print(f"Going quickly to level : {person.level}!")
        self.current_level = person.level


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
        return f"Person(level={self.level},going={self.level_target})"


if __name__ == '__main__':
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

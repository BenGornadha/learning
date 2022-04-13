from __future__ import annotations

import time
from typing import List, Tuple

from elevator_kata.direction import Direction
from elevator_kata.person import Person


class Elevator:
    MAX_LEVELS = 5  # In this perfect world, only 5 levels building are built.
    MIN_LEVELS = 0  # In this perfect world, no underground are allowed, because no one has a car.

    def __init__(self, current_level: int) -> None:
        self.current_level: int = current_level
        self.target_level: List[int] = []
        self.direction: str = Direction.UP
        self.persons_inside: List[Person] = []
        self.persons_outside: List[Person] = []

    def __str__(self) -> str:
        return f'Elevator Starting Position : {self.current_level}'

    def add_persons_to_take(self, list_persons: List[Person]) -> None:
        self.persons_outside = list_persons

    def go(self) -> None:
        while len(self.persons_outside) != 0:
            self._letting_enter_closest_person_waiting()

            levels = self._compute_levels_until_extremities(direction=self.persons_inside[0].get_direction())
            for next_level in levels:
                print(f"Going to level... {next_level}")
                self.current_level = next_level
                time.sleep(1)

                self._letting_outsiders_get_inside_if_needed()

                if self._someone_has_to_leave():
                    self._open_doors_for_exit()

                if not self.persons_inside:
                    print("No one inside elevator...")
                    break

    def _someone_has_to_leave(self) -> bool:
        return self.current_level == self.target_level[0]

    def _letting_enter_closest_person_waiting(self) -> None:
        closest_person, closest_person_index = self.get_closest_person_waiting()
        print(f'Closest person waiting is : {closest_person}')
        self._go_to_closest_person(person=closest_person)
        self._someone_enters(index=closest_person_index, person=closest_person)

    def _letting_outsiders_get_inside_if_needed(self) -> None:
        for index, person in enumerate(self.persons_outside):
            if self._check_if_worth_opening_door(person):
                print(f"Opening doors at level {self.current_level} for person : {person}")
                self._someone_enters(index, person)

    def _check_if_worth_opening_door(self, person: Person) -> bool:
        return self._has_same_direction(direction=person.get_direction()) and self._is_waiting_at_this_level(
            level=person.get_level())

    def _has_same_direction(self, direction: str) -> bool:
        return self.direction == direction

    def _is_waiting_at_this_level(self, level: int) -> bool:
        return self.current_level == level

    def _someone_enters(self, index: int, person: Person) -> None:
        print(f"{person} enters...")
        time.sleep(2)
        self.persons_inside.append(person)
        self.persons_outside.pop(index)
        print("Doors closing...")
        if person.get_level_target() >= max(self.target_level, default=0):
            self.target_level.append(person.get_level_target())
            self.target_level.sort()
        self.direction = person.get_direction()

    def _open_doors_for_exit(self) -> None:
        for person_to_remove_index in self._get_persons_to_exit():
            print(f"{self.persons_inside[person_to_remove_index]} leaves...")
            self.persons_inside.pop(person_to_remove_index)
            self._update_new_target_level()

    def _update_new_target_level(self) -> None:
        new_target_levels = []
        for person in self.persons_inside:
            new_target_levels.append(person.get_level_target())
        new_target_levels.sort()
        self.target_level = new_target_levels

    def _get_persons_to_exit(self) -> List[int]:
        persons_to_remove_indexes = []
        for index, person in enumerate(self.persons_inside):
            if person.get_level_target() == self.current_level:
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

    def _compute_levels_until_extremities(self, direction: str) -> List:
        if direction == Direction.UP:
            return [level + 1 for level in range(self.current_level, Elevator.MAX_LEVELS)]
        return [level - 1 for level in range(self.current_level, Elevator.MIN_LEVELS, -1)]

    def _compute_distance_to(self, person) -> int:
        return abs(self.current_level - person.get_level())

    def _go_to_closest_person(self, person: Person) -> None:
        print(f"Going quickly to level : {person.get_level()}!")
        self.current_level = person.get_level()
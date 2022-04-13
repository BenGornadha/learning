from __future__ import annotations

from typing import List




class Person:
    def __init__(self, level: int, level_target: int) -> None:
        self.level = level
        self.level_target = level_target
        self.direction = self._direction()
        self.distance = 0

    def _direction(self) -> str:
        if self.level > self.level_target:
            return "down"
        return "up"


class Elevator2:

    def __init__(self, current_level: int):
        self.current_level: int = current_level
        self.persons_inside: List[Person] = []
        self.persons_outside: List[Person] = []
        self.direction = "up"

    def __str__(self):
        return f'Elevator Position : {self.current_level}\n'

    def add_persons_outside(self, persons: List[Person]):
        self.persons_outside = persons

    def update_current_level(self):
        if self.persons_outside:
            min_distance_person = 5
            max_level_outside = 0
            person_with_min_distance = None

            for person in self.persons_outside:
                person.distance = abs(self.current_level - person.level)
                if person.level >= max_level_outside:
                    max_level_outside = person.level
                if person.distance <= min_distance_person:
                    if person.direction == self.direction:
                        person_with_min_distance = person

            if person_with_min_distance is None:
                person_with_min_distance = self.persons_outside[0]

            self.persons_inside.append(person_with_min_distance)
            self.persons_outside.remove(person_with_min_distance)

            max_level_inside = 0
            min_level_target_inside = 5
            for person in self.persons_inside:
                if person.level_target >= max_level_inside:
                    max_level_inside = person.level_target
                if person.level_target <= min_level_target_inside:
                    min_level_target = person.level_target

            print('---' * 50)
            print(f"Current level ={self.current_level}")
            self.current_level = min(person_with_min_distance.level, min_level_target)
            print(f"New Current level ={self.current_level}")
            print('---' * 50)
            maximum = max(max_level_outside, max_level_inside)
            if self.current_level == maximum:
                self._change_direction()

            self.update_current_level()

    def _change_direction(self):
        if self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "up"

if __name__ == '__main__':
    one_elevator = Elevator2(current_level=0)
    first_person = Person(level=0, level_target=4)  # up
    second_person = Person(level=1, level_target=0)  # down
    third_person = Person(level=2, level_target=5)  # up
    persons = [first_person, second_person, third_person]
    one_elevator.add_persons_outside(persons)
    one_elevator.update_current_level()
        # expected = [0, 2, 4, 5, 1, 0]

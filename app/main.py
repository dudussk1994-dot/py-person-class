class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person.name, person.age)
    result_list = []
    for person in Person.people:
        person_instance = Person.people[person["name"]]
        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)
        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            setattr(person_instance, spouse_key, spouse_instance)
        else:
            setattr(person_instance, spouse_key, None)
        result_list.append(person_instance)
    return result_list

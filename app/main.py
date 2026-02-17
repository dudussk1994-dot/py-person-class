class Person:
    # write your code here
    pass
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # write your code here
    pass
    [Person(p.get("name"), p.get("age")) for p in people]
    result_list = []
    for person in people:
        person_instance = Person.people.get(person("name"))
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name:
            setattr(person_instance, "wife", wife_name)
        if husband_name:
            setattr(person_instance, "husband", husband_name)
        result_list.append(person_instance)
    return result_list

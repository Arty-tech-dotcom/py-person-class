class Person:
    people = {}  # Class attribute to store Person instances by name

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self  # Add instance to people dictionary


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        new_person = Person(name, age)

        # Link spouses
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_dict:
                    new_person.wife = spouse
                else:
                    new_person.husband = spouse

        person_list.append(new_person)
    return person_list

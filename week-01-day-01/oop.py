class Person:  # Base class or super class
    # Object constructor (or initializer)
    def __init__(self, firstname, age, address):
        print("Person created")

        # Properties (or attributes)
        self.firstname = firstname
        self.age = age
        self.address = address

    # Methods
    def eat(self):
        print(f"{self.firstname} is eating")

    def walk(self):
        print(f"{self.firstname} is walking")

    def run(self):
        print(f"{self.firstname} is running")


class Male(Person):  # Derived class (inherits Person class)
    def __init__(self, firstname, age, address):
        # Initialize the base class Person with the respective parameters
        super().__init__(firstname, age, address)
        # Does the same as:
        # Person.__init__(self, firstname, age, address)

        # Access the properties
        print("Male created"
              f"\nFirst name: {self.firstname}"
              f"\nAge: {self.age}"
              f"\nAddress: {self.address}\n")


class Female(Person):  # Derived class (inherits Person class)
    def __init__(self, firstname, age, address):
        super().__init__(firstname, age, address)

        print("Female created"
              f"\nFirst name: {self.firstname}"
              f"\nAge: {self.age}"
              f"\nAddress: {self.address}")


if __name__ == "__main__":
    # Instantiate object of Male class
    m = Male("Guido", 65, "Netherlands")

    # Instantiate object of Female class
    # For named arguments, the arguments can be in any order
    f = Female(address="Virgina", age=85, firstname="Grace")

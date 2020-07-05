class Person:
    def __init__(self, first_name, middle_name, last_name, age, gender, birthday):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = int(age)
        self.gender = None

        if gender in ["male", "female"]:
            self.gender = gender
        else:
            raise Exception(f"Invalid Gender {gender}")

        self.birthday = str(birthday)
        self.degrees = []
        self.occupation = []
        self.hobbies = []

    def add_degree(self, degrees):
        self.degrees.append(degrees)

    def set_degree(self, degrees):
        self.degrees = [] if degrees is None else degrees

    def add_occupation(self, occupation):
        self.occupation.append(occupation)

    def set_occupation(self, occupation):
        self.occupation = [] if occupation is None else occupation

    def add_hobbies(self, hobbies):
        self.hobbies.append(hobbies)

    def set_hobbies(self, hobbies):
        self.hobbies = [] if hobbies is None else hobbies

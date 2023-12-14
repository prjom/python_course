print('Задание№2, 3')

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.num_students = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
        self.num_students += 1

class Student(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)

    def __len__(self):
        return len(self.knowledge)

    def random_forget(self):
        if self.knowledge:
            import random
            random_index = random.randint(0, len(self.knowledge) - 1)
            forgotten_material = self.knowledge.pop(random_index)
            print(f"{self.name} случайно забыл {forgotten_material}!")
        else:
            print(f"{self.name} не имеет знаний для забывания.")

class StudyMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):
        return len(self.materials)

study_materials = StudyMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher("Иванов", 35, "М")

student1 = Student("Петров", 18, "М")

teacher.teach(study_materials.materials[0], student1)

print(f"Количество знаний студента: {len(student1)}")
print(f"Количество материалов: {len(study_materials)}")

student1.random_forget()

print(f"Количество знаний студента после забывания: {len(student1)}")


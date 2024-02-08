import random


class Pupil:
    def __init__(self, name, knowledge):
        self.name = name
        self.knowledge = knowledge

    def randomly_forget(self, forget_percentage):
        forget_percentage = min(1, max(0, forget_percentage))
        forget_count = int(len(self.knowledge) * forget_percentage)
        forget_indices = random.sample(range(len(self.knowledge)), forget_count)

        for index in forget_indices:
            self.knowledge[index] = None

    def display_knowledge(self):
        print(f"Знания ученика {self.name}:")
        for knowledge_item in self.knowledge:
            if knowledge_item is not None:
                print("- " + knowledge_item)
            else:
                print("- Забыто")

pupil = Pupil("Roman", ["Математика", "Физика", "История", "Литература", "Химия"])
pupil.display_knowledge()

pupil.randomly_forget(0.3)
pupil.display_knowledge()
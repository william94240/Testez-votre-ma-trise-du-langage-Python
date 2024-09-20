students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

input_student = input("Entrez le nom de l’étudiant : ")
if input_student in students:
     print(f"Notes de {input_student}:")
     [print(f"{subject}: {note}") for subject, note in students[input_student].items()]    
     print(f"Moyenne de {input_student}: {sum(students[input_student].values())/len(students[input_student])}")
else:
     print(f"L'étudiant {input_student} n'existe pas dans la liste.")
     exit()


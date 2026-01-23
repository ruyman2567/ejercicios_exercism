"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    estudiantes=[]
    for calif in student_scores:
        estudiantes.append(round(calif))
    return estudiantes

def count_failed_students(student_scores):
    contador=0
    for calif in student_scores:
        if calif>40:
            continue
        else:
            contador+=1
    return contador


def above_threshold(student_scores, threshold):
    lista1=[]
    for calif in student_scores:
        if calif>=threshold:
            lista1.append(calif)
    return lista1


def letter_grades(highest):
    grades=[]
    steps= int((highest-40)/4)
    for calif in range(41,highest,steps):
        grades.append(calif)
    return grades

def student_ranking(student_scores, student_names):
    final_grades=[]
    n=1
    for index, name in enumerate(student_names):
        final_grades.append(f'{n}. {name}: {student_scores[index]}')
        n+=1
    return final_grades


def perfect_score(student_info):
    for i in student_info:
        if (len(i)>0) and i[1] == 100:
            return i
            
    return []


import datetime
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

def calculate_final_exam_score(grades, cutoffs, current_grade, exam_weight):
    final_exam_scores = {}
    zero_hit = False
    for grade, cutoff in zip(grades, cutoffs):
        score_needed = (cutoff - (current_grade * (1 - exam_weight))) / exam_weight
        if score_needed < 0 and not zero_hit:
            score_needed = 0
            zero_hit = True
        elif score_needed < 0 and zero_hit:
            score_needed = "N/A"
        final_exam_scores[grade] = score_needed
    return final_exam_scores

def print_final_exam_scores(grades, cutoffs, current_grade, exam_weight, class_name):
    final_exam_scores = calculate_final_exam_score(grades, cutoffs, current_grade, exam_weight)
    
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d")

    for grade, score_needed in final_exam_scores.items():

        file_name = f"FinalExamScoresNeeded-{class_name}-{formatted_datetime}.txt"

        with open(file_name, "w") as file:
            file.write("Final Exam Scores Needed\n")
            file.write("\n")
            file.write(f"Class Name: {class_name}\n")
            file.write(f"Date/Time: {formatted_datetime}\n")
            
            for grade, score_needed in final_exam_scores.items():
                if score_needed == "N/A":
                    file.write(f"\n{grade}\t{score_needed}")
                else:
                    file.write(f"\n{grade}\t{score_needed:.2f}")

grades = ['A', 'AB', 'B', 'BC', 'C', 'D', 'F']
cutoffs = [93, 90, 84, 80, 74, 67, 0]
current_grade = 100
exam_weight = 0.15

print_final_exam_scores(grades, cutoffs, current_grade, exam_weight, "ME368")

grades = ['A', 'AB', 'B', 'BC', 'C', 'D', 'F']
cutoffs = [92, 88, 82, 78, 72, 62, 0]
current_grade = 95.92
exam_weight = 0.2

print_final_exam_scores(grades, cutoffs, current_grade, exam_weight, "ME370")
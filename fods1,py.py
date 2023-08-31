import numpy as np

num_students = 4
num_subjects = 4
subjects = ['Math', 'Science', 'English', 'History']

student_scores = np.array([[int(input(f"Enter {subjects[j]} score for student {i+1}: ")) for j in range(num_subjects)] for i in range(num_students)])

print("Student Scores Matrix:")
print(student_scores)

average_scores = np.mean(student_scores, axis=0)

highest_average_subject_index = np.argmax(average_scores)
highest_average_subject = subjects[highest_average_subject_index]

print("Average scores for each subject:", subjects,average_scores)
print("Subject with the highest average score:", highest_average_subject)
'''
Enter Math score for student 1: 67
Enter Science score for student 1: 78
Enter English score for student 1: 89
Enter History score for student 1: 90
Enter Math score for student 2: 89
Enter Science score for student 2: 87
Enter English score for student 2: 67
Enter History score for student 2: 65
Enter Math score for student 3: 78
Enter Science score for student 3: 86
Enter English score for student 3: 56
Enter History score for student 3: 67
Enter Math score for student 4: 55
Enter Science score for student 4: 76
Enter English score for student 4: 98
Enter History score for student 4: 99
Student Scores Matrix:
[[67 78 89 90]
 [89 87 67 65]
 [78 86 56 67]
 [55 76 98 99]]
Average scores for each subject: ['Math', 'Science', 'English', 'History'] [72.25 81.75 77.5  80.25]
Subject with the highest average score: Science

'''

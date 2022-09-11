from operator import le


students = ["egoing", "sori", "maru"]
grades = [2,1,4]
print("students[1]",students[1])
print("len(students)", len(students))
print("min(grades)",min(grades))
print("max(grades)",max(grades))

import statistics #통계
print("statistics.mean(grades)",statistics.mean(grades)) #평균

import random #제비뽑기
print("random.choice(students)",random.choice(students))



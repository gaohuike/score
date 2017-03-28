import os
import os.path
def get_filelist(filedir):
    filelist = []
    for parent,dirnames,filenames in os.walk(filedir):
        for filename in filenames:
            filelist.append(os.path.join(parent,filename))
    return filelist

def readfile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

def scoring(standard_answer,student_answer):
    L = len(standard_answer)
    score = 0
    for i in range(L):
        if standard_answer[i] == student_answer[i]:
            score = score + 3
        else:
            score = score - 2
    return score

def mark_the_test(src1,src2):
    stand_answer = readfile(src1)
    student_list = get_filelist(src2)
    score = []
    for i in student_list:
        student_answer = readfile(i)
        j = scoring(stand_answer, student_answer)
        print j
        score.append(j)
    print score
    return score


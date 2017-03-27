import os
import os.path
def get_filelist(filedir):
    filelist = []
    for parent,dirnames,filenames in os.walk(filedir):
        for filename in filenames:
            filelist.append(os.path.join(parent,filename))
            #print "filename is:" + filename
    return filelist

def readfile(filename):
    f = open(filename)
    lines = f.readlines()
    file_content= []
    for line in lines:
        file_content.append(line)
    f.close()
    return file_content

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
    return score


mark_the_test('C:\Users\hgao\PycharmProjects\ghk\standard_answer.txt','C:\Users\hgao\PycharmProjects\ghk\student_answer')
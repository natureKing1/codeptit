n=int(input())
subjects=[]
for _ in range(n):
    subject_code=input().strip()
    subject_name = input().strip()
    subject_format = input().strip()
    subjects.append((subject_code,subject_name,subject_format))
subjects.sort(key= lambda x: x[0])
for code,name,format in subjects:
    print(code,name,format)
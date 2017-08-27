def round(grade):
    q, r = divmod(grade, 5)
    if grade > 37 and r > 2:
        grade = (q + 1)*5
    return grade

if __name__ == '__main__':
    for _ in range(int(input())):
        print(round(int(input())))

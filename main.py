def task_1(num):
    if num <= 0:
        return "Not correct age"
    if 0 < num <= 18:
        return "You are underage"
    if num > 18:
        return "You are adult"


def task_2(a, b):
    reminder = a%b
    if reminder == 0:
        return f"divide, {a/b}" 
    else:
        return f"with reminder {reminder}"


def task_3(salary, working=0):
    if 1 <= working <= 3:
        salary += salary * 0.1
    elif working > 3:
        salary += salary * 0.2
    if salary <= 4000:
        salary += 1000
    elif salary > 4000:
        salary +=500
    return salary



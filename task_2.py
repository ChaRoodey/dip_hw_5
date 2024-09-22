def lis_gen(names: list, salary: list, bonus: list):
    return {names[i] : round(float(bonus[i].strip('%')) * salary[i] / 100, 2) for i in range(len(names))}


names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

print(lis_gen(names, salary, bonus))
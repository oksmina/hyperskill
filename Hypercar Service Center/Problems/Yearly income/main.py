with open("salary.txt", "r") as salary, open("salary_year.txt", "a") as salary_year:
    for sal in salary:
        sal_i = int(sal.rstrip('\n'))
        salary_year.write(str(sal_i * 12) + ' \n')
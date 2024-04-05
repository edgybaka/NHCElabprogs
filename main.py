def salary(bs):
    ta=(10/100)*bs
    da=(12/100)*bs
    gs=bs+ta+da
    return gs
bs=float(input('Enter base salary: '))
print("Your Gross Salary is:",salary(bs))
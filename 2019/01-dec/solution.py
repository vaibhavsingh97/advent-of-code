from math import floor

res = 0
recursive_res = 0

# Part 1 solution
def get_fuel(mass):
    return floor(int(mass)/3) - 2

# Part 2 solution
def recursive_get_fuel(mass, sum=0):
    if mass <= 0:
        return sum
    new_fuel = get_fuel(mass)
    return recursive_get_fuel(new_fuel, sum + max(0, new_fuel))

with open('input.txt') as file:
    for num in file:
        mass = int(num)
        res += get_fuel(mass)
        recursive_res += recursive_get_fuel(mass)

print(f"Normal fuel sum: {res}")
print(f"Recursive fuel sum: {recursive_res}")

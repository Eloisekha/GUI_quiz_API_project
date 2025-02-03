# age: int
# name: str
# height: float
# is human: bool

# age = 12
# age ='twelve' #error

# TYPE HINTS
def greeting(name: str) -> str:
    return 'Hello '+name

def police_check(age: int) -> bool: #Type Hints
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive

if police_check(17):
    print("You may pass")
else:
    print("Pay a fine")

print(greeting('Kha'))
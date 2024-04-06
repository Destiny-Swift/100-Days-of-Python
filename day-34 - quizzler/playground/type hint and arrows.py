# variables can be created by assigning a data type and not a value like so:

# age: int
# name: str
# height: float
# is_human: bool


# type hints are also used in function args to specify type of data to be passed, saves from errors...
def police_check(age: int) -> bool:  # int arg, bool return
    if age >= 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive  # you get notified when return is not of data type "bool" as specified above


if police_check(12):  # you get notified when any data type besides int is passed into the int specified arg
    print('You may pass')
else:
    print('Pay a fine!')

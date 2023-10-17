# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    """
    Determines if a person is eligible to drive based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        bool: True if the person is 18 years or older, False otherwise.
    """
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass")
else:
    print("Pay a fine.")

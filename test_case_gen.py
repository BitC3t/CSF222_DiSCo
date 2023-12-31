"""
DiSCo 2023 - 24
Advik, Druva, Kushagra

[TEST CASE GENERATOR]
This is a custom script that generates test cases based on the config.json.
"""

import json
import random
import uuid

# Open and read configuration data from a JSON file
f = open("config/config.json")
data = json.load(f)

# Extract configuration parameters
prof_num = data["professors"]
fd_cout = data["fd_c"]
fd_eout = data["fd_e"]
hd_cout = data["hd_c"]
hd_eout = data["hd_e"]
total = data["total"]

# Initialize lists to store course categories
professors = []
fd_c = []
fd_e = []
hd_c = []
hd_e = []


def getRandomUUID():
    """
    Generate and return a random UUID.

    Returns:
    - str: Random UUID as a string.
    """
    return str(uuid.uuid4())


# Generate lists of professor names and course categories
for i in range(prof_num):
    professors.append("Professor " + str(i))

for j in range(fd_cout):
    fd_c.append("(FD-CDC) CS FP" + f"{j:02d}")

for k in range(fd_eout):
    fd_e.append("(FD-E) CS FQ" + f"{k:02d}")

for l in range(hd_cout):
    hd_c.append("(HD-CDC) CS FR" + f"{l:02d}")

for m in range(hd_eout):
    hd_e.append("(HD-E) CS FS" + f"{m:02d}")


def generate():
    """
    Generate random values for the number of professors in each course load category.

    Returns:
    - Tuple: Randomly generated values for x, y, and z.
    """
    x = random.randint(0, prof_num)
    rem = prof_num - x
    tot_rem = total - 0.5 * x
    z = 2 * (tot_rem - rem)
    y = rem - z
    if x < 0 or y < 0 or z < 0:
        return generate()
    else:
        return x, y, z


x, y, z = map(int, generate())
print(x, y, z)


def randomly_group():
    """
    Randomly assign professors to different course load categories.

    Returns:
    - float: Course load category assigned to a professor (0.5, 1, or 1.5).
    """
    global x, y, z
    l = [0.5] * x + [1] * y + [1.5] * z
    rand = randomly_pick(l, 1)[0]
    if rand == 0.5:
        x -= 1
        return 0.5
    elif rand == 1:
        y -= 1
        return 1
    elif rand == 1.5:
        z -= 1
        return 1.5


def randomly_pick(array, num):
    """
    Randomly pick elements from an array.

    Parameters:
    - array: List from which elements will be picked.
    - num: Number of elements to pick.

    Returns:
    - list: List of randomly picked elements.
    """
    T = random.sample(array, num)
    return T


# Adjust total if there are more course categories than the total number of courses
if total > (hd_eout + hd_cout + fd_eout + fd_cout):
    rem = total - hd_cout - hd_eout - fd_cout - fd_eout
    for i in range(rem):
        random_num = random.randint(0, 3)
        if random_num == 0:
            fd_c.append("(FD-CDC) CS FP" + f"{i + len(fd_c):02d}")
        elif random_num == 1:
            fd_e.append("(FD-E) CS FQ" + f"{i + len(fd_e):02d}")
        elif random_num == 2:
            hd_c.append("(HD-CDC) CS FR" + f"{i + len(hd_c):02d}")
        elif random_num == 3:
            hd_e.append("(HD-E) CS FS" + f"{i + len(hd_e):02d}")

# Initialize dictionary to store generated data
new_data = {}

# Generate and assign courses to professors
for prof in professors:
    FD_c = randomly_pick(fd_c, fd_cout)
    FD_e = randomly_pick(fd_e, fd_eout)
    HD_c = randomly_pick(hd_c, hd_cout)
    HD_e = randomly_pick(hd_e, hd_eout)

    courses = {
        "FD_CDC": {str(i + 1): FD_c[i] for i in range(fd_cout)},
        "FD_Electives": {str(i + 1): FD_e[i] for i in range(fd_eout)},
        "HD_CDC": {str(i + 1): HD_c[i] for i in range(hd_cout)},
        "HD_Electives": {str(i + 1): HD_e[i] for i in range(hd_eout)},
    }

    new_data[prof] = {
        "id": getRandomUUID(),
        "group": randomly_group(),
        "courses": courses,
    }

# Save generated data to a JSON file
with open("input.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)

print("Test Case Generated and Auto Saved!")

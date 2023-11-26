import json
import random
import uuid

f = open("config.json")

data = json.load(f)

prof_num = data["professors"]
fd_cout = data["fd_c"]
fd_eout = data["fd_e"]
hd_cout = data["hd_c"]
hd_eout = data["hd_e"]

professors = []
fd_c = []
fd_e = []
hd_c = []
hd_e = []


def randomly_pick(array, num):
    T = random.sample(array, num)

    return T


def randomly_group():
    l = [0.5, 1, 1.5]

    return random.sample(l, 1)


def getRandomUUID():
    return str(uuid.uuid4())


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

new_data = {}

for prof in professors:
    FD_c = randomly_pick(fd_c, fd_cout)
    FD_e = randomly_pick(fd_e, fd_eout)
    HD_c = randomly_pick(hd_c, hd_cout)
    HD_e = randomly_pick(hd_e, hd_eout)

    courses = {
        "FD_CDC": {str(i+1): FD_c[i] for i in range(fd_cout)},
        "FD_Electives": {str(i+1): FD_e[i] for i in range(fd_eout)},
        "HD_CDC": {str(i+1): HD_c[i] for i in range(hd_cout)},
        "HD_Electives": {str(i+1): HD_e[i] for i in range(hd_eout)},
    }

    new_data[prof] = {
        "id": getRandomUUID(),
        "group": 1,
        "courses": courses,
    }

with open("input.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)

print("Test Case Generated and Auto Saved!")

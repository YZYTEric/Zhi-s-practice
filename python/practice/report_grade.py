gpa_dict = {"Eric":56, "Kenny":65, "Jenny":70, "David": 50, "Jack": 40}

for name, gpa in gpa_dict.items():
    if gpa >= 50:
        print ("{0}, your grade is: {1}"". well done!".format(name, gpa))
    else:
        print ("{0}, your grade is: {1}"". you need working hard.".format(name, gpa))
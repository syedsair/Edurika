from flask import Flask, request


app = Flask(__name__)


@app.route('/announcements/')
def announcements():
    file = open("Announcements")
    lines = file.readlines()
    str = ""
    for line in lines:
        str += line
        str += "$"
    return str


@app.route('/validate/')
def validate():
    rollno = request.args.get('rollno')
    password = request.args.get('pass')
    file = open("Validate")
    lines = file.readlines()
    rollnumber = ""
    for line in lines:
        if rollnumber != "":
            if line[:-1] == password:
                return "Correct"
            else:
                return "Incorrect"
        if line[:-1] == rollno:
            rollnumber = line
    return "Incorrect"


@app.route('/tentativestudyplan/')
def tentativestudyplan():
    file = open("TSP")
    lines = file.readlines()
    str = ""
    for line in lines:
        str += line
        str += "$"
    return str


@app.route('/personaldetails/')
def personaldetails():
    rollno = request.args.get('rollno')
    file = open("Students")

    i = 1
    while True:
        name = file.readline()[:-1]
        guardian = file.readline()[:-1]
        cnic = file.readline()[:-1]
        dob = file.readline()[:-1]
        phone = file.readline()[:-1]
        roll = file.readline()
        sec = file.readline()[:-1]
        batch = file.readline()[:-1]
        degree = file.readline()[:-1]
        status = file.readline()[:-1]

        i += 1
        roll = roll[:8]

        if roll == rollno:
            return name+"$"+guardian+"$"+cnic+"$"+dob+"$"+phone+"$"+roll+"$"+sec+"$"+batch+"$" + degree+"$"+status
        else:
            print(name+"$"+guardian+"$"+cnic+"$"+dob+"$"+phone+"$"+roll+"$"+sec+"$"+batch+"$" + degree+"$"+status)
            if i == 6:
                break

    return "Invalid Roll No"


@app.route('/transcript/')
def transcript():
    rollno = str(request.args.get('rollno'))
    rollno = int(rollno[4:])
    if 1000 <= rollno <= 1004:
        rollno = request.args.get('rollno')
        file = open("Transcript")
        lines = file.readlines()
        l = ""
        for line in lines:
            l += line
            l += "%%"
        return l
    else:
        return "Invalid Roll Number"


@app.route('/attendance/')
def attendance():
    rollno = str(request.args.get('rollno'))
    file = open("Attendance")
    for i in range(0, 5):
        roll = file.readline()[:-1]
        data = file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline()
        if roll == rollno:
            return data
        else:
            pass
    else:
        return "Invalid Roll Number"


@app.route('/marks/')
def marks():
    rollno = str(request.args.get('rollno'))
    file = open("Marks")
    for i in range(0, 5):
        roll = file.readline()[:-1]
        data = file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline() + "%%" + file.readline()
        if roll == rollno:
            return data
        else:
            pass
    else:
        return "Invalid Roll Number"


@app.route('/')
def home():
    return "Hello from Edurica Server"


if __name__ == '__main__':
    app.run(host="0.0.0.0")


# host on heroku or pythonanywhere

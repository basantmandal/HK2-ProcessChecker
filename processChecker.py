import psutil
import subprocess
import smtplib

print("\n")
print('\n** Search Running Process Using List Comprehension **')

#  Pass the Process that needs to be checked & Check, If process run under this user.
processname = 'java'
cloudways_user = 'basant-k2'

pid_counter = 0

# ================ Find PIDs of all process & Check If User matches with Process Name Java ================ #
procObjList = [procObj for procObj in psutil.process_iter(['pid', 'name', 'username'])
               if processname in procObj.name().lower()]

for elem in procObjList:
    if(elem.info["username"] == cloudways_user):
        pid_counter += 1
    print(elem.info)

print("** Lets Check if Process needs to run ? **")
if pid_counter < 1:
    print("** Yes Process = " + processname + " Needs to Run...")
    subprocess.call('./fire_service.sh')

    # ================ Sending Email - Process Fired - Start ================ #
    s = smtplib.SMTP('smtp.office365.com', 587)
    s.starttls()
    s.login("demo_test@outlook.com", "demo_password")
    message = """\
    Subject: HK2 Python App Fired - Java Services

    Hi the HK2 Python Process Checked App for keeping alive Java Services has been fired"""

    s.sendmail("recipient@mail.com", message)
    s.quit()
    # ================ Sending Email Ends ================ #
else:
    print("** No - The Process = " + processname + " Does not need to run...")
    print("** Interceptor Exist **")

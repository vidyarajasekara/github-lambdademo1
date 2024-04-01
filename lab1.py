from _datetime import datetime
name="vidya rajasekaran"
course="cnet142-python programming"
print(name)
print(course)
t=datetime.today().strftime("%b-%d-%y %a (%I:%M:%S %p)")
print(t)
print(f"datetime is:{t}")
print("{:10}".format("name:"),name)
print("{:13}".format("time:"),t)
print(f"time:{t}")




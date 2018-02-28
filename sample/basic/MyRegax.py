import re
emailReg = re.compile(r"^\w+$")
print(emailReg.match("Email"));

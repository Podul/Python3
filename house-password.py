import re

# 是否包含数字 
# 是否包含大写字母
# 是否包含小写字母
def checkio(data):
    a = re.compile(r"^(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z]).{10,}$")
    return bool(a.match(data))

print(checkio('ASDsad'))
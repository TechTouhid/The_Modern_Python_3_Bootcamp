import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res = pattern.search('335 457-9876 or 777 888-9999')
print(res)
print(res.group())
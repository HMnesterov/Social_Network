import re
import random
s = re.compile(r'([A-Za-z0-9]{2}[:-]){5}[A-Za-z0-9]')
print(random.sample('1234111111111111111', 5))
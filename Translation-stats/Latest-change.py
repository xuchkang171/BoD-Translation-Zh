import re
import urllib.request
from datetime import date


fetch = urllib.request.urlopen("https://raw.githubusercontent.com/xuchkang171/BoD-Translation-Zh/master/README.md").read()
fetch = str(fetch, 'utf-8')
last_progress = re.search(r".+\((\d+)/\d+\).*\n" * 5, fetch)
last_progress = [int(x) for x in last_progress.groups()]

text = ""
present_percentage = ""
with open ("Progress.txt", "r") as myfile:
    text = myfile.read()
    present_percentage = re.search(r" (\d+)%", text)
    present_percentage = int(present_percentage.group(1))
present_progress = re.search(r".+\((\d+)/\d+\).*\n" * 5, text)
present_progress = [int(x) for x in present_progress.groups()]

update = list(present-last for present,last in zip(present_progress,last_progress))

details = "%+d: launcher:%+d / main:%+d / cards:%+d / gossips:%+d" % tuple(update)
# 2017-10-24：46% (+70: launcher: +0 / main: +14 / cards: +8 / gossips: +48)
print("{date}: {percentage}% ({details})".format(date=date.today(), percentage=present_percentage, details=details))
is_cold=True
is_hot=True
is_cold=False
if is_cold:
    print("Its cold day")
    print("Enjoy cold")
elif is_hot:
    print("Hot")
    print("Enjoy hot")
else:
    print("Fuck off")
is_cold=False
if is_cold:
    print("Its cold day")
print("Enjoy")#should keep in one line like first one

has_high_cgpa=True
has_good_credit=True
has_skills=True

if has_high_cgpa and has_good_credit :
    print("Eligible for TA")
has_high_cgpa=False
if has_high_cgpa or has_skills:
    print("Go for jobs")
has_high_cgpa=True
has_skills=False
if has_high_cgpa and not has_skills:
    print("Fuck off")
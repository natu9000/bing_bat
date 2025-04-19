import random 
import string

def generate_random_string():
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars) for _ in range(3))
    return random_string

for i in range(1,31):
    #url_ran = generate_random_string()
    url_content = """[InternetShortcut]\nURL="""
    with open(str(i) + ".url", "w") as file:
        file.write(url_content)
#print(url_ran)
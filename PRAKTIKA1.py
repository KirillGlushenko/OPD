def make_shirt(text, size):
    print("text: " + text)
    print("size: " + size)
make_shirt('Текст на футболке', 'XL')
# Результат: https://clck.ru/328bbE

def make_shirt(size = "L", text = "I love python"):
print("size: " + size)
print("text: " + text)
make_shirt()
make_shirt('XL','Big tshort')
# Результат: https://clck.ru/328bbp

def get_name(first_name, last_name):
    full_name =f"ФИО: {first_name} {last_name}"
    return full_name.title()
def get_student(department, speciality):
    college = f"Специальность и отделение: {department} {speciality}"
    return college.title()
fullname = get_name( 'Кирилл', 'Глушенко' )
print(fullname)
college = get_student('Связи и телекоммуникации', 'Прикладная информатика')
print(college)
# Результат: https://clck.ru/328brf

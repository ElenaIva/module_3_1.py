
calls = 0         #переменная для подсчета вызовов функций

def count_calls():        #функция для подсчета вызовов
    global calls
    calls += 1

def string_info(string):        #функция string_info
    count_calls()
    return len(string), string.upper(), string.title()

string1 = string_info('elephant')
string2 = string_info('wonderful')
string3 = string_info('peace')

print(string1)
print(string2)
print(string3)

def is_contains(string, list_to_search):           #функция is_contains
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

is_contains1 = is_contains('John', ['Joe', 'Daddy', 'joHN', 'jo'])
is_contains2 = is_contains('Bible', ['bubble', 'Bobby', 'nice'])

print(is_contains1)
print(is_contains2)

print(calls)      #всего вызовов







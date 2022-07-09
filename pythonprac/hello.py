print('hello sparta')

a=2
b=3
print(a+b)

first_name = 'seunghyun'
num = str(2)
print(first_name+num)

a_list = ['사과', '배', '감']
print(a_list[0])
a_list.append('수박')
print(a_list)

a_dict = {'name':'bob', 'age':27}
print(a_dict['age'])
a_dict['height'] = 178
print(a_dict)

# : 는 : 앞의 함수에 대한 내용물 즉 {} 대신 :
def sum(num1, num2):
    return num1+num2
result = sum(2,3)
print(result)

# tap 즉 줄 위치가 매우 중요
def is_adult(age):
    if age > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')
is_adult(30)
is_adult(15)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if fruit == '배':
        count += 1
print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]
for person in people:
    if person['age'] < 20:
        print(person)
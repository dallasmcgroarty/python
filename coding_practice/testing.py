d = {'Thomas':1,'Bobby':2,'Carlos':3}

for i in d:
    print (i)

str1 = 'Hey its me George Bush'
s = str1.split(' ')
print(s)
p = str1.find('George Bush')
x = p + len('George Bush')
print(p,x)
# i = p + len('George Bush')-1
# print('at index', p)
# print(len(str1))
print(i)

if 'George' in str1:
    print('found!')

str2 = '123'
print(len(str2))
name = 'John Adams'
print(len(name))

m = 'George H. W. Bush'
dd = m.split(' ')
print(dd[-1])

info = (1,'fff','fff')
print(info)

a = []
a.append(info)
print(a)

str3 = 'When was Richard Nixon president?'
start = str3.find('Richard Nixon')
end = start + len('Richard Nixon')
print(start,end)

presidents = {'George Washington':1, 'John Adams':2, 'Thomas Jefferson':3, 'James Madison':4, 'James Monroe':5, 'John Quincy Adams':6, 'Andrew Jackson':7, 'Martin Van Buren':8, 'William Henry Harrison':9, 'John Tyler':10, 'James K. Polk':11, 'Zachary Taylor':12, 'Millard Fillmore':13, 'Franklin Pierce':14, 'James Buchanan':15, 'Abraham Lincoln':16, 'Andrew Johnson':17, 'Ulysses S. Grant':18, 'Rutherford B. Hayes':19, 'James A. Garfield':20, 'Chester A. Arthur':21, 'Grover Cleveland':22, 'Benjamin Harrison':23, 'Grover Cleveland (2nd term)':24, 'William McKinley':25, 'Theodore Roosevelt':26, 'William Howard Taft':27, 'Woodrow Wilson':28, 'Warren G. Harding':29, 'Calvin Coolidge':30, 'Herbert Hoover':31, 'Franklin D. Roosevelt':32, 'Harry S. Truman':33, 'Dwight D. Eisenhower':34, 'John F. Kennedy':35, 'Lyndon B. Johnson':36, 'Richard Nixon':37, 'Gerald Ford':38, 'Jimmy Carter':39, 'Ronald Reagan':40, 'George H. W. Bush':41, 'Bill Clinton':42, 'George W. Bush':43, 'Barack Obama':44, 'Donald Trump':45}
for i in presidents:
    print(i)    
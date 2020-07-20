
import textwrap
a = input()

my_wrap = textwrap.TextWrapper(width = 4)
wrap_list = my_wrap.fill(text=a)

print(wrap_list)








"""""""""""
import textwrap
a = input()

my_wrap = textwrap.TextWrapper(width = 4)
wrap_list = my_wrap.wrap(text=a)

for line in wrap_list:


    print(line)
"""""







"""""""""""
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    """""
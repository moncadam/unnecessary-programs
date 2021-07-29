#Beta 0.3 - Commented Code - property of patogordo
#Python code that adds thousands with K, example, 7k + 6k = 13k.

first_value = input("Enter the first value (Example 7k): ")
second_value = input("Enter the second value (Example 6k): ")

def converter_and_adder(a, b):

    #Convert the strings to lists.
    c_fv = list(a)
    c_sv = list(b)

    if 'k' in c_fv and c_sv or 'K' in c_fv and c_sv:
        
        #Eliminate the K.
        del c_fv[-1]
        del c_sv[-1]
        
        #Removing spaces between letters from the list and converting it to an integer.
        u_fv = int("".join(c_fv))
        u_sv = int("".join(c_sv))
        
        #Adding and showing the final result.
        s_values = u_sv + u_fv
        if s_values < 1000 and s_values > 0:
            print(str(s_values) + "K")
        elif s_values == 1000:
            s_values_str = str(s_values)
            s_values_lst = list(s_values_str)
            del s_values_lst[-3 : -1]
            del s_values_lst[-1]
            s_values_f = int("".join(s_values_lst))
            print(str(s_values_f) + "M")
        elif s_values <= 0:
            print("You cannot add 0+0")
        elif s_values > 1000:
            print("This code only adds up to 1 million")

    else:
        print("Remember that the code needs a K that indicates thousands")

converter_and_adder(first_value, second_value)

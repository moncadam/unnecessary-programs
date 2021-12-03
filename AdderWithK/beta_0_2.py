#Beta 0.2 - Commented Code - property of patogordo
#Python code that adds thousands with K, example, 7k + 6k = 13k.
#In this I code the flow control is not commented because it is not necessary.

print("Try to use lower case k, the code may fail if you use upper case K.")

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
            print(str(s_values) + "k")
        elif s_values >= 1000 or s_values <= 0:
            print("There is no thousand thousand and you cannot add 0 + 0.")

    else:
        print("Remember that the code needs a K that indicates thousands")

converter_and_adder(first_value, second_value)
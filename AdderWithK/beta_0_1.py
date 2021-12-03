#Beta 0.1 - property of patogordo
#Python code that adds thousands with K, example, 7k + 6k = 13k.

first_value = input("Enter the first value (Example 7k): ")
second_value = input("Enter the second value (Example 6k): ")

def converter_and_adder(a, b):

    #Convert the strings to lists.
    c_fv = list(a)
    c_sv = list(b)

    #Eliminate the K.
    del c_fv[-1]
    del c_sv[-1]

    #Removing spaces between letters from the list and converting it to an integer.
    u_fv = int("".join(c_fv))
    u_sv = int("".join(c_sv))

    #Adding and showing the final result.
    s_values = u_sv + u_fv
    print(str(s_values) + "k")
    
converter_and_adder(first_value, second_value)
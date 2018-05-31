# define functions

# function which returns the reverse of the string
def reverse(s):
    return s[::-1]


def isPalin(s):
    # Call reverse function
    rev = reverse(s)

    # Check if both string are equal or not
    if (s == rev):
        print("Yes")
    else:
        print("No")


s_input = input("Enter String: ")
isPalin(s_input)

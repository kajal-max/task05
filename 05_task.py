# Question - 1
# try:
#     eval('print 3')
# except SyntaxError as e:
#     print('There is a syntax error in the code block.')


# Question - 2         ### it was hard to solve it.the instuction given were not clear to solve this question.###


# Question - 3
# num = int(input('Enter a number : '))
# while True:
#     if not 999 < num <= 9999:
#         print('The length is too short/long !!! Please provide only four digits')
#     else:
#         print('Your number is perfect. Bye!')
#         break
#     num = int(input('Enter a new number : '))


# Question - 4

# def login():
#     og_password = "python"
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")
#     tries = 0
#     if password==og_password:
#         print('Login Successful')
#     else:    
#         while tries < 3:
#             password_n = input("Incorrect pasword, try again Enter Password: ")
#             tries = tries+1
#             if password_n == og_password:
#                 print('Login Successful')
#                 break
#             else:
#                 password_n = input("Incorrect pasword, try again: ")
#                 tries = tries+1
#                 if password_n == og_password:
#                     print('Login Successful')
#                     break
#         if tries > 3:
#             print("3 Wrong passowrds tried, account suspended.")
# login()   


# Question - 6

# def return_even_lines(file_name):
#     file_1 = open(file_name,'r')
#     output = []
#     for data in file_1:
#         words = data.split()
#         for ch in words:
#             if len(ch)%2 == 0:
#                 output.append(ch)
#     return(output)

# ans = return_even_lines('doc.txt')
# print(ans)
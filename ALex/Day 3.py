num_user_cookies = int(input("how many cookies do u have? "))
if num_user_cookies >= 10:
    num_user_cookies += 5
    print("urwelcome")
elif num_user_cookies <= 1000 and num_user_cookies !> 20:
    num_user_cookies -= 100
print(num_user_cookies)

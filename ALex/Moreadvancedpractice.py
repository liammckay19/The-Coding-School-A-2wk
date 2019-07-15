def even(x):
    if x % 2 == 0:  # modulo operator also works here
        return True
    else:
        return False


a = 1
while a <= 10:
    print(a, even(a))
    a += 1

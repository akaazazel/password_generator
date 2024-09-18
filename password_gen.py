import random


def random_pass_gen(pass_len=12):
    """Generates a random password.
    Specify length as argument.
    Default length 12."""
    password = ""
    actual_pass_len = 0  # password length

    # divides password length equally for all 4 types of characters (alphabets, numbers, special chars)
    each_len = int(pass_len / 4)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {
        "up_alpha": alpha,
        "low_alpha": alpha.lower(),
        "nums": "1234567890",
        "chars": "!@#$%&*",
    }

    # keeps count of each type of characters present in password (limit is "each_len")
    count_dict = {
        "up_alpha": 0,
        "low_alpha": 0,
        "nums": 0,
        "chars": 0,
    }

    item_list = [key for key in count_dict.keys()]  # list of all type of characters

    while actual_pass_len < pass_len:
        if len(item_list) != 0:
            chosen_item = random.choice(item_list)  # choose character type
        chosen_char = random.choice(dict[chosen_item])  # choose the random character

        password += chosen_char  # add the character to password string
        actual_pass_len += 1  # increase the actual password length
        count_dict[str(chosen_item)] += 1  # keep the count of the chosen character

        # if the limit exceeds, remove the character type from list
        if chosen_item in item_list and count_dict[str(chosen_item)] == each_len:
            item_list.remove(str(chosen_item))

    return password


def main():
    print(
        "Enter any number and press enter to change the length of password. 'q' to quit"
    )
    command = input("Press enter to continue! ")
    pass_len = 12

    while True:
        if command in ["q", "quit"]:
            print("Exit!")
            return 0
        elif command.isdigit():
            pass_len = int(command)

        print(random_pass_gen(pass_len))

        command = input("Press enter to continue! ")


main()

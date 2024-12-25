import time

file_path = 'input.txt'
start_time = time.perf_counter()

ORD_Z = ord('z')
ORD_A = ord('a')
forbidden_letters = set([ord(c) for c in ['i', 'o', 'l']])

with open(file_path, 'r') as file:
    password = None
    for line in file:
        password = list([ord(c) for c in line.strip()])

def increment_string(string, index):
    char = string[index]
    if char == ORD_Z:
        string[index] = ORD_A
        if index == 0:
            raise IndexError
        else:
           increment_string(string, index-1)
    else:
        string[index] += 1

def check_string(string):
    straight = []
    had_straight = False

    double_letters_seen = 0
    indexes_used_in_pairs = set()
    had_two_pairs = False
    for i, char in enumerate(string):
        if char in forbidden_letters:
            return False

        if not had_straight:
            if not straight:
                straight.append(char)
            elif straight[-1] == char-1:
                straight.append(char)
                if len(straight) == 3:
                    had_straight = True
            else:
                straight = [char]

        if not had_two_pairs and i-1 not in indexes_used_in_pairs and i > 0:
            if char == string[i-1]:
                double_letters_seen += 1
                indexes_used_in_pairs.add(i)
                if double_letters_seen == 2:
                    had_two_pairs = True

    return had_two_pairs and had_straight

increment_string(password, len(password)-1)

while True:
    password_works = check_string(password)
    if password_works:
        break
    increment_string(password, len(password)-1)
    #print(f"Next: {"".join([chr(c) for c in password])}")

character_password = "".join([chr(c) for c in password])

end_time = time.perf_counter()
print(f"Cost: {character_password}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")

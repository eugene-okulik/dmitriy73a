import sys

sys.set_int_max_str_digits(1000000)


def fibonachi_num():
    num_1, num_2 = 0, 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


count = 1
for i in fibonachi_num():
    if count in [5, 200, 1000]:
        print(i)
    elif count == 100000:
        print(f"100000-е число содержит очень много цифр, а если точнее вот столько: {len(str(i))}")
        break
    count += 1

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

new_list_filter = list(filter(lambda x: x > 28, temperatures))

new_list_map = map(lambda x: x if x > 28 else "тут холодно)", temperatures)

print(f"самая высокая температура: {max(new_list_filter)}\n"
      f"самая низкая температура: {min(new_list_filter)}\n"
      f"средняя температура: {round(sum(new_list_filter) / len(new_list_filter), 2)}\n")
print(f"очень хотелось мапом попробоватьXD\n{[e for e in new_list_map if isinstance(e, int)]}")

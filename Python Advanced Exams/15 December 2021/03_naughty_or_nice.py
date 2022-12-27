def naughty_or_nice_list(*args, **kwargs):
    result = {"Nice": [], "Naughty": [], "Not found": []}
    output, list_with_names = "", args[0]
    for data in args[1:]:
        number, type_ = data.split("-")
        total_numbers = 0
        if sum(1 for num, name in list_with_names if int(number) == num) == 1:
            for pos, (num, name) in enumerate(list_with_names):
                if int(number) == num:
                    total_numbers += 1
                    result[type_].append(name)
                    del list_with_names[pos]
    for k_name, v_type in kwargs.items():
        if sum(1 for num, name in list_with_names if k_name == name) == 1:
            for pos, (num, name) in enumerate(list_with_names):
                if k_name == name:
                    del list_with_names[pos]
                    result[v_type].append(name)

    result["Not found"] = [not_found_name for _, not_found_name in list_with_names]
    for p_type, p_names in result.items():
        if p_names:
            output += f"{p_type}: {', '.join(p_names)}\n"

    return output

# 50/100 no reason!
# def naughty_or_nice_list(*args, **kwargs):
#     types = {
#         "Nice": [],
#         "Naughty": [],
#         "Not found": [],
#     }
#     names = {}
#     for arg in args[0]:
#         names[arg[0]] = arg[1]
#     for arg in args[1:]:
#         split = arg.split("-")
#         key, type = [int(x) if x.isdigit() else x for x in split]
#         if key in names:
#             types[type].append(names[key])
#             names.pop(key)
#     if kwargs:
#         for k, v in kwargs.items():
#             if v == "Nice":
#                 if k in types["Naughty"]:
#                     types["Naughty"].remove(k)
#             else:
#                 if k in types["Nice"]:
#                     types["Nice"].remove(k)
#             types[v].append(k)
#     for name in names.values():
#         types["Not found"].append(name)
#     output = ""
#     temp_list = []
#     for out in types:
#         if types[out]:
#             output += f"{out}: "
#             for x in types[out]:
#                 temp_list.append(x)
#             output += f"{', '.join(temp_list)}\n"
#         temp_list.clear()
#     return output


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

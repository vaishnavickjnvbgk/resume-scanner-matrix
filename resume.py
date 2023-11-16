import os
import condition_checker
condition = []

def scanner(data, choice, path):
    result = []

    for text in os.listdir(path):
        res_dct = {}
        resume1 = open(path + text, "r")
        resume2 = resume1.read().splitlines()
        resume3 = [i.split(":") for i in resume2]

        for i in resume3:
            if len(i) >= 2:  # Check if there are at least two elements
                key = i[0].strip()
                value = i[1].strip()
                res_dct[key] = value

        count = 0

        for i in range(len(choice)):
            print(data[i])
            print(choice[i])
            res = condition_checker.check_condition(res_dct, data[i], choice[i])

            if res == "-1":
                result.append("invalid")
                return result
            elif res:
                count += 1

        if count == len(choice):
            result.append(text)

    return result

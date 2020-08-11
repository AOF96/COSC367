import math

outcomes = []
dict = {}
time_dictionary = {}
with open('experiment_fitts_log.txt') as input_file:
    for line in input_file:
        line = (line.strip().split('\t'))
        key_tuple = (int(line[1]), int(line[2]), int(line[3]))
        time_tuple = (int(line[1]), int(line[2]))
        dict[key_tuple] = float(line[4])
        time_dictionary[time_tuple] = time_dictionary.get(time_tuple, []) + [float(line[4])]

result = {}
for key, value in dict.items():
    result_id = math.log2((key[0] / key[1]) + 1)
    tuple = (key[0], key[1])
    mean_time = (sum(time_dictionary.get(tuple)) / 8) / 1000
    result[round(result_id, 2)] = result.get(round(result_id, 2), []) + [mean_time]

outcomes = []
for key, value in result.items():
    mean = sum(value) / len(value)
    outcomes.append((key, round(mean, 3)))

file = open("summary.csv", "w")
file.write("ID, mean time\n")
for row in outcomes:
    file.write("{},{}\n".format(str(row[0]), row[1]))

file.close()

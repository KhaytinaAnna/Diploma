import json
import os

'''
export START_TEST=0
export END_TEST=163
'''

start_test = int(os.environ.get("START_TEST"))
end_test = int(os.environ.get("END_TEST"))


for i in range(start_test, end_test + 1):
    print(f"========== {i} ===========")
    file_name = f"my_dataset/{i}.json"

    with open(file_name, 'r') as file:
        parsed_data = json.load(file)
        method = parsed_data['method']
        coverage_sequences = parsed_data['tests']


        num_j_tests = len(coverage_sequences)

        for j in range(num_j_tests):
            file_name_2 = f"res_dataset/{i}/{i}_{j}.json"
            coverage_sequence = coverage_sequences[j]['coverage_sequence']
            
            with open(file_name_2, 'r') as fi:
                parsed_data = json.load(fi)
                test_case = parsed_data['result']
                print(test_case)
            
            sdt = method.split(':')[0].split(' ')[1].split('(')[0] + f"({test_case})"
            # print(sdt)

            code_to_execute = method + '\n' + "print(" + sdt + ")" + "\n" + "\n" + "# " + str(coverage_sequence)
            # print(code_to_execute)

            file_name_3 = f"res_dataset/{i}/{i}_{j}_code.py"

            with open(file_name_3, 'w') as file2:
                file2.write(code_to_execute)

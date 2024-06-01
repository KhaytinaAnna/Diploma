import os
import json
import re

def extract_symbols_from_file(file_path):
    symbols_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line:
                first_char = line[0]
                if first_char in ('>', '!'):
                    symbols_list.append(first_char)
    
    return symbols_list

def compare_lists(list1, list2):
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            return 0
    return 1

start_test = int(os.environ.get("START_TEST"))
end_test = int(os.environ.get("END_TEST"))
num_of_experiments = 0
matching_covs = 0

for i in range(start_test, end_test + 1):
    file_name = f"my_dataset/{i}.json"
    with open(file_name, 'r') as file:
        parsed_data = json.load(file)
        coverage_sequences = parsed_data['tests']
        num_j_tests = len(coverage_sequences)

    for j in range(num_j_tests):
        pattern = r'.*_code.py,cover$'
        
        # Проверяем соответствие шаблону
        if not os.path.exists(f'res_dataset/{i}/{i}_{j}_code_coverage'):
            continue
        for filename in os.listdir(path=f'res_dataset/{i}/{i}_{j}_code_coverage'):
            if re.search(pattern, filename):
                if os.path.exists(f'res_dataset/{i}/{i}_{j}_code_coverage/{filename}'):
                    file_path_cov = f"res_dataset/{i}/{i}_{j}_code_coverage/{filename}"
                    result = extract_symbols_from_file(file_path_cov) # последовательность ">", "!", полученная в результате chatgpt

                    coverage_sequence = coverage_sequences[j]['coverage_sequence']

                    num_of_experiments += 1
                    matching_covs += compare_lists(result, coverage_sequence)
                else:
                    print("No such file")
                    break

        

print(matching_covs / num_of_experiments * 100)
# 10/24/2022, author: Furkan Akkurt; adapted from 'Tester.py' of Murat Ozyurt
import subprocess
import sys


def runtest(test_data):
    executable_file = "./Main.py"
    command = [sys.executable, executable_file]

    input_to_test = test_data

    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)

    out, _ = p.communicate(bytes(input_to_test.encode("utf-8")))
    answer = out.decode("utf-8").rstrip()
    # print('#', input_to_test)
    # print(answer)
    # print()
    return answer

if __name__ == "__main__":

    for i in range(1, 4):
        data = 'file{i}.txt'.format(i=i)
        runtest(data)
    for i in range(1, 6):
        data = '../testcases/file_{i}.txt'.format(i=i)
        with open('../testcases/output{i}'.format(i=i)) as f:
            output_t = f.read()
        if output_t.strip() != runtest(data).strip():
            print('Error with input', i)


# 10/16/2022, author: Furkan Akkurt
# tests generated randomly by script src/create_input.py

# 20220601, author Murat Ozyurt
# Question tester for pre-grading check during exam.
# The tests feed the necessary input to your executable similar to the grading process.

# Value of the "executable_file" variable must match to the specified executable in TCAdmin
# Students or candidates should not modify this file, otherwise, compilation problems may occur during grading.

# Instructors can add as many tests as they need.
# In each testX() function, the test number, input lines and expected output lines must be returned.
# Be careful with the use of """ at the end of input and expected output:
# Terminating """ of the expected output has to be placed on a separate line,
# whereas the terminating """ of the input has to be placed on the same line as the last input line.

# Some students return the expected value without any calculation, so it is a better practice
# to avoid using these test values among the actual grading test cases.  Modified versions of this file
# can be bundled with the question for the students to use during exam and project development.

"""
https://stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes

ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
ps.wait()
"""

import subprocess
import sys


def runtest(executable_file, test_data):
    command = [sys.executable, executable_file]

    test_num = test_data[0]
    input_to_test = test_data[1]
    expected_output = test_data[2].rstrip()

    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)

    out, err = p.communicate(bytes(input_to_test.encode("utf-8")))
    answer = out.decode("utf-8").rstrip()
    print("_______________________________________________________")
    if answer == expected_output:
        print("| Test", test_num, ": SUCCESS.")
        return

    test_fail_message = ""
    test_success = True

    if answer.count("\n") != expected_output.count("\n"):
        test_fail_message = "The number of generated answer output lines does not match that of the expected output."
        test_success = False

    if test_success:
        answer_lines = answer.split("\n")
        expected_output_lines = expected_output.split("\n")

        for lineNumber in range(len(answer_lines)):
            if answer_lines[lineNumber].rstrip() != expected_output_lines[lineNumber].rstrip():
                test_success = False

                result = " \""+answer_lines[lineNumber]+"\" does not match the expected output \""\
                         + expected_output_lines[lineNumber]+"\""
                test_fail_message += "\n" + "Answer line " + \
                    str(lineNumber+1) + result

    if test_success:
        print("| Test", test_num, ": SUCCESS.")
        return

    print("Test", test_num, "FAILED.")
    print("---------------------\nANSWER BEGIN\n---------------------")
    print(answer)
    print("---------------------\nANSWER END")
    print("---------------------\nEXPECTED OUTPUT BEGIN\n---------------------")
    print(expected_output)
    print("---------------------\nEXPECTED OUTPUT END\n---------------------")
    print(test_fail_message)


def test1():

    input_to_test = """\
file1.txt"""

    expected_output = """\
3
12
0
12
0
24
12
75
-13
68
-40
156
38
490
-169
405
-530
1075
7
3377
-1674
2540
-5259
7709
-1404
24218
-14917
16759
-46863
56949
-18388
178910
-126231
115794
-396566
429871
-181630
1350479
-1038499
831229
-3262540
3293728
-1615676
10347551
-8405127
6144987
-26405485
25492716
"""
    return 1, input_to_test, expected_output


def test2():

    input_to_test = """\
file2.txt"""

    expected_output = """\
5
12
4
14
12
22
23
69
11
74
34
131
99
411
-7
407
-21
824
391
2588
-512
2332
-1608
5468
1126
17178
-6337
14009
-19908
37972
-922
119292
-61490
88547
-193176
273682
-56335
859797
-542568
588513
-1704527
"""
    return 2, input_to_test, expected_output


def test3():

    input_to_test = """\
file3.txt"""

    expected_output = """\
3
15
-1
14
-3
29
11
91
-23
79
-72
194
25
609
-254
482
-797
"""
    return 3, input_to_test, expected_output


if __name__ == "__main__":

    executable_file = "./Main.py"

    runtest(executable_file, test1())
    runtest(executable_file, test2())
    runtest(executable_file, test3())

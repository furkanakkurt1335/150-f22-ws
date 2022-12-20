
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
binary 3
half 3
in 3
is 4
search 7
target 6
the 15
to 3
value 4
in computer science binary search also known as half-interval search logarithmic or binary chop is a algorithm that finds the position of a target value within sorted array compares the target value to middle element of array if they are not equal half in which cannot lie is eliminated and continues on remaining half again taking middle element to compare and repeating this until found if ends with remaining being empty not
"""
    return 1, input_to_test, expected_output


def test2():

    input_to_test = """\
file2.txt"""

    expected_output = """\
of 4
science 3
computer science is the study of computation automation and information computer science spans theoretical disciplines (such as algorithms theory of computation information theory and automation) to practical disciplines (including the design implementation hardware software) is generally considered an area academic research distinct from programming
"""
    return 2, input_to_test, expected_output


def test3():

    input_to_test = """\
file3.txt"""

    expected_output = """\
as 5
automated 3
of 3
to 5
in mathematics and computer science an algorithm is a finite sequence of rigorous instructions typically used to solve a class of specific problems or to perform computation algorithms are used as specifications for performing calculations and data processing more advanced algorithms can perform automated deductions (referred as automated reasoning) use mathematical logical tests divert the code execution through various routes (referred decision-making) using human characteristics descriptors machines in metaphorical ways was already practiced by alan turing with terms such "memory" "search" "stimulus"
"""
    return 3, input_to_test, expected_output


if __name__ == "__main__":

    executable_file = "./Main.py"

    runtest(executable_file, test1())
    runtest(executable_file, test2())
    runtest(executable_file, test3())

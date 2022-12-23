
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
VALUE 4
TO 3
THE 15
TARGET 6
SEARCH 7
IS 4
IN 3
HALF 3
BINARY 3
IN COMPUTER SCIENCE BINARY SEARCH ALSO KNOWN AS HALF-INTERVAL SEARCH LOGARITHMIC OR BINARY CHOP IS A ALGORITHM THAT FINDS THE POSITION OF A TARGET VALUE WITHIN SORTED ARRAY COMPARES THE TARGET VALUE TO MIDDLE ELEMENT OF ARRAY IF THEY ARE NOT EQUAL HALF IN WHICH CANNOT LIE IS ELIMINATED AND CONTINUES ON REMAINING HALF AGAIN TAKING MIDDLE ELEMENT TO COMPARE AND REPEATING THIS UNTIL FOUND IF ENDS WITH REMAINING BEING EMPTY NOT
"""
    return 1, input_to_test, expected_output


def test2():

    input_to_test = """\
file2.txt"""

    expected_output = """\
SCIENCE 3
OF 4
COMPUTER SCIENCE IS THE STUDY OF COMPUTATION AUTOMATION AND INFORMATION COMPUTER SCIENCE SPANS THEORETICAL DISCIPLINES (SUCH AS ALGORITHMS THEORY OF COMPUTATION INFORMATION THEORY AND AUTOMATION) TO PRACTICAL DISCIPLINES (INCLUDING THE DESIGN IMPLEMENTATION HARDWARE SOFTWARE) IS GENERALLY CONSIDERED AN AREA ACADEMIC RESEARCH DISTINCT FROM PROGRAMMING
"""
    return 2, input_to_test, expected_output


def test3():

    input_to_test = """\
file3.txt"""

    expected_output = """\
TO 5
OF 3
AUTOMATED 3
AS 5
IN MATHEMATICS AND COMPUTER SCIENCE AN ALGORITHM IS A FINITE SEQUENCE OF RIGOROUS INSTRUCTIONS TYPICALLY USED TO SOLVE A CLASS OF SPECIFIC PROBLEMS OR TO PERFORM COMPUTATION ALGORITHMS ARE USED AS SPECIFICATIONS FOR PERFORMING CALCULATIONS AND DATA PROCESSING MORE ADVANCED ALGORITHMS CAN PERFORM AUTOMATED DEDUCTIONS (REFERRED AS AUTOMATED REASONING) USE MATHEMATICAL LOGICAL TESTS DIVERT THE CODE EXECUTION THROUGH VARIOUS ROUTES (REFERRED DECISION-MAKING) USING HUMAN CHARACTERISTICS DESCRIPTORS MACHINES IN METAPHORICAL WAYS WAS ALREADY PRACTICED BY ALAN TURING WITH TERMS SUCH "MEMORY" "SEARCH" "STIMULUS"
"""
    return 3, input_to_test, expected_output


if __name__ == "__main__":

    executable_file = "./Main.py"

    runtest(executable_file, test1())
    runtest(executable_file, test2())
    runtest(executable_file, test3())

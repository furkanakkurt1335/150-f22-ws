
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

def runtest(executable_file, test_data):
    # Instructors need not change this method, if you do please let us know.
    # command = ["/usr/local/bin/python3", executable_file]
    command = ["python", executable_file]


    test_num = test_data[0]
    input_to_test = test_data[1]
    expected_output = test_data[2].rstrip()

    p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


    #out, err = p.communicate(b"10\nsecondinput")
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
                         +expected_output_lines[lineNumber]+"\""
                test_fail_message += "\n" + "Answer line " +str(lineNumber+1)+ result


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
r: 32.00
Sphere's area: 12288.00
8.0
1
"""
    return 1, input_to_test, expected_output


def test2():

    input_to_test = """\
file2.txt"""

    expected_output = """\
r: 25.00
Sphere's area: 7500.00
4.0
1
"""
    return 2, input_to_test, expected_output

def test3():

    input_to_test = """\
file3.txt"""

    expected_output = """\
r: 5.00
Sphere's area: 300.00
2.0
100
"""
    return 3, input_to_test, expected_output

def testG1():

    input_to_test = """\
../testcases/file_1.txt"""

    expected_output = """\
r: 22.00
Sphere's area: 5808.00
7.0
3
"""
    return 4, input_to_test, expected_output

def testG2():

    input_to_test = """\
../testcases/file_2.txt"""

    expected_output = """\
r: 10.00
Sphere's area: 1200.00
10.0
1
"""
    return 5, input_to_test, expected_output

def testG3():

    input_to_test = """\
../testcases/file_3.txt"""

    expected_output = """\
r: 5.00
Sphere's area: 300.00
7.0
100
"""
    return 6, input_to_test, expected_output

def testG4():

    input_to_test = """\
../testcases/file_4.txt"""

    expected_output = """\
r: 24.00
Sphere's area: 6912.00
10.0
1
"""
    return 7, input_to_test, expected_output

def testG5():

    input_to_test = """\
../testcases/file_5.txt"""

    expected_output = """\
r: 14.00
Sphere's area: 2352.00
7.0
2
"""
    return 8, input_to_test, expected_output

if __name__ == "__main__":

    executable_file = "./Main.py"

    runtest(executable_file, test1())
    runtest(executable_file, test2())
    runtest(executable_file, test3())

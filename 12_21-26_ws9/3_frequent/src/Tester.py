
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
search 7
is 4
in computer science binary search also known as half-interval search logarithmic search or binary chop is a algorithm that finds the position of a target value within a sorted array binary compares the target value to the middle element of array if they are not equal half in which target cannot lie is eliminated and continues on remaining half again taking middle element to compare to value and repeating this until is found if ends with remaining half being empty not in array
"""
    return 1, input_to_test, expected_output


def test2():

    input_to_test = """\
file2.txt"""

    expected_output = """\
multiple 5
in 5
a 6
in computer architecture multithreading is the ability of a central processing unit or a single core in a multi-core processor to provide multiple threads of execution concurrently supported by the operating system this approach differs from multiprocessing in multithreaded application the threads share resources of single or multiple cores which include computing units cpu caches and translation lookaside buffer where multiprocessing systems include multiple complete processing units one or more cores multithreading aims to increase utilization single core by using thread-level parallelism as well as instruction-level parallelism as two techniques are complementary they are combined nearly all modern systems architectures with multithreading cpus and with cpus with cores
"""
    return 2, input_to_test, expected_output


def test3():

    input_to_test = """\
file3.txt"""

    expected_output = """\
path 5
other 4
nodes 4
node 7
in 6
graph 4
for 4
between 5
and 6
algorithm 7
a 10
dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph which may represent for example road networks it was conceived by computer scientist dijkstra in 1956 and published three years later the algorithm exists in many variants dijkstra's original found the shortest path between two given nodes but a more common variant fixes a single node as source node and finds shortest paths from source to all other nodes graph producing shortest-path treefor given source node graph finds path between that and every other it can also be used for finding paths from single to single destination by stopping once path to destination has been determined example if of represent cities edge costs represent driving distances pairs of cities connected by direct road dijkstra's can be used find route one city all other cities widely used application of algorithms is network routing protocols most notably is-is ospf it is also employed as subroutine algorithms such as johnson's
"""
    return 3, input_to_test, expected_output


if __name__ == "__main__":

    executable_file = "./Main.py"

    runtest(executable_file, test1())
    runtest(executable_file, test2())
    runtest(executable_file, test3())

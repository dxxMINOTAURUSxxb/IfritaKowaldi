from HTMLParsers import ProblemsLinkParser
from subprocess import Popen, PIPE

CONTEST = 928

programs = {
    "A": "./a",
    "B": "./b",
    "C": "./c",
    "D": "./d",
}

for name, tests in ProblemsLinkParser(CONTEST).problems.items():
    print("Problem %s\n" % name)
    for test in tests:
        prog = Popen(programs[name], stdout=PIPE, stdin=PIPE)
        out = prog.communicate(input=bytes(test["input"], 'utf-8'))[0].decode('utf-8').replace('\n', ' ').strip()
        answer = out == test["output"]
        if answer:
            print("\t%s: OK! \n" % test["name"])
        else:
            print("\t%s: FAIL\n\t\tInput: %s\n\t\tOutput: %s\n\t\tYour answer: %s\n" %
                  (test["name"], test["input"], test["output"], out))

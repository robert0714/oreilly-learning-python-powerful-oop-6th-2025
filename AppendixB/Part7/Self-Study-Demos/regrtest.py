# Simple test for regressions in the output of a set of scripts

import os
testscripts = [dict(script='test1.py', args=''),       # Edit me to use (or glob)
               dict(script='test2.py', args='-opt')]   # Add encodings if needed

for testcase in testscripts:
    commandline = '%(script)s %(args)s' % testcase
    output = os.popen(commandline).read()
    result = testcase['script'] + '.result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult = open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
            print(output)
        else:
            print('Passed:', testcase['script'])


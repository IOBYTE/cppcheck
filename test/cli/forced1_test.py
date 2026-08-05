
# python -m pytest forced1_test.py

import os

from testutils import cppcheck

__script_dir = os.path.dirname(os.path.abspath(__file__))
__proj_dir = os.path.join(__script_dir, 'forced1')

def get_lines(s):
    return sorted(s.split('\n'))

def test_forced1():
    args = [
        '--template=cppcheck1',
        '--project=forced1/forced1.cppcheck',
        '--no-cppcheck-build-dir'
    ]
    ret, stdout, stderr = cppcheck(args, cwd=__script_dir)
    filename1 = os.path.join('forced1', 'DebugX64.cpp')
    filename2 = os.path.join('forced1', 'DebugX64.h')
    assert ret == 0, stdout
    expected = (
        '[%s:5]: (error) Division by zero.\n'
        '[%s:4]: (error) Division by zero.\n' % (filename1, filename2)
    )
    assert get_lines(stderr) == get_lines(expected)

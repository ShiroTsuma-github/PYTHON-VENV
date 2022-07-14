import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def test_syspath():
    assert os.path.dirname(os.path.dirname(os.path.realpath(__file__))) in sys.path

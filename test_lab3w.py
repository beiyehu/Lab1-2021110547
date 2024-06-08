from lab1 import find_shortest_path, convert_to_networkx

def run_tests():
    test_cases = [
        {
            'G': {
                'a': {'b': 1, 'c': 4},
                'b': {'c': 2, 'd': 5},
                'c': {'d': 1},
                'd': {}
            },
            'source': 'a',
            'target': 'd',
            'expected_output': ['a', 'b', 'c', 'd']
        },
        {
            'G': {
                'a': {'b': 1},
                'b': {},
                'c': {'d': 1},
                'd': {}
            },
            'source': 'a',
            'target': 'd',
            'expected_output': None
        },
        {
            'G': {
                'a': {'b': 2},
                'b': {'c': 2},
                'c': {'d': 2},
                'd': {'e': 2},
                'e': {}
            },
            'source': 'a',
            'target': 'e',
            'expected_output': ['a', 'b', 'c', 'd', 'e']
        },
        {
            'G': {
                'a': {'b': 2},
                'b': {'c': 2},
                'c': {'d': 2},
                'd': {'a': 2},
            },
            'source': 'a',
            'target': 'a',
            'expected_output': ['a']
        },
        {
            'G': {
                'a': {'b': 1},
                'b': {'c': 1},
                'c': {'d': 1},
                'd': {'b': 1},
            },
            'source': 'a',
            'target': 'd',
            'expected_output': ['a', 'b', 'c', 'd']
        }
    ]

    for i, case in enumerate(test_cases):
        G = convert_to_networkx(case['G'])
        source = case['source']
        target = case['target']
        print(f"Running test case {i + 1}")
        result = find_shortest_path(G, source, target)
        if result:
            result_output = list(result)
        else:
            result_output = result
        assert result_output == case['expected_output'], f"Test case {i + 1} failed. Expected {case['expected_output']}, but got {result_output}"
        print(f"Test case {i + 1} passed.")

if __name__ == '__main__':
    run_tests()


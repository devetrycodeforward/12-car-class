from Car import Car

test_cases = [
    {
        "input": 10,
        "output": 3,
    },
    {
        "input": 20,
        "output": 0,
    },
    {
        "input": 5.5,
        "output": 7.5,
    },
    {
        "input": 12.5,
        "output": .5,
    },
    {
        "input": 13,
        "output": 0,
    },
]

def test__car__fill_up():
    for test_case in test_cases:
        assignment_response = Car(test_case['input']).fill_up()
        assert assignment_response == test_case[
            'output'], f"""
For
\nInput:    {test_case['input']}
\nExpected: {test_case['output']}
\nGot:      {assignment_response}\n"""

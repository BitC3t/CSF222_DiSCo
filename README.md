# CSF222_DiSCo


# Optimization of Unversity Course Allocation

## Description

The project aims to compare different algorithms for course allocation within a university. Two approaches, the Hungarian Algorithm and a Brute-force method, are implemented.

## Implementation

### Brute-force

- This is a trivial brute-force approach to the problem where inputs are taken from an `input.json` file.
- The script processes the input data and extracts information about professors, their groups, and course preferences.
- All possible combinations of courses are generated, and assignments are done iteratively.
- Details of valid assignments are stored in a JSON file.

### Hungarian Algorithm

- The `networkx` library is used to create a bipartite graph with two sets of nodes: professors and courses. Professors are divided into three groups based on the courses they can take per semester.
- Edges with weights are added between professors and courses, forming a bipartite graph.
- The graph is converted into a JSON file.
- The algorithm is then run to find all possible maximum matchings, stored in a matches list.
- A check for duplicate solutions is performed using hash functions. Valid matches are stored in a `valid_matches` list, sorted to determine the best possible solution.
- All outputs are stored in an `all_output.json` file.

## Test Cases and Results

- To generate test cases, alter the specifications in the config file and run the `test_case_gen.py` program.
- This provides an `input.json` file, which can be used as input for the programs.
- Seven test cases are provided in the repository in the `test_cases` folder.
- Each folder contains an `input.json` file and all the outputs of the Hungarian algorithm.



## Running the Project
- Clone the repo: `git clone https://github.com/BitC3t/CSF222_DiSCo`
- Install requirements: `pip install -r requirements.txt`
- Generate test cases: `python3 test_case_gen.py`: Reads from `config.json`
- Run algo.py: `python3 algo.py`: Reads from input.json => Outputs to all_outputs.json


## Contributors

 - [Advik Raj Basani](https://github.com/BitC3t)
- [Druva Dhakshinamoorthy](https://github.com/Ceres445)
- [Kushagra Malviya](https://github.com/darthlazius)

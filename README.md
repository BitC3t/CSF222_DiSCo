# CSF222_DiSCo


# Optimizing University Course Assignments through Adaptive Perfect Matching

## Description

This project serves to be a scalable and adaptive framework for the CS F222 assignment. The project aims to optimize the assignment of courses to professors using an adaptive perfect matching algorithm, while comparing different algorithms for course allocation within a university. Two approaches, the Hungarian Algorithm and a Brute-force method, are implemented.

## Implementation

### Brute-force

- This is a trivial brute-force approach to the problem where inputs are taken from an `input.json` file.
- The script processes the input data and extracts information about professors, their groups, and course preferences.
- All possible combinations of courses are generated, and assignments are done iteratively.
- Details of valid assignments are stored in a JSON file.
- (Do note that `bruteforce.py` is a test file to check the functioning of the brute-force mechanism; it may not work, please do not run this.)

### Hungarian Algorithm

- The `networkx` library is used to create a bipartite graph with two sets of nodes: professors and courses. Professors are divided into three groups based on the courses they can take per semester.
- Based on the grouping of each professor, they are made as multiple nodes (1 if grouping is 0.5, 2 if grouping is 1, 3 if grouping is 1.5) to satisfy constraints.
- Edges with weights are added between professors and courses, forming a complete bipartite graph. 
- The algorithm is then run to find all possible perfect matchings (via enumerations), stored in a matches list.
- A check for duplicate solutions is performed using hash functions. Valid matches are stored in a `valid_matches` list, sorted to determine the best possible solution.
- All outputs are stored in an `all_outputs.json` file. This json file will be fully sorted based on the preferences of the professors, via our custom weight sorter. The first solution will always be the most optimized one.

## Test Cases and Results

- To generate test cases, alter the specifications in the config file and run the `test_case_gen.py` program.
- This provides an `input.json` file, which can be used as input for the programs.
- Seven test cases are provided in the repository in the `test_cases` folder.
- Each folder contains an `input.json` file and all the outputs of the Hungarian algorithm.
- Our algorithm further tests for crash cases and follows through with `Exception`s due to invalid groupings or such.

## Documentation
Our research paper / project paper can be found in the `/docs/` folder -> `DiSCo_Project.pdf`. This pdf is comprehensive and covers the use and implementation of our algorithm. Our working video is also in the same folder, labelled as `disco-final.mp4`.

Since this video may be too big, you can also watch it here: https://youtu.be/1iAyMyAltlY

## Running the Project
- Clone the repo: `git clone https://github.com/BitC3t/CSF222_DiSCo`
- Install requirements: `pip install -r requirements.txt`
- Change the `config.json` in the `config` folder: you can change the number of professors, number of CDCs & electives (for both FD and HD), this will help our test case generator create a valid test case for running the algorithm. Do note that the `total` variable in the file MUST be the sum of all courses (ie total must be 30, if there are 10 FD_CDCs, 10 HD_CDCs, 5 FD_Electives, 5 HD_Electives). `fd_c` represents FD CDCs; `fd_e` represents FD Electives; `hd_c` represents HD CDCs; `hd_e` represents HD Electives.
- Generate test cases: `python3 test_case_gen.py`: Reads from `config.json`
- Run algo.py: `python3 algo.py`: Reads from input.json => Outputs to all_outputs.json


## Contributors

- [Advik Raj Basani](https://github.com/BitC3t)
- [Druva Dhakshinamoorthy](https://github.com/Ceres445)
- [Kushagra Malviya](https://github.com/darthlazius)

Contact via email - f20221155@goa.bits-pilani.ac.in

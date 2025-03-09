## Table of Contents
- [About](#About)
- [Installation](#Installation)
- [Usage](#Usage)
- [Result](#Result)

## About
In this repo, we implement an approach that reduces the depth of quantum circuits, specifically focusing on the CNOT gate.
```bash
.
├── AES.txt
├── Can_depth_one.py
├── Greedy.py
├── ImprovedGreedy.py
├── LICENSE
├── README.md
├── config.py
├── cost_function.py
├── operations.py
├── verify.py
└── writers.py
```

## Installation
To execute this repo, please create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
Then install the modules used in the algorithm
```
pip install numpy
pip install random
pip install copy
```
## Usage
The command executes this Greedy algorithm
```
python3 ImprovedGreedy.py
```
## Result
The algorithm generates the CNOT synthesis result record in files

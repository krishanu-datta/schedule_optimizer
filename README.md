# Welcome to the Schedule Optimizer!
## Overview
The goal of project was to design a tool that applies the ideas of customization, optimization and prioritization (which people
already unknowingly apply in their personal lives) to people’s rigid daytime schedules. In particular, this application aims to
to create an optimal schedule for high school or college students by analyzing their tastes and preferences in which subjects
they want to enroll in, which professors or teachers they want to learn from, and what types of classes they want to take.

### How It Works
This schedule optimization application is coded with Python in a Jupyter
Notebook IDE. However, the brains of the application is the SAT4j MAXSAT solver, a tool
which solves boolean satisfaction and optimization problems. The utilization of this solver is
what allows the magic to happen. A normal SAT solver solves boolean satisfaction problems by
accepting a CNF, a string of clauses containing literals, and outputting whether or not the
problem is true or false (can or cannot be satisfied). However, a MAXSAT solver accepts a
weighted CNF, a string of weighted clauses containing literals, and outputs the set of literals
which maximizes the weights of the CNF. Furthermore, the CNF fed into the solver has a series
of hard clauses which the solver must satisfy with its optimal output and a group of soft clauses
(prioritized by assigned weight) which the solver must attempt to satisfy with its output. In the
case of this project, the hard clauses were used to ensure that the student took one and only one
class in every time slot, and to guarantee that the student did not take multiple sections of the
same subject in their schedule. The soft clauses were wielded to enforce the student’s subject
choices, professor choices and class type choices. In our application, the resulting output of the
MAXSAT solver is a string of positive and negative literals, with the positive values
corresponding to class IDs of the classes the student should enroll in.


### Instructions
- Download all the files in this repo.
- Download and install Anaconda (https://www.anaconda.com/) into your computer.
- Open the Jupyter Notebook application and open the `Class Schedule Optimizer.ipynb` file.
- In the first cell, input the information that is asked.
- Run all the cells in the Notebook and watch the application returns your perfect schedule!

### Other Notes
Tests (examples of tool in use) can be found in the `Schedule Optimization Tests.ipynb` file.


### Additional Information
For more information, access the `Giving Students What They Want.pdf` file, as this project was originally part of a research project
for a logic and computation class.


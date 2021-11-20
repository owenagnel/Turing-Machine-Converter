# Turing Machine table converter

## History and motivation
In 1936, Alan Turing published his monumental paper proving that Hilbert's Entscheidungsproblem has no solution. This paper, along with Gödel's incompleteness theorem published five years earlier, are arguably the two most fundemental theorems about mathematics. Although Alonzo Church beat Turing to the solution, submitting his own version of the proof just 6 earlier, the novelty of Turing's approach, namely his ingenious invention of the Turing machine as a model of computation, where deemed of sufficient interest to publish.

In the course of his proof, Turing attributes to every Turing machine a unique "description number" which allows him to show the enumerability of computable numbers (an astonishing result on its own). This program allows the user to convert description numbers back into a readable machine table and vis-versa.

## Usage
To run the program, start by locating a text file with either the description number or the machien table in the correct format. For example:
````
q3  _  Ə  N q3;
q3  Ə  Ə  R q1;
q1  _  _  N q3;
q1  Ə  Ə  R q3;
````
Or
````
3111322326311731132223222243117
````

Note that a semi-colon (or a 7) must be added at the end of each instruction line, and that the number of spaces between each part of the instruction doesn't matter in the machine table. Blanks are represented usin "_".

To execute the program, run:
````
> python3 converter.py (-r) -i inputfile.txt (-o outputfile.txt)
````
The optional (-r) is to run the program in reverse order (that is to go from description number back to a machine table). The output file name/location is optional (the program will just create one in the working directory otherwise). However, the input file name must be passed as an argument. 
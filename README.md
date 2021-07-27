# FastQ_Analyzer
Opens and reads a FastQ file, determining various statistics for each line, for further visualization or analysis downstream.
Produces an .out file containing the following information:
  1. Length of sequence
  2. GC %
  3. Average quality score of the sequence
  4. Position of the base with the minimum quality score
  5. Proportion of the sequence w/ a "good" score [>=30]
  6. Proportion of the sequence w/ an "ok" score [>=20]
  7. Proportion of the sequence w/ a "bad" score [<20]
It then prints to the terminal:
  1. Number of sequences in the FastQ file
  2. Average length of the sequences in the FastQ file


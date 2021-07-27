# FastQ_Analyzer
Opens and reads a FastQ file, determining various statistics for each line, for further visualization or analysis downstream.
Produces an .out file containing the following information:
  Markup: *Length of sequence
  *GC %
  *Average quality score of the sequence
  *Position of the base with the minimum quality score
  *Proportion of the sequence w/ a "good" score [>=30]
  *Proportion of the sequence w/ an "ok" score [>=20]
  *Proportion of the sequence w/ a "bad" score [<20]
It then prints to the terminal:
  *Number of sequences in the FastQ file
  *Average length of the sequences in the FastQ file


def main():
    infile = open('example.fastq','r') #fastq file to open and read

    outfile = open('example.out','w') #file to write results to, in this case an .out file

    count = 0 #variable to keep track of the number of reads given in the fastq file
    avglen = 0 #variable to save the saverage length of all reads

    for i in infile: #loop to process each read, "reads" 1st line automatically here
        count += 1 #increment read number
        
        seq = infile.readline().strip('\n') #"read" the 2nd line AKA sequence, while also stripping the newline char, and saving it to a variable
        seq_len = len(seq) #grab length of the sequence
        C = seq.count('C') #find amount of C nucleotides in sequence
        G = seq.count('G') #find amount of G nucleotides in sequence
        GC = (C+G)/seq_len #calculate GC %

        avglen = avglen + seq_len
        infile.readline() #"read" 3rd line, the identifier

        qual = infile.readline().strip('\n') #"read" 4th line, also stripping newline char, saved to a variable

        qual_total = 0 #start counter for sum of qual scores
        qual_list = [] #list to hold each quality score in the read
        
        #variables to categorize quality scores in read
        good = 0 
        ok = 0
        bad = 0

        for q in qual: #looping through each quality score in the quality score sequence
            basequal = ord(q) - 33 #calculate the Q score
            qual_list.append(basequal) #add it to the list
            qual_total = qual_total + basequal #add it to the total
            
            #determine category of quality score
            if basequal >= 30:
                good += 1
            elif basequal >= 20:
                ok += 1
            else:
                bad += 1

        ave_qual = qual_total / seq_len #calculate the average quality score of the read
        pos_min = qual_list.index(min(qual_list))+1 #find the position of the lowest quality score within the read
        
        #determine the proportions of each quality score category
        prop_good = good / seq_len
        prop_ok = ok / seq_len
        prop_bad = bad / seq_len

        #write to the output file
        outfile.write( str(seq_len) + '\t' + str(GC) + '\t' + str(ave_qual) + '\t' + str(pos_min) + '\t' + str(prop_good)
            + '\t' + str(prop_ok) + '\t' + str(prop_bad) + '\n') 

    avglen = avglen / count

    print("Number of sequences: " + str(count)) #print number of sequences to terminal
    print("Average length of sequences: " + str(avglen)) #print avg length of sequences to terminal

    infile.close()
    outfile.close()

main()
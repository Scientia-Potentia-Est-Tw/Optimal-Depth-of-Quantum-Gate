import config
def Recording(sequence, layers, select):
	#Open a file that Layers and sequences with SIZE for square cost function to store the operations
	if select == 0:
		layer_file = config.sq_Layer_File
		seq_file = config.sq_Seq_File
	#another is store the Layers and sequences for the product cost function operations
	elif select == 1:
		layer_file = config.prod_Layer_File
		seq_file = config.prod_Seq_File
	#store the operaiton sequences and store the amounts of CNOT and length of sequence
	with open(layer_file, "w") as f:
		for l in layers:
			for lay in l:
				f.write("%d %d " % (lay[0], lay[1]))
			f.write("\n")
		f.write("CNOT: %d, depth: %d\n" % (len(sequence), len(layers)))

	f.close()
	#store the operations from sequence
	with open(seq_file, "w") as f:
		for i in sequence:
			f.write("%d %d %d\n" % (i[0], i[1], i[2]))
		f.write("CNOT: %d\n" % (len(sequence)))
	f.close()
	
	#recording each experimental result for repeatedly
	if select == 0:
		record_file = open(config.row_Record_File, "a")
		record_file.write("CNOT: %d, depth: %d\n" % (len(sequence), len(layers)))
		record_file.close()
	elif select == 1:
		record_file = open(config.col_Record_File, "a")
		record_file.write("CNOT: %d, depth: %d\n" % (len(sequence), len(layers)))
		record_file.close()

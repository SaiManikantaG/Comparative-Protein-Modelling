from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='4zwvA', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4zwvA', atom_files='4zwvA.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-4zwvA.ali', alignment_format='PIR')
aln.write(file='qseq1-4zwvA.pap', alignment_format='PAP')

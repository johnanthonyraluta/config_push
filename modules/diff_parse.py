import subprocess
import sys
from datetime import datetime

def main():
    #previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    #previous_date_str = previous_date.strftime("%b%d")
    #date_today_str = datetime.datetime.today().strftime("%b%d%")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
       sys.argv[1]
       sys.argv[2]
    except:
       print('Specify the files for output comparison ')
       sys.exit(1)
       sys.exit(2)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    args = ["diff", "-y", "-W", "168", "/home/users/jraluta/tnt_script/UPGRADE/data_output/" + file1, \
            "/home/users/jraluta/tnt_script/UPGRADE/data_output/"+file2]
    output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
    output2 =output.decode('utf-8')
    with open(f'/home/users/jraluta/tnt_script/UPGRADE/data_output/diff_raw_{file1}_{file2}_'+ current_time, 'a+') as parse_results:
        for line in output2:
        #   if 'show' in line: 
           parse_results.writelines(line)
        print('Done saving output')

if __name__ == '__main__':
    main()

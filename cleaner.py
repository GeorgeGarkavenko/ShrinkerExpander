import csv
from sys import argv

def main(main_file="spec.csv", output_file="spec_cleaned.csv"):
    """
    Will clean some articles.
    """
    
    replace_pos = \
    ['1378021', '1378026', '1378034', '1378053',
     '1378058', '1378178']
    
    del_pos = \
    ['1378144', '1378192', '1378222', '1378235',
     '1378342', '1378150', '1378025', '1378325',
     '1378309']
    
    inactive_pos = \
    ['1378063', '1378067', '1378077', '1378078',
     '1378134', '1378080', '1378082', '1378083',
     '1378084', '1378086', '1378087', '1378089',
     '1378117', '1378120', '1378121', '1378122',
     '1378123', '1378124', '1378125', '1378318',
     '1378143', '1378165', '1378193', '1378196',
     '1378201', '1378227', '1378151', '1378156',
     '1378175', '1378194', '1378197', '1378203',
     '1378229', '1378158', '1378164', '1378190',
     '1378195', '1378198', '1378204', '1378231']
    
    # reading and processing main data
    with open(main_file, 'rb') as main_f:
        # open output_file for output
        with open(output_file, 'wb') as f:
            # read the main data (by default spec.csv)
            
            all_records = csv.reader(main_f, delimiter=";")
            
            output = csv.writer(f, delimiter=";")
            
            for row in all_records:
                
                row_list = list(row)
                # print row_list

                if row_list[3] in replace_pos or row_list[3] in del_pos or row_list[3] in inactive_pos:
                    row_list[12] = '0'
                        
                output.writerow(row_list)    
                  
        
if __name__ == "__main__":
    main(*argv[1:])
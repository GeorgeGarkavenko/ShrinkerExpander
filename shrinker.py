import csv
from string import upper, strip
from sys import argv

def main(main_file="spec.csv", output_file="spec_compact.csv"):
    """
    Will shrink main_file list (remove missed sizes)
    Out to the output_file.
    """

    # reading and processing main data
    with open(main_file, 'rb') as main_f:
        # open output_file for output
        with open(output_file, 'wb') as f:
            # read the main data (by default spec.csv)
            
            all_records = csv.reader(main_f, delimiter=";")
            
            output = csv.writer(f, delimiter=";")
            
            prev_article = None
            
            position = 0
            
            for row in all_records:
                
                new_article = strip(row[3])
                
                if int(strip(row[12])) != 0:
                    
                    row_list = list(row)
                    
                    row_list[0] = ''
                    
                    if new_article != prev_article:
                        
                        position += 1
                        row_list[0] = str(position)
                    # else:
                    #     row_list[0] = '|'+new_article + '|' + prev_article + '|'
                    output.writerow(row_list)    
                        
                    prev_article = strip(row[3])
                
        
if __name__ == "__main__":
    main(*argv[1:])
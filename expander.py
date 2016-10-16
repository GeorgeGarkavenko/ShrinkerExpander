import csv
from string import upper, strip
from sys import argv

def main(main_file="spec.csv", output_file="spec_full.csv"):
    """
    Will expand main_file list (add missed sizes)
    Out to the output_file.
    """
    
    sizes_key = ('XS','S','M','L','XL','2XL','3XL','4XL')
    
    sizes_values = {
        'XS': 40,
        'S': 42,
        'M': 44,
        'L': 46,
        'XL': 48,
        '2XL': 50,
        '3XL': 52,
        '4XL': 54
        }
    
    # reading and processing main data
    with open(main_file, 'rb') as main_f:
        # open output_file for output
        with open(output_file, 'wb') as f:
            # read the main data (by default spec.csv)
            
            all_records = csv.reader(main_f, delimiter=";")
            
            output = csv.writer(f, delimiter=";")
            
            prev_row = None
            
            sizes_buffer = {}
            
            position = 0
            
            for row in all_records:
                new_article = strip(row[3])
                prev_article = strip(prev_row[3]) if prev_row else None
                
                if new_article != prev_article and prev_article:
                    
                    position += 1
                    prev_row_list = list(prev_row)
                    
                    for key in sizes_key:
                        # change prev_row_list key values
                        prev_row_list[0] = str(position) if key == 'XS' else ''
                        
                        prev_row_list[5] = key
                        prev_row_list[6] = sizes_values.get(key, '')
                        
                        prev_row_list[12] = sizes_buffer.get(key, 0)
                        
                        output.writerow(prev_row_list)
                        
                    # new clean sizes_buffer
                    
                    sizes_buffer = {}
                
                sizes_buffer[row[5]] = row[12]
                
                prev_row = row
                
            # last position
            
            position += 1
            prev_row_list = list(prev_row)
            
            for key in sizes_key:
                # change prev_row_list key values
                prev_row_list[0] = str(position) if key == 'XS' else ''
                
                prev_row_list[5] = key
                prev_row_list[6] = sizes_values.get(key, '')
                
                prev_row_list[12] = sizes_buffer.get(key, 0)
                
                output.writerow(prev_row_list)
        
        
if __name__ == "__main__":
    main(*argv[1:])
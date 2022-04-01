import os
import csv

def get_value(key_value_str: str):
    """
    Takes a string on the format "key=value" and returns the "value" part.
    """
    return key_value_str.partition('=')[2]

def parse_log_file(log_file_path):
    """
    Takes a path to a log file containing purchaches in a store.
    Returns a list of tuples. Each tuple describes one purchache.
    """

    # Get store name from log_file_path
    file_name = os.path.split(log_file_path)[1]
    store_name = os.path.splitext(file_name)[0]

    # Öppna filen med sökvägen log_file_path
    with open(log_file_path) as store:
        # Skapar en CSV iterator för att i nedan for-loop kunna gå igenom alla rader
        reader = csv.reader(store)

        # Skapar en tom dict som for-loopen fyller allt eftersom med värden. Innehåller id som key i syfte att kunna söka och ta bort canceled-rader. 
        dict = {}
        for line in reader:
            # Första kolumen avgör om ordern är canceled eller inte.
            if line[0] == "canceled":
                # Tar ut id ur den cancelerade ordern   
                id = get_value(line[1])
                # Tar bort ordern från dicten
                del dict[id]
            else:
                # Tar ut värden som ska fylla tuplen sales
                id = get_value(line[1])
                time = get_value(line[2])
                total_sek = get_value(line[3])
                member = get_value(line[4])
                birth_year = get_value(line[5])
                age = 2022 - int(birth_year) if birth_year.isdigit() else "na"

                # Skapar en tupel
                sales = (time, store_name, total_sek, member, age)
                # I dict läggs id in som key och sales-tupeln som värde
                dict[id] = sales
        # Funktionen returnerar en lista av värderna i dicten
        return list(dict.values())   

def write_csv_file(csv_file_path, entries):
    """
    Adds all purchases from the list entries as rows in the CSV file csv_file_path.
    The first row in the CSV file is a header with the column names.
    """
    # Skapar rubriker 
    header = ["time", "store", "total_sek", "member", "age"]
    # Öppnar filen och gör det möjligt att skriva i den
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Fyller på med rubrik och rader
        writer.writerow(header)
        writer.writerows(entries)    

def merge_log_files_to_csv(log_dir, csv_file_path):
    """
    Read and parse all store log files in log_dir, and then write all entries to a CSV file at csv_file_path.
    """
    # Skapar en tom lista
    all_entries = []
    
    # Gå igenom alla filer i mappen log_dir
    for file_name in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file_name)
        # Kontrollerar så att det är en log-fil
        if os.path.isfile(file_path) and file_name.endswith('.log'):
        
            # Fyller på listan med alla tuples från funktionen parse_log_file för nuvarande fil
            all_entries = all_entries + parse_log_file(file_path)
    # Sorterar listan, default sorterar på första elementet, dvs tiden
    all_entries.sort()

    #Anropar funktionen write_csv_file som skriver över raderna i all_entries till CSV-filen
    write_csv_file(csv_file_path, all_entries)

if __name__ == '__main__':
    merge_log_files_to_csv(log_dir='stores/', csv_file_path='output/all-stores.csv')
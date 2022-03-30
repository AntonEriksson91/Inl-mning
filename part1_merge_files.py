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

    with open(log_file_path) as store:
        reader = csv.reader(store)

        dict = {}
        for line in reader:
            if line[0] == "canceled":    
                id = get_value(line[1])
                
                del dict[id]
            else:
                id = get_value(line[1])
                time = get_value(line[2])
                total_sek = get_value(line[3])
                member = get_value(line[4])
                birth_year = get_value(line[5])
                age = 2022 - int(birth_year) if birth_year.isdigit() else "na"

                sales = (time, store_name, total_sek, member, age)

                dict[id] = sales
        
        # print(dict)
        return list(dict.values())   

# file_path = "C:\\Users\\Ida\\OneDrive - Nackademin AB\\Business Intelligence-relaterade programspråk\\Inlämningsuppgift grupp\\Inl-mning\\stores\\store1.log"

# # entry = parse_log_file(file_path)
# parse_log_file(file_path)

    # """
    # Öppna logfilen och gå igenom alla raderna:
    #     Om raden startar med "sale," så ska innehållet läggas till i listan av köp.
    #     Om raden startar med "canceled," så var det något som var fel med köpet, och köpet med samma id ska plockas bort från listan med köp.

    # returnera en lista med en tupel för varje köp.
    #     Varje tupel ska innehålla: (time, store_name, total_sek, member, age)

    # Hint - Ignorera rader med "cancel" till att börja med om ni kör fast.
    # Hint - Använd dict för att hålla reda på kopplingen mellan köp-id för att hantera rader med "cancel"
    # Hint - "123".isdigit() kan användas för att se om en text kan göras om till int
    # Hint - get_value kan användas för att få ut värden från key=value
    # """


def write_csv_file(csv_file_path, entries):
    """
    Adds all purchases from the list entries as rows in the CSV file csv_file_path.
    The first row in the CSV file is a header with the column names.
    """

    """
    TODO
    Öppna CSV-filen med sökvägen csv_file_path för skrivning.
    Skriv en header-rad med dessa kolumnnamn: 'time', 'store', 'total_sek', 'member', 'age'
    Skriv en rad för varje köp i listan entries.
    """
    
    header = ["time", "store", "total_sek", "member", "age"]
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(header)
        writer.writerows(entries)    

def merge_log_files_to_csv(log_dir, csv_file_path):
    """
    Read and parse all store log files in log_dir, and then write all entries to a CSV file at csv_file_path.
    """
    
    all_entries = []
    a2 = []
    for file_name in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.log'):
            # TODO Läs ut alla entries från logfilen file_path med parse_log_file och lägg till dem på all_entries
            
            all_entries = all_entries + parse_log_file(file_path)
    all_entries.sort()
    # TODO Se till att raderna är sorterade på tid.
    # Hint: Med tidsformatet som används går det bra att sortera på textsträngar.
    # Hint: Listor med tupler sorteras på första elementet i tuplerna om inget annat anges.
    write_csv_file(csv_file_path, all_entries)
    # TODO Skriv raderna till CSV-filen (csv_file_path) med funktionen write_csv_file


if __name__ == '__main__':
    merge_log_files_to_csv(log_dir='stores/', csv_file_path='output/all-stores.csv')
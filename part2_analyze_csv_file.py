from calendar import month
from datetime import datetime as dt
from itertools import count
from time import time
import statistics


def sek_per_purchase(entries):
    print('\nMean sek sum per purchase:')

    res = statistics.mean(item['total_sek'] for item in entries)
    """
    TODO
    Skriv ut genomsnittsbeloppet som betalades vid varje köp.
    """
    
    print(f'{res:.2f} sek/purchase\n')


def member_vs_not_member_sum_per_moth(entries):
    # Entries är en lista av dicts. 
    # {"key=butiken":values=dict.{key=månad:values=[total summa, antal poster]}}
    
    stores = {"store1": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store2": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store3": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store4": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}}

    for item in entries:
        month = item["time"].month
        store = item["store"]
        value = item["total_sek"]

        # Summan
        stores[store][month][0] = stores[store][month][0] + value
        # Antal poster
        stores[store][month][1] = stores[store][month][1] + 1
        
    store_names = ['store1','store2','store3','store4']
    month_numbers = [1,2,3,4,5,6]

    for store in store_names:
        for month in month_numbers:
            mean = stores[store][month][0]/stores[store][month][1] if stores[store][month][1] != 0 else 0
            print(f'For {store} and month {month} mean is {mean:.2f}')

    
    """
    TODO
    Räkna ut och skriv ut genomsnittlig total försäljning per affär och månad.
    Räkna ut och skriv ut separat för medlemmar och icke medlemmar.

    Det är ok att hårdkoda in att tidsintervallet sträcker sig över 6 månader och det finns 4 affärer.
    """

    #print('\nTotal sum per month and store:')
    print(f'')
    #print(f'Members: {res_members:.2f} sek/month/store')
    #print(f'Not members: {res_not_members:.2f} sek/month/store')


def members_mean_age_per_hour(entries):
    print('\nMean member customer age per open hour:')
    
    """
    TODO
    Affärerna är öppna mellan 7 och 22.
    Skriv ut en rad för varje öppen timme, där varje rad innehåller timme och genomsnittsåldern på medlemmar som handlade denna timme.

    Skriv ut på det här formatet:
    print(f'hour={hour} mean_age={mean_age:.1f}')
    """


def read_csv_file(csv_file_path):
    import csv
    entries = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['time'] = dt.fromisoformat(row['time'])
            row['total_sek'] = int(row['total_sek'])
            row['member'] = row['member'] == 'True'
            
            if row['age'].isdigit():
                row['age'] = int(row['age'])
            else:
                row['age'] = None

            entries.append(row)
        
        
    return entries
      
    
if __name__ == '__main__':
    entries = read_csv_file('output/all-stores.csv')
    sek_per_purchase(entries)
    member_vs_not_member_sum_per_moth(entries)
    members_mean_age_per_hour(entries)
from calendar import month
from datetime import datetime as dt
from itertools import count
from time import time
import statistics


def sek_per_purchase(entries):
    print('\nMean sek sum per purchase:')

    # Räknar ut genomsnittet för samtliga rader i entries
    res = statistics.mean(item['total_sek'] for item in entries)
    """
    TODO
    Skriv ut genomsnittsbeloppet som betalades vid varje köp.
    """
    
    print(f'{res:.2f} sek/purchase\n')


def member_vs_not_member_sum_per_moth(entries):

    # Entries är en lista av dicts.
    # Skapar två dict-dict-listor i syfte att kunna fylla på stores med mina värden. 
    # {"key=butiken":values=dict {key=månad:values=[total summa, antal poster]}} 
    stores_members = {"store1": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store2": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store3": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store4": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}}

    stores_not_members = {"store1": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store2": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store3": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}, \
            "store4": {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}}    

    # Skapar en loop för att gå igenom varje rad i entries
    for item in entries:
        # Hämtar ut värden och benämner de 
        month = item["time"].month
        store = item["store"]
        value = item["total_sek"]
        member = item["member"]

        if member == True:
            # Adderar summan med nya värdet
            stores_members[store][month][0] = stores_members[store][month][0] + value 
            # Ökar antal poster med 1
            stores_members[store][month][1] = stores_members[store][month][1] + 1
        else:
            stores_not_members[store][month][0] = stores_not_members[store][month][0] + value 
            # Ökar antal poster med 1
            stores_not_members[store][month][1] = stores_not_members[store][month][1] + 1

    # Skapar två listor för att kunna gå igenom dessa värden i en loop i syfte att matcha keys mot values i dicts.     
    store_names = ['store1','store2','store3','store4']
    month_numbers = [1,2,3,4,5,6]

    #Loopa igenom varje butik, och för varje butik loopa igenom de månader som finns. 
    for s in store_names:
        for m in month_numbers:
            #Månad 6 har inga värden, därför behövs en if-sats.
            mean_members = stores_members[s][m][0]/stores_members[s][m][1] if stores_members[s][m][1] != 0 else 0
            mean_not_members = stores_not_members[s][m][0]/stores_not_members[s][m][1] if stores_not_members[s][m][1] != 0 else 0
            print(f'For {s} and month {m} mean is {mean_members:.2f} for members and {mean_not_members:.2f} for not members')

def members_mean_age_per_hour(entries):
    print('\nMean member customer age per open hour:')

    # Skapar en dict med en lista för att kunna fylla på värden.
    hours = {7:[0,0],8: [0,0],9: [0,0],10: [0,0],11: [0,0],12: [0,0],13: [0,0],14: [0,0],15: [0,0],16: [0,0],17:[0,0],18:[0,0],19:[0,0],20: [0,0],21: [0,0],22: [0,0]}

    # Skapar en loop för att gå igenom varje rad i entries
    for item in entries:

        # Hämtar ut värden och benämner de 
        member = item["member"]
        hour = item["time"].hour
        age = item["age"]
        
        # Kolla endast de rader som är en medlem och som handlat mellan 7-22
        if member == True and 7 <= hour and hour <= 22 :
                      
            # Adderar summan med nya värdet
            hours[hour][0] = hours[hour][0] + age 
            # Ökar antal poster med 1
            hours[hour][1] = hours[hour][1] + 1

    # Skapar en lista för att kunna gå igenom dessa värden i en loop i syfte att matcha keys mot values i dict.   
    open_hours = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

    # Gå igenom listan open_hours och hämta värdena i list-delen på plats 0 och 1. Räkna ut genomsnittet genom dessa värden. Totala summan / antal poster
    for h in open_hours:
        mean = hours[h][0]/hours[h][1]
        print(f'hour={h} mean_age={mean:.1f}')      

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
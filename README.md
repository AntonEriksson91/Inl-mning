# Uppgift - Matbutiker

Uppgiften går ut på att sammanställa information om köp från 4 butiker i den lilla matbutikskedjan Mat&Annat, och sedan besvara några frågor baserat på den hopsamlade informationen.

Informationen från butikerna sträcker sig över en 6 månaders period.

Del 1 går ut på att samla ihop information från loggfiler från varje butik och producera en CSV-fil.

Del 2 går ut på att läsa CSV-filen för att besvara några frågor.

### Inlämning

Den färdiga uppgiften lämnas in genom att lämna in filerna `part1_merge_files.py` och `part2_analyze_csv_file.py` på studentportalen.


## Del 1 - Sammanställ logfiler

För varje köp som görs i en butik läggs en rad till en logfil för den butiken. Loggfilen innehåller två sorters rader: Köp och ångrade köp.
Fälten i raderna är kommaseparerade, och alla fält (utom det första) är på formen `key=value`.

Alla rader som loggar ett köp börjar med `sale,`

En rad kan se ut såhär för en medlem:
`sale,id=13157102,time=2021-01-05T14:47:27+00:00,total_sek=171,member=True,birth_year=1927`

Och för en icke medlem:
`sale,id=24878294,time=2021-01-05T14:49:59+00:00,total_sek=50,member=False,birth_year=na`

Key-value-fälten är:
* Ett unikt id för köpet
* Tiden för köpet
* Summan av köpet i kr, utan decimaler
* Om kunden är medlem i butiken. "True" eller "False"
* Kundens födelseår, men enbart om kunden är medlem, annars står istället "na" (not available)

Lösningen ska göras genom att göra klart filen `part1_merge_files.py`, som innehåller påbörjade funktioner.


### Ångrade köp

Ibland blir något fel ett köp, och köpet ångras. När detta händer läggs en rad till som börjar med ´canceled,´. En sådan rad kan se ut såhär:

`canceled,id=13157102,time=2021-01-05T14:55:21+00:00`

När ett köp ångras ska köpet med matchande _id_ plockas bort ur sammanställningen.

Eftersom ångrade köp inte händer så ofta så påverkar det inte resultaten mycket. Om det gör lösningen lättare kan det vara bra att böja med att bara ignorera  dessa rader.


### Skriv alla köp till en CSV-fil

När alla rader är inlästa från log-filerna ska de skrivas ut i en och samma CSV-fil, sorterat på tid.

* Den första raden i CSV-filen är en header som innehåller namnen på kolumnerna
* Kolumnerna som ska vara med i CSV-filen:
    * time - Samma som i logfilerna
    * store - Vilken affär köpet gjordes i. Namnet tas från namnet på logfilen. Ex: alla rader från store1.log ska ha store1 i CSV-filen
    * total_sek - Samma som i logfilerna
    * member - Samma som i logfilerna
    * age - Kundens ålder räknat som: 2022 - födelseår. Om födelseåret är "na" i loggfilen ska age vara "na" i CSV-filen.

Exempel på hur de första 3 raderna i CSV-filen kan se ut:
```
time,store,total_sek,member,age
2021-01-02T07:01:25+00:00,store1,587,False,na
2021-01-02T07:01:59+00:00,store1,55,True,43
```

## Del 2 - Besvara frågor från CSV-filen

Använd CSV-filen all-stores.csv som producerades i del 1 för att ta fram:
 * Den genomsnittliga summan för varje köp (funktionen sek_per_purchase)
 * Vad den genomsnittlig total försäljning per affär och månad. Räkna ut detta separat för medlemmar och icke medlemmar (funktionen member_vs_not_member_sum_per_moth)
 * Genomsnittsåldern på kunder som är medlemmar för varje timme mellan 7 och 22 (funktionen members_mean_age_per_hour)

Lösningen ska göras genom att göra klart filen `part2_analyze_csv_file.py`, som innehåller färdig kod för att läsa CSV-filen och påbörjade funktioner för att besvara frågorna.

### output/small-sample.csv

För att kunna påbörja och testa del 2 utan att ha en färdig del 1 kan filen `output/small-sample.csv` användas. Den innehåller en mindre mängd data.

Exempel på utskrift från `part2_analyze_csv_file.py` med `small-sample.csv`:
```
Mean sek sum per purchase:
309.74 sek/purchase

Total sum per month and store:
Members: 6000.75 sek/month/store
Not members: 6504.83 sek/month/store

Mean member customer age per open hour:
hour=7 mean_age=74.2
hour=8 mean_age=71.5
...
```
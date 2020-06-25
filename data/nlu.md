## intent:greet
- hallo
- schönen tag
- guten morgen
- guten abend
- willkommen
- angenehmen tag
- hey
- aloha
- alola

## intent:help
- was kann ich machen
- was kannst du
- was kann public transport hero
- was kann publictransporthero
- was kann ich tun

## intent:explain
- hilfe
- wozu benötigst du das
- wozu ist das gut
- warum wird das benötigt
- wozu dient das
- warum muss ich das eingeben
- warum muss ich das bekannt geben
- warum wird das benötigt
- warum musst du das wissen
- was bringt das
- was soll ich machen
- was soll ich tun
- ich kenne mich nicht aus

## intent:start_journey_planning
- ich möchte eine reise planen
- ich möchte eine reise nach wien planen
- ich möchte einen ausflug planen
- ich möchte einen ausflug nach wien planen
- ich möchte einen citytrip planen
- ich möchte einen citytrip nach wien planen
- ich würde gerne nach wien fahren
- ich möchte nach wien fahren
- ich möchte nach wien
- ich möchte das beste ticket für wien finden
- ich möchte das beste ticket für eine reise nach wien finden
- ich möchte das beste ticket für einen ausflug nach wien finden
- ich möchte das beste ticket für einen citytrip nach wien finden

## intent:lookup_single_connection
- ich möchte eine verbindung suchen
- ich möchte eine verbindung nachschlagen
- ich möchte eine verbindung anzeigen
- ich suche eine verbindung
- wie komme ich wohin
- wie komme ich nach [taubstummengasse]{"entity": "station", "role": "departure"}

## intent:specify_departure_and_arrival_station
- ich möchte von [stranitzkygasse]{"entity": "station", "role": "departure"} nach [taubstummengasse u]{"entity": "station", "role": "departure"}
- ich möchte von [taubstummengasse u]{"entity": "station", "role": "departure"} nach [stranitzkygasse]{"entity": "station", "role": "departure"}
- ich möchte vom [stephansplatz]{"entity": "station", "role": "departure"} nach [johnstraße]{"entity": "station", "role": "departure"}
- ich fahre von [stranitzkygasse]{"entity": "station", "role": "departure"} nach [alterlaa u]{"entity": "station", "role": "arrival"}
- [floridsdorf s+u]{"entity": "station", "role": "departure"} nach [simmering s+u]{"entity": "station", "role": "arrival"}
- [rathaus]{"entity": "station", "role": "departure"} nach [schwedenplatz]{"entity": "station", "role": "arrival"}
- [heiligenstadt s+u]{"entity": "station", "role": "departure"} nach [schönbrunn]{"entity": "station", "role": "arrival"}
- [stranitzkygasse]{"entity": "station", "role": "departure"} nach [taubstummengasse u]{"entity": "station", "role": "arrival"}
- ich fahre aus [siebenhirten u]{"entity": "station", "role": "departure"} nach [kettenbrückengasse u]{"entity": "station", "role": "arrival"}
- ich fahre vom [rathaus]{"entity": "station", "role": "departure"} zum [praterstern s+u]{"entity": "station", "role": "arrival"}
- ich fahre vom [hauptbahnhof]{"entity": "station", "role": "departure"} nach [meidling s+u]{"entity": "station", "role": "arrival"}
- vom [flughafen]{"entity": "station", "role": "departure"} nach [landstraße]{"entity": "station", "role": "arrival"}
- von [kettenbrückengasse u]{"entity": "station", "role": "departure"} nach [oberdöbling]{"entity": "station", "role": "arrival"}
- ich fahre von der [simmeringer haide]{"entity": "station", "role": "departure"} zum [handelskai]{"entity": "station", "role": "arrival"}
- ich fahre von der [wopenkastraße]{"entity": "station", "role": "departure"} in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- ich fahre vom [keplerplatz u]{"entity": "station", "role": "departure"} in die [seestadt u]{"entity": "station", "role": "arrival"}
- ich will von [alte donau U]{"entity": "station", "role": "departure"} zur [donauinsel u]{"entity": "station", "role": "arrival"}
- ich will von [kagran U]{"entity": "station", "role": "departure"} in die [bruno-kreisky-gasse]{"entity": "station", "role": "arrival"}
- bring mich vom [rathaus]{"entity": "station", "role": "departure"} in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- bring mich von der [stranitzkygasse]{"entity": "station", "role": "departure"} in die [schlachthausgasse u]{"entity": "station", "role": "arrival"}
- ich fahre vom [hauptbahnhof]{"entity": "station", "role": "departure"} in die [schlachthausgasse u]{"entity": "station", "role": "arrival"}
- ich fahre vom [stephansplatz]{"entity": "station", "role": "departure"} nach [michelbeuern-akh]{"entity": "station", "role": "arrival"}

## intent:select_arrival_station
- ich komme am [hauptbahnhof]{"entity": "station", "role": "arrival"} an
- [hauptbahnhof]{"entity": "station", "role": "arrival"}
- ich komme am [flughafen wien]{"entity": "station", "role": "arrival"} an
- [flughafen]{"entity": "station", "role": "arrival"}
- [flughafen wien]{"entity": "station", "role": "arrival"}
- ich steige am [hauptbahnhof]{"entity": "station", "role": "arrival"} aus
- ich steige in [meidling s+u]{"entity": "station", "role": "arrival"} aus
- mein zug kommt in [hütteldorf s+u]{"entity": "station", "role": "arrival"} an
- ich parke am [westbahnhof s+u]{"entity": "station", "role": "arrival"}
- ich fahre in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- ich möchte nach [alterlaa U]{"entity": "station", "role": "arrival"} ab
- ich fahre nach [simmering s+u]{"entity": "station", "role": "arrival"}
- mein ziel ist [ottakring s+u]{"entity": "station", "role": "arrival"}
- ich will nach [floridsdorf s+u]{"entity": "station", "role": "arrival"}
- ich fahre nach [siebenhirten u]{"entity": "station", "role": "arrival"}
- ich fahre zum [rathaus]{"entity": "station", "role": "arrival"}
- ich fahre zum [stephansplatz]{"entity": "station", "role": "arrival"}
- ich fahre zum [schloss schönbrunn]{"entity": "station", "role": "arrival"}
- ich will zum [stephansplatz]{"entity": "station", "role": "arrival"}
- ich will zum [schloss schönbrunn]{"entity": "station", "role": "arrival"}
- bring mich zum [stephansplatz]{"entity": "station", "role": "arrival"}
- bring mich zum [schloss schönbrunn]{"entity": "station", "role": "arrival"}
- bring mich in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- bring mich in die [schlachthausgasse]{"entity": "station", "role": "arrival"}
- ich fahre in die [schlachthausgasse u]{"entity": "station", "role": "arrival"}
- ich fahre nach [michelbeuern-akh]{"entity": "station", "role": "arrival"}
- bring mich nach [michelbeuern-akh]{"entity": "station", "role": "arrival"}

## intent:add_destination_journey_planning
- ich möchte einen stopp hinzufügen
- ich möchte noch wo hin fahren
- ich möchte einen halt hinzufügen
- noch einen stopp
- stopp hinzufügen
- halt hinzufügen
- stopp einfügen
- halt einfügen
- nächster halt
- nächster stopp
- ich möchte noch wo hin
- ich möchte noch einen stopp einfügen
- ich möchte einen halt einfügen
- ich möchte noch einen stopp einlegen
- ich möchte einen halt einlegen

## intent:wait_for_next_day
- ich möchte einen abend pause machen
- genug für heute
- eine pause wäre angebracht
- eine pause wäre gut
- ich mache morgen weiter
- ich mache am nächsten tag weiter
- ich mache am folgenden tag weiter
- ich möchte eine pause einlegen

## intent:finish_journey_planning
- ich bin fertig
- ich bin fertig mit dem planen
- ich bin mit dem planen fertig
- ich habe die planung abgeschlossen
- ich habe die planung beendet
- ich möchte nirgends mehr hin
- ich habe fertig geplant

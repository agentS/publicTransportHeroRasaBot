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
- was bring das
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
- ich möchte von [stranitzkygasse]{"entity": "station", "role": "departure"} nach [taubstummengasse]{"entity": "station", "role": "departure"}
- ich möchte von [taubstummengasse]{"entity": "station", "role": "departure"} nach [stranitzkygasse]{"entity": "station", "role": "departure"}
- ich möchte vom [stephansplatz]{"entity": "station", "role": "departure"} nach [johnstraße]{"entity": "station", "role": "departure"}
- ich fahre von [stranitzkygasse]{"entity": "station", "role": "departure"} nach [alterlaa U]{"entity": "station", "role": "arrival"}
- [floridsdorf U]{"entity": "station", "role": "departure"} nach [simmering S+U]{"entity": "station", "role": "arrival"}
- [rathaus]{"entity": "station", "role": "departure"} nach [schwedenplatz]{"entity": "station", "role": "arrival"}
- [heiligenstadt]{"entity": "station", "role": "departure"} nach [schönbrunn]{"entity": "station", "role": "arrival"}
- [stranitzkygasse]{"entity": "station", "role": "departure"} nach [taubstummengasse]{"entity": "station", "role": "arrival"}
- ich fahre aus [siebenhirten U]{"entity": "station", "role": "departure"} nach [kettenbrückengasse]{"entity": "station", "role": "arrival"}
- ich fahre vom [rathaus]{"entity": "station", "role": "departure"} zum [praterstern]{"entity": "station", "role": "arrival"}
- ich fahre vom [hauptbahnhof]{"entity": "station", "role": "departure"} nach [meidling]{"entity": "station", "role": "arrival"}
- vom [flughafen]{"entity": "station", "role": "departure"} nach [landstraße]{"entity": "station", "role": "arrival"}
- von [favoriten]{"entity": "station", "role": "departure"} nach [oberdöbling]{"entity": "station", "role": "arrival"}
- ich fahre von der [simmeringer haide]{"entity": "station", "role": "departure"} zum [handelskai]{"entity": "station", "role": "arrival"}
- ich fahre von der [wopenkastraße]{"entity": "station", "role": "departure"} in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- ich fahre vom [keplerplatz]{"entity": "station", "role": "departure"} in die [seestadt U]{"entity": "station", "role": "arrival"}
- ich will von [alte donau U]{"entity": "station", "role": "departure"} zur [donauinsel]{"entity": "station", "role": "arrival"}
- ich will von [kagran U]{"entity": "station", "role": "departure"} in die [bruno-kreisky-gasse]{"entity": "station", "role": "arrival"}

## intent:select_first_station
- ich komme am [hauptbahnhof]{"entity": "station", "role": "arrival"} an
- [hauptbahnhof]{"entity": "station", "role": "arrival"}
- ich komme am [flughafen wien]{"entity": "station", "role": "arrival"} an
- [flughafen]{"entity": "station", "role": "arrival"}
- [flughafen wien]{"entity": "station", "role": "arrival"}
- ich steige am [hauptbahnhof]{"entity": "station", "role": "arrival"} aus
- ich steige in [meidling]{"entity": "station", "role": "arrival"} aus
- mein zug kommt in [hütteldorf]{"entity": "station", "role": "arrival"} an
- ich parke am [westbahnhof]{"entity": "station", "role": "arrival"}
- ich fahre in die [stranitzkygasse]{"entity": "station", "role": "arrival"}
- ich möchte nach [alterlaa U]{"entity": "station", "role": "arrival"} ab
- ich fahre nach [simmering S+U]{"entity": "station", "role": "arrival"}
- mein ziel ist [ottakring]{"entity": "station", "role": "arrival"}
- ich will nach [floridsdorf U]{"entity": "station", "role": "arrival"}
- ich will nach [schönbrunn]{"entity": "station", "role": "arrival"}
- ich fahre nach [siebenhirten U]{"entity": "station", "role": "arrival"}
- ich fahre zum [rathaus]{"entity": "station", "role": "arrival"}

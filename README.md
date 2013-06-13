CRE
===
This is a simple demo of combining scraping and Stanford NER tool. 
Change the link in demo.sh, then run the script it will ouput name entities.

Rightnow the link is: 
http://www.rejournals.com/2013/06/12/dtz-to-relocate-expand-its-chicago-office-to-77-w-wacker-drive/

And the output is:

Dzungs-MacBook-Air:Demo andrey$ ./demo.sh 
Loading classifier from english.all.3class.distsim.crf.ser.gz ... done [5.1 sec].

Chicago/ORGANIZATION
Brokerage/ORGANIZATION
Operation/ORGANIZATION
Global/ORGANIZATION
Corporate/ORGANIZATION
Services/ORGANIZATION
and/ORGANIZATION
Facility/ORGANIZATION
Management/ORGANIZATION
N./PERSON
Clark/PERSON
St./PERSON
Chicago/LOCATION
Greg/PERSON
Schementi/PERSON
U.S./LOCATION
W./PERSON
Wacker/PERSON
Chicago/LOCATION
Christopher/PERSON
Wood/PERSON
Chicago/LOCATION
Chicago/LOCATION
Chris/PERSON
Wood/PERSON
Todd/PERSON
Mintz/PERSON
Kyle/PERSON
Harding/PERSON
Molly/PERSON
Carroll/PERSON
Monica/PERSON
Moore/PERSON
Jones/PERSON
Lang/PERSON
Jones/ORGANIZATION
Lang/ORGANIZATION
LaSalle/ORGANIZATION
United/ORGANIZATION

2) SETUP:

Include the stanford-ner.jar (download from http://nlp.stanford.edu/software/CRF-NER.shtml) in CLASSPATH:

export CLASSPATH=$CLASSPATH:/path-to-stanford-ner.jar


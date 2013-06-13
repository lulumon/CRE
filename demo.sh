# Demo script

link=http://www.rejournals.com/2013/06/12/dtz-to-relocate-expand-its-chicago-office-to-77-w-wacker-drive/

python scraping.py $link
java -mx400m NERDemo english.all.3class.distsim.crf.ser.gz temp.txt 
#!/usr/bin/sh
lista_0="csv_files.txt"
split -l 5 "$lista_0" part_

mv part_aa parte1.txt
mv part_ab parte2.txt
mv part_ac parte3.txt

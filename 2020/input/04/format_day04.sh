#!/bin/bash
cat input.txt | 
sed 's/^$/Thisisablankline/g' | 
sed ':a;N;$!ba;s/\n/ /g' | 
sed 's/Thisisablankline/}\n/g' | 
sed 's/^/{/g' | 
sed 's/{ /{/g' | 
sed 's/ }/}/g' | 
sed 's/ /,/g' | 
sed 's/byr/"byr"/g' | 
sed 's/eyr/"eyr"/g' | 
sed 's/iyr/"iyr"/g' | 
sed 's/ecl/"ecl"/g' | 
sed 's/hcl/"hcl"/g' | 
sed 's/hgt/"hgt"/g' | 
sed 's/cid/"cid"/g' | 
sed 's/pid/"pid"/g' |
sed 's/:/:"/g'|
sed 's/,/",/g' |
sed 's/}/"}/g' |
sed '/^{$/d' > input_formatted.txt

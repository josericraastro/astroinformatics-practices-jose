#!/usr/bin/sh


for file in data*.csv; do
    newname="data${file#data}"
    newname="${newname%.csv}.lc"
    cp "$file" "$newname"
done

for file in data*.lc; do
    output="col_$(basename "$file")"
    awk -F',' 'BEGIN {OFS=","} NR==1 || NF >= 9 {print $1, $8, $9}' "$file" > "$output"
    echo "Archivo procesado: $output"
done

for file in col_data*.lc; do
    sed 's/,/ /g' "$file" > "${file%.lc}_flux.lc"
done




cat extracted/ETL8B2C1_00.txt extracted/ETL8B2C1_01.txt extracted/ETL8B2C1_02.txt extracted/ETL8B2C1_03.txt extracted/ETL8B2C1_04.txt extracted/ETL8B2C1_05.txt > hiragana_labels.txt
sed -i -z 's/\n//g' hiragana_labels.txt

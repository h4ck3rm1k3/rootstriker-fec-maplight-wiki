wget http://data.maplight.org/FEC/2014/summaries/all.json
sed -e's!{"person_id":!\n{"person_id":!g' all.json  > all_split.json


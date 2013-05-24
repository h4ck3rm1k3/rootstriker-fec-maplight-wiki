import re
import json
from pprint import pprint

fields = [ 'all_count', 'all_rank',  'chamber_count',  'chamber_rank',  'contrib_end', 
           'contrib_start', 'contrib_total', 'district_holding', 'district_running',
           'first_name', 'full_name', 'gender', 'ico', 'last_name', 'office_holding',
           'office_running', 'party', 'person_id', 'state', 'status', 'status_date',           'url_photo' ]

for i in fields :
    print "|-\n|" + i +  "\n|" +  "{{{" + i + "}}}"

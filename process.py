import re
import json
from pprint import pprint

fields = [ 'all_count', 'all_rank',  'chamber_count',  'chamber_rank',  'contrib_end', 
           'contrib_start', 'contrib_total', 'district_holding', 'district_running',
           'first_name', 'full_name', 'gender', 'ico', 'last_name', 'office_holding',
           'office_running', 'party', 'person_id', 'state', 'status', 'status_date',           'url_photo' ]

f = open("Wiki.xml", 'w')

with open("all_split.json") as infile:
    for line in infile:
        if 'person_id' in line:
#            print line
            if(line[-1] == ']'):
                data = json.loads(line[:-1])
            else:
                data = json.loads(line[:-2])

            f.write ( "{{-start-}}\n") 
            full_name=data['full_name']
            sutf8 = full_name.encode('UTF-8')
            f.write ( "'''" + sutf8 + "'''\n") 

            s = '{{maplight candidate|'
            for i in fields :
                if i not in data :
                    print "not there " + i 
                    next

                d = data[i]
                if (isinstance( d, int )):
                    d= str(d)
                if d is None:
                    next
                else:
                    s = s + "|" + i + "=" + d

            s = s + '}}' + "\n"
            sutf8 = s.encode('UTF-8')
            f.write(sutf8)
            top_orgs = data['top_orgs']
            if (len(top_orgs) > 0):
                for x in top_orgs.iteritems() :
                    f.write( "{{maplight sponsorship|" + x[1] ['name'] +  "|"+  x[1] ['total'] + "}}\n")

            f.write( "{{maplight finish}}\n")
            f.write ( "{{-stop-}}\n") 


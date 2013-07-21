import zipfile
import os.path
import ContributionstoaCandidateCommittee as f1
         
#e= ExpendituresbyaCommitteeFile ()
#e.generate()
#e.process_csv ("FEC2014c3.zip")
#e=ZipCSV()
#e.process_generate ("FEC2014c2.zip","ContributionstoaNonCandidateCommittee")
#e.process_generate ("FEC2014c1.zip","ContributionstoaCandidateCommittee")

e=f1.ContributionstoaCandidateCommitteeFile()
e.process_csv ("FEC2014c1.zip")

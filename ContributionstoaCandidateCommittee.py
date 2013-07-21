import zipcsv

class ContributionstoaCandidateCommittee:
    def __init__(self,v):
        self.v=v
    TransactionTypeCode=0
    def getTransactionTypeCode(self):
        return self.v[ContributionstoaCandidateCommittee.TransactionTypeCode]
    TransactionType=1
    def getTransactionType(self):
        return self.v[ContributionstoaCandidateCommittee.TransactionType]
    ElectionCycle=2
    def getElectionCycle(self):
        return self.v[ContributionstoaCandidateCommittee.ElectionCycle]
    ReportingCommitteeMLID=3
    def getReportingCommitteeMLID(self):
        return self.v[ContributionstoaCandidateCommittee.ReportingCommitteeMLID]
    ReportingCommitteeFECID=4
    def getReportingCommitteeFECID(self):
        return self.v[ContributionstoaCandidateCommittee.ReportingCommitteeFECID]
    ReportingCommitteeName=5
    def getReportingCommitteeName(self):
        return self.v[ContributionstoaCandidateCommittee.ReportingCommitteeName]
    ReportingCommitteeNameNormalized=6
    def getReportingCommitteeNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.ReportingCommitteeNameNormalized]
    PrimaryGeneralIndicator=7
    def getPrimaryGeneralIndicator(self):
        return self.v[ContributionstoaCandidateCommittee.PrimaryGeneralIndicator]
    TransactionID=8
    def getTransactionID(self):
        return self.v[ContributionstoaCandidateCommittee.TransactionID]
    FileNumber=9
    def getFileNumber(self):
        return self.v[ContributionstoaCandidateCommittee.FileNumber]
    RecordNumberML=10
    def getRecordNumberML(self):
        return self.v[ContributionstoaCandidateCommittee.RecordNumberML]
    RecordNumberFEC=11
    def getRecordNumberFEC(self):
        return self.v[ContributionstoaCandidateCommittee.RecordNumberFEC]
    TransactionDate=12
    def getTransactionDate(self):
        return self.v[ContributionstoaCandidateCommittee.TransactionDate]
    TransactionAmount=13
    def getTransactionAmount(self):
        return self.v[ContributionstoaCandidateCommittee.TransactionAmount]
    RecipientName=14
    def getRecipientName(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientName]
    RecipientNameNormalized=15
    def getRecipientNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientNameNormalized]
    RecipientCity=16
    def getRecipientCity(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCity]
    RecipientState=17
    def getRecipientState(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientState]
    RecipientZipCode=18
    def getRecipientZipCode(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientZipCode]
    RecipientEmployer=19
    def getRecipientEmployer(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientEmployer]
    RecipientEmployerNormalized=20
    def getRecipientEmployerNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientEmployerNormalized]
    RecipientOccupation=21
    def getRecipientOccupation(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientOccupation]
    RecipientOccupationNormalized=22
    def getRecipientOccupationNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientOccupationNormalized]
    RecipientOrganization=23
    def getRecipientOrganization(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientOrganization]
    RecipientEntityTypeCode=24
    def getRecipientEntityTypeCode(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientEntityTypeCode]
    RecipientEntityType=25
    def getRecipientEntityType(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientEntityType]
    RecipientCommitteeMLID=26
    def getRecipientCommitteeMLID(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeMLID]
    RecipientCommitteeFECID=27
    def getRecipientCommitteeFECID(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeFECID]
    RecipientCommitteeName=28
    def getRecipientCommitteeName(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeName]
    RecipientCommitteeNameNormalized=29
    def getRecipientCommitteeNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeNameNormalized]
    RecipientCommitteeTreasurer=30
    def getRecipientCommitteeTreasurer(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeTreasurer]
    RecipientCommitteeDesignationCode=31
    def getRecipientCommitteeDesignationCode(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeDesignationCode]
    RecipientCommitteeDesignation=32
    def getRecipientCommitteeDesignation(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeDesignation]
    RecipientCommitteeTypeCode=33
    def getRecipientCommitteeTypeCode(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeTypeCode]
    RecipientCommitteeType=34
    def getRecipientCommitteeType(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeType]
    RecipientCommitteeParty=35
    def getRecipientCommitteeParty(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCommitteeParty]
    RecipientCandidateMLID=36
    def getRecipientCandidateMLID(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateMLID]
    RecipientCandidateFECID=37
    def getRecipientCandidateFECID(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateFECID]
    RecipientCandidateName=38
    def getRecipientCandidateName(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateName]
    RecipientCandidateNameNormalized=39
    def getRecipientCandidateNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateNameNormalized]
    RecipientCandidateParty=40
    def getRecipientCandidateParty(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateParty]
    RecipientCandidateICO=41
    def getRecipientCandidateICO(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateICO]
    RecipientCandidateStatus=42
    def getRecipientCandidateStatus(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateStatus]
    RecipientCandidateOfficeState=43
    def getRecipientCandidateOfficeState(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateOfficeState]
    RecipientCandidateOffice=44
    def getRecipientCandidateOffice(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateOffice]
    RecipientCandidateDistrict=45
    def getRecipientCandidateDistrict(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateDistrict]
    RecipientCandidateGender=46
    def getRecipientCandidateGender(self):
        return self.v[ContributionstoaCandidateCommittee.RecipientCandidateGender]
    DonorName=47
    def getDonorName(self):
        return self.v[ContributionstoaCandidateCommittee.DonorName]
    DonorNameNormalized=48
    def getDonorNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.DonorNameNormalized]
    DonorCity=49
    def getDonorCity(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCity]
    DonorState=50
    def getDonorState(self):
        return self.v[ContributionstoaCandidateCommittee.DonorState]
    DonorZipCode=51
    def getDonorZipCode(self):
        return self.v[ContributionstoaCandidateCommittee.DonorZipCode]
    DonorEmployer=52
    def getDonorEmployer(self):
        return self.v[ContributionstoaCandidateCommittee.DonorEmployer]
    DonorEmployerNormalized=53
    def getDonorEmployerNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.DonorEmployerNormalized]
    DonorOccupation=54
    def getDonorOccupation(self):
        return self.v[ContributionstoaCandidateCommittee.DonorOccupation]
    DonorOccupationNormalized=55
    def getDonorOccupationNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.DonorOccupationNormalized]
    DonorOrganization=56
    def getDonorOrganization(self):
        return self.v[ContributionstoaCandidateCommittee.DonorOrganization]
    DonorEntityTypeCode=57
    def getDonorEntityTypeCode(self):
        return self.v[ContributionstoaCandidateCommittee.DonorEntityTypeCode]
    DonorEntityType=58
    def getDonorEntityType(self):
        return self.v[ContributionstoaCandidateCommittee.DonorEntityType]
    DonorCommitteeMLID=59
    def getDonorCommitteeMLID(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeMLID]
    DonorCommitteeFECID=60
    def getDonorCommitteeFECID(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeFECID]
    DonorCommitteeName=61
    def getDonorCommitteeName(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeName]
    DonorCommitteeNameNormalized=62
    def getDonorCommitteeNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeNameNormalized]
    DonorCommitteeTreasurer=63
    def getDonorCommitteeTreasurer(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeTreasurer]
    DonorCommitteeDesignationCode=64
    def getDonorCommitteeDesignationCode(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeDesignationCode]
    DonorCommitteeDesignation=65
    def getDonorCommitteeDesignation(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeDesignation]
    DonorCommitteeTypeCode=66
    def getDonorCommitteeTypeCode(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeTypeCode]
    DonorCommitteeType=67
    def getDonorCommitteeType(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeType]
    DonorCommitteeParty=68
    def getDonorCommitteeParty(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCommitteeParty]
    DonorCandidateMLID=69
    def getDonorCandidateMLID(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateMLID]
    DonorCandidateFECID=70
    def getDonorCandidateFECID(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateFECID]
    DonorCandidateName=71
    def getDonorCandidateName(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateName]
    DonorCandidateNameNormalized=72
    def getDonorCandidateNameNormalized(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateNameNormalized]
    DonorCandidateParty=73
    def getDonorCandidateParty(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateParty]
    DonorCandidateICO=74
    def getDonorCandidateICO(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateICO]
    DonorCandidateStatus=75
    def getDonorCandidateStatus(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateStatus]
    DonorCandidateOfficeState=76
    def getDonorCandidateOfficeState(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateOfficeState]
    DonorCandidateOffice=77
    def getDonorCandidateOffice(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateOffice]
    DonorCandidateDistrict=78
    def getDonorCandidateDistrict(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateDistrict]
    DonorCandidateGender=79
    def getDonorCandidateGender(self):
        return self.v[ContributionstoaCandidateCommittee.DonorCandidateGender]
    UpdateTimestamp=80
    def getUpdateTimestamp(self):
        return self.v[ContributionstoaCandidateCommittee.UpdateTimestamp]
    fields=['TransactionTypeCode', 'TransactionType', 'ElectionCycle', 'ReportingCommitteeMLID', 'ReportingCommitteeFECID', 'ReportingCommitteeName', 'ReportingCommitteeNameNormalized', 'PrimaryGeneralIndicator', 'TransactionID', 'FileNumber', 'RecordNumberML', 'RecordNumberFEC', 'TransactionDate', 'TransactionAmount', 'RecipientName', 'RecipientNameNormalized', 'RecipientCity', 'RecipientState', 'RecipientZipCode', 'RecipientEmployer', 'RecipientEmployerNormalized', 'RecipientOccupation', 'RecipientOccupationNormalized', 'RecipientOrganization', 'RecipientEntityTypeCode', 'RecipientEntityType', 'RecipientCommitteeMLID', 'RecipientCommitteeFECID', 'RecipientCommitteeName', 'RecipientCommitteeNameNormalized', 'RecipientCommitteeTreasurer', 'RecipientCommitteeDesignationCode', 'RecipientCommitteeDesignation', 'RecipientCommitteeTypeCode', 'RecipientCommitteeType', 'RecipientCommitteeParty', 'RecipientCandidateMLID', 'RecipientCandidateFECID', 'RecipientCandidateName', 'RecipientCandidateNameNormalized', 'RecipientCandidateParty', 'RecipientCandidateICO', 'RecipientCandidateStatus', 'RecipientCandidateOfficeState', 'RecipientCandidateOffice', 'RecipientCandidateDistrict', 'RecipientCandidateGender', 'DonorName', 'DonorNameNormalized', 'DonorCity', 'DonorState', 'DonorZipCode', 'DonorEmployer', 'DonorEmployerNormalized', 'DonorOccupation', 'DonorOccupationNormalized', 'DonorOrganization', 'DonorEntityTypeCode', 'DonorEntityType', 'DonorCommitteeMLID', 'DonorCommitteeFECID', 'DonorCommitteeName', 'DonorCommitteeNameNormalized', 'DonorCommitteeTreasurer', 'DonorCommitteeDesignationCode', 'DonorCommitteeDesignation', 'DonorCommitteeTypeCode', 'DonorCommitteeType', 'DonorCommitteeParty', 'DonorCandidateMLID', 'DonorCandidateFECID', 'DonorCandidateName', 'DonorCandidateNameNormalized', 'DonorCandidateParty', 'DonorCandidateICO', 'DonorCandidateStatus', 'DonorCandidateOfficeState', 'DonorCandidateOffice', 'DonorCandidateDistrict', 'DonorCandidateGender', 'UpdateTimestamp']

#    def process(self,

class  ContributionstoaCandidateCommitteeFile(zipcsv.ZipCSV) : 
    def  process(self,line):
        v=line.split(",")
        if  len(v) < len(ContributionstoaCandidateCommittee.fields) :
            print "too short",len(v)
            return 

        if v[0] == ContributionstoaCandidateCommittee.fields[0]:
            #first row
            return 

        r =ContributionstoaCandidateCommittee(v)
        print r.getTransactionType(),r.getTransactionAmount(),r.getRecipientNameNormalized(),r.getDonorOrganization(),r.getDonorEmployerNormalized(), r.getDonorNameNormalized()


#encoding=utf8
dbfile=open("/home/huangxy/GRASP2fullDataset").readlines()
#dbfile=open("/home/huangxy/testDatabase.txt").readlines()
#NHLBIkey HUPfieldLastCurationDateCreationDateSNPid(dbSNP134)chr(hg19)pos(hg19) PMID SNPid(inpaper) LocationWithinPaperPvalue Phenotype PaperPhenotype DescriptionPaperPhenotypeCategoriesDatePubInNHGRIcat(asof3/31/12)JournalTitleIncludesMale/FemaleOnlyAnalysesExclusivelyMale/FemaleInitialSampleDescriptionReplicationSampleDescriptionPlatform[SNPspassingQC]GWASancestryDescriptionTotalSamples(discovery+replication)TotalDiscoverySamplesEuropeanDiscoveryAfricanDiscoveryEastAsianDiscoveryIndian/SouthAsianDiscoveryHispanicDiscoveryNativeDiscoveryMicronesianDiscoveryArab/MEDiscoveryMixedDiscoveryUnspecifiedDiscoveryFilipinoDiscoveryIndonesianDiscoveryTotalreplicationsamplesEuropeanReplicationAfricanReplicationEastAsianReplicationIndian/SouthAsianReplicationHispanicReplicationNativeReplicationMicronesianReplicationArab/MEReplicationMixedReplicationUnspecifiedReplicationFilipinoReplicationIndonesianReplicationInGeneNearestGeneInLincRNAInMiRNAInMiRNABSdbSNPfxndbSNPMAFdbSNPalleles/het/sedbSNPvalidationdbSNPClinStatusORegAnnoConservPredTFBSHumanEnhancerRNAeditPolyPhen2SIFTLS-SNPUniProtEqtlMethMetabStudy
#1 7 8 12
infile=open("/home/huangxy/Disease.txt").readlines()
#snp_id
out=open("/home/huangxy/output.xls","w")


dic2={}

for i in dbfile:
	dic2[i.split("\t")[0]+"\t"+i.split("\t")[8]]=i.split("\t")[7]+"\t"+i.split("\t")[12]

for key in dic2:
	#print key
	for snp_id in infile:
		if key.strip().split("\t")[1] == snp_id.strip():
			out.write(key+"\t"+dic2[key]+"\n")		
		else:
			pass
out.close()
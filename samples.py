from sys import argv

samples = {#"vbfHmm_powheg": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14/VBFHToMuMu_M125_14TeV_powheg_pythia8_200PU/"],

           #"DYToLL_madgraphMLM": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	   #"GluGluHToMuMu_powheg": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/GluGluHToMuMu_M125_14TeV_powheg_pythia8_200PU/"],
	   
	   #"EWKZ2Jets_ZToLL_madgraph":  ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15_hadd/EWKZ2Jets_ZToLL_M-50_14TeV-madgraph-pythia8_200PU/"],
	   
	   #"DYJets_MLL_50_madgraphMLM" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DYJets_incl_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	   
	   #"DYJetsToLL_M_100_madgraphMLM" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DYJetsToLL_M-100_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8_200PU/"],
	   
	   #"TT_Tune_powheg" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8_200PU/"]
	   
	   #"TTJets_madgraphMLM_pythia8": ["/"]



	#"DY50HT70_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY50HT100_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY50HT200_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY50HT400_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	#"DY50HT600_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	#"DY50HT800_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	#"DY50HT1200_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	#"DY50HT2500_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_hadd/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"]


	#"TTlep_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15_hadd/TTJets_DiLept_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DYJets_incl_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY100_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DYJetsToLL_M-100_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY0J50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DY0Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"], #FNAL: 
	
	#"DY0J50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_split/DYToLL-M-50_0J_14TeV-madgraphMLM-pythia8_200PU/"],

	"DY1J50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15_hadd/DY1Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],
	
	#"DY2J50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DY2Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"],

	#"DY3J50_2026MGPY" : ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre15/DY3Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8_200PU/"] #FNAL: 
	
	#"DY3J50_2026MGPY": ["/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14_split/DYToLL-M-50_3J_14TeV-madgraphMLM-pythia8_200PU/"]

}

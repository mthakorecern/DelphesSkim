import ROOT
from sys import argv
import os
#print("Example: python converter.py  test.root test_inputfiles.txt")
filename, outputFileName, inputFileName = argv                      # "vbfHmm_powheg", "DYToLL_madgraphMLM"
from variables import newVariables

#inputFileNames = open("%s"%inputFileName, "r")
#inputFileNames.read()
#inputFileNames = inputFileNames.split("\n")

with open("%s"%inputFileName, "r") as f:
    inputFileNames = list(f)

nEvents_max = -1
#nEvents_max = 100
nVariables = set()


InvariantMass_code ='''
float InvariantMass (float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2)
{
   TLorentzVector mu1, mu2;
   mu1.SetPtEtaPhiM( pt1, eta1, phi1, mass1);
   mu2.SetPtEtaPhiM( pt2, eta2, phi2, mass2);
   float mass = (mu1+mu2).M();
   return mass;
}
'''

InvariantMassVect_code ='''
float InvariantMassVect (const ROOT::RVec<float>& pt, const ROOT::RVec<float>& eta, const ROOT::RVec<float>& phi, const float mass, const ROOT::RVec<float>& charge, int nMuons) {
 // std::cout << "nMuons" <<nMuons;
    float bestMass = -1;
	if(nMuons>=2){
	 for (int i=0; i < nMuons; i++){
   		for (int j=0; j < nMuons; j++){
			if(charge[i] != charge[j]){
				TLorentzVector mu1, mu2;
				mu1.SetPtEtaPhiM( pt[i], eta[i], phi[i], mass);
				mu2.SetPtEtaPhiM( pt[j], eta[j], phi[j], mass);
				float mass = (mu1+mu2).M();
				// std::cout << "mass" <<mass << std::endl;

				if(std::fabs(mass-125) < std::fabs(bestMass-125)) {
				bestMass = mass;
					}
				}
			}
		}
            }
return bestMass;
}
'''

print("Running sample: %s"%outputFileName)
fnames = ROOT.std.vector('string')()
for n in inputFileNames: 
    n = n.replace("\n","").replace(" ","")
    fnames.push_back(n)
#    print(n)

df = ROOT.RDataFrame("Delphes", fnames)

if nEvents_max>0:
    print("I'm running on %d events"%nEvents_max)
    df = df.Range(0, nEvents_max)

df_out = df.Define("sum_size", "MuonTight_size+Jet_size")

for oldVariable in newVariables:
    df_out = df_out.Define(newVariables[oldVariable], oldVariable)
    nVariables.add(newVariables[oldVariable])	

    ## Define DiMuon mass ##
ROOT.gInterpreter.Declare(InvariantMass_code) ## compile invariant mass code
ROOT.gInterpreter.Declare(InvariantMassVect_code) ## compile invariant mass code

#df_out = df_out.Define("DiMuon_mass", "InvariantMass( Muon_pt[0], Muon_eta[0], Muon_phi[0], 0.106,  Muon_pt[1], Muon_eta[1], Muon_phi[1], 0.106)") ## define DiMuon_mass variable (0.106 GeV is the muon mass)

df_out = df_out.Define("DiMuon_mass", "InvariantMassVect(Muon_pt, Muon_eta, Muon_phi, 0.106,  Muon_charge, nMuons)") ## define DiMuon_mass variable (0.106 GeV is the muon mass)
    
df_out = df_out.Define("DiJet_mass", "InvariantMass(Jet_pt[0], Jet_eta[0], Jet_phi[0], Jet_mass[0],  Jet_pt[1], Jet_eta[1], Jet_phi[1], Jet_mass[1])")

df_out = df_out.Define("DiJetPUPPI_mass", "InvariantMass(JetPUPPI_pt[0], JetPUPPI_eta[0], JetPUPPI_phi[0], JetPUPPI_mass[0],  JetPUPPI_pt[1], JetPUPPI_eta[1], JetPUPPI_phi[1], JetPUPPI_mass[1])")

counter = df_out.Histo1D(("processedEvents", "processedEvents", 1, -100000,100000), "MuonTight_size")

Vertex_size = df_out.Histo1D(("Vertex_size", "Vertex_size", 1, -100000,100000), "Vertex_size")

    ## Cuts ##
 
df_out = df_out.Filter("MuonTight_size >= 2") #require at least two muon
df_out = df_out.Filter("Muon_pt[0] > 20 && Muon_pt[1] > 20")
df_out = df_out.Filter("abs(Muon_eta[0]) < 2.8 && abs(Muon_eta[1]) < 2.8") #require the first muon to have pt>50 GeV
df_out = df_out.Filter("DiMuon_mass > 110 && DiMuon_mass < 150") #require at least two muon

    #df_out = df_out.Filter("Jet_size >= 2")
df_out = df_out.Filter("(Jet_pt[0] > 35 && Jet_pt[1] > 25) || (JetPUPPI_pt[0] > 35 && JetPUPPI_pt[1] > 25)")
df_out = df_out.Filter("(abs(Jet_eta[0]) < 4.7 && abs(Jet_eta[1]) < 4.7) || (JetPUPPI_eta[0] < 4.7 && JetPUPPI_eta[1] < 4.7)")
df_out = df_out.Filter("(abs(Jet_eta[0] - Jet_eta[1]) > 2.5) || (abs(JetPUPPI_eta[0] - JetPUPPI_eta[1]) > 2.5)")
df_out = df_out.Filter("(DiJet_mass > 400) || (DiJetPUPPI_mass > 400)")

counter_1 = df_out.Histo1D(("filteredEvents", "filteredEvents", 1, -100000,100000), "MuonTight_size")

hist = df_out.Histo1D("Muon_pt")
print("Launch Snapshot ", outputFileName)
df_out.Snapshot("Events", "%s"%outputFileName, nVariables)
print("Snapshot done")

file = ROOT.TFile("%s"%outputFileName,"update")
counter.Write()
counter_1.Write()
Vertex_size.Write()
file.Close()

print("Finished files: %s"%inputFileNames)
print("Finished sample %s"%outputFileName)

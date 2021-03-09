import ROOT
from sys import argv
import os
filename, outputFileName, inputFileName = argv                      # "vbfHmm_powheg", "DYToLL_madgraphMLM"
from variables import newVariables

#inputFileNames = open("%s"%inputFileName, "r")
#inputFileNames.read()
#inputFileNames = inputFileNames.split("\n")

with open("%s"%inputFileName, "r") as f:
    inputFileNames = list(f)

nEvents_max = -1
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
df_out = df_out.Define("DiMuon_mass", "InvariantMass( Muon_pt[0], Muon_eta[0], Muon_phi[0], 0.106,  Muon_pt[1], Muon_eta[1], Muon_phi[1], 0.106)") ## define DiMuon_mass variable (0.106 GeV is the muon mass)
    ###
df_out = df_out.Define("DiJet_mass", "InvariantMass( Jet_pt[0], Jet_eta[0], Jet_phi[0], Jet_mass[0],  Jet_pt[1], Jet_eta[1], Jet_phi[1], Jet_mass[1] )")

counter = df_out.Histo1D(("processedEvents", "processedEvents", 1, -100000,100000), "MuonTight_size")
vertex = df_out.Histo1D(("Vertex_size", "Vertex_size", 1, -100000,100000), "Vertex_size")

    ## Cuts ##

 
df_out = df_out.Filter("MuonTight_size >= 2") #require at least two muon
df_out = df_out.Filter("Muon_pt[0] > 20 && Muon_pt[1] > 20")
df_out = df_out.Filter("abs(Muon_eta[0]) < 2.8 && abs(Muon_eta[1]) < 2.8") #require the first muon to have pt>50 GeV
df_out = df_out.Filter("DiMuon_mass > 110 && DiMuon_mass < 150") #require at least two muon

    #df_out = df_out.Filter("Jet_size >= 2")
df_out = df_out.Filter("Jet_pt[0] > 35 && Jet_pt[1] > 25")
df_out = df_out.Filter("abs(Jet_eta[0]) < 4.7 && abs(Jet_eta[1]) < 4.7")
df_out = df_out.Filter("abs(Jet_eta[0] - Jet_eta[1]) > 2.5")
df_out = df_out.Filter("DiJet_mass > 400")

counter_1 = df_out.Histo1D(("filteredEvents", "filteredEvents", 1, -100000,100000), "MuonTight_size")

hist = df_out.Histo1D("Muon_pt")
print("Launch Snapshot")
df_out.Snapshot("Events", "%s"%outputFileName, nVariables)
print("Snapshot done")

file = ROOT.TFile("%s"%outputFileName,"update")
counter.Write()
counter_1.Write()
vertex.Write()
file.Close()

print("Finished files: %s"%inputFileNames)
print("Finished sample %s"%outputFileName)

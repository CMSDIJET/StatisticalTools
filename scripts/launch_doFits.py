#!/usr/bin/python
import os

sigXStimesA = {
    1000.0:  0.4101E+03,
    1100.0:  0.2620E+03,
    1200.0:  0.1721E+03,
    1300.0:  0.1157E+03,
    1400.0:  0.7934E+02,
    1500.0:  0.5540E+02,
    1600.0:  0.3928E+02,
    1700.0:  0.2823E+02,
    1800.0:  0.2054E+02,
    1900.0:  0.1510E+02,
    2000.0:  0.1121E+02,
    2100.0:  0.8390E+01,
    2200.0:  0.6328E+01,
    2300.0:  0.4807E+01,
    2400.0:  0.3674E+01,
    2500.0:  0.2824E+01,
    2600.0:  0.2182E+01,
    2700.0:  0.1694E+01,
    2800.0:  0.1320E+01,
    2900.0:  0.1033E+01,
    3000.0:  0.8116E+00,
    3100.0:  0.6395E+00,
    3200.0:  0.5054E+00,
    3300.0:  0.4006E+00,
    3400.0:  0.3182E+00,
    3500.0:  0.2534E+00,
    3600.0:  0.2022E+00,
    3700.0:  0.1616E+00,
    3800.0:  0.1294E+00,
    3900.0:  0.1038E+00,
    4000.0:  0.8333E-01,
    4100.0:  0.6700E-01,
    4200.0:  0.5392E-01,
    4300.0:  0.4344E-01,
    4400.0:  0.3503E-01,
    4500.0:  0.2827E-01,
    4600.0:  0.2283E-01,
    4700.0:  0.1844E-01,
    4800.0:  0.1490E-01,
    4900.0:  0.1205E-01,
    5000.0:  0.9743E-02,
    5100.0:  0.7880E-02,
    5200.0:  0.6373E-02,
    5300.0:  0.5155E-02,
    5400.0:  0.4169E-02,
    5500.0:  0.3371E-02,
    5600.0:  0.2725E-02,
    5700.0:  0.2202E-02,
    5800.0:  0.1779E-02,
    5900.0:  0.1437E-02,
    6000.0:  0.1159E-02,
    6100.0:  0.9353E-03,
    6200.0:  0.7541E-03,
    6300.0:  0.6076E-03,
    6400.0:  0.4891E-03,
    6500.0:  0.3935E-03,
    6600.0:  0.3164E-03,
    6700.0:  0.2541E-03,
    6800.0:  0.2039E-03,
    6900.0:  0.1635E-03,
    7000.0:  0.1310E-03,
    7100.0:  0.1049E-03,
    7200.0:  0.8385E-04,
    7300.0:  0.6699E-04,
    7400.0:  0.5347E-04,
    7500.0:  0.4264E-04,
    7600.0:  0.3397E-04,
    7700.0:  0.2704E-04,
    7800.0:  0.2151E-04,
    7900.0:  0.1709E-04,
    8000.0:  0.1357E-04,
    8100.0:  0.1077E-04,
    8200.0:  0.8544E-05,
    8300.0:  0.6773E-05,
    8400.0:  0.5367E-05,
    8500.0:  0.4251E-05,
    8600.0:  0.3367E-05,
    8700.0:  0.2666E-05,
    8800.0:  0.2112E-05,
    8900.0:  0.1673E-05,
    9000.0:  0.1326E-05
                       
}                
for i in range(1200,6100,100):
  cmd = "python create_datacard.py --histpdfSig --histpdfBkg -m "+str(i)+" --lumi 1000 -n genHistBkg_1100to4000 --sigEff 1. --sigXS "+str(sigXStimesA[i])+"  -o /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_combine/src/CMSDIJET/StatisticalTools/datacards_pseudodatasetDinko_fitData/  --inputSig /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeMaker/test/Resonance_Shapes_qg_PU20_13TeV_newJEC.root --inputData /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeAnalyzer/test_fit/dijetFitResults_FuncType0_nParFit4_MC_1fb-1_Dinko.root --inputBkg /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeAnalyzer/scripts/histo_bkg_mjj.root"
  cmd = "python create_datacard.py --histpdfSig --fitDat -m "+str(i)+" --lumi 1000 -n toFit_1100to4000 --sigEff 1. --sigXS "+str(sigXStimesA[i])+"  -o /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_combine/src/CMSDIJET/StatisticalTools/datacards_pseudodatasetDinko_fitData/ --inputSig /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeMaker/test/Resonance_Shapes_qg_PU20_13TeV_newJEC.root --inputData /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeAnalyzer/test_fit/dijetFitResults_FuncType0_nParFit4_MC_1fb-1_Dinko.root --inputBkg /cmshome/gdimperi/Dijet/CMSDIJETrepo/CMSSW_7_2_1_DiJet/src/CMSDIJET/DijetRootTreeAnalyzer/scripts/histo_bkg_mjj.root"
  print cmd
  os.system(cmd)  

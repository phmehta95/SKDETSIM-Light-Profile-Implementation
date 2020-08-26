/* ---------------- scanGraph.cxx ---------------- *
 * This will hopefully scan over the TGraphs from  *
 * the diffuser profiles and create a CDF which    *
 * can then be sampled from in order to produce a  *
 * correct diffuser MC sample.                     *
 *                                                 *
 *                                                 *
 *                      jmmcelwee1@sheffield.ac.uk *
 * ------------------------------ J. McElwee ----- */

#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TGraph.h"
#include <iostream>
#include "TGraphErrors.h"
#include "TF1.h"
#include <vector>
#include <fstream>

float returnFuncVal(float, TF1*);

int main(int argc, char const *argv[]){

  // READ IN DIFFUSER FILE
  // Somehow work out how to have random files input in this.
  // Extract the canvas from the ROOT file to allow extraction of the data.
  TFile diffuserPlot("B5/B5_diffuser_(D6)_air_graph_wPoly.root", "READ");
  diffuserPlot.ls();
  TCanvas *canvRead = (TCanvas*) diffuserPlot.Get("Canvas_1");
  canvRead->ls();
  

  // READ CANVAS
  TGraph *gh = (TGraph*)canvRead->GetListOfPrimitives()->FindObject("B5_Diffuser_(D6)_air_1d_theta_dist_graph");
  gh->GetListOfFunctions();


  // REPLOT AND FIT PROFILE
  // Refit the polynomial so I can use it later. So far not possible? 
  TCanvas fitCanv("fitCanv","");
  fitCanv.cd();
  gh->Fit("pol8");
  gh->Draw("AP");
  fitCanv.Print("B5/B5_fit.pdf");


  TF1 *example = (TF1*) gh->GetListOfFunctions()->FindObject("pol8");


  // REMAKE PROFILE USING FIT 
  // Remake the diffuser profile using the fit parameters found. Stores variables
  // in vectors for later.
  std::vector<float> angVec, CDFVec, cValVec;
  float currentVal, CDFVecHold;

  std::ofstream profile;
  profile.open("B5/B5_diff_prof.dat");
  for (float ang = -40.; ang < 40.1; ang+=0.5 ){
    currentVal = returnFuncVal(ang, example);
    cValVec.push_back(currentVal);
    angVec.push_back(ang);
  }
  std::vector<float>::iterator pedLoc = std::min_element(cValVec.begin(), cValVec.end());
  float pedestal = cValVec[std::distance(cValVec.begin(), pedLoc)];
  for (int i=0; i < cValVec.size(); i++) cValVec[i] -= pedestal;


  CDFVecHold = 0;
  for (int i=0; i < angVec.size(); i++){
    CDFVecHold += cValVec[i];
    CDFVec.push_back(CDFVecHold);
  }
  for (int i=0; i < CDFVec.size(); i++){
    CDFVec[i] /= CDFVecHold;
  }
  for (float i=0; i < cValVec.size(); i++){
    cValVec[i] /= CDFVecHold;
    profile << angVec[i] << " ";
    profile << std::setprecision(3) << cValVec[i] << "\n";
  }
  profile.close();
  
  TGraph *norm_profile = new TGraph(angVec.size(), &angVec[0], &cValVec[0]);
  TCanvas npCanv("npCanv", "");
  norm_profile->Draw("AL");
  npCanv.SaveAs("B5/B5_norm_profile.pdf");
  npCanv.Close();
  
  TCanvas cdfCanv("cdfCanv","");
  cdfCanv.cd();
  TGraph *CDF = new TGraph(angVec.size(), &angVec[0], &CDFVec[0]);
  CDF->Draw("ALP");
  cdfCanv.SaveAs("B5/B5_norm_CDF.pdf");
  cdfCanv.Close();

  return 0;
}





float returnFuncVal(float x, TF1 *function){

  // Okay I know this is bad and needs to change but it looks pretty
  //float coeff0 = function->GetParameter(0);
  float coeff1 = function->GetParameter(1) * x;
  float coeff2 = function->GetParameter(2) * x * x;
  float coeff3 = function->GetParameter(3) * x * x * x;
  float coeff4 = function->GetParameter(4) * x * x * x * x;
  float coeff5 = function->GetParameter(5) * x * x * x * x * x;
  float coeff6 = function->GetParameter(6) * x * x * x * x * x * x;
  float coeff7 = function->GetParameter(7) * x * x * x * x * x * x * x;
  float coeff8 = function->GetParameter(8) * x * x * x * x * x * x * x * x;

  float funcEquation = coeff1 + coeff2 + coeff3 + coeff4 + coeff5 + coeff6 + coeff7 + coeff8;

  return funcEquation;

}



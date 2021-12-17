# Purpose: Create a program to enter and calculate new insurance policy information for customers.
# Author: Zachary Butler
# Date: 12/10/2021
import datetime
x = datetime.datetime.now()

CustFirstName = input("Enter first name: ")
CustLastName = input("Enter last name: ")
CustAd = input("Street Address: ")
CustCity = input("City: ")
CustProv = input("Province: ")
CustPostal = input("Enter Postal code: ")
CustPhone = input("Enter phone number: ")
NumCarInsure = int(input("Enter amount of cars being insured: "))
ExtraLiability = (input("Enter Y or N, For extra liability up to $1,000,000: "))
OptGlassCov = input("Enter Y or N, For Optional Glass Coverage: ")
OptLoanCar = input("Enter Y or N, For Optional Loaner Car: ")
GlassCovPrice = 86.00
LoanCarPrice = 58.00
if ExtraLiability == "Y":
    ExtraLiability = "Yes"
elif ExtraLiability =="N":
    ExtraLiability = "No"
if OptGlassCov == "Y":
    OptGlassCov = "Yes"
elif OptGlassCov =="N":
    OptGlassCov = "No"
if OptLoanCar == "Y":
    OptLoanCar = "Yes"
elif OptLoanCar == "N":
    OptLoanCar = "No"
InsurancePrem = 0
if NumCarInsure >= 2:
    InsurancePrem = float(869.00 * .75)
elif NumCarInsure == 1:
    InsurancePrem = 869.00
ExtraLiabilityCost = 0
while OptLoanCar == "Y" or OptGlassCov == "Y":
    ExtraLiabilityCost = 130.00 * NumCarInsure

TotalExtraCost = float(ExtraLiabilityCost + GlassCovPrice + LoanCarPrice)
TotalInsurePrem = float(InsurancePrem + TotalExtraCost)
InsurepremHST = float(0.15 * TotalInsurePrem)
TotalCost = float(TotalInsurePrem + InsurepremHST)
ProcessFee = 39.99
MonthlyPaymentPrice = float(TotalCost + ProcessFee) / 12
MonthlyPaymentPriceRound = str(round(MonthlyPaymentPrice, 2))
f = open("Policies.dat", "a")
#f.write("{}, ".format())
f.write("{} ".format(CustFirstName))
f.write("{} ".format(CustLastName))
f.write("{} ".format(CustAd))
f.write("{} ".format(CustCity))
f.write("{} ".format(CustProv))
f.write("{} ".format(CustPostal))
f.write("{} ".format(CustPhone))
f.write("{} ".format(NumCarInsure))
f.write("{} ".format(ExtraLiability))
f.write("{} ".format(OptGlassCov))
f.write("{} ".format(OptLoanCar))
f.write("{} ".format(TotalCost))
f.close()
print("Policy processed and saved.")
PolicyDefault = 1944
print("1234567890123456789012345678901234567890")
print()
print("                ""One Stop Insurance")
print("                ""123 Kenmount Road")
print("             ""St. John's NL, A1A 1A1")
print("                 ""(709) 234-0987")
print("")
print("{} {} {}" .format("Customer Name:", CustFirstName, CustLastName))
print("{} {}" .format("Customer Phone:", CustPhone))
print("{} {} {} {} {}" .format("Customer Address:", CustAd, CustCity, CustProv, CustPostal))
print("")
print("            ""{} {}" .format("Number Of Cars Insured:", NumCarInsure))
print("            ""{} ${}" .format("Extra Costs: ", TotalExtraCost))
print("            ""{} ${}" .format("Insurance Price: ", TotalInsurePrem))
print("            ""{} ${}" .format("HST Price: ", InsurepremHST))
print("            ""{} ${}" .format("Total Cost:", TotalCost))
print("            ""{} ${}" .format("Monthly Cost:", MonthlyPaymentPrice))
print("**")
print("           ", x)
print("1234567890123456789012345678901234567890123456789012345678901234567890")
print()
print("ONE STOP INSURANCE COMPANY")
print("{} {}" .format("POLICY LISTING AS OF","dd-mm-yy"))
print()
print("{} {}                 {}  {}         {}" .format("POLICY", "CUSTOMER", "INSURANCE", "EXTRA", "TOTAL"))
print("{} {}                      {}   {}        {}" .format("NUMBER", "NAME", "PREMIUM", "COSTS", "PREMIUM"))
print("================================================================")
print("{}   {} {}                {}{}   {}{}      {}{}" .format(PolicyDefault, CustFirstName, CustLastName, "$", InsurancePrem, "$", TotalExtraCost, "$", TotalInsurePrem))
print()
print()
print("{}   {} {}                {}{}   {}{}      {}{}" .format(PolicyDefault, CustFirstName, CustLastName, "$", InsurancePrem, "$", TotalExtraCost, "$", TotalInsurePrem))
print("================================================================")
print()
print("{} : {}              {}{}   {}{}      {}{}" .format("Total policies:", NumCarInsure, "$", InsurancePrem, "$", TotalExtraCost, "$", TotalInsurePrem))
print("1234567890123456789012345678901234567890123456789012345678901234567890")
print()
print("ONE STOP INSURANCE COMPANY")
print("{} {}" .format("MONTHLY PAYMENT LISTING AS OF", x))
print()
print("{} {}             {}                 {}  {}" .format("POLICY", "CUSTOMER", "TOTAL", "TOTAL", "MONTHLY"))
print("{} {}                 {}     {}       {}   {}" .format("NUMBER", "NAME", "PREMIUM", "HST", "COST", "PAYMENT"))
print("================================================================")
print("{}  {} {}           {}{}   {}{}    {}{}   {}{}" .format(PolicyDefault, CustFirstName, CustLastName, "$", TotalInsurePrem, "$", InsurepremHST, "$", TotalCost, "$", MonthlyPaymentPriceRound))
print()
print("{}  {} {}           {}{}   {}{}    {}{}    {}{}" .format(PolicyDefault, CustFirstName, CustLastName, "$", TotalInsurePrem, "$", InsurepremHST, "$", TotalCost, "$", MonthlyPaymentPriceRound))
print("================================================================")
print("{}: {}         {}{}   {}{}   {}{}     {}{}". format("Total policies:", NumCarInsure, "$", TotalInsurePrem, "$", InsurepremHST, "$", TotalCost, "$", MonthlyPaymentPriceRound))

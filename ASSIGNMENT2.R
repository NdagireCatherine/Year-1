library(dplyr)
library(readxl)
library(DT)
library(ggplot2)

#setting a working directorate
setwd("~/Documents/INTRODUCTION TO DATA SCIENCE")

#I imported my data set and renamed it as data
data0<-read_excel("Loan_Approval_Data.xlsx")


#NUMBER 1#
#Exploration of my data#
#this enables me to see the number of columns and rows
dim(data0)
#I was able to see that my data set has 614 columns and 12 rows

#at this step I am going to find out which variables are categorical and which ones are continuous
sapply(data, class)
#categorical variables are loan_ID, gender, married, dependents, education, self_employed, loan_status
#continuous variables are applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history

#since the categorical variables are nominal we shall treat them as functions
data0$Loan_ID = as.factor(data0$Loan_ID)
data0$Gender = as.factor(data0$Gender)
data0$Married = as.factor(data0$Married)
data0$Dependents = as.factor(data0$Dependents)
data0$Education = as.factor(data0$Education)
data0$Self_Employed = as.factor(data0$Self_Employed)
data0$Loan_Status = as.factor(data0$Loan_Status)


#NUMBER 2#
library(dplyr)
#finding missing data
sum(is.na(data0))
#there is 150 missing data in the data set
#futher more we notice that only 24% of the data is missing hence we can replace the missing data with the median

summary(data0)
#from the summary we discover that none of the variables are normally distributed thus we can replace the missing data with the median
data0_impute_median = data0 %>%
  mutate_if(is.numeric, function(x) ifelse(is.na(x), median(x, na.rm = T), x))

sum(is.na(data0_impute_median))
#the sum is now 64 hence the missing data of the continuous variables has been imputed with the median

#handling outliers#
#to view the outliers I am going to use boxplots
boxplot(data0$ApplicantIncome, main="Applicant income")
boxplot(data0$CoapplicantIncome, main="Coapplicant income")
boxplot(data0$LoanAmount, main="Loan amount")
boxplot(data0$Loan_Amount_Term, main="Loan amount term")
boxplot(data0$Credit_History, main="Credit history")

#this function is going to be able to detect outliers in each variable
detect_outlier = function(x) {
  Quantile1 = quantile(x, probs=.25)
  Quantile3 = quantile(x, probs=.75)
  IQR = Quantile3 - Quantile1
  x > Quantile3 + (IQR * 1.5) | x < Quantile1 - (IQR * 1.5)
}

#this function is goin to be to remove the outliers detected in each variable
remove_outlier = function(dataframe, columns = names(dataframe)) {
  for (col in columns) {
    dataframe = dataframe[!detect_outlier(dataframe[[col]]), ]
  }
  print("Remove outliers")
  print(dataframe)
}
data0_new = remove_outlier(data0_impute_median, c("ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"))
View(data0_new)
#the new data set has 383 observations hence outliers have been removed


#NUMBER 3#
#saved the new dataset as an csv file
write.csv(data0_new, file="loan_approaval_data_new.csv")


#NUMBER 4#
#visualization between two continuous variables using a scatter plot
ggplot(data0_new, mapping = aes(x=ApplicantIncome, y=LoanAmount))+
  geom_point()+
  labs(x="Applicant Income",
       y="LoanAmount",
       title="Applicant Income vs LoanAmount")

#statistical tests on two continuous variables
#covariance
cov(data0_new$ApplicantIncome, data0_new$LoanAmount, use="complete.obs")
#result=33402.53 hence the two variables are positively varying over time
#As the applicants income increases the loan amount also increases

#correlation
cor(data0_new$ApplicantIncome, data0_new$LoanAmount, use="complete.obs")
#result=0.4669335 hence a moderate positive correlation

cor.test(data0_new$ApplicantIncome, data0_new$LoanAmount, use="complete.obs")
#p-value=2.2e^-16 hence correlation is not equal to 0 thus null hypothesis rejected otherwise not normally distributed



#NUMBER 5#
#visualization between a categorial variable and a continuous variable using a frequency line
ggplot(data = data0_new, mapping = aes(x = CoapplicantIncome )) +
  geom_freqpoly(mapping = aes(colour = Dependents))+
  labs(x="Coapplicant Income",
       title="Coappliacant Income depending on the dependents")

#statistical tests between a categoriable variable and a continuous variable
install.packages("dgof")
library(dgof)
ks.test(data0_new$CoapplicantIncome, "pnorm")
#P-value = 2.2e-16 which is less than 0.05 hence Coapplicant Income is not normally didstributed



#NUMBER 6#
#visualization between two categorical variables using a count plot
ggplot(data = data0_new)+
  geom_count(mapping = aes(x=Gender, y= Education))+
  labs(x="Gender",
       y="Education",
       title="Level of eduaction for each Gender")





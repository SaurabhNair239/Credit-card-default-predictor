# Credit Card Defaulter

It is an machine learning classification based model which is helpful in predicting that the user will opt for the default payment system or not.

## Design and Technologies
- Engineered the development using the CI/CD Pipeline Model
- sklearn  
- Docker
- Microsoft Azure
    - Azure SQL Database
    - Azure Container Registry

## Introduction to Dataset

This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

### Features
-ID: ID of each client
-LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
-SEX: Gender (1=male, 2=female)
-EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
-MARRIAGE: Marital status (1=married, 2=single, 3=others)
-AGE: Age in years
-PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
-PAY_2: Repayment status in August, 2005 (scale same as above)
-PAY_3: Repayment status in July, 2005 (scale same as above)
-PAY_4: Repayment status in June, 2005 (scale same as above)
-PAY_5: Repayment status in May, 2005 (scale same as above)
-PAY_6: Repayment status in April, 2005 (scale same as above)
-BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
-BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
-BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
-BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
-BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
-BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
-PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
-PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
-PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
-PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
-PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
-PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
-default.payment.next.month: Default payment (1=yes, 0=no)


## Data Analysis using SQL Commands

No of female candidates
> SELECT COUNT(*) FROM data where sex='Female' 

No of Male candidates

> SELECT COUNT(*) FROM data where sex='Female' 

No of Female accoding to education

> SELECT EDUCATION,COUNT(*) FROM data where sex='Female' group by "EDUCATION" 
 
No of Male according to education

> SELECT EDUCATION,COUNT(*) FROM data where sex='Male' group by "EDUCATION" 

No data from seperate Marriage status

> select MARRIAGE,count(MARRIAGE) FROM data group by MARRIAGE

Update Married status

> UPDATE data SET MARRIAGE ='Other' where MARRIAGE IS NULL

Education and marriage in a descending order

> SELECT EDUCATION,MARRIAGE,count(MARRIAGE) as counting FROM data group by EDUCATION, MARRIAGE order by counting desc;

Education vs output

> SELECT EDUCATION, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by EDUCATION,default_payment_next_month order by Count_values desc

Gender vs output

> SELECT SEX, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by SEX,default_payment_next_month order by Count_values desc

Average LIMIT balance of gender on the basis of their default pyment next month

> SELECT round(avg(LIMIT_BAL),2) as average_limit_balance,sex,default_payment_next_month from data group by SEX,default_payment_next_month order by average_limit_balance  

Average payment_amount of month 1 to 6 according to gender and education 

> SELECT EDUCATION,SEX,AVG(PAY_AMT1+PAY_AMT2+PAY_AMT3+PAY_AMT4+PAY_AMT5+PAY_AMT6) as Average_payment from data group by EDUCATION,SEX order by Average_payment desc;

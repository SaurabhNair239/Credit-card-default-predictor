# Credit Card Defaulter

It is an machine learning classification based model which is helpful in predicting that the user will opt for the default payment system or not.

## Design and Technologies
- Designed using CI/CD model
- sklearn  
- Docker
- Microsoft Azure
    - Azure SQL Database
    - Azure Container Registry

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

> select Education,MARRIAGE,count(MARRIAGE) as counting FROM data group by Education, MARRIAGE order by counting desc;

Education vs output

> select education, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by education,default_payment_next_month order by Count_values desc

Gender vs output

> select sex, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by sex,default_payment_next_month order by Count_values desc

Average LIMIT balance of gender on the basis of their default pyment next month

> select round(avg(limit_bal),2) as average_limit_balance,sex,default_payment_next_month from data group by sex,default_payment_next_month order by average_limit_balance  

Average payment_amount of month 1 to 6 according to gender and education 

> select education,sex,AVG(PAY_AMT1+PAY_AMT2+PAY_AMT3+PAY_AMT4+PAY_AMT5+PAY_AMT6) as Average_payment from data group by education,sex order by Average_payment desc;

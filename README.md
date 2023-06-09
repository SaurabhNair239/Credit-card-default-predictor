# Default of Credit Card Clients Dataset
It is an machine learning classification based model which is helpful in predicting that the user will opt for the default payment system or not.
### Workflow 
![ML Workflow](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/Imgs/workflow.jpg)

Dataset: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

Application link: https://credit-card-defaulter.azurewebsites.net/

## Data Analysis

###  Data Analysis using SQL Commands 

No of female candidates
> SELECT COUNT(*) FROM data where sex='Female' 

No of Male candidates

> SELECT COUNT(*) FROM data where sex='Female' 

![Female male customer](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/figure1.jpeg)

No of Female accoding to education

> SELECT EDUCATION,COUNT(*) FROM data where sex='Female' group by "EDUCATION" 
 
No of Male according to education

> SELECT EDUCATION,COUNT(*) FROM data where sex='Male' group by "EDUCATION" 

![Marriage Education](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/figure2.jpeg)

No data from seperate Marriage status

> select MARRIAGE,count(MARRIAGE) FROM data group by MARRIAGE

![Customer Marital status](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/figure3.jpeg)

Update Married status

> UPDATE data SET MARRIAGE ='Other' where MARRIAGE IS NULL

Education and marriage in a descending order

> SELECT EDUCATION,MARRIAGE,count(MARRIAGE) as counting FROM data group by EDUCATION, MARRIAGE order by counting desc;

![Marital status education](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/figure4.jpeg)

Education vs output

> SELECT EDUCATION, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by EDUCATION,default_payment_next_month order by Count_values desc

![Education vs Output](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/figure5.jpeg)

Gender vs output

> SELECT SEX, default_payment_next_month as output_val, count(default_payment_next_month) Count_values from data group by SEX,default_payment_next_month order by Count_values desc

Average LIMIT balance of gender on the basis of their default pyment next month

> SELECT round(avg(LIMIT_BAL),2) as average_limit_balance,sex,default_payment_next_month from data group by SEX,default_payment_next_month order by average_limit_balance  

Average payment_amount of month 1 to 6 according to gender and education 

> SELECT EDUCATION,SEX,AVG(PAY_AMT1+PAY_AMT2+PAY_AMT3+PAY_AMT4+PAY_AMT5+PAY_AMT6) as Average_payment from data group by EDUCATION,SEX order by Average_payment desc;

** Note you can find data visualisation and EDA code in [EDA VISUALISATION](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/notebook/EDA%20VISUALISATION.ipynb) file

## Docker command
*  Building Docker file
> docker build -t <YOUR_USERNAME>/<IMAGE_NAME> .

* Running Docker file on local system
> docker run server=<SERVER_LINK> -e db_name=<DATABASE_NAME> -e username=<USERNAME> -e password=<PASSWORD> -p 8501:8501 <YOUR_USERNAME>/<IMAGE_NAME> 

** Note the application will start in localhost on port number 8501: https://localhost:8501

* Pushing Docker file on Docker Hub 
>docker push <<YOUR_USERNAME>/<IMAGE_NAME>

## Deployment on Azure

![azure page 1](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/Imgs/azure_1.jpg)

![azure page 2](https://github.com/SaurabhNair239/Credit-card-default-predictor/blob/main/Imgs/azure_2.jpg)

** Note the deployment is not free of cost one so if you are using this service for educational purpose stop it after the usage. 

## Next step:
* Imporving models by determining important features
* Data analysis using R programming 

## Reference

Krish Naik: https://youtu.be/S_F_c9e2bz4

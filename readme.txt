*** Read Me Before You Run The Code ***

0. get_job_links.py and get_job_details.py is used to scrapy the job data from indeed, the  data already scrapied and stored in job_details_all_without_duplicate.csv, to save your time, you don't need to run these two files

1. job_details_pre_process.ipynb is used to pre_process data, if you want to change it, it will refresh the job_details_processed.csv. You may not need to change it if no big issues of the code.

2. job_details_clustering.ipynb is used to cluster the data, you need to change the number of clusters of KMeans to check which result is better. Please do it.

3. get_job_skills.ipynb and get_education_levels.ipynb are used to get the skills and education_levels, please run it after you change job_details_clustering.ipynb to get the latest result.

Our proposal:

In "technology" domain, in Singapore,
1. Which job has highest demands in Singapore? - Cluster (Generate word cloud)
2. What are the most common skills for the highest demanded positions? 
3. What is the preferred education level for the highest demanded jobs? (Diploma, Bachelor, Master, Phd - if no: Not-mentioned or set to Bachelor)


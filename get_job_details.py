from gevent.monkey import patch_all; patch_all()
from gevent.pool import Pool
import pickle
import pandas as pd
from selenium import webdriver

import time

df = pd.read_csv('job_links.csv')
job_links = df.job_link.tolist()

# Need to replace with correct version of chromedriver for your laptop
driver = webdriver.Chrome("./chromedriver")


# Define a function to get jod details
def get_jd (driver, idx, job_link):
	print(job_link)
	driver.get(job_link)
	print(idx)
	time.sleep(5)

	try:
		job_title_elem = driver.find_elements_by_class_name('jobsearch-JobInfoHeader-title')
		job_title = job_title_elem[0].text

		job_company_elem = driver.find_elements_by_class_name('jobsearch-InlineCompanyRating')
		job_company = job_company_elem[0].text.split('\n')[0]

		job_description_elem = driver.find_elements_by_class_name('jobsearch-JobComponent-description')
		job_description = job_description_elem[0].text

		job_detail = (job_link, job_title, job_company, job_description)
		job_details.append(job_detail)
		# print(job_detail)
	except Exception as e:
		print(job_link, e)
		return False, job_link
	return True, job_detail


# Use multi-thread to scrapy job details from Indeed.com.sg
todo_jobs = job_links
job_details = []

pool = Pool(10)

while todo_jobs:
	lets = []
	for idx, job_link in enumerate(todo_jobs):
		lets.append(pool.spawn(get_jd, driver, idx, job_link))
	pool.join()
	job_details.extend(list(let.value[1] for let in lets if let.value[0]))
	todo_jobs = [let.value[1] for let in lets if not let.value[0]]
	print(len(todo_jobs))
	with open("failed_jobs.dump", "wb") as f:
		pickle.dump(todo_jobs, f)
	time.sleep(5)

driver.quit()

# Remove the duplicate job_details and save them to csv
filename = "job_details_all_without_duplicate.csv"
df = pd.DataFrame(job_details).rename(columns={0:"job_link", 1:"job_title", 2:"company", 3:"job_desc"})
df = df.groupby(["job_title", "company"]).first().reset_index()[["job_link", "job_title", "company", "job_desc"]]
df.to_csv(filename, index=False)

	






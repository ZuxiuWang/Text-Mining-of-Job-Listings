from selenium import webdriver

import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('window-size=2560,1440')
driver = webdriver.Chrome("./chromedriver", chrome_options=options)

# Get the links of full-time jobs
job_links = []
# base_url = 'https://www.indeed.com.sg/jobs?q=technology&l=Singapore&start='
base_url = 'https://www.indeed.com.sg/jobs?q=technology&l=Singapore&jt=fulltime&start='


for page_idx in range(2, 10):
	start = str(10 * page_idx)
	url = base_url + str(start)

	driver.get(url)
	time.sleep(5)

	job_title_elems = driver.find_elements_by_class_name('turnstileLink')

	for job_title_elem in job_title_elems:
		if 'slNoUnderline' not in job_title_elem.get_attribute("class"):
			# job_title = job_title_elem.text
			job_link = job_title_elem.get_attribute('href').split('\n')[0]
	
			job_links.append(job_link)

driver.quit()

# Remove the invalid links
job_links_clear = []
for job_link in job_links:
	job_yield = job_link.split("/")

	if job_yield[3] != "cmp":
		if job_link not in job_links_clear:
			job_links_clear.append(job_link)

# Write job_link to csv
df = pd.DataFrame(job_links_clear).rename(columns={0:"job_link"})
df.to_csv('job_links.csv', index=False)





# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:38:47 2024

@author: a.eddelymy
"""

import unicodecsv

enrollments_filename = 'C:/Users/a.eddelymy/Documents/data_analysis/enrollments.csv'


with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

engagement_filename = 'C:/Users/a.eddelymy/Documents/data_analysis/daily_engagement.csv'
submissions_filename = 'C:/Users/a.eddelymy/Documents/data_analysis/project_submissions.csv'
    
with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)
    print(daily_engagement[0])

with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)
    print(project_submissions[0])
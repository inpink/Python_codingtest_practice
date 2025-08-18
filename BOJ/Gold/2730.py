import sys
input = sys.stdin.readline
from datetime import date

def is_leap_year(year):
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(year,month,day):
  if month==2 and day==29:
    if is_leap_year(year):
      return True
    else:
      return False
  return True

n=int(input())
for i in range(n):
  due_date, report_date= input().split()
  due_month,due_day,due_year = map(int,due_date.split("/"))
  report_month,report_day=map(int,report_date.split("/"))

  due_date_object=date(due_year, due_month, due_day)

  candidates=dict()

  #this report
  if is_valid_date(due_year,report_month,report_day):
    this_report_date_object=date(due_year, report_month, report_day)
    this_diff=this_report_date_object-due_date_object
    candidates[this_diff.days]=due_year

  #before report
  before_year=due_year-1
  if is_valid_date(before_year,report_month,report_day):
    before_report_date_object=date(before_year, report_month, report_day)
    before_diff=before_report_date_object-due_date_object
    candidates[before_diff.days]=before_year

  #next report
  next_year=due_year+1
  if is_valid_date(next_year,report_month,report_day):
    next_report_date_object=date(next_year,report_month,report_day)
    next_diff=next_report_date_object-due_date_object
    candidates[next_diff.days]=next_year

  # print(candidates)

  if len(candidates)==0:
    print("OUT OF RANGE")
    continue

  if 0 in candidates.keys():
    print("SAME DAY")
    continue

  isContinue=False
  for key in candidates:
    if key>=-7 and key<0:
      if key==-1:
        print(f"{report_month}/{report_day}/{candidates[key]} IS {abs(key)} DAY PRIOR")
      else:
        print(f"{report_month}/{report_day}/{candidates[key]} IS {abs(key)} DAYS PRIOR")
      isContinue=True
      break
    elif key>0 and key<=7:
      if key==1:
        print(f"{report_month}/{report_day}/{candidates[key]} IS {abs(key)} DAY AFTER")
      else:
        print(f"{report_month}/{report_day}/{candidates[key]} IS {abs(key)} DAYS AFTER")
      isContinue=True
      break

  if not isContinue:
    print("OUT OF RANGE")
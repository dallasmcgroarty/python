# function that return outputs

def format_name(f_name, l_name):
  """
  Take a first and lase name and format it to return the title case version.
  """
  if f_name == '' or l_name == '':
    return 'You didn\'t provide valid inputs'
  title_f = f_name.title()
  title_l = l_name.title()

  return f'{title_f} {title_l}'

print(format_name('daLLas', 'MCGROARTY'))
print(format_name(input('What is your first name? '), input('What is your last name? ')))

# return days in month accounting for leap year
def is_leap(year):
  """
    Calculates if the year is a leap year or not. Returns True if leap year, otherwise return False
  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month == 2:
    return month_days[month-1] + 1    
  return month_days[month-1]

year = 2019
month = 2
days = days_in_month(year, month)
print(days)

# doc strings

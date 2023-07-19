import re


def convert_company_name_to_re_pattern(company_name):
    re_pattern = ''.join([c + '.*' for c in company_name])
    return re_pattern


if __name__ == '__main__':
    company_list = ['qwerty', 'q.w.e.r.t.y', 'QWERTY', 'q.w.e.r.t.y LTD', 'Qwerty LTD', 'zxcvbn']
    company_to_find = 'qwerty'
    regex = convert_company_name_to_re_pattern(company_to_find)
    #    print(regex)
    for company in company_list:
        match = re.search(regex, company, re.IGNORECASE)
        print(match[0] if match else 'Not found')

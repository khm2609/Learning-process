import re


text = '''1.Peter 30
2.Nastya 50
3.Hunter 100
4.Eu 50
'''

text1 = '''edjjeee fjfej rjfejfjj kwofovdocv 13/10/2022 difrkgr dieifivi22/12/23 kfirold05/06/2040'''
re.findall(r'([A-z]+)\s(\d+)',text)
print(re.findall(r'(\d{1,2}.\d{1,2}.\d{2,4})',text1))

    #ihateregex
    #regex101


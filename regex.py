import re
text = 'ggjgjgjhg ggggg gugugu dhurrell@hotmail.vo.europe'

pattern = re.search(r'[\w]+@[\w]+.[\w]+.?\w{6}?',text)
print(pattern.group())

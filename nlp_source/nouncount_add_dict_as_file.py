# 단어를 엑셀파일 형태로 불러와서 twitter에 추가한다
# 명사추출 후 noun count 결과를 저장한다 
# count 결과를 dict 형태에서 바로 dataframe 으로 바꾸도록 수정함~

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
from ckonlpy.tag import Twitter


def noun_count(root, file_name, twitter):
    f = open(root + file_name, 'r', encoding='UTF8')
    text = f.read()
    nouns = twitter.nouns(text)
    count = Counter(nouns)

    df1 = pd.DataFrame(list(count.items()), columns = ['word', 'count'])
    df1 = df1.sort_values(by='count', ascending=False)
    df1.to_excel(root + '%s_noun_count.xlsx' %(file_name), index=False)

def add_new_word(root):
    dict_name = 'add_dict_for_backpack.xlsx'
    add_dict = pd.read_excel(root + dict_name)
    new_word = list(add_dict['new_word'])
    return new_word
    
def main():
    root = 'C:/Users/leevi/Desktop/데상트_3월/'
    file_name_list = ['스타일쉐어_content만.txt']
    
    new_word = add_new_word(root)
    twitter = Twitter()
    twitter.add_dictionary(new_word, 'Noun')
    
    for file_name in file_name_list:
        noun_count(root, file_name, twitter)
        print('noun parsing 저장완료')
        

if __name__ == "__main__":
    main()




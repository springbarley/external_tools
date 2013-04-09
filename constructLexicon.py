#coding = utf-8
import codecs
from string import Template
import time

fcitx_file = "D:\\xmu_GP\\corpus_for_input\\fcitx\\pyPhrase.org"
lexicon_style_file = "D:\\xmu_GP\corpus_for_input\\pytrie_lexicon\
\\lexicon_text.org"

single_word_file = ""
single_lexicon_file = ""
max_single_word_length = 20

lexicon_line = Template('${chinese_word} ${id} ${pinyin_first}:${cost} \n')

def doConstruct(fcitx_file,  lexicon_style_ile):
    in_file = codecs.open(fcitx_file, 'r', 'utf-8')
    out_file = codecs.open(lexicon_style_file,  'w',  'utf-8')
    id = 0
    begin = time.clock()
    for aline in in_file:
        aline = aline.rstrip()
        (pinyin,  chinese) = aline.split(" ")
        #print(lexicon_line.substitute(chinese_word = chinese, id = id,  pinyin_first = pinyin, cost = 1.0))
        out_file.write(lexicon_line.substitute(chinese_word = chinese, id = id,  pinyin_first = pinyin, cost = 1.0))
        print(id)
        id += 1
    print('usiage',  time.clock() - begin)
    in_file.close()
    out_file.close()
    
def doConstructSingleWordLexicon(single_word_file,  single_lexicon_file):
    in_file = codecs.open(single_word_file,  'r',  'utf-8')
    out_file = codecs.open(single_lexicon_file,  'w',  'utf-8')
    id = 0
    for line in in_file:
        syllable,space, word_string = line.partition("\t")
        syllable = syllable.strip()
        word_string = word_string.strip()
        len_lower = len(word_string);
        if len(word_string) > max_single_word_length:
            len_lower = max_single_word_length; 
        for i in range(len_lower):
            out_file.write(lexicon_line.substitute(chinese_word = word_string[i],  id = id,  pinyin_first = syllable,  cost = 1.0/len_lower))
            id += 1
    in_file.close()
    out_file.close()
    
if __name__ == '__main__':
    print("construct pytrie lexicon begin...")
    test_string = 'asdf asdf asdf asdf'
    #print(test_string.split(" ",  1))
    #doConstruct()
    doConstructSingleWordLexicon("D:\\xmu_GP\\corpus_for_input\\chinese single word\\chinese_single.txt",  "D:\\xmu_GP\\corpus_for_input\\chinese single word\\single_lexicon.org")
    print("const pytrie lexicon end...")

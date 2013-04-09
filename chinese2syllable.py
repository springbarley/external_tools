import os
import sys
import codecs
#coding = gbk
def loadDictionary(dictionary_path,  dic_map):
    dic_file = codecs.open(dictionary_path,  'r',  'utf-8')
    #file_length = os.stat(dictionary_path).st_size
    dic_map = {}
    print("already remove %s" % "BOM_UTF8")
    if dic_file.readline()[:3] == codecs.BOM_UTF8:
        dic_file.read(3)
    while True:
        line = dic_file.readline()
        key_value = line.split(" ")
        dic_map[key_value[0]] = key_value[1]
    print("load dictionary done...")
    
#if __name__ == "__main__":
  #  print (sys.getdefaultencoding())
    #dic_map = {}
    #loadDictionary("D:\\xmu_GP\\corpus_for_input\\fcitx\\pyPhrase.org", dic_map)

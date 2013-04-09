
#coding = utf-8
import sys
import os
import codecs
def removePos(filename,  outfile):
    print("do remove pos...")
    in_stream = codecs.open(filename,  'r',  'utf-8')
    out_stream = codecs.open(outfile,  'w',  'utf-8')
    for line in in_stream:
        if len(line) <= 2:
            continue
        word_pos_list = [word_pos.strip() for word_pos in line.split(" ")]
        #print( word_pos_list )
        word_list = [item.split("/")[0] + " " for item in word_pos_list if item.find('-') < 0 and len(item) > 0]
        #print( word_list )
        out_stream.writelines(word_list)
        out_stream.write("\n")
    in_stream.close()
    out_stream.close()
    print("have done...")

def transferWordSplitToCharacterSplit(file_name,  out_file):
    in_stream = codecs.open(file_name,  'r',  'utf-8')
    out_stream = codecs.open(out_file,  'w',  'utf-8')
    print("do split single character in a file...")
    for line in in_stream:
        word_list = line.split(" ")
        new_single_list = []
        for item in word_list:
            new_single_list.extend([character.strip() + " " for character in item])
        new_single_list.extend(['\n'])
        #print(new_single_list)
        out_stream.writelines(new_single_list)
    in_stream.close()
    out_stream.close()
    print("split done...")

if __name__ == "__main__":
    #removePos("D:\\xmu_GP\\corpus_for_input\\98\\peoples publication 98 1.txt",  "D:\\xmu_GP\\corpus_for_input\\98\\98_with_no_pos.org")
    transferWordSplitToCharacterSplit("D:\\xmu_GP\\corpus_for_input\\98\\98_with_no_pos.org",  "D:\\xmu_GP\\corpus_for_input\\98\\98_no_pos_character_based.org")

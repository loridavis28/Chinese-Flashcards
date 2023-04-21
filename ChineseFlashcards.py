from tkinter import *
import random

class Card:
    def __init__(self, ChineseAnswer, PinyinAnswer, EnglishAnswer, Chapter):
        self.ChineseAnswer = ChineseAnswer
        self.PinyinAnswer = PinyinAnswer
        self.EnglishAnswer = EnglishAnswer
        self.Chapter = Chapter

EntryWindow = Tk()


#################By default, the target entry language is English, with both characters and pinyin showing.################################
TargetEntry = "English"
ShowChineseToggle = 1
ShowPinyinToggle = 1
ShowEnglishToggle = 0
TotalAsked = 0
TotalCorrect = 0


##This reads in the All Time totals
file = open("ChineseFlashcards.txt", "r")
lines = file.readlines()
AllTimeTotalAsked = int(lines[0])
AllTimeTotalCorrect = int(lines[1])
file.close

##This creates the total list of words
TotalCardList = []
TotalCardList.append(Card("我", "wo3", "I", 1))
TotalCardList.append(Card("你", "ni3", "you", 1))
TotalCardList.append(Card("好", "hao3", "good", 1))
TotalCardList.append(Card("一", "yi1", "one", 1))
TotalCardList.append(Card("二", "er4", "two", 1))
TotalCardList.append(Card("三", "san1", "three", 1))
TotalCardList.append(Card("四", "si4", "four", 1))
TotalCardList.append(Card("五", "wu3", "five", 1))
TotalCardList.append(Card("六", "liu4", "six", 1))
TotalCardList.append(Card("七", "qi1", "seven", 1))
TotalCardList.append(Card("八", "ba1", "eight", 1))
TotalCardList.append(Card("九", "jiu3", "nine", 1))
TotalCardList.append(Card("十", "shi2", "ten", 1))
TotalCardList.append(Card("先生", "xian1sheng", "Mr.", 1))
TotalCardList.append(Card("你好", "ni3hao3", "hello", 1))
TotalCardList.append(Card("小姐", "xiao3jie", "Miss", 1))
TotalCardList.append(Card("请问", "qing3wen4", "May I ask", 1))
TotalCardList.append(Card("请", "qing3", "please", 1))
TotalCardList.append(Card("问", "wen4", "to ask", 1))
TotalCardList.append(Card("您", "nin2", "you (polite)", 1))
TotalCardList.append(Card("贵姓", "gui4xing4", "What is your honorable surname?", 1))
TotalCardList.append(Card("贵", "gui4", "honorable", 1))
TotalCardList.append(Card("姓", "xing4", "surname", 1))
TotalCardList.append(Card("呢", "ne", "a particle", 1))
TotalCardList.append(Card("叫", "jiao4", "to be called", 1))
TotalCardList.append(Card("什麽", "shen2me", "what", 1))
TotalCardList.append(Card("名字", "ming2zi", "name", 1))
TotalCardList.append(Card("王", "wang2", "king", 1))
TotalCardList.append(Card("李", "li3", "plum", 1))
TotalCardList.append(Card("是", "shi4", "to be", 1))
TotalCardList.append(Card("老师", "lao3shi1", "teacher", 1))
TotalCardList.append(Card("吗", "ma", "question particle", 1))
TotalCardList.append(Card("不", "bu4", "not, no", 1))
TotalCardList.append(Card("学生", "xue2sheng", "student", 1))
TotalCardList.append(Card("也", "ye3", "also", 1))
TotalCardList.append(Card("中国人", "Zhong1guo2ren2", "Chinese person", 1))
TotalCardList.append(Card("中国", "Zhong1guo2", "China", 1))
TotalCardList.append(Card("人", "ren2", "person", 1))
TotalCardList.append(Card("美国人", "Mei3guo2ren2", "American person", 1))
TotalCardList.append(Card("美国", "Mei3guo2", "USA", 1))
TotalCardList.append(Card("朋友", "peng2you", "friend", 1))
TotalCardList.append(Card("太太", "tai4tai", "wife", 1))
TotalCardList.append(Card("英国", "Ying1guo2", "England", 1))
TotalCardList.append(Card("法国", "Fa3guo2", "France", 1))
TotalCardList.append(Card("日本", "Ri4ben3", "Japan", 1))
TotalCardList.append(Card("德国", "De2guo2", "Germany", 1))

TotalCardList.append(Card("那", "na4", "that", 2))
TotalCardList.append(Card("张", "zhang1", "MW for flat objects", 2))
TotalCardList.append(Card("照片", "zhao4pian4", "picture", 2))
TotalCardList.append(Card("的", "de", "possessive particle", 2))
TotalCardList.append(Card("这", "zhe4", "this", 2))
TotalCardList.append(Card("爸爸", "ba4ba", "dad", 2))
TotalCardList.append(Card("妈妈", "ma1ma", "mom", 2))
TotalCardList.append(Card("个", "ge4", "MW for general objects", 2))
TotalCardList.append(Card("男孩子", "nan2hai2zi", "boy", 2))
TotalCardList.append(Card("男", "nan2", "male", 2))
TotalCardList.append(Card("孩子", "hai2zi", "child", 2))
TotalCardList.append(Card("谁", "shei2", "who", 2))
TotalCardList.append(Card("他", "ta1", "he", 2))
TotalCardList.append(Card("第第", "di4di", "younger brother", 2))
TotalCardList.append(Card("女孩子", "nü3hai2zi", "girl", 2))
TotalCardList.append(Card("女", "nü3", "female", 2))
TotalCardList.append(Card("妹妹", "mei4mei", "younger sister", 2))
TotalCardList.append(Card("她", "ta1", "she", 2))
TotalCardList.append(Card("女儿", "nü3'er2", "daughter", 2))
TotalCardList.append(Card("有", "you3", "to have", 2))
TotalCardList.append(Card("儿子", "er2zi", "son", 2))
TotalCardList.append(Card("没", "mei2", "not", 2))
TotalCardList.append(Card("小", "xiao3", "small", 2))
TotalCardList.append(Card("家", "jia1", "family", 2))
TotalCardList.append(Card("几", "ji3", "how many", 2))
TotalCardList.append(Card("哥哥", "ge1ge", "older brother", 2))
TotalCardList.append(Card("两", "liang3", "both", 2))
TotalCardList.append(Card("姐姐", "jie3jie", "older sister", 2))
TotalCardList.append(Card("和", "he2", "and", 2))
TotalCardList.append(Card("做", "zuo4", "to do", 2))
TotalCardList.append(Card("英文", "Ying1wen2", "English", 2))
TotalCardList.append(Card("律师", "lü4shi1", "lawyer", 2))
TotalCardList.append(Card("都", "dou1", "both, all", 2))
TotalCardList.append(Card("大学生", "da4xue2sheng1", "college student", 2))
TotalCardList.append(Card("大学", "da4xue2", "college", 2))
TotalCardList.append(Card("医生", "yi1sheng1", "doctor, physician", 2))

TotalCardList.append(Card("九月", "jiu3yue4", "September", 3))
TotalCardList.append(Card("月", "yue4", "month", 3))
TotalCardList.append(Card("十二", "shi2er4", "twelve", 3))
TotalCardList.append(Card("号", "hao4", "day of the month; number", 3))
TotalCardList.append(Card("星期四", "xing1qi1si4", "Thursday", 3))
TotalCardList.append(Card("星期", "xing1qi1", "week", 3))
TotalCardList.append(Card("天", "tian1", "day", 3))
TotalCardList.append(Card("生日", "sheng1ri4", "birthday", 3))
TotalCardList.append(Card("生", "sheng1", "to be born", 3))
TotalCardList.append(Card("日", "ri4", "day, sun", 3))
TotalCardList.append(Card("今年", "jin1nian2", "this year", 3))
TotalCardList.append(Card("年", "nian2", "year", 3))
TotalCardList.append(Card("多大", "duo1da4", "how old", 3))
TotalCardList.append(Card("多", "duo1", "how many", 3))
TotalCardList.append(Card("大", "da4", "big, old", 3))
TotalCardList.append(Card("十八", "shi2ba1", "eighteen", 3))
TotalCardList.append(Card("岁", "sui4", "year (of age)", 3))
TotalCardList.append(Card("请", "qing3", "to invite", 3))
TotalCardList.append(Card("吃", "chi1", "to eat", 3))
TotalCardList.append(Card("晚饭", "wan3fan4", "dinner", 3))
TotalCardList.append(Card("晚", "wan3", "evening", 3))
TotalCardList.append(Card("饭", "fan4", "meal", 3))
TotalCardList.append(Card("吃饭", "chi1fan4", "to eat (a meal)", 3))
TotalCardList.append(Card("怎么样", "zen3meyang4", "okay?", 3))
TotalCardList.append(Card("太。。。了", "tai4...le", "too", 3))
TotalCardList.append(Card("谢谢", "xie4xie", "thank you", 3))
TotalCardList.append(Card("喜欢", "xi3huan", "to like", 3))
TotalCardList.append(Card("还是", "hai2shi4", "or", 3))
TotalCardList.append(Card("可是", "ke3shi4", "but", 3))
TotalCardList.append(Card("好", "hao3", "ok", 3))
TotalCardList.append(Card("我们", "wo3men", "we", 3))
TotalCardList.append(Card("点钟", "dian3zhong1", "o'clock", 3))
TotalCardList.append(Card("钟", "zhong1", "clock", 3))
TotalCardList.append(Card("半", "ban4", "half", 3))
TotalCardList.append(Card("晚上", "wan3shang", "evening, night", 3))
TotalCardList.append(Card("见", "jian4", "to see", 3))
TotalCardList.append(Card("再见", "zai4jian4", "good-bye", 3))
TotalCardList.append(Card("再", "zai4", "again", 3))
TotalCardList.append(Card("白", "bai2", "white", 3))
TotalCardList.append(Card("现在", "xian4zai4", "now", 3))
TotalCardList.append(Card("刻", "ke4", "15 minutes", 3))
TotalCardList.append(Card("事", "shi4", "matter, affair", 3))
TotalCardList.append(Card("明天", "ming2tian1", "tomorrow", 3))
TotalCardList.append(Card("忙", "mang2", "busy", 3))
TotalCardList.append(Card("今天", "jin1tian1", "today", 3))
TotalCardList.append(Card("很", "hen3", "very", 3))
TotalCardList.append(Card("为什么", "wei4shen2me", "why", 3))
TotalCardList.append(Card("为", "wei4", "for", 3))
TotalCardList.append(Card("因为", "yin1wei4", "because", 3))
TotalCardList.append(Card("还有", "hai2you3", "also", 3))
TotalCardList.append(Card("同学", "tong2xue2", "classmate", 3))
TotalCardList.append(Card("认识", "ren4shi", "to know (someone)", 3))
TotalCardList.append(Card("分", "fen1", "minute", 3))
TotalCardList.append(Card("差", "cha4", "to be short of, lack", 3))
TotalCardList.append(Card("昨天", "zuo2tian1", "yesterday", 3))
TotalCardList.append(Card("前天", "qian2tian1", "day before yesterday", 3))
TotalCardList.append(Card("后天", "hou4tian1", "day after tomorrow", 3))
TotalCardList.append(Card("明年", "ming2nian2", "next year", 3))
TotalCardList.append(Card("去年", "qu4nian2", "last year", 3))
TotalCardList.append(Card("前年", "qian2nian2", "year before last", 3))
TotalCardList.append(Card("后年", "hou4nian2", "year after next", 3))
TotalCardList.append(Card("下个月", "xia4geyue4", "next month", 3))
TotalCardList.append(Card("表", "biao3", "watch", 3))

TotalCardList.append(Card("周末", "zhou1mo4", "weekend", 4))
TotalCardList.append(Card("打球", "da3qiu2", "to play ball", 4))
TotalCardList.append(Card("打", "da3", "to hit", 4))
TotalCardList.append(Card("球", "qiu2", "ball", 4))
TotalCardList.append(Card("看", "kan4", "to watch", 4))
TotalCardList.append(Card("电视", "dian4shi4", "TV", 4))
TotalCardList.append(Card("电", "dian4", "electricity", 4))
TotalCardList.append(Card("视", "shi4", "vision", 4))
TotalCardList.append(Card("唱", "chang4", "to sing", 4))
TotalCardList.append(Card("歌", "ge1", "song", 4))
TotalCardList.append(Card("跳舞", "tiao4wu3", "to dance", 4))
TotalCardList.append(Card("跳", "tiao4", "to jump", 4))
TotalCardList.append(Card("舞", "wu3", "dance", 4))
TotalCardList.append(Card("听", "ting1", "to listen", 4))
TotalCardList.append(Card("音乐", "yin1yue4", "music", 4))
TotalCardList.append(Card("对", "dui4", "right, correct", 4))
TotalCardList.append(Card("有时候", "you3 shi2hou4", "sometimes", 4))
TotalCardList.append(Card("看书", "kan4shu1", "to read", 4))
TotalCardList.append(Card("书", "shu1", "book", 4))
TotalCardList.append(Card("电影", "dian4ying3", "movie", 4))
TotalCardList.append(Card("影", "ying3", "shadow", 4))
TotalCardList.append(Card("常常", "chang2chang2", "often", 4))
TotalCardList.append(Card("那", "na4", "in that case", 4))
TotalCardList.append(Card("去", "qu4", "to go", 4))
TotalCardList.append(Card("外国", "wai4guo2", "foreign country", 4))
TotalCardList.append(Card("请客", "qing3ke4", "to invite someone to dinner", 4))
TotalCardList.append(Card("昨天", "zuo2tian1", "yesterday", 4))
TotalCardList.append(Card("锁以", "suo3yi3", "so", 4))
TotalCardList.append(Card("好久", "hao3jiu3", "a long time", 4))
TotalCardList.append(Card("久", "jiu3", "for a long time", 4))
TotalCardList.append(Card("不错", "bu2cuo4", "not bad", 4))
TotalCardList.append(Card("错", "cuo4", "wrong", 4))
TotalCardList.append(Card("想", "xiang3", "to want to, to think", 4))
TotalCardList.append(Card("觉得", "jue2de", "to feel", 4))
TotalCardList.append(Card("有意思", "you3 yi4si", "interesting", 4))
TotalCardList.append(Card("意思", "yi4si", "meaning", 4))
TotalCardList.append(Card("只", "zhi3", "only", 4))
TotalCardList.append(Card("睡觉", "shui4jiao4", "to sleep", 4))
TotalCardList.append(Card("算了", "suan4le", "forget it", 4))
TotalCardList.append(Card("找", "zhao3", "to look for", 4))
TotalCardList.append(Card("别的", "bie2de", "other", 4))
TotalCardList.append(Card("对了", "dui4le", "Right!", 4))
TotalCardList.append(Card("蓝球", "lan2qiu2", "basketball", 4))
TotalCardList.append(Card("网球", "wang3qiu2", "tennis", 4))
TotalCardList.append(Card("橄榄球", "gan3lan3qiu2", "football", 4))
TotalCardList.append(Card("棒球", "bang4qiu2", "baseball", 4))
TotalCardList.append(Card("足球", "zu2qiu2", "soccer", 4))
TotalCardList.append(Card("排球", "pai2qiu2", "volleyball", 4))

TotalCardList.append(Card("呀", "ya", "(used to soften a question)", 5))
TotalCardList.append(Card("进", "jin4", "to enter", 5))
TotalCardList.append(Card("快", "kuai4", "fast", 5))
TotalCardList.append(Card("进来", "jin4lai2", "come in", 5))
TotalCardList.append(Card("来", "lai2", "to come", 5))
TotalCardList.append(Card("介绍", "jie4shao4", "to introduce", 5))
TotalCardList.append(Card("意下", "yi2xia4", "a little (adv)", 5))
TotalCardList.append(Card("高兴", "gao1xing4", "happy", 5))
TotalCardList.append(Card("漂亮", "piao4liang", "pretty", 5))
TotalCardList.append(Card("坐", "zuo4", "to sit", 5))
TotalCardList.append(Card("在", "zai4", "at, in, on", 5))
TotalCardList.append(Card("哪儿", "nar3", "where", 5))
TotalCardList.append(Card("工作", "gong1zuo4", "to work", 5))
TotalCardList.append(Card("学校", "xue2xiao4", "school", 5))
TotalCardList.append(Card("喝", "he1", "to drink", 5))
TotalCardList.append(Card("点", "dian3", "a little", 5))
TotalCardList.append(Card("茶", "cha2", "tea", 5))
TotalCardList.append(Card("咖啡", "ka1fei1", "coffee", 5))
TotalCardList.append(Card("啤酒", "pi2jiu3", "beer", 5))
TotalCardList.append(Card("酒", "jiu3", "wine", 5))
TotalCardList.append(Card("吧", "ba", "(used to soften the tone)", 5))
TotalCardList.append(Card("姚", "yao4", "to want", 5))
TotalCardList.append(Card("杯", "bei1", "cup", 5))
TotalCardList.append(Card("可乐", "ke3le4", "cola", 5))
TotalCardList.append(Card("可以", "ke3yi3", "can, may", 5))
TotalCardList.append(Card("对不起", "dui4buqi3", "I'm sorry", 5))
TotalCardList.append(Card("给", "gei3", "to give", 5))
TotalCardList.append(Card("水", "shui3", "water", 5))
TotalCardList.append(Card("玩", "wan2", "to have fun", 5))
TotalCardList.append(Card("图书馆", "tu2shu1guan3", "library", 5))
TotalCardList.append(Card("瓶", "ping2", "bottle", 5))
TotalCardList.append(Card("一起", "yi4qi3", "together", 5))
TotalCardList.append(Card("聊天", "liao2tian1", "to chat", 5))
TotalCardList.append(Card("才", "cai2", "not until (later than expected)", 5))
TotalCardList.append(Card("回家", "hui2jia1", "to go home", 5))
TotalCardList.append(Card("回", "hui2", "to return", 5))
TotalCardList.append(Card("打工", "da3gong1", "to have a part-time job", 5))
TotalCardList.append(Card("好吃", "hao3chi1", "good to eat", 5))
TotalCardList.append(Card("好喝", "hao3he1", "good to drink", 5))
TotalCardList.append(Card("好看", "hao3kan4", "good-looking", 5))
TotalCardList.append(Card("好玩", "hao3wan2", "fun", 5))
TotalCardList.append(Card("可口可乐", "ke3kou3ke3le4", "Coke", 5))
TotalCardList.append(Card("百事可乐", "bai3shi4ke3le4", "Pepsi", 5))
TotalCardList.append(Card("雪碧", "xue3bi4", "Sprite", 5))
TotalCardList.append(Card("汽水", "qi4shui3", "soft drink", 5))
TotalCardList.append(Card("矿泉水", "kuang4quan2shui3", "mineral water", 5))

TotalCardList.append(Card("给", "gei3", "to, for", 6))
TotalCardList.append(Card("打电话", "da3dian4hua4", "to make a phone call", 6))
TotalCardList.append(Card("电话", "dian4hua4", "phone", 6))
TotalCardList.append(Card("话", "hua4", "speech", 6))
TotalCardList.append(Card("喂", "wei4", "hello", 6))
TotalCardList.append(Card("在", "zai4", "to be present, to be at", 6))
TotalCardList.append(Card("哪", "na3", "which", 6))
TotalCardList.append(Card("位", "wei4", "MW for people", 6))
TotalCardList.append(Card("下午", "xia4wu3", "afternoon", 6))
TotalCardList.append(Card("时间", "shi2jian1", "time", 6))
TotalCardList.append(Card("几", "ji3", "some", 6))
TotalCardList.append(Card("问题", "wen4ti2", "question", 6))
TotalCardList.append(Card("要", "yao4", "will, be going to", 6))
TotalCardList.append(Card("开会", "kai1hui4", "to have a meeting", 6))
TotalCardList.append(Card("开", "kai1", "to hold (a meeting, party...)", 6))
TotalCardList.append(Card("上午", "shang4wu3", "morning", 6))
TotalCardList.append(Card("节", "jie2", "MW for class period", 6))
TotalCardList.append(Card("课", "ke4", "class, lesson", 6))
TotalCardList.append(Card("年级", "nian2ji2", "grade in school", 6))
TotalCardList.append(Card("考是", "kao3shi4", "test", 6))
TotalCardList.append(Card("以后", "yi3hou4", "after", 6))
TotalCardList.append(Card("有空", "you3kong4", "to have time", 6))
TotalCardList.append(Card("要是", "yao4shi4", "if", 6))
TotalCardList.append(Card("方便", "fang1bian4", "convenient", 6))
TotalCardList.append(Card("到。。。去", "dao4...qu4", "to go to", 6))
TotalCardList.append(Card("瓣公室", "ban4gong1shi4", "office", 6))
TotalCardList.append(Card("行", "xing2", "all right", 6))
TotalCardList.append(Card("没问题", "mei2wen4ti2", "no problem", 6))
TotalCardList.append(Card("等", "deng3", "to wait", 6))
TotalCardList.append(Card("不客气", "bu2ke4qi", "you're welcome", 6))
TotalCardList.append(Card("客气", "ke4qi", "polite", 6))
TotalCardList.append(Card("帮盲", "bang1mang2", "to do a favor", 6))
TotalCardList.append(Card("别客气", "bie2ke4qi", "don't be so polite!", 6))
TotalCardList.append(Card("别", "bie2", "don't", 6))
TotalCardList.append(Card("下个星期", "xia4gexing1qi1", "next week", 6))
TotalCardList.append(Card("下", "xia4", "next", 6))
TotalCardList.append(Card("中文", "Zhong1wen2", "Chinese language", 6))
TotalCardList.append(Card("帮", "bang1", "to help", 6))
TotalCardList.append(Card("练习", "lian4xi2", "to practice", 6))
TotalCardList.append(Card("说", "shuo1", "to say, speak", 6))
TotalCardList.append(Card("啊", "a", "(emphasize agreement)", 6))
TotalCardList.append(Card("但是", "dan4shi4", "but", 6))
TotalCardList.append(Card("得", "dei3", "must", 6))
TotalCardList.append(Card("知道", "zhi1dao4", "to know", 6))
TotalCardList.append(Card("回来", "hui2lai2", "to come back", 6))
TotalCardList.append(Card("中午", "zhong1wu3", "noon", 6))
TotalCardList.append(Card("法文", "Fa3wen2", "French language", 6))
TotalCardList.append(Card("日文", "Ri4wen2", "Japanese language", 6))
TotalCardList.append(Card("德文", "De2wen2", "German language", 6))
TotalCardList.append(Card("韩国", "Han2guo2", "Korea", 6))
TotalCardList.append(Card("韩文", "Han2wen2", "Korean language", 6))
TotalCardList.append(Card("俄国", "E2guo2", "Russia", 6))
TotalCardList.append(Card("俄文", "E2wen2", "Russian language", 6))
TotalCardList.append(Card("西班牙", "Xi1ban1ya2", "Spain", 6))
TotalCardList.append(Card("西班牙文", "Xi1ban1ya2wen2", "Spanish language", 6))
TotalCardList.append(Card("意大利", "Yi4da4li4", "Italy", 6))
TotalCardList.append(Card("意大利文", "Yi4da4li4wen2", "Italian language", 6))
TotalCardList.append(Card("葡萄牙", "Pu2tao2ya2", "Portugal", 6))
TotalCardList.append(Card("葡萄牙文", "Pu2tao2ya2wen2", "Portuguese language", 6))
TotalCardList.append(Card("希腊", "Xi1la4", "Greece", 6))
TotalCardList.append(Card("希腊文", "Xi1la4wen2", "Greek language", 6))
TotalCardList.append(Card("拉丁文", "La1ding1wen2", "Latin", 6))
TotalCardList.append(Card("越南", "Yue4nan2", "Vietnam", 6))
TotalCardList.append(Card("菲律宾", "Fei1lv4bin1", "Philippines", 6))
TotalCardList.append(Card("泰国", "Tai4guo2", "Thailand", 6))
TotalCardList.append(Card("马来西亚", "Ma3lai2xi1ya4", "Malaysia", 6))
TotalCardList.append(Card("夏威夷", "Xia4wei1yi2", "Hawaii", 6))

TotalCardList.append(Card("跟", "gen1", "and", 7))
TotalCardList.append(Card("说话", "shuo1hua4", "to talk", 7))
TotalCardList.append(Card("上个星期", "shang4gexing1qi1", "last week", 7))
TotalCardList.append(Card("得", "de", "(a particle used after a verb and before a descriptive complement)", 7))
TotalCardList.append(Card("帮助", "bang1zhu4", "to help", 7))
TotalCardList.append(Card("复习", "fu4xi2", "to review", 7))
TotalCardList.append(Card("字", "zi4", "word", 7))
TotalCardList.append(Card("写", "xie3", "to write", 7))
TotalCardList.append(Card("慢", "man4", "slow", 7))
TotalCardList.append(Card("教", "jiao1", "to teach", 7))
TotalCardList.append(Card("就", "jiu4", "(indicates that something takes place sooner than expected)", 7))
TotalCardList.append(Card("学", "xue2", "to study", 7))
TotalCardList.append(Card("笔", "bi3", "pen", 7))
TotalCardList.append(Card("难", "nan2", "difficult", 7))
TotalCardList.append(Card("快", "kuai4", "fast", 7))
TotalCardList.append(Card("哪里", "na3li", "not at all (polite reply to a compliment)", 7))
TotalCardList.append(Card("第", "di4", "(prefix for ordinal numbers)", 7))
TotalCardList.append(Card("预习", "yu4xi2", "to preview", 7))
TotalCardList.append(Card("语法", "yu3fa3", "grammar", 7))
TotalCardList.append(Card("容易", "rong2yi4", "easy", 7))
TotalCardList.append(Card("多", "duo1", "many", 7))
TotalCardList.append(Card("懂", "dong3", "to understand", 7))
TotalCardList.append(Card("生词", "sheng1ci2", "new words", 7))
TotalCardList.append(Card("汉字", "Han4zi4", "Chinese characters", 7))
TotalCardList.append(Card("有一点儿", "you3yi4dianr3", "a little", 7))
TotalCardList.append(Card("不谢", "bu2xie4", "don't mention it", 7))
TotalCardList.append(Card("平常", "ping2chang2", "usually", 7))
TotalCardList.append(Card("早", "zao3", "early", 7))
TotalCardList.append(Card("怎么", "zen3me", "how come", 7))
TotalCardList.append(Card("这么", "zhe4me", "so, such", 7))
TotalCardList.append(Card("半夜", "ban4ye4", "midnight", 7))
TotalCardList.append(Card("功课", "gong1ke4", "homework", 7))
TotalCardList.append(Card("朋友", "peng2you", "friend", 7))
TotalCardList.append(Card("真", "zhen1", "really", 7))
TotalCardList.append(Card("大家", "da4jia1", "everybody", 7))
TotalCardList.append(Card("造", "zao3", "good morning", 7))
TotalCardList.append(Card("开始", "kai1shi3", "to start", 7))
TotalCardList.append(Card("上课", "shang4ke4", "to go to class", 7))
TotalCardList.append(Card("念", "nian4", "to read aloud", 7))
TotalCardList.append(Card("课文", "ke4wen2", "text of a lesson", 7))
TotalCardList.append(Card("录音", "lu4yin1", "sound recording", 7))
TotalCardList.append(Card("男的", "nan2de", "male", 7))
TotalCardList.append(Card("帅", "shuai4", "handsome", 7))
TotalCardList.append(Card("铅笔", "qian1bi3", "pencil", 7))
TotalCardList.append(Card("钢笔", "gang1bi3", "fountain pen", 7))
TotalCardList.append(Card("毛笔", "mao2bi3", "writing brush", 7))
TotalCardList.append(Card("纸", "zhi3", "paper", 7))
TotalCardList.append(Card("本子", "ben3zi", "notebook", 7))
TotalCardList.append(Card("午觉", "wu3jiao4", "nap", 7))

TotalCardList.append(Card("篇", "pian1", "MW for essays", 8))
TotalCardList.append(Card("日记", "ri4ji4", "diary", 8))
TotalCardList.append(Card("早上", "zao3shang4", "morning", 8))
TotalCardList.append(Card("起床", "qi3chuang2", "to get up", 8))
TotalCardList.append(Card("床", "chuang2", "bed", 8))
TotalCardList.append(Card("洗澡", "xi3zao3", "to take a bath/shower", 8))
TotalCardList.append(Card("早饭", "zao3fan4", "breakfast", 8))
TotalCardList.append(Card("一边。。。一边", "yi4bian1...yi4bian1", "(indicates two simultaneous actions)", 8))
TotalCardList.append(Card("教室", "jiao4shi4", "classroom", 8))
TotalCardList.append(Card("发音", "fa1yin1", "pronunciation", 8))
TotalCardList.append(Card("新", "xin1", "new", 8))
TotalCardList.append(Card("电脳", "dian4nao3", "computer", 8))
TotalCardList.append(Card("脳", "nao3", "brain", 8))
TotalCardList.append(Card("中午", "zhong1wu3", "noon", 8))
TotalCardList.append(Card("餐厅", "can1ting1", "dining room", 8))
TotalCardList.append(Card("午饭", "wu3fan4", "lunch", 8))
TotalCardList.append(Card("报", "bao4", "newspaper", 8))
TotalCardList.append(Card("宿舍", "su4she4", "dormitory", 8))
TotalCardList.append(Card("到", "dao4", "to arrive", 8))
TotalCardList.append(Card("那人", "nar4", "there", 8))
TotalCardList.append(Card("。。。的时候", "...deshi2hou4", "when", 8))
TotalCardList.append(Card("正在", "zheng4zai4", "in the middle of", 8))
TotalCardList.append(Card("以前", "yi3qian2", "before", 8))
TotalCardList.append(Card("高速", "gao4su4", "to tell", 8))
TotalCardList.append(Card("已经", "yi3jing1", "already", 8))
TotalCardList.append(Card("封", "feng1", "MW for letters", 8))
TotalCardList.append(Card("信", "xin4", "letter", 8))
TotalCardList.append(Card("最近", "zui4jin4", "recently", 8))
TotalCardList.append(Card("最", "zui4", "most", 8))
TotalCardList.append(Card("近", "jin4", "near", 8))
TotalCardList.append(Card("学期", "xue2qi1", "semester", 8))
TotalCardList.append(Card("除了。。。以外", "chu2le...yi3wai4", "besides", 8))
TotalCardList.append(Card("专业", "zhuan1ye4", "major", 8))
TotalCardList.append(Card("会", "hui4", "can (know how to)", 8))
TotalCardList.append(Card("开始", "kai1shi3", "to begin", 8))
TotalCardList.append(Card("习惯", "xi2guan4", "to be accustomed to", 8))
TotalCardList.append(Card("后来", "hou4lai2", "later", 8))
TotalCardList.append(Card("清楚", "qing1chu", "clear", 8))
TotalCardList.append(Card("进步", "jin4bu4", "to make progress", 8))
TotalCardList.append(Card("音乐会", "yin1yue4hui4", "concert", 8))
TotalCardList.append(Card("希望", "xi1wang4", "to hope", 8))
TotalCardList.append(Card("能", "neng2", "can, able to", 8))
TotalCardList.append(Card("用", "yong4", "to use", 8))
TotalCardList.append(Card("笑", "xiao4", "to laugh", 8))
TotalCardList.append(Card("祝", "zhu4", "to wish", 8))


TotalCardList.append(Card("買", "mai3", "to buy", 9))
TotalCardList.append(Card("东西", "dong1xi", "things", 9))
TotalCardList.append(Card("售货员", "shou4huo4yuan2", "shop assistant", 9))
TotalCardList.append(Card("要", "yao4", "to have a desire for", 9))
TotalCardList.append(Card("衣服", "yi1fu", "clothes", 9))
TotalCardList.append(Card("件", "jian4", "MW for shirts", 9))
TotalCardList.append(Card("衬衫", "chen4shan1", "shirt", 9))
TotalCardList.append(Card("颜色", "yan2se4", "color", 9))
TotalCardList.append(Card("黄", "huang2", "yellow", 9))
TotalCardList.append(Card("红", "hong2", "red", 9))
TotalCardList.append(Card("穿", "chuan1", "to wear", 9))
TotalCardList.append(Card("条", "tiao2", "MW for pants and long, thin objects", 9))
TotalCardList.append(Card("裤子", "ku4zi", "pants", 9))
TotalCardList.append(Card("号", "hao4", "number, size", 9))
TotalCardList.append(Card("中", "zhong1", "medium", 9))
TotalCardList.append(Card("贵", "gui4", "expensive", 9))
TotalCardList.append(Card("便宜", "pian2yi", "cheap", 9))
TotalCardList.append(Card("付钱", "fu4qian2", "to pay money", 9))
TotalCardList.append(Card("钱", "qian2", "money", 9))
TotalCardList.append(Card("这儿", "zher4", "here", 9))
TotalCardList.append(Card("一共", "yi2gong4", "altogether", 9))
TotalCardList.append(Card("多少", "duo1shao", "how much", 9))
TotalCardList.append(Card("块", "kuai4", "dollar", 9))
TotalCardList.append(Card("毛", "mao2", "dime", 9))
TotalCardList.append(Card("分", "fen1", "cent", 9))
TotalCardList.append(Card("拜", "bai3", "hundred", 9))
TotalCardList.append(Card("找钱", "zhao3qian2", "to give change", 9))
TotalCardList.append(Card("双", "shuang1", "a pair", 9))
TotalCardList.append(Card("鞋", "xie2", "shoes", 9))
TotalCardList.append(Card("换", "huan4", "to change, exchange", 9))
TotalCardList.append(Card("一样", "yi2yang4", "same", 9))
TotalCardList.append(Card("虽然", "sui1ran2", "although", 9))
TotalCardList.append(Card("大小", "da4xiao3", "size", 9))
TotalCardList.append(Card("合适", "he2shi4", "suitable", 9))
TotalCardList.append(Card("咖啡色", "ka1fei1se4", "brown", 9))
TotalCardList.append(Card("黑", "hei1", "black", 9))
TotalCardList.append(Card("不用", "bu2yong4", "need not", 9))
TotalCardList.append(Card("钱", "qian2", "money", 9))
TotalCardList.append(Card("卖", "mai4", "to sell", 9))
TotalCardList.append(Card("裙子", "qun2zi", "skirt", 9))
TotalCardList.append(Card("大衣", "da4yi1", "overcoat", 9))
TotalCardList.append(Card("夹克", "jia2ke4", "jacket", 9))
TotalCardList.append(Card("外套", "wai4tao4", "coat", 9))
TotalCardList.append(Card("西装", "xi1zhuang1", "suit", 9))
TotalCardList.append(Card("毛衣", "mao2yi1", "sweater", 9))
TotalCardList.append(Card("T恤衫", "T-xu4shan1", "T-shirt", 9))
TotalCardList.append(Card("戴", "dai4", "to wear", 9))
TotalCardList.append(Card("帽子", "mao4zi", "hat", 9))
TotalCardList.append(Card("顶", "ding3", "MW for hat", 9))
TotalCardList.append(Card("袜子", "wa4zi", "socks", 9))
TotalCardList.append(Card("长", "chang2", "long", 9))
TotalCardList.append(Card("短", "duan3", "short", 9))
TotalCardList.append(Card("蓝", "lan2", "blue", 9))
TotalCardList.append(Card("绿", "lv4", "green", 9))
TotalCardList.append(Card("紫", "zi3", "purple", 9))
TotalCardList.append(Card("粉红色", "fen3hong2se4", "pink", 9))
TotalCardList.append(Card("橘红色", "ju2hong2se4", "orange", 9))
TotalCardList.append(Card("灰", "hui1", "grey", 9))

TotalCardList.append(Card("天气", "tian1qi4", "weather", 10))
TotalCardList.append(Card("比", "bi3", "(comparison)", 10))
TotalCardList.append(Card("下雨", "xia4yu3", "to rain", 10))
TotalCardList.append(Card("报上", "bao4shang", "in the newspaper", 10))
TotalCardList.append(Card("预报", "yu4bao4", "forecast", 10))
TotalCardList.append(Card("更", "geng4", "even more", 10))
TotalCardList.append(Card("不但。。。而且", "bu2dan4...er2qie3", "not only...but also", 10))
TotalCardList.append(Card("会", "hui4", "probably will", 10))
TotalCardList.append(Card("暖和", "nuan3huo", "warm", 10))
TotalCardList.append(Card("一点儿", "yi4dianr3", "a bit", 10))
TotalCardList.append(Card("约", "yue1", "to make an appointment", 10))
TotalCardList.append(Card("共园", "gong1yuan2", "park", 10))
TotalCardList.append(Card("红叶", "hong2ye4", "red fall leaves", 10))
TotalCardList.append(Card("怎么办", "zen3meban4", "what to do", 10))
TotalCardList.append(Card("录像", "lu4xiang4", "video recording", 10))
TotalCardList.append(Card("海", "hai3", "ocean", 10))
TotalCardList.append(Card("糟糕", "zao1gao1", "bad luck", 10))
TotalCardList.append(Card("又", "you4", "again", 10))
TotalCardList.append(Card("刚才", "gang1cai2", "just now", 10))
TotalCardList.append(Card("这个", "zhe4ge", "this", 10))
TotalCardList.append(Card("出去", "chu1qu", "to go out", 10))
TotalCardList.append(Card("热", "re4", "hot", 10))
TotalCardList.append(Card("舒服", "shu1fu", "comfortable", 10))
TotalCardList.append(Card("夏天", "xia4tian1", "summer", 10))
TotalCardList.append(Card("这样", "zhe4yang4", "so, like this", 10))
TotalCardList.append(Card("凉快", "liang2kuai", "nice and cool", 10))
TotalCardList.append(Card("春天", "chun1tian1", "spring", 10))
TotalCardList.append(Card("冬天", "dong1tian1", "winter", 10))
TotalCardList.append(Card("又。。。又", "you4...you4", "both...and", 10))
TotalCardList.append(Card("冷", "leng3", "cold", 10))
TotalCardList.append(Card("闷", "men1", "stuffy", 10))
TotalCardList.append(Card("下次", "xia4ci4", "next time", 10))
TotalCardList.append(Card("次", "ci4", "time, occurrence", 10))
TotalCardList.append(Card("最好", "zui4hao3", "had better", 10))
TotalCardList.append(Card("秋天", "qiu1tian1", "fall", 10))
TotalCardList.append(Card("潮湿", "chao2shi1", "wet, humid", 10))
TotalCardList.append(Card("云", "yun2", "cloud", 10))
TotalCardList.append(Card("雪", "xue3", "snow", 10))
TotalCardList.append(Card("晴", "qing2", "sunny", 10))
TotalCardList.append(Card("阴", "yin1", "overcast", 10))
TotalCardList.append(Card("加拿大", "Jia1na2da4", "Canada", 10))


TotalCardList.append(Card("寒假", "han2jia4", "winter vacation", 11))
TotalCardList.append(Card("飞机", "fei1ji1", "airplane", 11))
TotalCardList.append(Card("飞", "fei1", "to fly", 11))
TotalCardList.append(Card("机", "ji1", "machine", 11))
TotalCardList.append(Card("票", "piao4", "ticket", 11))
TotalCardList.append(Card("飞机场", "fei1ji1chang3", "airport", 11))
TotalCardList.append(Card("坐", "zuo4", "to travel by", 11))
TotalCardList.append(Card("公共汽车", "gong1gong4qi4che1", "bus", 11))
TotalCardList.append(Card("公共", "gong1gong4", "public", 11))
TotalCardList.append(Card("汽车", "qi4che1", "automobile", 11))
TotalCardList.append(Card("车", "che1", "car", 11))
TotalCardList.append(Card("或者", "huo4zhe3", "or", 11))
TotalCardList.append(Card("地铁", "di4tie3", "subway", 11))
TotalCardList.append(Card("走", "zou3", "to walk", 11))
TotalCardList.append(Card("先", "xian1", "first", 11))
TotalCardList.append(Card("站", "zhan4", "stop, station", 11))
TotalCardList.append(Card("下车", "xia4che1", "to get off", 11))
TotalCardList.append(Card("然后", "ran2hou4", "then", 11))
TotalCardList.append(Card("绿", "lv4", "green", 11))
TotalCardList.append(Card("线", "xian4", "line", 11))
TotalCardList.append(Card("最后", "zui4hou4", "finally", 11))
TotalCardList.append(Card("蓝", "lan2", "blue", 11))
TotalCardList.append(Card("麻烦", "ma2fan", "troublesome", 11))
TotalCardList.append(Card("还是", "hai2shi", "had better", 11))
TotalCardList.append(Card("出租汽车", "chu1zu1qi4che1", "taxi", 11))
TotalCardList.append(Card("出租", "chu1zu1", "to rent out", 11))
TotalCardList.append(Card("租", "zu1", "to rent", 11))
TotalCardList.append(Card("汽车", "kai1che1", "to drive a car", 11))
TotalCardList.append(Card("汽", "kai1", "to drive, operate", 11))
TotalCardList.append(Card("送", "song4", "to take someone (somewhere)", 11))
TotalCardList.append(Card("不过", "bu2guo4", "however", 11))
TotalCardList.append(Card("让", "rang4", "to allow or cause", 11))
TotalCardList.append(Card("花", "hua1", "to spend", 11))
TotalCardList.append(Card("不好意思", "bu4hao3yi4si", "to feel embarrassed", 11))
TotalCardList.append(Card("这几天", "zhe4ji3tian1", "the past few days", 11))
TotalCardList.append(Card("每天", "mei3tian1", "every day", 11))
TotalCardList.append(Card("每", "mei3", "every", 11))
TotalCardList.append(Card("高速公路", "gao1su4gong1lu4", "highway", 11))
TotalCardList.append(Card("高速", "gao1su4", "high speed", 11))
TotalCardList.append(Card("公路", "gong1lu4", "highway", 11))
TotalCardList.append(Card("路", "lu4", "road", 11))
TotalCardList.append(Card("紧张", "jin3zhang1", "nervous", 11))
TotalCardList.append(Card("自己", "zi4ji3", "oneself", 11))
TotalCardList.append(Card("新年", "xin1nian2", "new year", 11))
TotalCardList.append(Card("快", "kuai4", "soon", 11))
TotalCardList.append(Card("快乐", "kuai4le4", "happy", 11))
TotalCardList.append(Card("走路", "zou3lu4", "walk", 11))
TotalCardList.append(Card("火车", "huo3che1", "train", 11))
TotalCardList.append(Card("计程车", "ji4cheng2che1", "taxi", 11))
TotalCardList.append(Card("点车", "dian4che1", "tram", 11))
TotalCardList.append(Card("船", "chuan2", "boat", 11))
TotalCardList.append(Card("辆", "liang4", "MW for cars", 11))


TotalCardList.append(Card("饭馆", "fan4guan3", "restaurant", 12))
TotalCardList.append(Card("服务员", "fu2wu4yuan2", "waiter", 12))
TotalCardList.append(Card("服务", "fu2wu4", "to give service to", 12))
TotalCardList.append(Card("好像", "hao3xiang4", "to seem", 12))
TotalCardList.append(Card("位子", "wei4zi", "seat", 12))
TotalCardList.append(Card("卓子", "zhuo1zi", "table", 12))
TotalCardList.append(Card("点菜", "dian3cai4", "to order", 12))
TotalCardList.append(Card("菜", "cai4", "dish", 12))
TotalCardList.append(Card("饺子", "jiao3zi", "dumplings", 12))
TotalCardList.append(Card("素", "su4", "vegetarian", 12))
TotalCardList.append(Card("盘", "pan2", "plate", 12))
TotalCardList.append(Card("豆腐", "dou4fu", "tofu", 12))
TotalCardList.append(Card("肉", "rou4", "meat", 12))
TotalCardList.append(Card("碗", "wan3", "bowl", 12))
TotalCardList.append(Card("酸", "suan1", "sour", 12))
TotalCardList.append(Card("辣", "la4", "spicy", 12))
TotalCardList.append(Card("汤", "tang1", "soup", 12))
TotalCardList.append(Card("放", "fang4", "to add", 12))
TotalCardList.append(Card("味精", "wei4jing1", "MSG", 12))
TotalCardList.append(Card("渴", "ke3", "thirsty", 12))
TotalCardList.append(Card("这些", "zhe4xie1", "these", 12))
TotalCardList.append(Card("些", "xie1", "MW for indefinite amount", 12))
TotalCardList.append(Card("够", "gou4", "enough", 12))
TotalCardList.append(Card("饿", "e4", "hungry", 12))
TotalCardList.append(Card("上菜", "shang4cai4", "to serve", 12))
TotalCardList.append(Card("好吃", "hao3chi1", "delicious", 12))
TotalCardList.append(Card("师傅", "shi1fu", "master worker", 12))
TotalCardList.append(Card("中餐", "zhong1can1", "Chinese food", 12))
TotalCardList.append(Card("西餐", "xi1can1", "Western food", 12))
TotalCardList.append(Card("糖", "tang2", "sugar", 12))
TotalCardList.append(Card("醋", "cu4", "vinegar", 12))
TotalCardList.append(Card("鱼", "yu2", "fish", 12))
TotalCardList.append(Card("甜", "tian2", "sweet", 12))
TotalCardList.append(Card("极", "ji2", "extremely", 12))
TotalCardList.append(Card("牛肉", "niu2rou4", "beef", 12))
TotalCardList.append(Card("牛", "niu2", "cow", 12))
TotalCardList.append(Card("卖完", "mai4wan2", "sold out", 12))
TotalCardList.append(Card("卖", "mai4", "to sell", 12))
TotalCardList.append(Card("完", "wan2", "to finish", 12))
TotalCardList.append(Card("黄瓜", "huang2gua", "cucumber", 12))
TotalCardList.append(Card("再", "zai4", "in addition", 12))
TotalCardList.append(Card("米饭", "mi3fan4", "cooked rice", 12))
TotalCardList.append(Card("错", "cuo4", "wrong", 12))
TotalCardList.append(Card("明儿", "mingr2", "tomorrow", 12))
TotalCardList.append(Card("鸡", "ji1", "chicken", 12))
TotalCardList.append(Card("鸭", "ya1", "duck", 12))
TotalCardList.append(Card("烤", "kao3", "to roast", 12))
TotalCardList.append(Card("猪肉", "zhu1rou4", "pork", 12))
TotalCardList.append(Card("羊肉", "yang2rou4", "lamb", 12))


TotalCardList.append(Card("借", "jie4", "to borrow", 13))
TotalCardList.append(Card("学生证", "xue2shengzheng4", "student ID", 13))
TotalCardList.append(Card("留", "liu2", "to leave behind", 13))
TotalCardList.append(Card("语言", "yu3yan2", "language", 13))
TotalCardList.append(Card("实验室", "shi2yan4shi4", "laboratory", 13))
TotalCardList.append(Card("实验", "shi2yan4", "experiment", 13))
TotalCardList.append(Card("楼下", "lou2xia4", "downstairs", 13))
TotalCardList.append(Card("再", "zai4", "then and only then", 13))
TotalCardList.append(Card("还", "huan2", "to return", 13))
TotalCardList.append(Card("忘", "wang4", "to forget", 13))
TotalCardList.append(Card("带", "dai4", "to bring", 13))
TotalCardList.append(Card("其他的", "qi2ta1de", "other", 13))
TotalCardList.append(Card("证件", "zheng4jian4", "identification", 13))
TotalCardList.append(Card("信用卡", "xin4yong4ka3", "credit card", 13))
TotalCardList.append(Card("信用", "xin4yong4", "trustworthiness", 13))
TotalCardList.append(Card("卡", "ka3", "card", 13))
TotalCardList.append(Card("开到", "kai1dao4", "open till", 13))
TotalCardList.append(Card("开", "kai1", "to open", 13))
TotalCardList.append(Card("关门", "guan1men2", "to close door", 13))
TotalCardList.append(Card("关", "guan1", "to close", 13))
TotalCardList.append(Card("门", "men2", "door", 13))
TotalCardList.append(Card("剩", "sheng4", "to remain", 13))
TotalCardList.append(Card("钟头", "zhong1tou2", "hour", 13))
TotalCardList.append(Card("可能", "ke3neng2", "maybe", 13))
TotalCardList.append(Card("来不及", "lai2buji2", "not enough time", 13))
TotalCardList.append(Card("本", "ben3", "MW for books", 13))
TotalCardList.append(Card("图书馆员", "tu2shu1guan3yuan2", "librarian", 13))
TotalCardList.append(Card("进去", "jin4qu4", "to go into", 13))
TotalCardList.append(Card("找到", "zhao3dao4", "to find", 13))
TotalCardList.append(Card("姐书证", "jie4shu1zheng4", "library card", 13))
TotalCardList.append(Card("多久", "duo1jiu3", "how long", 13))
TotalCardList.append(Card("如果", "ru2guo3", "if", 13))
TotalCardList.append(Card("过期", "guo4qi1", "overdue", 13))
TotalCardList.append(Card("罚", "fa2", "to fine, to punish", 13))
TotalCardList.append(Card("续借", "xu4jie4", "to renew", 13))
TotalCardList.append(Card("必须", "bi4xu1", "must", 13))
TotalCardList.append(Card("字典", "zi4dian3", "dictionary", 13))
TotalCardList.append(Card("办法", "ban4fa3", "method", 13))
TotalCardList.append(Card("小时", "xiao3shi2", "hour", 13))
TotalCardList.append(Card("分钟", "fen1zhong1", "minute", 13))
TotalCardList.append(Card("楼上", "lou2shang4", "upstairs", 13))
TotalCardList.append(Card("词典", "ci2dian3", "dictionary", 13))
TotalCardList.append(Card("研究生", "yan2jiu1sheng1", "graduate student", 13))
TotalCardList.append(Card("声音", "sheng1yin1", "sound", 13))

TotalCardList.append(Card("上", "shang4", "to go", 14))
TotalCardList.append(Card("重心", "zhong1xin1", "center", 14))
TotalCardList.append(Card("运动", "yun4dong4", "sports", 14))
TotalCardList.append(Card("场", "chang3", "field", 14))
TotalCardList.append(Card("旁边", "pang2bian1", "side", 14))
TotalCardList.append(Card("远", "yuan3", "far", 14))
TotalCardList.append(Card("哪里", "na3li", "where", 14))
TotalCardList.append(Card("住", "zhu4", "to live", 14))
TotalCardList.append(Card("地方", "di4fang", "place", 14))
TotalCardList.append(Card("离", "li2", "from, away", 14))
TotalCardList.append(Card("近", "jin4", "near", 14))
TotalCardList.append(Card("活动中心", "huo2dong4zhong1xin1", "activity center", 14))
TotalCardList.append(Card("活动", "huo2dong4", "activity", 14))
TotalCardList.append(Card("中间", "zhong1jian1", "middle", 14))
TotalCardList.append(Card("书店", "shu1dian4", "bookstore", 14))
TotalCardList.append(Card("店", "dian4", "store", 14))
TotalCardList.append(Card("早知道", "zao3zhi1dao", "had known earlier", 14))
TotalCardList.append(Card("同路", "tong2lu4", "to go the same way", 14))
TotalCardList.append(Card("问路", "wen4lu4", "to ask for directions", 14))
TotalCardList.append(Card("田", "tian2", "field (surname)", 14))
TotalCardList.append(Card("金", "jin1", "gold (surname)", 14))
TotalCardList.append(Card("过", "guo", "(used after a verb to mean past)", 14))
TotalCardList.append(Card("城", "cheng2", "town", 14))
TotalCardList.append(Card("地图", "di4tu2", "map", 14))
TotalCardList.append(Card("眼睛", "yan3jing", "eye", 14))
TotalCardList.append(Card("都", "dou1", "(extremely, hypothetically)", 14))
TotalCardList.append(Card("从", "cong2", "from", 14))
TotalCardList.append(Card("一直", "yi4zhi2", "straight", 14))
TotalCardList.append(Card("往", "wang4", "towards", 14))
TotalCardList.append(Card("南", "nan2", "south", 14))
TotalCardList.append(Card("过", "guo4", "to pass", 14))
TotalCardList.append(Card("路口", "lu4kou3", "intersection", 14))
TotalCardList.append(Card("西", "xi1", "west", 14))
TotalCardList.append(Card("一。。。就", "yi1...jiu4...", "as soon as...then...", 14))
TotalCardList.append(Card("拐", "guai3", "to turn", 14))
TotalCardList.append(Card("哎", "ai1", "(suprise or dissatisfaction)", 14))
TotalCardList.append(Card("东", "dong1", "east", 14))
TotalCardList.append(Card("北", "bei3", "north", 14))
TotalCardList.append(Card("前", "qian2", "forward", 14))
TotalCardList.append(Card("红绿灯", "hong2lv4deng1", "traffic light", 14))
TotalCardList.append(Card("灯", "deng1", "light", 14))
TotalCardList.append(Card("右", "you4", "right", 14))
TotalCardList.append(Card("不对", "bu2dui4", "incorrect", 14))
TotalCardList.append(Card("对", "dui4", "correct", 14))
TotalCardList.append(Card("单行道", "dan1xing2dao4", "one-way street", 14))
TotalCardList.append(Card("单", "dan1", "single", 14))
TotalCardList.append(Card("行", "xing2", "to walk, go", 14))
TotalCardList.append(Card("左", "zuo3", "left", 14))
TotalCardList.append(Card("前面", "qian2mian4", "ahead", 14))
TotalCardList.append(Card("京", "jing1", "capital", 14))
TotalCardList.append(Card("边", "bian4", "side", 14))
TotalCardList.append(Card("上边", "shang4bian", "top", 14))
TotalCardList.append(Card("下边", "xia4bian", "bottom", 14))
TotalCardList.append(Card("前边", "qian2bian", "front", 14))
TotalCardList.append(Card("后边", "hou4bian", "back", 14))
TotalCardList.append(Card("外头", "wai4tou", "outside", 14))
TotalCardList.append(Card("东北", "dong1bei3", "northeast", 14))
TotalCardList.append(Card("只好", "zhi3hao3", "have to", 14))
TotalCardList.append(Card("黑板", "hei1ban3", "blackboard", 14))
TotalCardList.append(Card("墙", "qiang2", "wall", 14))
TotalCardList.append(Card("方向", "fang1xiang4", "direction", 14))
TotalCardList.append(Card("医院", "yi1yuan4", "hospital", 14))
TotalCardList.append(Card("电影院", "dian4ying3yuan4", "movie theater", 14))

TotalCardList.append(Card("呢", "ne", "(action in progress)", 15))
TotalCardList.append(Card("过生日", "guo4", "to celebrate", 15))
TotalCardList.append(Card("舞会", "wu3hui4", "dance", 15))
TotalCardList.append(Card("女朋友", "nv3peng2you", "girlfriend", 15))
TotalCardList.append(Card("表姐", "biao3jie3", "older (female) cousin", 15))
TotalCardList.append(Card("班", "ban1", "class", 15))
TotalCardList.append(Card("做饭", "zuo4fan4", "cook", 15))
TotalCardList.append(Card("汽水", "qi4shui3", "soft drink", 15))
TotalCardList.append(Card("水果", "shui3guo3", "fruit", 15))
TotalCardList.append(Card("果汁", "guo3zhi1", "fruit juice", 15))
TotalCardList.append(Card("接", "to meet", "jie1", 15))
TotalCardList.append(Card("走路", "zou3lu4", "to walk", 15))
TotalCardList.append(Card("礼物", "li3wu4", "gift", 15))
TotalCardList.append(Card("说到", "shuo1dao4", "to mention", 15))
TotalCardList.append(Card("聪明", "cong1ming2", "intelligent", 15))
TotalCardList.append(Card("用功", "yong4gong1", "diligent", 15))
TotalCardList.append(Card("暑期学校", "shu3qi1xue2xiao4", "summer school", 15))
TotalCardList.append(Card("可爱", "ke3ai4", "cute", 15))
TotalCardList.append(Card("爱", "ai4", "to love", 15))
TotalCardList.append(Card("前年", "qian2nian2", "the year before last", 15))
TotalCardList.append(Card("属", "shu3", "to belong to", 15))
TotalCardList.append(Card("狗", "gou3", "dog", 15))
TotalCardList.append(Card("鼻子", "bi2zi", "nose", 15))
TotalCardList.append(Card("嘴", "zui3", "mouth", 15))
TotalCardList.append(Card("像", "xiang4", "to be like", 15))
TotalCardList.append(Card("将来", "jiang1lai2", "in the future", 15))
TotalCardList.append(Card("一定", "yi2ding4", "certain", 15))
TotalCardList.append(Card("脸", "lian3", "face", 15))
TotalCardList.append(Card("腿", "tui3", "leg", 15))
TotalCardList.append(Card("长", "chang2", "long", 15))
TotalCardList.append(Card("手指", "shou3zhi3", "finger", 15))
TotalCardList.append(Card("以后", "yi3hou4", "afterwards", 15))
TotalCardList.append(Card("应该", "ying1gai1", "should", 15))
TotalCardList.append(Card("弹", "tan2", "to play (an instrument)", 15))
TotalCardList.append(Card("钢琴", "gang1qin2", "piano", 15))
TotalCardList.append(Card("鼠", "shu3", "rat", 15))
TotalCardList.append(Card("牛", "niu2", "cow", 15))
TotalCardList.append(Card("虎", "hu3", "tiger", 15))
TotalCardList.append(Card("兔", "tu4", "rabbit", 15))
TotalCardList.append(Card("龍", "long2", "dragon", 15))
TotalCardList.append(Card("蛇", "she2", "snake", 15))
TotalCardList.append(Card("马", "ma3", "horse", 15))
TotalCardList.append(Card("羊", "yang2", "sheep", 15))
TotalCardList.append(Card("猴", "hou2", "monkey", 15))
TotalCardList.append(Card("身高", "shen1gao1", "height", 15))
TotalCardList.append(Card("公分", "gong1fen1", "centimeter", 15))
TotalCardList.append(Card("尺", "chi3", "foot (measurement)", 15))
TotalCardList.append(Card("寸", "cun4", "inch (measurement)", 15))
TotalCardList.append(Card("体重", "ti3zhong4", "weight", 15))
TotalCardList.append(Card("磅", "bang4", "pound (measurement)", 15))
TotalCardList.append(Card("公斤", "gong1jin1", "kilogram", 15))
TotalCardList.append(Card("脚", "jiao3", "foot", 15))
TotalCardList.append(Card("站", "zhan4", "to stand", 15))
TotalCardList.append(Card("男朋友", "nan2peng2you", "boyfriend", 15))

TotalCardList.append(Card("看病", "kan4bing4", "to see a doctor", 16))
TotalCardList.append(Card("肚子", "du4zi", "stomach", 16))
TotalCardList.append(Card("疼死", "teng2si3", "to really hurt", 16))
TotalCardList.append(Card("疼", "teng2", "to be painful", 16))
TotalCardList.append(Card("死", "si3", "to die", 16))
TotalCardList.append(Card("一些", "yi4xie1", "some", 16))
TotalCardList.append(Card("剩菜", "sheng4cai4", "leftovers", 16))
TotalCardList.append(Card("好几", "hao3ji3", "quite a few", 16))
TotalCardList.append(Card("厠所", "ce4suo3", "bathroom", 16))
TotalCardList.append(Card("放", "fang4", "to put", 16))
TotalCardList.append(Card("躺下", "tang3xia4", "to lie down", 16))
TotalCardList.append(Card("检查", "jian3cha2", "to examine", 16))
TotalCardList.append(Card("吃坏", "chi1huai4", "to get sick from food", 16))
TotalCardList.append(Card("坏", "huai4", "bad", 16))
TotalCardList.append(Card("打针", "da3zhen1", "to get a shot", 16))
TotalCardList.append(Card("针", "zhen1", "needle", 16))
TotalCardList.append(Card("种", "zhong3", "kind of thing", 16))
TotalCardList.append(Card("药", "yao4", "medicine", 16))
TotalCardList.append(Card("片", "pian4", "MW for slices, pills", 16))
TotalCardList.append(Card("小时", "xiao3shi2", "hour", 16))
TotalCardList.append(Card("饿死", "e4si3", "to starve", 16))
TotalCardList.append(Card("办法", "ban4fa3", "method", 16))
TotalCardList.append(Card("想家", "xiang3jia1", "to be homesick", 16))
TotalCardList.append(Card("身体", "shen1ti3", "body", 16))
TotalCardList.append(Card("流", "liu2", "to shed ", 16))
TotalCardList.append(Card("眼泪", "yan3lei4", "tear", 16))
TotalCardList.append(Card("养", "yang3", "to itch", 16))
TotalCardList.append(Card("对。。。过敏", "dui4..guo4min3", "to be allergic", 16))
TotalCardList.append(Card("药店", "yao4dian4", "pharmacy", 16))
TotalCardList.append(Card("拿", "na2", "to take", 16))
TotalCardList.append(Card("干快", "gan3kuai4", "right away", 16))
TotalCardList.append(Card("要不然", "yao4buran2", "otherwise", 16))
TotalCardList.append(Card("越来越", "yue4lai2yue4", "more and more", 16))
TotalCardList.append(Card("重", "zhong4", "serious", 16))
TotalCardList.append(Card("花钱", "hua1qian2", "to cost money", 16))
TotalCardList.append(Card("花时间", "hua1shi2jian1", "to cost time", 16))
TotalCardList.append(Card("试", "shi4", "to try", 16))
TotalCardList.append(Card("再说", "zai4shuo1", "moreover", 16))
TotalCardList.append(Card("生病", "sheng1bing4", "to get sick", 16))
TotalCardList.append(Card("健康", "jian4kang1", "health", 16))
TotalCardList.append(Card("保险", "bao3xian3", "insurance", 16))
TotalCardList.append(Card("猜", "cai1", "to guess", 16))
TotalCardList.append(Card("马", "ma3", "horse", 16))
TotalCardList.append(Card("头疼", "tou2teng2", "to have a headache", 16))
TotalCardList.append(Card("头", "tou2", "head", 16))
TotalCardList.append(Card("咳嗽", "ke2sou4", "to cough", 16))
TotalCardList.append(Card("打喷嚏", "da3pen1ti", "to sneeze", 16))
TotalCardList.append(Card("发烧", "fa1shao1", "to run a fever", 16))
TotalCardList.append(Card("感冒", "gan3mao4", "to have a cold", 16))
TotalCardList.append(Card("生气", "sheng1qi4", "to be angry", 16))
TotalCardList.append(Card("班", "ban1", "to move", 16))
TotalCardList.append(Card("对。。。有兴趣", "dui4…you3xing4qu", "to be interested in", 16))
TotalCardList.append(Card("兴趣", "xing4qu", "interest", 16))


ChineseAnswer = "undefined"
PinyinAnswer = "undefined"
EnglishAnswer = "undefined"

ctr = 0


def FilterChapters(TotalList, ChaptersWanted):

    FilteredList = []
    
    for i in TotalList:
        if i.Chapter in ChaptersWanted:
            FilteredList.append(i)

    return FilteredList


##This sets the default so that all chapters are initially included.##
AllChaptersWanted = [1,2,3,4,5,6,7,8,9,10,11]        
CardList = FilterChapters(TotalCardList, AllChaptersWanted)

    

for i in CardList:
    print(i.ChineseAnswer)

##This shuffles the list.
random.shuffle(CardList)



def CompareAnswers():
    global TotalAsked
    global TotalCorrect
    global AllTimeTotalAsked
    global AllTimeTotalCorrect
    print("just started CompareAnswers")
    print(AllTimeTotalCorrect)
    global TargetEntry

    ##This sets a variable to the user's entry
    UserAnswer = UserEntry.get()

    ##This displays all the correct answers, including the one that we didn't do before.
    Character.config(text=CardList[ctr].ChineseAnswer)
    Character.grid(row=0, column=2)
    Pinyin.config(text=CardList[ctr].PinyinAnswer)
    Pinyin.grid(row=1, column=2)
    English.config(text=CardList[ctr].EnglishAnswer)
    English.grid(row=2, column=2)

    ##This compares answers and determines correct vs incorrect
    if TargetEntry == "English":
        if CardList[ctr].EnglishAnswer== UserAnswer:
            Grade.config(text="Correct!")
            Grade.grid(row=5, column=2)
            TotalCorrect+=1  ##Increases correct for score.
            AllTimeTotalCorrect+=1
            print("just Target Entry == English")
            print(AllTimeTotalCorrect)

        else:
            Grade.config(text="Incorrect")
            Grade.grid(row=5, column=2)
    elif TargetEntry == "Pinyin":
        if CardList[ctr].PinyinAnswer== UserAnswer:
            Grade.config(text="Correct!")
            Grade.grid(row=5, column=2)
            TotalCorrect+=1  ##Increases correct for score.
            AllTimeTotalCorrect+=1
            print("just Target Entry == Pinyin")
            print(AllTimeTotalCorrect)

        else:
            Grade.config(text="Incorrect")
            Grade.grid(row=5, column=2)
    elif TargetEntry == "Characters":
        if CardList[ctr].ChineseAnswer== UserAnswer:
            Grade.config(text="Correct!")
            Grade.grid(row=5, column=2)
            TotalCorrect+=1  ##Increases correct for score.
            AllTimeTotalCorrect+=1
            print("just Target Entry == Characters")
            print(AllTimeTotalCorrect)

        else:
            Grade.config(text="Incorrect")
            Grade.grid(row=5, column=2)

    TotalAsked+=1  ##Increases total for score.
    AllTimeTotalAsked+=1
    TotalAskedDisplay.config(text=TotalAsked)
    TotalAskedDisplay.grid(row=6, column=2)
    TotalCorrectDisplay.config(text=TotalCorrect)
    TotalCorrectDisplay.grid(row=7, column=2)
    AllTimeTotalAskedDisplay.config(text=AllTimeTotalAsked)
    AllTimeTotalAskedDisplay.grid(row=9, column=2)
    AllTimeTotalCorrectDisplay.config(text=AllTimeTotalCorrect)
    AllTimeTotalCorrectDisplay.grid(row=10, column=2)
    Score()

##I do not know why I need the function below, but I get errors if I try
##to have the Enter key go directly to CompareAnswers. Something to do with self.
def HittingEnter(self):
    CompareAnswers()

##I am assuming I would have the same issues here.
def HittingDown(self):
    ClearAndResetAnswers()
    UserEntry.focus()  ##This keeps the cursor on the entry widget.

def SetLabels():    ##This sets and displays the answers
    Character.config(text=CardList[ctr].ChineseAnswer)
    Pinyin.config(text=CardList[ctr].PinyinAnswer)
    English.config(text=CardList[ctr].EnglishAnswer)
    


def ClearAndResetAnswers():
    global TargetEntry
    global ctr
    global ShowEnglishToggle
    global ShowPinyinToggle
    global ShowChineseToggle
    ctr+=1
    if ctr >= len(CardList):
        ctr = 0
        random.shuffle(CardList)
    Character.config(text="")
    Pinyin.config(text="")
    English.config(text="")
    UserEntry.delete(0, END)
    Grade.config(text="")
    SetLabels()
    if ShowEnglishToggle == 0:
        English.grid_forget()
    if ShowPinyinToggle == 0:
        Pinyin.grid_forget()
    if ShowChineseToggle == 0:
        Character.grid_forget()
    UserEntry.focus()


def Score():
    global TotalAsked
    global TotalCorrect
    global AllTimeTotalAsked
    global AllTimeTotalCorrect

    if TotalAsked == 0:
        TotalScore = 0
    else:
        TotalScore = str(round(TotalCorrect*100.0/TotalAsked,2))

    if AllTimeTotalAsked == 0:
        AllTimeTotalScore = 0
    else:
        AllTimeTotalScore = str(round(AllTimeTotalCorrect*100.0/AllTimeTotalAsked,2))
        
    PercentageCorrect.config(text=TotalScore)
    PercentageCorrect.grid(row=8, column=2)
    AllTimePercentageCorrect.config(text=AllTimeTotalScore)
    AllTimePercentageCorrect.grid(row=11, column=2)


def SaveAndQuit():
    global AllTimeTotalAsked
    global AllTimeTotalCorrect
    
    file = open("ChineseFlashcards.txt","w")

    file.write(str(AllTimeTotalAsked))
    file.write("\n")
    file.write(str(AllTimeTotalCorrect)) 
     
    file.close()

    EntryWindow.destroy()

def Reset():
    global AllTimeTotalAsked
    global AllTimeTotalCorrect

    AllTimeTotalAsked = 0
    AllTimeTotalCorrect = 0

    AllTimeTotalAskedDisplay.config(text=AllTimeTotalAsked)
    AllTimeTotalAskedDisplay.grid(row=9, column=2)
    AllTimeTotalCorrectDisplay.config(text=AllTimeTotalCorrect)
    AllTimeTotalCorrectDisplay.grid(row=10, column=2)


def TargetAndShow():
    global TargetEntry
    global ShowChineseToggle
    global ShowPinyinToggle
    global ShowEnglishToggle
    
    if PromptChinese.get() == 1:
        TargetEntry = "Characters"
        PromptPinyinButton.deselect()
        PromptEnglishButton.deselect()
    elif PromptPinyin.get() == 1:
        TargetEntry = "Pinyin"
        PromptChineseButton.deselect()
        PromptEnglishButton.deselect()
    elif PromptEnglish.get() == 1:
        TargetEntry = "English"
        PromptChineseButton.deselect()
        PromptPinyinButton.deselect()

    if ShowChinese.get() == 1:
        print("Show Chinese")
        ShowChineseToggle = 1
    else:
        ShowChineseToggle = 0
    if ShowPinyin.get() == 1:
        print("Show Pinyin")
        ShowPinyinToggle = 1
    else:
        ShowPinyinToggle = 0
    if ShowEnglish.get() == 1:
        print("Show English")
        ShowEnglishToggle = 1
    else:
        ShowEnglishToggle = 0
    




##This creates the answer button
AnswerButton = Button(EntryWindow, text="Answer", command=CompareAnswers)
AnswerButton.grid(row=4, column=2)

##This creates the grade widget, since otherwise I get an error
Grade = Label(EntryWindow, text="")
Grade.grid(row=5, column=2)

##This creates the next button
NextButton = Button(EntryWindow, text="Next", command=ClearAndResetAnswers)
NextButton.grid(row=4, column=3)

##This displays the score for the current game
TotalAskedLabel = Label(EntryWindow, text="Current Total Asked: ")
TotalAskedLabel.grid(row=6, column=1)
TotalAskedDisplay = Label(EntryWindow, text=TotalAsked)
TotalAskedDisplay.grid(row=6, column=2)
TotalCorrectLabel = Label(EntryWindow, text="Current Total Correct: ")
TotalCorrectLabel.grid(row=7, column=1)
TotalCorrectDisplay = Label(EntryWindow, text=TotalCorrect)
TotalCorrectDisplay.grid(row=7, column=2)
PercentageCorrectLabel = Label(EntryWindow, text="Current Percentage: ")
PercentageCorrectLabel.grid(row=8, column=1)
PercentageCorrect = Label(EntryWindow, text=0)
PercentageCorrect.grid(row=8, column=2)

##This displays the all time score
AllTimeTotalAskedLabel = Label(EntryWindow, text="All Time Total Asked: ")
AllTimeTotalAskedLabel.grid(row=9, column=1)
AllTimeTotalAskedDisplay = Label(EntryWindow, text=AllTimeTotalAsked)
AllTimeTotalAskedDisplay.grid(row=9, column=2)
AllTimeTotalCorrectLabel = Label(EntryWindow, text="All Time Total Correct: ")
AllTimeTotalCorrectLabel.grid(row=10, column=1)
AllTimeTotalCorrectDisplay = Label(EntryWindow, text=AllTimeTotalCorrect)
AllTimeTotalCorrectDisplay.grid(row=10, column=2)
AllTimePercentageCorrectLabel = Label(EntryWindow, text="All Time Percentage: ")
AllTimePercentageCorrectLabel.grid(row=11, column=1)
AllTimePercentageCorrect = Label(EntryWindow, text=0)
AllTimePercentageCorrect.grid(row=11, column=2)


##This places the character and label.
CharacterLabel = Label(EntryWindow, text="Character: ", font=("Helvetica", 16))
CharacterLabel.grid(row=0, column=1)
Character = Label(EntryWindow, text=ChineseAnswer, font=("Helvetica", 16))
if ShowChineseToggle == 1:
    Character.grid(row=0, column=2)

##This places the pinyin and label.
PinyinLabel = Label(EntryWindow, text="Pinyin: ", font=("Helvetica", 16))
PinyinLabel.grid(row=1, column=1)
Pinyin = Label(EntryWindow, text=PinyinAnswer, font=("Helvetica", 16))
if ShowPinyinToggle == 1:
    Pinyin.grid(row=1, column=2)

##This places the English and label. The English is shown only if that is not
##the answer we are looking for./
EnglishLabel = Label(EntryWindow, text="English: ", font=("Helvetica", 16))
EnglishLabel.grid(row=2, column=1)
English = Label(EntryWindow, text=EnglishAnswer, font=("Helvetica", 16))
if ShowEnglishToggle == 1:
    English.grid(row=2, column=2)

##This creates the entry for an answer
UserEntryLabel = Label(EntryWindow, text="Your Answer", font=("Helvetica", 16))
UserEntryLabel.grid(row=3, column=1)
UserEntry = Entry(EntryWindow, bd=5)
UserEntry.bind('<Return>', HittingEnter)
UserEntry.bind('<Down>', HittingDown)
UserEntry.grid(row=3, column=2)
UserEntry.focus()



##This allows the user to choose a typing language.
PromptLabel = Label(EntryWindow, text="Select the language to type:")
PromptChinese = IntVar()
PromptPinyin = IntVar()
PromptEnglish = IntVar()
PromptChineseButton = Checkbutton(EntryWindow, text = "Chinese", variable = PromptChinese, command = TargetAndShow,
                 onvalue = 1, offvalue = 0, height=2, width = 5)
PromptPinyinButton = Checkbutton(EntryWindow, text = "Pinyin", variable = PromptPinyin, command = TargetAndShow,
                 onvalue = 1, offvalue = 0, height=2, width = 5)
PromptEnglishButton = Checkbutton(EntryWindow, text = "English", variable = PromptEnglish, command = TargetAndShow,
                 onvalue = 1, offvalue = 0, height=2, width = 5)
PromptEnglishButton.select()
PromptLabel.grid(row=21, column=1)
PromptChineseButton.grid(row=22, column=2)
PromptPinyinButton.grid(row=22, column=3)
PromptEnglishButton.grid(row=22, column=4)

##This allows for showing or forgetting the secondary language.
ShowLabel = Label(EntryWindow, text="Select the language to show:")
ShowChinese = IntVar()
ShowPinyin = IntVar()
ShowEnglish = IntVar()
ShowChineseButton = Checkbutton(EntryWindow, text = "Chinese", variable = ShowChinese, command = TargetAndShow, 
                 onvalue = 1, offvalue = 0, height=2, width = 5)
ShowChineseButton.select()
ShowPinyinButton = Checkbutton(EntryWindow, text = "Pinyin",variable = ShowPinyin, command = TargetAndShow,
                 onvalue = 1, offvalue = 0, height=2, width = 5)
ShowPinyinButton.select()
ShowEnglishButton = Checkbutton(EntryWindow, text = "English", variable = ShowEnglish, command = TargetAndShow,
                 onvalue = 1, offvalue = 0, height=2, width = 5)
ShowLabel.grid(row=23, column=1)
ShowChineseButton.grid(row=24, column=2)
ShowPinyinButton.grid(row=24, column=3)
ShowEnglishButton.grid(row=24, column=4)


##This resets the card list if the user changes the chapters wanted.
def ResetList():
    global AllChaptersWanted
    global TotalCardList
    global CardList
    AllChaptersWanted = []

    
    if ChapterSelection1.get() == 1:
        AllChaptersWanted.append(1)
        
    if ChapterSelection2.get() == 1:
        AllChaptersWanted.append(2)

    if ChapterSelection3.get() == 1:
        AllChaptersWanted.append(3)

    if ChapterSelection4.get() == 1:
        AllChaptersWanted.append(4)

    if ChapterSelection5.get() == 1:
        AllChaptersWanted.append(5)

    if ChapterSelection6.get() == 1:
        AllChaptersWanted.append(6)

    if ChapterSelection7.get() == 1:
        AllChaptersWanted.append(7)

    if ChapterSelection8.get() == 1:
        AllChaptersWanted.append(8)

    if ChapterSelection9.get() == 1:
        AllChaptersWanted.append(9)

    if ChapterSelection10.get() == 1:
        AllChaptersWanted.append(10)

    if ChapterSelection11.get() == 1:
        AllChaptersWanted.append(11)

    CardList = FilterChapters(TotalCardList, AllChaptersWanted)
    random.shuffle(CardList)



##This allows the user to choose a chapter.
ChapterLabel = Label(EntryWindow, text="Select the chapters to test:")
ChapterSelection1 = IntVar()
ChapterSelection2 = IntVar()
ChapterSelection3 = IntVar()
ChapterSelection4 = IntVar()
ChapterSelection5 = IntVar()
ChapterSelection6 = IntVar()
ChapterSelection7 = IntVar()
ChapterSelection8 = IntVar()
ChapterSelection9 = IntVar()
ChapterSelection10 = IntVar()
ChapterSelection11 = IntVar()
Chapter1 = Checkbutton(EntryWindow, text = "1", variable = ChapterSelection1, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter1.select()
Chapter2 = Checkbutton(EntryWindow, text = "2", variable = ChapterSelection2, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter2.select()
Chapter3 = Checkbutton(EntryWindow, text = "3", variable = ChapterSelection3, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter3.select()
Chapter4 = Checkbutton(EntryWindow, text = "4", variable = ChapterSelection4, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter4.select()
Chapter5 = Checkbutton(EntryWindow, text = "5", variable = ChapterSelection5, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter5.select()
Chapter6 = Checkbutton(EntryWindow, text = "6", variable = ChapterSelection6, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter6.select()
Chapter7 = Checkbutton(EntryWindow, text = "7", variable = ChapterSelection7, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter7.select()
Chapter8 = Checkbutton(EntryWindow, text = "8", variable = ChapterSelection8, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter8.select()
Chapter9 = Checkbutton(EntryWindow, text = "9", variable = ChapterSelection9, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter9.select()
Chapter10 = Checkbutton(EntryWindow, text = "10", variable = ChapterSelection10, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter10.select()
Chapter11 = Checkbutton(EntryWindow, text = "11", variable = ChapterSelection11, \
                 onvalue = 1, offvalue = 0, height=2, width = 3, command=ResetList)
Chapter11.select()

ChapterLabel.grid(row=27, column=1)
Chapter1.grid(row=28, column=2)
Chapter2.grid(row=28, column=3)
Chapter3.grid(row=28, column=4)
Chapter4.grid(row=28, column=5)
Chapter5.grid(row=28, column=6)
Chapter6.grid(row=28, column=7)
Chapter7.grid(row=29, column=2)
Chapter8.grid(row=29, column=3)
Chapter9.grid(row=29, column=4)
Chapter10.grid(row=29, column=5)
Chapter11.grid(row=29, column=6)

##To Reset the All Time Settings
ResetAllTime = Button(EntryWindow, text="ResetAllTimeScores", command=Reset)
ResetAllTime.grid(row=30, column=1)


##This creates a Save and Quit button at the bottom
QuitButton = Button(EntryWindow, text="Save and Quit", command=SaveAndQuit)
QuitButton.grid(row=30, column=2)

SetLabels()


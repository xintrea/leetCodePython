#!/bin/python3

class Solution:

    def isPalinrome(self, s: str) -> bool:
        divPoint=len(s)//2
        return s[0:divPoint]==s[-1:-divPoint-1:-1]


    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        if len(s)==2:
            if s[0:1]==s[1:2]:
                return s
            else:
                return s[0:1]

        maxLen=0
        maxPal=""

        # Проверяются подстроки-палиндромы, начиная с пары символов
        for i in range(0, len(s)-1):
            for j in range(i+max(1, maxLen), len(s)):
                if j-i+2>maxLen:
                    p=s[i:j+1]
                    # print("Curr: "+p+" From: "+str(i)+" To: "+str(j))
                    if self.isPalinrome(p):
                        maxLen=len(p)
                        maxPal=p

                    if (len(s)-i)<maxLen:
                        return maxPal

        # Если палиндром в парах не найден, возвращается первый символ 
        # так как он и есть палиндром, а длина входной строки здесь от трех и выше
        if len(maxPal)==0:
            return s[0:1]
        else:
            return maxPal
     
      
solution=Solution()

data=[]
data.append("abacab")
data.append("abcda")
data.append("ccc")
data.append("abb")
data.append("a")
data.append("ac")
data.append("aca")
data.append("affa")
data.append("babad")
data.append("cbbd")
data.append("abcabcbb")
data.append("bbbbb")
data.append("pwwkew")
data.append("abcabcbca")
data.append("borcdubqiupahpwjizjjbkncelfazeqynfbrnzuvbhjnyvrlkdyfyjjxnprfocrmisugizsgvhszooktdwhehojbrdbtgkiwkhpfjfcstwcajiuediebdhukqnroxbgtvottummbypokdljjvnthcbesoyigscekrqswdpalnjnhcnqrarxuufzzmkwizptyvjhpfidgmskuaggtpxqisdlyloznkarxofzeeyvteynluofuhbllyiszszbwnsglqjkignusarxsjvctpgiwnhdufmfpanfwxjwlmhgllzsmdpncbwnsbdtsvrjybynifywkulqnzprcxockbhrhvnwxrkvwumyieazclcviumvormynbryaziijpdinwatwqppamfiqfiojgwkvfzyxadyfjrgmtttvlgkqghgbcfhkigfojjkhskzenlpasyozcsuccdxhulcubsgomvcrbqwakrraesfifecmoztayrdjicypakrrneulfbqqxtrdelggedvloebqaztmfyfkhuonrognejxpesmwgnmnnnamvkxqvzrgzdqtvuhccryeowywmbixktnkqnwzlzfvloyqcageugmjqihyjxhssmhkfzxpzxmgpjgsduogfolnkkqizitbvvgrkczmojxnabruwwzxxqcevdwvtiigwckpxnnxxxdhxpgomncttjutrsvyrqcfwxhexhaguddkiesmfrqfjfdaqbkeqinwicphktffuwcazlmerdhraufbpcznbuipmymipxbsdhuesmcwnkdvilqbnkaglloswcpqzdggnhjdkkumfuzihilrpcvemwllicoqiugobhrwdxtoefynqmccamhdtxujfudbglmiwqklriolqfkknbmindxtljulnxhipsieyohnczddabrxzjmompbtnnxvivmoyfzfrxlufowtqzojfclmatthjtbhotdoheusnpirwicbtyrcuojsdmfcx")
data.append("kfdgljweoirufhkcjxfnsdvbfdsjhfggdhfgweiufwieughjdshhfbcbhvsdhjsddsjkadhsjhibnvmsadjkhfdgjhsdkgfskjhaiwqeiuqwwqgryugfuyhdsfhdsbfhdscbzzzzmxcnbvfdsgfsdfggjehfdheiurepfhdsgsfhcxbmcxvbhgfeuygudjhsgsahfgzzmncbvhsdfvasvgdgwgvdqyfdwqfveqwvdsghvgvsszmmcxnvcxvzbdhfhkdsfgewaueyrfgsgfdbhdsgbzbdvfhdsfbvadshfaffxcvcvcmvcmmmfhhdfdhgfhsgfsudgfehgfhdbfahbfuhewcbuyixznijcijnocmoswijdcnuwehbwygeywgecwygdcvywgvsyqgygsvyavdguyaduvaujshcbudbhuhbwubauhbsdduhasbduhbasdhubahusdyqwvdyqwvytfqyfqtwyettruyesgtfydsgfhjgdshjfbhjcvhmbznmbmncvmbzvzbkdfgpaqeiuyrwpeiydfgdshgfhdbschdsbccbhsdjnxzjhansxhassdbhsbchdsfdsvfghjsvafgjwfkweghvdgedfdgewiiorgoqugqwuoguyewgfdshvbfhavsdhfavdhgfvsghfvdsghdfvqeyrqoqweuyrtesdhfbvdhsvbzvghfdghwvegwvqghwvegvvdfgtsafdusaafgdshgfbsdgbvmcnxzvzxmvmadshugfbudbgvucyznbvdzbyudfnbavwefyaervtwertvsnfvszvdnznvggdsvnfasfvgvhsavfghjavgfdhvafiyweavryawetvrftyevatvdfgdnfvgzvgdfvzjvndgvzngfvdgvaigsvfdiavfiewvyrvaywetaftdgvfadtygvayvdnbvncxbvzbdhkjsfahjdgwuygqugwquygsahjgvfhgjsdfkdsfpasdfigfdsagfnfgbnvgbdsayabsrftvaityuefacbefrafwetyfdbgdsfgaGHsdfghjfdsfdwetfbrawefrywteaftyfatydfznbfdtbtftyyitwfeayftemnbvzxcjghfsdffqpwiutyeewuytrfhsagfdczhgvcxvsdgfvgweqruaighvdasgfdhsafagdjdfghffgdjhsqpiwuuygghhvzcxxcvmbnbxcvjhsdagajhgfiuwyerqieuryierutrpotrpotieropiwoeuirweuyqweuygajhgsfasfgdjnbzxcvcmzxvfzmzmx")
data.append("busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjnufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi")

for s in data:
    print("Given: "+s)
    result=solution.longestPalindrome(s)
    print("Result: "+result)

# print("Result cache:: "+str(solution.cache))

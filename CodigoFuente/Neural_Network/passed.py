import csv


class NN:
    def __init__(self):
        self.into = "NB"
        self.rows= []
        self.words = []
        self.u_words = []
        self.spams = []
        self.hams = []
        self.priorSpam = 0.00
        self.priorHam = 0.00


    def think(self, message):
        with open("test.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = next(csv_reader)

            for row in csv_reader:
                self.rows.append(row[1])

                if row[0] == 'spam':
                    self.spams.append(row[1])
                if row[0] == 'ham':
                    self.hams.append(row[1])
        
                ws = row[1].split()
                for i in range(len(ws)):
                    self.words.append(i)
        
        self.u_words = set(self.words)
        self.priorHam = float(float(len(self.hams)) /float(float(len(self.spams)) + float(len(self.hams))))
        self.priorSpam = float(float(len(self.spams)) / float(float(len(self.hams)) + float(len(self.spams))))
        print("rows : ", len(self.rows))
        print("spams : ",len(self.spams))
        print("hams : ", len(self.hams))
        print("words : ",len(self.words))
        print("vocabuylary : ",len(self.u_words))
        print("priorspam : ", self.priorHam)
        print("priorham : ",self.priorSpam)


        #Recover info
        alpha = 0.0000000000001
        wordsSearch = message.split()

        wordsFoundSpam = dict.fromkeys(wordsSearch, 0.0)
        wordsFoundHam = dict.fromkeys(wordsSearch, 0.0)

        print("wfs : ",wordsFoundSpam)
        print("wfh : ",wordsFoundHam)

        #setting count(c,n)
        for word in self.spams:
            wss = word.split()
            #print("wss : ",wss)
            for w in wss:
                if w in wordsFoundSpam:
                    wordsFoundSpam[w] += 1.0
        
        for word in self.hams:
            #print("wss : ",wss)
            wss = word.split()
            for w in wss:
                if w in wordsFoundHam:
                    wordsFoundHam[w] += 1.0

        print("Words in hams : \n", wordsFoundHam)
        print("Words in spams : \n", wordsFoundSpam)
        
        #Setting weights
        for i in wordsFoundSpam:
            wordsFoundSpam[i] = float(float(wordsFoundSpam[i] + alpha) / float(float(len(self.spams))+float(len(self.words))))

        for i in wordsFoundHam:
            wordsFoundHam[i] = float(float(wordsFoundHam[i] + alpha) / float( float(len(self.hams)) +float(len(self.words))))
        

        weightMessageSpam = self.priorSpam
        weightMessageHam = self.priorHam

        for i in wordsFoundSpam:
            weightMessageSpam *= wordsFoundSpam[i]
        
        for i in wordsFoundHam:
            weightMessageHam *= wordsFoundHam[i]

        print("Words in hams : \n", wordsFoundHam)
        print("Words in spams : \n", wordsFoundSpam)

        print("W ham : ",weightMessageHam)
        print("W spam : ",weightMessageSpam)

        if weightMessageHam>weightMessageSpam:
            return 'ham'
        else:
            return 'spam'








        
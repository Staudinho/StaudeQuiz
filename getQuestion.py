class getQuestions:

    def __init__(self, chosenQ):
        self.__chosenQ=chosenQ

    # select the question to be displayed        
    def choseQuestion(self):
        if self.__chosenQ==1:
            result = ("Wann wurde Nick geboren?","2008", "2011", "2006", "2012", '1')
        elif self.__chosenQ==2:
            result = ("Wann wurde Leon geboren?","2008", "2011", "2006", "2012", '2')
        elif self.__chosenQ==3:
            result = ("Wann wurde Papa geboren?","1982", "1976", "1972", "1979", '2')
        elif self.__chosenQ==4:
            result = ("Wann wurde Mama geboren?","1980", "1985", "1989", "1977", '4')
        elif self.__chosenQ==5:
            result = ("wie lautet die Hauptstadt von Italien?", "Mailand", "Paris", "Madrid", "Rom", '4')
        elif self.__chosenQ==6:
            result = ("Auf welchem Kontinent liegt Kamerun?", "Europa", "Amerika","Asien", "Afrika", '4')
        elif self.__chosenQ==7:
            result = ("Auf welchem Kontinent liegt Japan?", "Europa", "Amerika","Asien", "Afrika", '3')
        elif self.__chosenQ==8:
            result = ("Auf welchem Kontinent liegt Kanada?", "Europa", "Amerika","Asien", "Afrika", '2')
        elif self.__chosenQ==9:
            result = ("Wieviel Einwohner hat Singapur ungefähr?","ca. 5,6 Mio", "ca. 10 Mio", "ca. 20 Mio", "ca. 1,5 Mio", '1')
        elif self.__chosenQ==10:
            result = ("Wer ist deutscher Rekordmeister im Fussball?","Bayern München", "Borussia Dortmund", "RB Leipzig", "Borussia Mönchengladbach", '1')
        elif self.__chosenQ==11:
            result = ("was besteht aus Holz?","Holz Tisch", "Radierer", "Magnet", "Scheibe", '1')    
        elif self.__chosenQ==12:
            result = ("Aus wie viel Spieler besteht eine Fußballmannschaft?", "12", "10", "11","13", '3')
        elif self.__chosenQ==13:
            result = ("Aus wie viel Spieler besteht eine Handballmannschaft?", "2", "7", "5","13", '2') 
        elif self.__chosenQ==14:
            result = ("Auf welchen platz ist fc bayern im januar 2021?", "3.Platz", "1.Platz", "5.Platz", "4.Platz", '2') 
        elif self.__chosenQ==15:
            result = ("Wieviel knochen hat der mensch?", "194", "302", "206", "98", '3')
        elif self.__chosenQ==16:            
            result = ("Woher kommt das Corona Virus?", "Singapur", "China", "Deutschland", "Mailand", '2')
        elif self.__chosenQ==17:            
            result = ("Aus was besteht Glas?", "Sand", "Papier", "Schnee", "Holz", '1')
        elif self.__chosenQ==18: 
            result = ("Wie schnell darf man inerorts?", "30", "50", "60", "40", '2')        
        elif self.__chosenQ==19: 
            result = ("Wie heißt der Welt Fußballer des Jahres 2020?", "Robert Lewandowski", "Manuel Neuer", "Thomas Müller", "David Alaba", '1')
        elif self.__chosenQ==20:
            result = ("Seit wann gibt es den VFB Stuttgart?","1893","1830","2010","1950",'1')
        elif self.__chosenQ==21:
            result = ("Wie viele Spiele hat der FC Bayern München 2020 verloren?"," 1 Spiel ","2 Spiele","0 Spiele","5 Spiele", '1 (Gegen Hoffenheim)')
        elif self.__chosenQ==22:
            result = ("wie ist Mamas Vorname?","Maria","Berta","Dalia","Sue", '3')
        elif self.__chosenQ==23:
            result = ("Wie heißt das Maskottchen des FC Bayern?","Fritzchen","Juan","Leon","Berni", '4')
        elif self.__chosenQ==24:
            result = ("wie heißt die Hauptstadt Frankreichs?","Rom","London","Paris","Berlin",'3')
        elif self.__chosenQ==25:
            result = ("Wie hoch ist der Mount Everest?","8848m","10000m","218m","5530m", '1')
        elif self.__chosenQ==26:
            result = ("Welches Wort ist kein Land?","China","Malta","Mailand","Östereich", '3')
        elif self.__chosenQ==27:
            result = ("Wer ist der reichste Mensch der Welt?","Jesus","Jeff Bezos","Christiano Ronaldo","Robert Lewandowski", '2')
        elif self.__chosenQ==28:
            result = ("Welcher Berg ist der höhste Berg Deutschlands?","Hohenstaufen","Zugspitze","Mount Everest","Wasserberg", '2')
        elif self.__chosenQ==29:
            result = ("Welche Rückennumer hat Thomas Müller?","25","1","18","98", '1')
        elif self.__chosenQ==30:
            result = ("In welchem Jahr war die deutsche Wiedervereinigung?","1990","1989","1978","1998", '1')
        return result

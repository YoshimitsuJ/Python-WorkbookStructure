import datetime

class WorkbookStructure:
    # Description of the entire clas
    "The class representing the entire data of one PDF fot the Ministry Workbook"

    # The title is valid for all weeks
    title = "Our Christian Life and Ministery"

    # An array of weeks (each containing one MinistryWeek)
    weeks = []

    def toString(self):
        content = "WorkbookStructure:\n" + self.title
        content += "\n----------------------------\n"
        for week in self.weeks:
            content += week.toString()
            content += "\n"
        return content

class MinistryWeek:
    "One Week"
    date = datetime.datetime.now()
    scripture = "Genesis 1-3"
    president = "Ragusa"

    elements = []
    def toString(self):
        content = ""
        for element in self.elements:
            if len(content) > 0:
                content += "\n"
            content += element.toString()
        return content

workbook = WorkbookStructure()

class Detail:
    time = datetime.datetime.now()
    topic = "Song 55"
    name = "Lusso"
    def toString(self) :
        return self.time.strftime("%M:%M") + " | " + self.topic + " | by " + self.name

class Color:
    "A clas represemting a color"
    def __init__(self,r=0,g=0,b=0) :
        self.red = r
        self.green = g
        self.blue = b
    def toString(self) :
        return "color(" + str(self.red) + "," + str(self.green) + "," + str(self.blue) + ")"

class Section:
    name = "TREASURES FROM GOD'S WORLD "
    # The color of the selection is by deafault a light gray
    color = Color(64,64,64)
    def toString(self) :
        return "# " + self.name + "- (" + self.color.toString() + ")"

    
workbook = WorkbookStructure()

week_one = MinistryWeek()
week_one.scripture = "revelation 17-19"
week_one.president = "Ventre"
detail_first_song = Detail()
detail_first_song.time = datetime.datetime.strptime('2020-03-17 19:00', '%Y-%m-%d %H:%M')
detail_first_song.name = "Prayer: Previti"
week_one.elements.append(detail_first_song)

# the rigth name and color per default
detail_first_section = Section()
week_one.elements.append(detail_first_section)

workbook.weeks.append(week_one)

print(workbook.toString())

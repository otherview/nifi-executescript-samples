import sys
import traceback
import datetime

class GenerateDates():
    def __init__(self, dateStart, dateEnd, dayStep):
        self.dateStart = datetime.datetime.strptime(dateStart, '%Y-%m-%d').date()
        self.dateEnd = datetime.datetime.strptime(dateEnd, '%Y-%m-%d').date()
        self.dayStep = datetime.timedelta(days=dayStep)
        pass

    def process(self):
        try:
            flowFileList = []

            while self.dateStart <= self.dateEnd:
                currentDateStart = self.dateStart.strftime('%Y-%m-%d')
                self.dateStart += self.dayStep
                currentDateEnd = self.dateStart.strftime('%Y-%m-%d')

                flowFile = session.create()
                flowFile = session.putAttribute(flowFile, "dateStart", currentDateStart)
                flowFile = session.putAttribute(flowFile, "dateEnd", currentDateEnd)
                flowFileList.append(flowFile)

            session.transfer(flowFileList, REL_SUCCESS)
                
        except:
            traceback.print_exc(file=sys.stdout)
            raise

dateStart = dateStart.getValue()
dateEnd = dateEnd.getValue()
dayStep = dayStep.getValue()
GenerateDates(dateStart, dateEnd, int(dayStep)).process()

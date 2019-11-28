import test_lib as Tester
import matplotlib.pyplot as plt

#Demo - part 1
plt.rcParams["figure.figsize"] = (11,11)
independentList, dependentList = Tester.getAssignmentDataset()
plt.scatter(independentList, dependentList, s=100)
Tester.fitLineAndPlot(independentList, dependentList, plt, order=1)
Tester.fitLineAndPlot(independentList, dependentList, plt, order=2)


#Demo - part 2
#independentList, dependentList = Tester.generateDataSet([10, 2, 5, 4])
#Tester.drawScatterPlot(independentList, dependentList, plt)
#Tester.fitLineAndPlot(independentList, dependentList, plt, order=1)
#Tester.fitLineAndPlot(independentList, dependentList, plt, order=2)
#Tester.fitLineAndPlot(independentList, dependentList, plt, order=3)
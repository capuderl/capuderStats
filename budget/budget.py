from budgetFxns import *
from budget_2021 import *
from budget_2022 import *
import matplotlib.pyplot as plt
import numpy
import math
import statistics
import sys
def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)

#set up variables
b = dict([('car', []), ('subscriptions', []), ('groceries', []), ('misc', []), ('rest', []), ('bills', []), ('adventure', [])])
#b = dict([('car', numpy.array([])), ('subscriptions', numpy.array([])), ('groceries', numpy.array([])), ('misc', numpy.array([])), ('rest', numpy.array([])), ('bills', numpy.array([])), ('adventure', numpy.array([]))])
income = [];

"""
    ## template

    car = [
        ];
    subscriptions = [
        ];
    groceries = [
        ];
    misc = [
        ];
    adventure = [
        ];
    rest = [
        ];
    bills = [
        ];
    investingMonth = [
        ];
    netWorthMonth = [
        #checking
        #savings
        #vanguard
        #Robinhood
        #fidelity
        #coinbase
        #iBond
        ];
    retirementMonth = [
        ];

    b = updateBudget(b, sum(car), sum(subscriptions), sum(groceries), sum(misc), sum(rest), sum(bills), sum(adventure));
    income.append();
    investing.append(sum(investingMonth));
    netWorth.append(sum(netWorthMonth));
    retirement.append(sum(retirementMonth));
    monthLabel.append('Aug');
    numDays.append(31);
"""

############################### 2021

[b, income, investing, monthLabel, numDays, netWorth,  retirement] = budget_2021(b,income)

############################### 2022

[b, income, investing, monthLabel, numDays, netWorth,  retirement] = budget_2022(b, income, investing, monthLabel, numDays, netWorth,  retirement)

############################### plot

#Convert everything to numpy arrays for math
income = numpy.array(income)
investing = numpy.array(investing)
monthLabel = numpy.array(monthLabel)
numDays = numpy.array(numDays)
netWorth = numpy.array(netWorth)
retirement = numpy.array(retirement)


numMonths = len(b['car']);

plt.figure(1)
ax = plt.gca()
fn = list(b.keys())
totSepnding=numpy.array(numMonths*[0])
h = [];
forLegend = {};
for iFn in range(len(fn)):
    b[fn[iFn]] = numpy.array(b[fn[iFn]])
    plt.plot( range(1,numMonths+1), b[fn[iFn]], '.-', label=fn[iFn])
    totSepnding = totSepnding + b[fn[iFn]]
    #if isequal(fn{iFn}, 'adventure')
    #    set(h(end), 'Color', 'r');
    #end
    
plt.plot(range(1,numMonths+1), totSepnding, 'rs-', linewidth=2, label='Total Spending');
#forLegend{end+1} = 'Total Spending';
plt.plot(range(1,numMonths+1), income, 'o-', color=[0, 0.5, 0], linewidth=2, label='Income');
#forLegend{end+1} = 'Income';
plt.xlabel('Month')
plt.ylabel('Money')
ax.set_xticks(range(1,numMonths+1))
ax.set_xticklabels(monthLabel)
plt.legend(loc="upper left")

plt.figure(2)
ax = plt.gca()
plt.plot(range(1,numMonths+1), income - totSepnding, 'k.-', label='Income Minus Spending');
plt.plot(range(1,numMonths+1), investing, 'r.-', label='Investing');
plt.plot(range(1,numMonths+1), income - totSepnding - investing, 'b.-', label='Total Net (minus investing)', linewidth=2);
plt.title('Net')
plt.xlabel('Month')
plt.ylabel('Money')
ax.set_xticks(range(1,numMonths+1))
ax.set_xticklabels(monthLabel)
plt.legend(loc="upper left")


plt.figure(3)
ax = plt.gca()
plt.plot(range(1,numMonths+1), b['rest']/numDays, 'b.-', label='rest');
plt.plot(range(1,numMonths+1), b['groceries']/numDays, 'k.-', label='groceries');
plt.plot(range(1,numMonths+1), (b['groceries']+b['rest'])/numDays, 'rs-', linewidth=2, label='both');
yl = ax.get_ylim()
ax.set_ylim([0, yl[1]])
#print(ax.get_ylim())
plt.title('Food Cost Per Day')
plt.xlabel('Month')
plt.ylabel('Money')
ax.set_xticks(range(1,numMonths+1))
ax.set_xticklabels(monthLabel)
plt.legend(loc="upper left")

plt.figure(4)
ax = plt.gca()
plt.plot(range(1,numMonths+1), netWorth/1e3, 'k.-', label='Net Worth Avail');
plt.plot(range(1,numMonths+1), retirement/1e3, 'k^-', label='Retirement');
plt.plot(range(1,numMonths+1), (netWorth+retirement)/1e3, 'b.-', linewidth=2, label='Total Net Worth');
yl = ax.get_ylim()
ax.set_ylim([0, yl[1]])
plt.title('Net Worth')
plt.xlabel('Month')
plt.ylabel('Money (/1,000)')
ax.set_xticks(range(1,numMonths+1))
ax.set_xticklabels(monthLabel)
plt.legend(loc="upper left")

fprintf(sys.stdout, '\nAvg Income - Spending (over %d months): %d\n', numMonths, math.floor(statistics.mean(income - totSepnding)))  #floor(mean(income - totSepnding)))

plt.show()
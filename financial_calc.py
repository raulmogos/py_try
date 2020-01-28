import matplotlib.pyplot as plt

EURO = 4.78
DOBANDA = 0.03

def main(years, money_per_month, initial_sum):

    current_sum = initial_sum
    c = initial_sum
    for i in range(years * 12):
        c += money_per_month
        current_sum += money_per_month
        current_sum += current_sum * DOBANDA
        if i % 12 == 0:
            plt.scatter(i+1, current_sum / EURO)
            plt.scatter(i+1, c / EURO)
        print(f'your sum after {i + 1} iteration:      {current_sum}')
    
    print('\n\n')
    print(f'sum with investment:        {current_sum / EURO} \n')
    print(f'sum without investment:     {(years * 12 * money_per_month + initial_sum) / EURO}\n')
    print(f'profit:                     {(current_sum - (years * 12 * money_per_month + initial_sum)) / EURO}')
    
    plt.show()
    
main(
        int(input('years: ')),
        float(input('money per month: ')),
        float(input('initial sum: '))
    )

'''
TODO:
    Find the best parameters that maximizes profit:
    input:
        years,
        money_per_year() = between[a, b]
            
    y(i) = 0.12 * y(i-1)
'''
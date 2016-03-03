import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ['睡觉', '吃饭', '工作', '娱乐']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.title('有趣的图表\n试试看吧')
plt.show()

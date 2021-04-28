#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[5]:


data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data.sample(5)


# In[7]:


data.describe()


# # Предобработка

# In[22]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

 = (data['revenue']- data['budget'])
#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[ ]:


# в словарь вставляем номер вопроса и ваш ответ на него
# запишите свой вариант ответа
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650) '
# если ответили верно, можете добавить комментарий со значком "+"


# In[46]:



data[data['budget'] == data['budget'].max()] #выбираем строку, значение бюджета которой равно максимальному


# ВАРИАНТ 2

# In[ ]:





# # 2. Какой из фильмов самый длительный (в минутах)?

# In[ ]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals (tt0279111)'


# In[47]:



data[data['runtime'] == data['runtime'].max()]


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[ ]:


answers['3'] = 'Winnie the Pooh'


# In[48]:



data[data['runtime'] == data['runtime'].min()]


# # 4. Какова средняя длительность фильмов?
# 

# In[ ]:


answers['4'] = '110'


# In[49]:



data['runtime'].mean()


# # 5. Каково медианное значение длительности фильмов? 

# In[ ]:


answers['5'] = '107'


# In[50]:



data['runtime'].median()


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[ ]:


answers['6'] = 'Avatar'


# In[51]:



data['profit'] = (data['revenue']- data['budget'])
data[data['profit'] == data['profit'].max()]


# # 7. Какой фильм самый убыточный? 

# In[ ]:


answers['7'] = 'The Lone Ranger'


# In[52]:



data['profit'] = (data['revenue']- data['budget'])
data[data['profit'] == data['profit'].min()]


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[ ]:


answers['8'] = '1478'


# In[53]:



data['profit'] = (data['revenue']- data['budget'])
profitable = data[data['profit']>0]
len(profitable.index)


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[ ]:


answers['9'] = 'The Dark Knight'


# In[54]:



data['profit'] = (data['revenue']- data['budget'])
data_2008 = data[data['release_year']== 2008]
data_2008[data_2008['profit'] == data_2008['profit'].max()]


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[ ]:


answers['10'] = 'The Lone Ranger'


# In[55]:


data['profit'] = (data['revenue']- data['budget'])
data_2012_2014 = data[((data['release_year']> 2011) & (data['release_year']<2015)) ]
data_2012_2014[data_2012_2014['profit'] == data_2012_2014['profit'].min()]


# # 11. Какого жанра фильмов больше всего?

# In[ ]:


answers['11'] = 'Drama'


# In[40]:


def stringtolist(string):
    result = string.str.split('|')
    return result
data['genrelist']= stringtolist(data['genres'])
Counter(data['genrelist'].sum()).most_common(1)


# ВАРИАНТ 2

# In[ ]:





# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[ ]:


answers['12'] = 'Drama'


# In[45]:



profitable = data[data['profit']>0]

Counter(profitable.genres.str.split('|').sum()).most_common(1)


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[ ]:


answers['13'] = 'Peter Jackson'


# In[74]:


data['directorlist'] = data.director.str.split('|')
data = data.explode('directorlist')
data.groupby(['directorlist'])['revenue'].sum().sort_values(ascending=False)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[ ]:


answers['14'] = 'Robert Rodriguez'


# In[83]:


data['directorlist'] = data.director.str.split('|')
data = data.explode('directorlist')
data['genrelist'] = data.genres.str.split('|')
data = data.explode('genrelist')
films_Action = data[data['genrelist'] =='Action']
films_Action.groupby(['directorlist'])['imdb_id'].count().sort_values(ascending=False)


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[ ]:


answers['15'] = 'Chris Hemsworth'


# In[102]:


films_2012 = data[data['release_year'] == 2012]
films_2012['actorlist'] = films_2012.cast.str.split('|')
films_2012 = films_2012.explode('actorlist')
data2 = films_2012.groupby(
        ['actorlist'])['revenue'].max().sort_values(ascending=False)
data2.head(10)




# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[ ]:


answers['16'] = 'Matt Damon'


# In[115]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data['actorlist'] = data.cast.str.split('|')
data = data.explode('actorlist')
high_budget_films = data[(data['budget'] > data['budget'].mean())]
data3 = high_budget_films.groupby(
        ['actorlist'])['imdb_id'].count().sort_values(ascending=False)
data3.head()


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[ ]:


answers['17'] = 'Action'


# In[120]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data['actorlist'] = data.cast.str.split('|')
data = data.explode('actorlist')
films_with_Nic = data[data['actorlist'] == 'Nicolas Cage']
Counter(films_with_Nic.genres.str.split('|').sum()).most_common(3)


# # 18. Самый убыточный фильм от Paramount Pictures

# In[ ]:


answers['18'] = 'K-19: The Widowmaker'


# In[122]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data['profit'] = (data['revenue']- data['budget'])
data['companies_list'] = data.production_companies.str.split('|')
data = data.explode('companies_list')
films_by_Paramount = data[data['companies_list'] == 'Paramount Pictures']
films_by_Paramount[(films_by_Paramount['profit'] == films_by_Paramount['profit'].min())]


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[ ]:


answers['19'] = '2015'


# In[123]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[ ]:


answers['20'] = '2014'


# In[132]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data['profit'] = (data['revenue']- data['budget'])
data['companies_list'] = data.production_companies.str.split('|')
data = data.explode('companies_list')
films_by_Warner = data[data.companies_list.str.contains('Warner Bros')]
films_by_Warner.head()
films_by_Warner.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[141]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
data = pd.read_csv('C:/Users/kushta_ay/Downloads/movie_bd_v5.csv')
data.groupby([data.release_date.dt.month])['imdb_id'].sum().sort_values(ascending=False)


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[ ]:





# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[ ]:





# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[ ]:





# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:





# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[ ]:





# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# ВАРИАНТ 2

# # Submission

# In[13]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[ ]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:





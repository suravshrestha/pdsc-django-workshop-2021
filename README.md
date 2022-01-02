# PDSC Django Workshop 2021
This repository contains the lecture projects and assignments of the workshop organized by PDSC.

PDSC (Plan | Design | Solve | Create) (initially named as Pulchowk Data Science Community, started at IOE, Pulchowk campus) is a community of students who are interested in IT. They organize workshops related to Python, Data Science, Machine Learning, web development, MATLAB and other related topics.

The workshop runs for a total span of 4 weeks -- 3 days a week.<br>
The lectures are live and one-hour long, from 6:30 to 7:30, each Friday, Saturday, and Sunday.

[PDSC Facebook group](https://www.facebook.com/groups/2781195002157144/)

## Week 1
Day 1 - Basics of Object Oriented Programming(OOP) in Python<br>
Day 2 - Real world implementation of OOP in Python<br>
Day 3 - Introduction to django<br>

## Week 2
Day 1 - Views and URL configurations<br>
Day 2 - Templates<br>
Day 3 - Practice with todo project<br>

## Week 3
Day 1 - Database and Model<br>
Day 2 - Django forms<br>

## Assignments:
<details>
  <summary>Week 1 Day 1</summary>
<ol>
Implement the following using OOP in Python:
    
![week1-day1-assignment](https://user-images.githubusercontent.com/24486999/147358747-5b671d4b-a0ce-405f-ad80-21cf99a56b7c.png)
    
Solution [here](https://github.com/suravshrestha/pdsc-django-workshop-2021/blob/main/week-01-day-01/oop.py)
<ol>
</details>
  
<details>
  <summary>Week 1 Day 2</summary>
  <ol>
    
View the assignment [here](https://github.com/suravshrestha/pdsc-django-workshop-2021/blob/f66d3e96d9f81acd6da7dd3646fd31b68abba089/week-01-day-02/instructor-lecture-file.py#L70)    
Solution [here](https://github.com/suravshrestha/pdsc-django-workshop-2021/blob/main/week-01-day-02/bank.py)
  </ol>
</details>

<details>
  <summary>Week 2 Day 2</summary>
  <ol>
Create a django project that has a form which takes two numbers as input and display their average on another page.<br>
Use Python to calculate, don't use Javascript.

Solution [here](https://github.com/suravshrestha/pdsc-django-workshop-2021/tree/main/week-02-day-02/assignment)
  </ol>
</details>
  
<details>
  <summary>Week 2 Day 3</summary>
  <ol>
Try to complete the todo project demonstrated in the workshop.<br>
Run the project and try to implement the project in django.

Solution [here](https://github.com/suravshrestha/pdsc-django-workshop-2021/tree/main/week-02-day-03/project)
  </ol>
</details>
  
  ## Requirements
- Python 3.2+

## Usage
1.  Clone the repository 
```
git clone https://github.com/suravshrestha/pdsc-django-workshop-2021.git
```

2.  Navigate to the repository :open_file_folder:
```
cd pdsc-django-workshop-2021
```

3. Create a virtual environment
```
python -m venv venv
```

4. Activate the virtual environment
```
.\venv\Scripts\activate
```

5. Install the dependencies:
```
pip install -r requirements.txt
```

6. Change the working directory to the django project you want to view

7. Make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```

8. Start the development server
```
python manage.py runserver
```

9. Open your browser and go to your local domain `http://127.0.0.1:8000`

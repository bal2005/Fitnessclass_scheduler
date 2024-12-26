# Fitness Class Scheduler

Fitness Class Scheduler is a web application that allows users to schedule and view fitness classes. The application is built using Django and FullCalendar.

## Features

- Schedule fitness classes by clicking on the calendar.
- View scheduled classes.
- Delete individual scheduled classes.
- Clear all scheduled classes.

## Requirements

- Python 3.10
- Django 3 or higher

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/fitnessclass_scheduler.git
cd fitnessclass_scheduler
```

2. Create and activate a virtual environment:
```sh 
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate
```  

3. Install the required packages:
```sh
pip install -r requirements.txt
```

4. Apply database migrations:
```sh
python manage.py migrate
```

5. Run the development server:
```sh
python manage.py runserver
```

## Project Structure

```markdown
fitnessclass_scheduler/
├── scheduler/
│   ├── static/
│   │   ├── scheduler/
│   │   │   ├── styles.css
│   │   │   ├── schedule_success.css
│   │   │   ├── view_schedules.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── schedule.html
│   │   ├── schedule_success.html
│   │   ├── view_schedules.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── fitnessclass_scheduler/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
```

# Fitness Class Scheduler

## Usage

### Schedule a Class
- Click on a date in the calendar to schedule a class.
- Enter the class title and click "Schedule".

### View Scheduled Classes
- Click on the "View Scheduled Classes" button.
- View the list of scheduled classes.

### Delete a Scheduled Class
- Click the "Delete" button next to the class you want to delete.

### Clear All Scheduled Classes
- Click the "Clear All Schedules" button to delete all scheduled classes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Django
- FullCalendar


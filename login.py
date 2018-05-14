import requests
from bs4 import BeautifulSoup

class Course:
    def __init__(self, crn, subj, course, title, final_grade, attempted, earned, gpa_hours, quality_points):
        self.crn = crn
        self.subj = subj
        self.course = course
        self.title = title
        self.final_grade = final_grade
        self.attempted = attempted
        self.earned = earned
        self.gpa_hours = gpa_hours
        self.quality_points = quality_points

    def __str__(self):
        return self.title + " " + self.final_grade
    __repr__ = __str__

def login(username, password):
    
    payload = {
        'user': username,
        'pass': password,
        'uuid': '0xACA021'
    }

    with requests.Session() as request_session:
        print("Logging in as %s" % payload['user'])
        request_session.post(
            'https://portal.mycampus.ca/cp/home/login', data=payload)
        detail_url = 'https://ssbp.mycampus.ca/prod_uoit/bwskogrd.P_ViewTermGrde'
        r = request_session.get(
            'https://portal.mycampus.ca/cp/ip/login?sys=sct&url=' + detail_url)

        soup = BeautifulSoup(r.text, 'html.parser')
        semesters = [semester['value'] for semester in soup.find_all('option')]

        course_data = [] 
        for semester in semesters:
            course_data += (get_grades(request_session.post('https://ssbp.mycampus.ca/prod_uoit/bwskogrd.P_ViewGrde',data={'term_in': semester}).text))
        
        for c in course_data:
            print(c)


    return

def get_grades(page):
    soup = BeautifulSoup(page, 'html.parser')
    courses = soup.find('acronym').parent.parent.parent.find_all('tr')
    course_data = []
    for course_info in courses[1:]:
        data = [c.string for c in course_info.find_all('td')]
        course_data.append(Course(data[0], data[1], data[2], data[4], data[6], data[7], data[8], data[9], data[10]))
        
    return course_data

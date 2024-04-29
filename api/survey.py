from flask import request, jsonify, Blueprint
from flask_restful import Api, Resource
from __init__ import app, db, cors
from model.surveys import Survey
from datetime import datetime

survey_api = Blueprint('survey_api', __name__, url_prefix='/api/survey')
api = Api(survey_api)

class SurveyAPI:
    class _CRUD(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            print(body) 
            
            independent = body['independent']
            artisticTalent = body['artisticTalent']
            communicationSkills = body['communicationSkills']
            fastTyper = body['fastTyper']
            handyPerson = body['handyPerson']
            problemSolving = body['problemSolving']
            showOff = body['showOff']
            teamPlayer = body['teamPlayer']
            
            
            job_suggested = suggest_job(independent, artisticTalent, communicationSkills, fastTyper, handyPerson, problemSolving, showOff, teamPlayer)
            print(job_suggested)
            survey = Survey(
                independent=independent,
                artisticTalent=artisticTalent,
                communicationSkills=communicationSkills,
                fastTyper=fastTyper,
                handyPerson = handyPerson,
                problemSolving = problemSolving,
                showOff = showOff,
                teamPlayer = teamPlayer,
                jobsuggested=job_suggested
            )
            survey = survey.create()
            
            if survey:
                return jsonify(survey.read())

            
            return {'message': f'Error processing request'}, 400
            
        def get(self):
            surveys = surveys.query.all()  
            json_ready = [survey.read() for survey in surveys]  
            return jsonify(json_ready) 

    api.add_resource(_CRUD, '/')
def suggest_job(independent, artistic_talent, communication_skills, fastTyper, handy_person, problem_solving, show_off, team_player):
    points = {
        "Graphic Designer": 0,
        "Multimedia Artist": 0,
        "Virtual Assistant": 0,
        "Software Engineer": 0
    }

    job_questions = {
        "Graphic Designer": [1, 3, 8],
        "Multimedia Artist": [1, 4, 8],
        "Virtual Assistant": [2, 5, 6],
        "Software Engineer": [1, 3, 7]
    }
    

    answers = [independent, artistic_talent, communication_skills, fastTyper, handy_person, problem_solving, show_off, team_player]

    for job, questions in job_questions.items():
        for question in questions:
            if answers[question - 1] == 'yes':
                points[job] += 1

    max_points = max(points.values())
    suggested_jobs = [job for job, score in points.items() if score == max_points]
    suggestion = ' or '.join(suggested_jobs)
    print(suggestion)
    return suggestion





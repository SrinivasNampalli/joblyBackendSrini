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
            surveys = surveys.query.all()    # read/extract all users from database
            json_ready = [survey.read() for survey in surveys]  # prepare output in json
            return jsonify(json_ready) # j

    api.add_resource(_CRUD, '/')
def suggest_job(independent, artistic_talent, communication_skills, fastTyper, handy_person, problem_solving, show_off, team_player):
    points = {
        "Graphic Designer": 0,
        "Multimedia Artist": 0,
        "Virtual Assistant": 0,
        "Social Media Influencer": 0,
        "Public Relations Specialist": 0,
        "Communications Specialist": 0,
        "Data Entry Clerk": 0,
        "Maintenance Technician": 0,
        "Problem Solver": 0,
        "Salesperson": 0,
        "Team Coordinator": 0
    }

    traits = [
        (independent, "Graphic Designer", 2),
        (artistic_talent, "Graphic Designer", 1),
        (artistic_talent, "Multimedia Artist", 1),
        (communication_skills, "Multimedia Artist", 1),
        (communication_skills, "Public Relations Specialist", 1),
        (communication_skills, "Communications Specialist", 1),
        (communication_skills, "Team Coordinator", 1),
        (fastTyper, "Virtual Assistant", 1),
        (fastTyper, "Data Entry Clerk", 1),
        (handy_person, "Virtual Assistant", 1),
        (handy_person, "Maintenance Technician", 1),
        (problem_solving, "Social Media Influencer", 1),
        (problem_solving, "Problem Solver", 1),
        (show_off, "Social Media Influencer", 1),
        (show_off, "Salesperson", 1),
        (team_player, "Public Relations Specialist", 1),
        (team_player, "Team Coordinator", 1)
    ]

    for trait, job, point in traits:
        if trait == 'Yes':
            points[job] += point

    job_suggested = max(points, key=points.get)

    return job_suggested



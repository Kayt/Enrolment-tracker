# Enrolment-tracker

Quick Setup
-----------

1. Clone this repository.
2. Move into the project dir `cd enrolment_tracker/backend`
3. Create a virtualenv and install the requirements.
4. Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute `run-redis.sh` to install and launch a private copy).
5. Open a third terminal window and start a Celery worker: `venv/bin/celery worker -A entrack.celery --loglevel=info`.
5. Start the Flask application on your original terminal window: `python run.py`
6. Go to `http://localhost:5000/` and enjoy this application!
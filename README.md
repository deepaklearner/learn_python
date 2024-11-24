    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install Flask

    pip freeze > requirements.txt
    pip install -r requirements.txt

    To Run: python app.py

    git branch -d <branch name>

alien_invasion_v1.x
    v1.1 Basic
    v1.2 Added colors 
    v1.3 Added settings module
    v1.4 Added ship image
    v1.5 Refactor run_game check_events() and _update_screen()
    v1.6 set the ship at center of screen
    v1.7 ability to move ship right
    v1.8 ability to move ship both left and right
    v1.9 Change ship speed

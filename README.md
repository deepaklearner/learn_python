    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install Flask

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt

    To Run: python app.py

alien_invasion
    v1.1 Basic
    v1.2 Added colors 
    v1.3 Added settings module
    v1.4 Added ship image
    v1.5 Refactor run_game check_events() and _update_screen()
    v1.6 set the ship at center of screen
    v1.7 ability to move ship left and right

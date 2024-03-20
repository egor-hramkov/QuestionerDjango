def prepare_survey_data(survey_data: dict) -> dict:
    """Подготавливает данные для ответа, сортирует вопросы в правильный порядок"""
    if len(survey_data['questions']) == 1:
        return survey_data

    questions = survey_data.pop('questions')
    links = survey_data.pop("links")
    links_ids = []

    # Формируем список айдишников, в каком порядке должны идти вопросы
    for i, link in enumerate(links):
        links_ids.append(link['from_question'])
        if i == len(links) - 1:
            links_ids.append(link['to_question'])

    sorted_questions = []
    # Достаём вопросы по айдишнику, таким образом формируя сортированный порядок
    for link_id in links_ids:
        q = next((item for item in questions if item["id"] == link_id), None)
        sorted_questions.append(q)
    survey_data['questions'] = sorted_questions
    return survey_data

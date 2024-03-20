def prepare_survey_data(survey_data: dict) -> dict:
    """Подготавливает данные для ответа, сортирует вопросы в правильный порядок"""
    if len(survey_data['questions']) == 1:
        return survey_data

    questions = survey_data.pop('questions')
    links = survey_data.pop("links")

    links_ids = [item['from_question'] for item in links]
    links_ids.append(links[-1]['to_question'])

    sorted_questions = sorted(questions, key=lambda x: links_ids.index(x["id"]))
    survey_data['questions'] = sorted_questions
    return survey_data

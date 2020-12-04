from ..models import Activity, activity_schema


def get_all_activities():
    activities = Activity.get_all()
    result = activity_schema.dump(activities, many=True)
    return result


def create_activity(id_user, term, action, payload, word):
    if action == 'learn':
        result = True
    elif action == 'ask':
        if word['term'] == payload:
            result = True
        else:
            result = False

    activity = Activity(id_user,term, result, action, payload)
    Activity.add(activity)
    new_activity = activity_schema.dump(activity)
    return new_activity


def get_filter_activities(filters):
    allowed_filters = ['id_user','term','result','action']
    final_filters = {k: v for k, v in filters.items() if k in allowed_filters}
    activities = Activity.get_filtes(**final_filters)

    return activity_schema.jsonify(activities, many=True)


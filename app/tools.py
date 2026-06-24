def check_appointment_slots(department):

    slots = {
        "cardiology": [
            "10:00 AM",
            "02:00 PM",
            "04:30 PM"
        ],
        "neurology": [
            "11:00 AM",
            "01:30 PM"
        ],
        "orthopedics": [
            "09:00 AM",
            "03:00 PM"
        ]
    }

    return {
        "department": department,
        "available_slots": slots.get(
            department.lower(),
            []
        )
    }
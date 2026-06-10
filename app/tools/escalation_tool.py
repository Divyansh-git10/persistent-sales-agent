def flag_for_human(user_id, reason):

    print(f"""
    ESCALATION ALERT

    User: {user_id}

    Reason: {reason}
    """)

    return {
        "flagged": True,
        "reason": reason
    }
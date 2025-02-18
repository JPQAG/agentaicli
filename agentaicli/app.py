def lambda_handler(event, context):
    """
    Main Lambda handler for the AgentAI CLI
    """
    return {
        'statusCode': 200,
        'body': 'Hello from AgentAI CLI!'
    } 
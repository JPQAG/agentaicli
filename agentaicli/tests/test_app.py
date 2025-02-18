import pytest
from app import lambda_handler

def test_lambda_handler():
    # Test with a basic event
    event = {}
    context = None
    response = lambda_handler(event, context)
    
    # Verify the response structure
    assert isinstance(response, dict)
    assert 'statusCode' in response
    assert response['statusCode'] == 200
    assert 'body' in response
    assert isinstance(response['body'], str) 
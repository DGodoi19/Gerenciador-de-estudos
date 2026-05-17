import pytest
from django.urls import reverse
from unittest.mock import patch

@pytest.mark.django_db
@patch('requests.get')
def test_index_carrega_com_sucesso_e_exibe_feriados_da_api(mock_get, client):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            "date": "2026-12-25",
            "name": "Natal",
            "type": "national"
        }
    ]
    
   
    url = reverse('index') 
    resposta = client.get(url)
    
    
    assert resposta.status_code == 200
    
    
    assert b"Natal" in resposta.content

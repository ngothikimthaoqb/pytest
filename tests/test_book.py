import pytest

from utils.json_schema_validator import verify_json_schema, load_json_data

@pytest.mark.usefixtures("api", "config")
@pytest.mark.SMOKE
class TestBook:
    def test_get_book_positive(self, api, config):
        response = api.get(config["apiPath"]["books"]["getBook"])
        assert response.status_code == 200

        books_response = response.json()
        books_expected = load_json_data('../schemas/book/list_books.json')
        verify_json_schema(books_response, books_expected)


    
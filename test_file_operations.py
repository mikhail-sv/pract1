import os
import pytest
from file_operations import (
    read_file, write_file, delete_last_lines, edit_line,
    search_line, clear_file
)

# flake8: noqa: E501

@pytest.fixture
def temp_file():
    """Create a temporary file for testing and clean up after the test."""
    filename = 'test_example.txt'
    # Create a test file with some initial content
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")
    yield filename  # This makes the file available for the test
    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)


def test_read_file(temp_file):
    """Test reading a file."""
    content = read_file(temp_file)
    assert content == "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n", "The file content was not as expected."

    # Test file not found error handling
    content = read_file('nonexistent_file.txt')
    assert content == "Файл не найден.", "Error message for nonexistent file was not correct."


def test_write_file(temp_file):
    """Test writing to a file."""
    write_file(temp_file, "New line")
    content = read_file(temp_file)
    assert "New line" in content, "The new line was not written to the file."


def test_delete_last_lines(temp_file):
    """Test deleting the last lines from the file."""
    delete_last_lines(temp_file, 2)
    content = read_file(temp_file)
    assert "Line 4" not in content and "Line 5" not in content, "Last lines were not deleted correctly."


def test_search_line(temp_file):
    """Test searching for a line in the file."""
    matches = search_line(temp_file, "Line 3")
    assert len(
        matches) == 1 and "Line 3" in matches[0], "Search results were not correct."

    matches = search_line(temp_file, "Nonexistent line")
    assert matches == [
        "Совпадений не найдено."], "Search for a non-existent line did not return the expected result."


def test_edit_line(temp_file):
    """Test editing a line in the file."""
    result = edit_line(temp_file, 2, "Edited Line 2")
    assert result == "Строка 2 изменена.", "The line edit result was not as expected."

    content = read_file(temp_file)
    assert "Edited Line 2" in content, "The line content was not updated."

    # Test invalid line number
    result = edit_line(temp_file, 10, "This should fail")
    assert result == "Номер строки вне диапазона.", "The error message for invalid line number was not correct."


def test_clear_file(temp_file):
    """Test clearing the file contents."""
    result = clear_file(temp_file)
    assert result == f"Файл '{temp_file}' очищен.", "File clearing result was not as expected."

    content = read_file(temp_file)
    assert content == "", "The file was not cleared correctly."

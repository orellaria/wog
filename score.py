from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5

    try:
        # Try to read the current score
        with open(SCORES_FILE_NAME, 'r') as score_file:
            current_score = int(score_file.read())
    except (FileNotFoundError, ValueError):
        # If the file doesn't exist or is invalid, start with a score of 0
        current_score = 0

    # Update the score
    new_score = current_score + points_of_winning

    try:
        # Write the new score back to the file
        with open(SCORES_FILE_NAME, 'w') as score_file:
            score_file.write(str(new_score))
    except Exception as e:
        print(f"Failed to write score to file: {e}")
        return BAD_RETURN_CODE

    return new_score

"""
Utility functions for the Hello World project.

Provides reusable logic for filtering people by course enrollment
and writing personalised greetings to an output file.
"""


def get_greetings(people, config):
    """
    Generate greeting strings for people enrolled in the configured course.

    Args:
        people (list): List of dicts, each with a name and a list of courses.
        config (dict): Configuration dict with keys 'course' and 'courses'.

    Returns:
        list: List of greeting strings for enrolled people.
    """
    greetings = []
    for person in people:
        if config['course'] in person[config['courses']]:
            greetings.append(f"Hello {person['name']}\n")
    return greetings


def write_greetings(greetings, output_dir, config):
    """
    Write greeting strings to a text file in the specified output directory.

    Args:
        greetings (list): List of greeting strings to write.
        output_dir (str): Path to the output directory.
        config (dict): Configuration dict with key 'output_file'.
    """
    output_path = f"{output_dir}/{config['output_file']}"
    with open(output_path, 'w') as f:
        f.writelines(greetings)
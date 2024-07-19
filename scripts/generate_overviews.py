import os

import yaml
from jinja2 import Environment, FileSystemLoader

# Get the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the YAML file
with open(
    os.path.join(script_dir, "../docs/course-data.yaml"), "r", encoding="utf-8"
) as f:
    courses = yaml.load(f, Loader=yaml.FullLoader)

# Define the Jinja2 environment and load the template
env = Environment(
    loader=FileSystemLoader(os.path.join(script_dir, "../src/ac_microcourses")),
    keep_trailing_newline=True,
)
overview_template = env.get_template("overview.md.jinja")
index_template = env.get_template("index.md.jinja")

# For each course, render the templates and write the results to markdown files
for course_key, course_data in courses.items():
    course_data["course_key"] = course_key
    # Render the overview template
    overview = overview_template.render(course_data)

    # replace {{ hello-world }} with the course title of the hello-world course
    for key in courses.keys():
        overview = overview.replace(f"{{{{ {key} }}}}", courses[key]["course_title"])
        overview = overview.replace(
            "{{ courses.hello-world.course_assessments_and_grading_schema }}",
            courses["hello-world"]["course_assessments_and_grading_schema"],
        )
        # e.g., replace {{ hello-world }} with title of hello-world course

    # Strip trailing new lines
    overview = overview.rstrip() + "\n"

    # Write the overview markdown to a file
    with open(
        os.path.join(script_dir, f"../docs/courses/{course_key}/overview.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(overview)

    # Render the index template
    index = index_template.render(course_data)

    # Write the index markdown to a file
    with open(
        os.path.join(script_dir, f"../docs/courses/{course_key}/index.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(index)

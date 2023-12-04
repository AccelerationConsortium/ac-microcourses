import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML file
with open("docs/course-data.yaml", "r", encoding="utf-8") as f:
    courses = yaml.load(f, Loader=yaml.FullLoader)

# Define the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader("src/ac_microcourses"))
template = env.get_template("overview.md.jinja")

# For each course, render the template and write the result to a markdown file
for course_name, course_data in courses.items():
    # Render the template
    markdown = template.render(course_data)
    # replace {{ hello-world }} with the course title of the hello-world course

    for key in courses.keys():
        markdown = markdown.replace(f"{{{{ {key} }}}}", courses[key]["course_title"])
        markdown = markdown.replace(
            "{{ courses.hello-world.course_assessments_and_grading_schema }}",
            courses["hello-world"]["course_assessments_and_grading_schema"],
        )
        # e.g., replace {{ hello-world }} with title of hello-world course

    # Write the markdown to a file
    with open(f"docs/courses/{course_name}/overview.md", "w", encoding="utf-8") as f:
        f.write(markdown)

1 + 1

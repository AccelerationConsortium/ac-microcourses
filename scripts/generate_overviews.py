import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML file
with open("course-data.yaml", "r") as f:
    courses = yaml.load(f, Loader=yaml.FullLoader)

# Define the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader("../ac-microcourses"))
template = env.get_template("overview.md.jinja")

# For each course, render the template and write the result to a markdown file
for course in courses:
    # Render the template
    markdown = template.render(course=course)

    # Write the markdown to a file
    with open(f"{course['name']}.md", "w") as f:
        f.write(markdown)

1 + 1

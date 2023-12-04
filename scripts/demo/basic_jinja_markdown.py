from jinja2 import Template

# Define the template
template = Template("# {{ course_emoji }} {{ course_title }}")

# Define the dictionary with the course data
course_data = {
    "course_emoji": "📚",
    "course_title": "Example Course",
}

# Render the template with the course data
rendered_template = template.render(course_data)

print(rendered_template)

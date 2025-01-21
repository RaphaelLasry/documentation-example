from docutils.parsers.rst import Directive
from docutils import nodes


class click_to_expand(Directive):
    """
    A custom directive to create a clickable content in the documentation.
    """

    has_content = True  # Allow content inside the directive
    optional_arguments = 100  # Allow title of max 100 words

    def run(self):
        # Extract the title for the <summary> tag
        title = " ".join(self.arguments) if self.arguments else "Click to expand"

        # Prepare the HTML structure
        raw_html = f"""
        <details>
        <summary><a>{title}</a></summary>
        <div><br>{"".join(self.content)}<br></div>
        </details>
        <div style="margin-top: 1.5em;"></div>
        """

        # Create a raw HTML node
        raw_node = nodes.raw("", raw_html, format="html")
        return [raw_node]


def setup_custom_directives(app):
    app.add_directive("click", click_to_expand)

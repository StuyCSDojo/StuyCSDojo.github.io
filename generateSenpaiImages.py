import os

aboutHTML = open("./about.html").read()
anchor_start = "<!-- SENPAI IMAGE START -->"
anchor_end = "<!-- SENPAI IMAGE END -->"


def extract_name(filename: str) -> str:
    """
    turns "William Cao.jpeg" to "William Cao"
    """
    parts = filename[:-5].split(" ")
    return parts[-2] + " " + parts[-1]


# Generate the HTML to be inserted
photo_names = os.listdir("./static/photos")
photo_names.sort()
photo_html = ""
for file_name in photo_names:
    if file_name.endswith(".jpeg"):
        # Ignore directories, extraneous files
        photo_html += f"""
        <div class="mdl-card mdl-shadow--2dp mdl-cell--3-col" style="width: 256px; height: 256px; margin: 3px">
          <div class="mdl-card__title mdl-card--expand" style="background: url('./static/photos/{file_name}') center / cover;"></div>
          <div class="mdl-card__actions mdl-card--border">{extract_name(file_name)}</div>
        </div>
        """


# Wrap in a grid div
photo_html = f"""
<div class="mdl-grid">
{photo_html}
</div>
"""
# Remove old photos if any
index_to_insert = aboutHTML.index(anchor_start) + len(anchor_start)
index_to_end = aboutHTML.index(anchor_end)
aboutHTML = aboutHTML[:index_to_insert] + aboutHTML[index_to_end:]

# Insert the html
aboutHTML = aboutHTML[:index_to_insert] + photo_html + aboutHTML[index_to_insert:]

print(aboutHTML)
open('about.html', 'w').write(aboutHTML)

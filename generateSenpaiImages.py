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
        <div class="mdl-shadow--2dp mdl-cell mdl-cell--3-col" style="background: url('./static/photos/{file_name}') center / cover; width: 256px; height: 256px;">
          <div class="mdl-card__title mdl-card--expand"></div>
          <div class="mdl-card__actions" style="height: 52px;padding: 16px;background: rgba(255, 255, 255, 0.8);margin-top:150px">
            <span class="demo-card-image__filename" style="color: #000; font-size: 14px; font-weight: 500;">{extract_name(file_name)}</span>
          </div>
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

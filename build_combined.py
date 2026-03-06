import os

dir_path = r"c:\Users\vijay electronics\Desktop\muti electronics service website"

files_to_combine = [
    "electronics-service-center-unnao.html",
    "smart-mp3-school-bell-system.html",
    "best-school-cctv-bell-service.html",
    "best-cctv-camera-service-unnao.html"
]

# Get the basic template from index.html or one of the files
with open(os.path.join(dir_path, files_to_combine[0]), 'r', encoding='utf-8') as f:
    template_content = f.read()

# Extract header (everything before <section class="section">)
header_end = template_content.find('<section class="section">')
header = template_content[:header_end]

# Modify header title & description
header = header.replace('<title>Home Electronics & Electric Service Center in Unnao | Vijay Electronics</title>', '<title>Complete Electronics, CCTV & School Bell Services in Unnao | Vijay Electronics</title>')
header = header.replace('<meta name="description" content="Looking for the best home electronics and electric service center in Unnao? Vijay Electronics provides expert repair and maintenance for LED TVs, inverters, and more.">', '<meta name="description" content="Looking for the best CCTV, School Bell, and Electronics repair services in Unnao? Vijay Electronics provides expert solutions for all your needs.">')

# Modify sub-hero
subhero_start = header.find('<header class="sub-hero">')
subhero_end = header.find('</header>') + len('</header>')
if subhero_start != -1:
    new_subhero = '''<header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 20px; line-height: 1.3;">Complete Electronics, CCTV & School Bell Services in Unnao</h1>
            <p>Your Trusted Partner for Comprehensive Tech Solutions.</p>
        </div>
    </header>'''
    header = header[:subhero_start] + new_subhero + header[subhero_end:]

# Extract footer (everything from </section> onwards)
footer_start = template_content.find('</section>')
footer = template_content[footer_start:]

# Replace links in footer
links_to_replace = '''<li><a href="electronics-service-center-unnao.html">Home Electronics Service Center Unnao</a></li>
                        <li><a href="smart-mp3-school-bell-system.html">Smart MP3 School Bell System</a></li>
                        <li><a href="best-school-cctv-bell-service.html">Best School CCTV & Bell Service Unnao</a></li>
                        <li><a href="best-cctv-camera-service-unnao.html">Best CCTV Camera Service Unnao</a></li>'''

replacement = '<li><a href="complete-services-unnao.html">Complete Services Guide Unnao</a></li>'
footer = footer.replace(links_to_replace, replacement)

combined_panels = ""

# Extract content from each file
for file in files_to_combine:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        start = content.find('<div class="glass-panel"')
        end = content.find('</section>')
        
        if start != -1 and end != -1:
            # We want everything from <div class="glass-panel"... to the closing </div> of glass-panel
            # The structure is:
            # <section class="section">
            #   <div class="container" ...>
            #     <div class="glass-panel"...>
            #       ... content ...
            #     </div>
            #   </div>
            # </section>
            # So the glass-panel ends at the SECOND to last </div> before </section>
            
            section_inner = content[start:end]
            # Strip trailing whitespace and the last closing </div> which belongs to the container
            section_inner = section_inner.rstrip()
            if section_inner.endswith('</div>'):
                section_inner = section_inner[:-6].rstrip() # remove container's closing div
            
            # The remaining is the glass-panel div
            combined_panels += f"\n<!-- SECTION FROM {file} -->\n"
            combined_panels += section_inner + "\n"

# Assemble full HTML
final_html = header + '<section class="section">\n    <div class="container" style="max-width: 900px;">\n' + combined_panels + '\n    </div>\n' + footer

with open(os.path.join(dir_path, "complete-services-unnao.html"), 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Created complete-services-unnao.html")

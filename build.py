import os
import json

# Read keywords
with open('multi keywards.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith('Service-Type Keywords') and not line.startswith('Modifiers & Quality')]

seo_keywords_string = " &bull; ".join(lines)

def wrap_page(title, description, content, extra_head=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
    {extra_head}
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="logo">
                <img src="logo.png" alt="Vijay Electronics Logo" style="height: 50px;">
            </a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="school-bell.html">School Bells</a></li>
                <li><a href="cctv-security.html">CCTV Security</a></li>
                <li><a href="electronics-repair.html">Electronics</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="faq.html">FAQ</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="nav-cta">
                <a href="tel:8090090051" class="btn btn-primary">Call: 8090090051</a>
            </div>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    {content}

    <footer class="main-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Vijay Electronics</h4>
                    <p>Complete Electronics Solutions in Unnao & UP. Authorized Dealer & Expert Service Provider with 1000+ Happy Customers.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="school-bell.html">Smart School Bells</a></li>
                        <li><a href="cctv-security.html">CCTV Installation</a></li>
                        <li><a href="electronics-repair.html">TV & Laptop Repair</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Phone: 8090090051</li>
                        <li>Location: Unnao, Uttar Pradesh</li>
                        <li>Service Areas: Unnao, Kanpur, Lucknow</li>
                    </ul>
                </div>
            </div>
            
            <div class="seo-dump">
                <h5>Areas & Services We Cover</h5>
                <p>{seo_keywords_string}</p>
            </div>
            
            <div class="copy-right">
                &copy; 2026 Vijay Electronics. All Rights Reserved.
            </div>
        </div>
    </footer>

    <div class="sticky-footer-cta">
        <a href="tel:8090090051" class="cta-call">📞 Call Now</a>
        <a href="https://wa.me/918090090051" class="cta-whatsapp" target="_blank">📱 WhatsApp Us</a>
    </div>

    <script src="js/script.js"></script>
</body>
</html>"""
    return html

# ----------------- HOME PAGE -----------------
index_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "ElectronicsStore", "SecuritySystemProvider"],
  "name": "Vijay Electronics",
  "image": "logo.png",
  "telephone": "8090090051",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Unnao",
    "addressLocality": "Unnao",
    "addressRegion": "UP",
    "addressCountry": "IN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 26.5393,
    "longitude": 80.4878
  },
  "url": "https://vijayelectronicsunnao.com",
  "priceRange": "$$"
}
</script>
"""

index_content = """
    <header class="sub-hero" style="padding-top: 120px; padding-bottom: 60px;">
        <div class="container">
            <h1>Top Automatic School Bell Manufacturers in Unnao & UP</h1>
            <p>Smart IoT School Bells, Professional CCTV Installation, and Complete Electronic Solutions.</p>
            <div style="margin-top: 30px; display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="school-bell.html" class="btn btn-primary">Explore School Bells</a>
                <a href="tel:8090090051" class="btn btn-secondary" style="background: white; border-color: white;">Call to Order: 8090090051</a>
            </div>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <h2 class="section-title">Our Core Services</h2>
            <div class="footer-grid" style="gap: 30px;">
                <div class="card glass-panel">
                    <div class="card-icon">🔔</div>
                    <h3 class="card-title">Smart School Bells</h3>
                    <p>Automatic, IoT, and Voice-enabled (MP3) School Bell Systems. Perfect for exam modes and PA system integration. No manual ringing required. Starting at ₹12,400/piece.</p>
                    <a href="school-bell.html" class="btn btn-secondary" style="margin-top: 20px;">Learn More</a>
                </div>
                <div class="card glass-panel">
                    <div class="card-icon">📷</div>
                    <h3 class="card-title">CCTV Security</h3>
                    <p>CP Plus & Hikvision Authorized Dealer. Complete campus and commercial security solutions, installation, and AMC Contracts.</p>
                    <a href="cctv-security.html" class="btn btn-secondary" style="margin-top: 20px;">Learn More</a>
                </div>
                <div class="card glass-panel">
                    <div class="card-icon">📺</div>
                    <h3 class="card-title">Electronics Repair</h3>
                    <p>LED TV Panel & Motherboard Repair, Refurbished Laptops & Desktop repair, Inverters, and Stabilizers with Doorstep Service.</p>
                    <a href="electronics-repair.html" class="btn btn-secondary" style="margin-top: 20px;">Learn More</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section" style="background-color: var(--white);">
        <div class="container">
             <div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center;">
                 <div style="flex: 1; min-width: 300px;">
                     <h2 style="font-size: 2.2rem; color: var(--primary-color);">Why Choose Vijay Electronics?</h2>
                     <ul style="list-style: none; margin-top: 20px;">
                         <li style="margin-bottom: 15px;"><strong>✅ 1000+ Happy Customers</strong> across Unnao, Kanpur, and Lucknow.</li>
                         <li style="margin-bottom: 15px;"><strong>✅ Expert Technicians</strong> with years of specialized experience.</li>
                         <li style="margin-bottom: 15px;"><strong>✅ Same-Day Doorstep Service</strong> for maximum convenience.</li>
                         <li style="margin-bottom: 15px;"><strong>✅ Wholesale & Retail Pricing</strong> ensuring the best value.</li>
                         <li style="margin-bottom: 15px;"><strong>✅ AMC Contracts Available</strong> for long-term peace of mind.</li>
                     </ul>
                 </div>
                 <div style="flex: 1; min-width: 300px;">
                     <video controls autoplay muted loop style="border-radius: 16px; box-shadow: var(--box-shadow); width: 100%;">
                         <source src="hero video.mp4" type="video/mp4">
                         Your browser does not support the video tag.
                     </video>
                 </div>
             </div>
        </div>
    </section>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("Vijay Electronics | Top Automatic School Bell Manufacturers in Unnao",
                      "Best Smart IoT School Bell systems, CCTV installation, and electronics repair in Unnao. Contact Vijay Electronics for complete electronics solutions.",
                      index_content, index_schema))


# ----------------- SCHOOL BELL PAGE -----------------
bell_content = """
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">Automatic & Voice School Bell Systems in Unnao</h1>
            <p>Upgrade your school with a modern MP3 voice-enabled, IoT smart bell system. Automate your daily timetable effortlessly.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="school bell img.png" alt="Automatic School Bell Machine" style="border-radius: 12px; box-shadow: var(--box-shadow); margin-bottom: 20px;">
                    <img src="school bell img 1.png" alt="School Bell Installation" style="border-radius: 12px; box-shadow: var(--box-shadow);">
                </div>
                <div style="flex: 1.5; min-width: 300px;">
                    <h2 style="color: var(--primary-color);">Complete School Automation & Safety</h2>
                    <p style="margin-bottom: 20px;">Vijay Electronics provides a "school-specialist" solution in Unnao for CCTV and digital/MP3 voice bell setups. Manual bells are a thing of the past. Ensure perfect periods, accurate timing, and clear announcements.</p>
                    
                    <h3 style="color: var(--secondary-color); margin-top: 30px;">Key Features of Our Systems</h3>
                    <ul style="margin-left: 20px; margin-bottom: 30px;">
                        <li style="margin-bottom: 10px;"><strong>Digital School Bell Machine:</strong> Set the timing once for periods, lunch, prayer, and assembly. Fully automatic!</li>
                        <li style="margin-bottom: 10px;"><strong>MP3 Voice Integration:</strong> Hindi/English voice announcements ("First period start", "Lunch break over").</li>
                        <li style="margin-bottom: 10px;"><strong>Timer Controller:</strong> Full week scheduling, including custom holiday & Sunday logic.</li>
                        <li style="margin-bottom: 10px;"><strong>PA System & Intercom Ready:</strong> Seamlessly integrate into existing amplification setups.</li>
                        <li style="margin-bottom: 10px;"><strong>Inverter & Stabilizer Supported:</strong> Works without interruption during power cuts.</li>
                    </ul>
                    
                    <div class="glass-panel" style="padding: 20px; background: rgba(0,51,102,0.05);">
                        <h4 style="color: var(--primary-color);">Special Pricing</h4>
                        <p style="font-size: 1.2rem; font-weight: bold; color: var(--secondary-color);">Complete MP3 Setups starting from ₹12,400 per piece</p>
                        <p style="font-size: 0.9rem;">Includes setup, programming, and basic training for school staff.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
with open("school-bell.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("Smart Automatic School Bell Systems | Unnao | Vijay Electronics",
                      "Get the best automatic, IoT, and MP3 Voice school bell systems in Unnao. Simplify your school's schedule with Vijay Electronics.",
                      bell_content))

# ----------------- CCTV PAGE -----------------
cctv_content = """
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">Professional CCTV Security Installation in Unnao</h1>
            <p>Authorized Dealers for CP Plus & Hikvision. Comprehensive planning, installation, and AMC for Schools, Homes, and Businesses.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; gap: 40px;">
                 <div style="flex: 1.5; min-width: 300px;">
                    <h2 style="color: var(--primary-color);">CCTV Installation – From Planning to Monitoring</h2>
                    <p style="margin-bottom: 20px;">We don't just sell cameras. We provide a complete end-to-end security solution tailored to your premises. Perfect for schools requiring discipline and transparent safety, and homes/businesses needing 24/7 protection.</p>
                    
                    <div class="glass-panel" style="padding: 30px; margin-bottom: 30px;">
                        <h3 style="color: var(--secondary-color);">Our Process</h3>
                        <ol style="margin-left: 20px; margin-top: 15px;">
                            <li style="margin-bottom: 10px;"><strong>Site Survey:</strong> Analyzing gates, corridors, cash counters, and perimeters.</li>
                            <li style="margin-bottom: 10px;"><strong>Camera Planning:</strong> Selecting the right mix of Dome, Bullet, Wide-angle, or PTZ cameras.</li>
                            <li style="margin-bottom: 10px;"><strong>Wiring & Installation:</strong> Safe, neat, and anti-tamper wiring setups.</li>
                            <li style="margin-bottom: 10px;"><strong>DVR/NVR Configuration:</strong> Ensuring 15 to 30 days backup, motion detection, and alerts.</li>
                            <li style="margin-bottom: 10px;"><strong>Mobile View Setup:</strong> Live monitoring access on your smartphone or PC from anywhere.</li>
                        </ol>
                    </div>
                 </div>
                 <div style="flex: 1; min-width: 300px; display:flex; flex-direction:column; gap:20px;">
                    <img src="cctv camera service.jpeg" alt="CCTV Camera Service" style="border-radius: 12px; box-shadow: var(--box-shadow);">
                    <img src="cctv installing.jpeg" alt="CCTV Installing" style="border-radius: 12px; box-shadow: var(--box-shadow);">
                 </div>
            </div>
        </div>
    </section>
"""
with open("cctv-security.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("Best CCTV Camera Shop & Installation in Unnao | Vijay Electronics",
                      "Authorized CP Plus and Hikvision CCTV dealers in Unnao. Professional installation, AMC, and repair services for homes, shops, and schools.",
                      cctv_content))

# ----------------- ELECTRONICS PAGE -----------------
elec_content = """
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">Multi-Electronic Repair & Services</h1>
            <p>LED TVs, Laptops, Desktops, Inverters, and General Home Electrical Services in Unnao.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <p class="text-center" style="max-width: 800px; margin: 0 auto 50px; font-size: 1.1rem;">Vijay Electronics provides expert repair and maintenance for a wide variety of household and office electronics. Enjoy our same-day doorstep service!</p>
            
            <div class="footer-grid" style="gap: 30px;">
                <div class="card glass-panel">
                    <img src="led tv home service.jpeg" alt="LED TV Service" style="border-radius: 8px; margin-bottom: 15px;">
                    <h3 class="card-title">LED/LCD TV Repair</h3>
                    <p>Expert panel framing and motherboard repair. Fast and reliable home service.</p>
                </div>
                <div class="card glass-panel">
                    <img src="laptop service.jpeg" alt="Laptop Repair" style="border-radius: 8px; margin-bottom: 15px;">
                    <h3 class="card-title">Laptop & Desktop</h3>
                    <p>Hardware upgrades, OS installation, chip-level motherboard repair, and refurbished sales.</p>
                </div>
                <div class="card glass-panel">
                    <img src="inverter service home.jpeg" alt="Inverter Service" style="border-radius: 8px; margin-bottom: 15px;">
                    <h3 class="card-title">Inverters & Power Backup</h3>
                    <p>Battery maintenance, stabilizer repair, and full power backup installations for continuous supply.</p>
                </div>
            </div>
        </div>
    </section>
"""
with open("electronics-repair.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("LED TV, Laptop, Inverter & Electronics Repair Unnao",
                      "Same-day doorstep repair service for LED TVs, Laptops, Desktops, Inverters, and Stabilizers in Unnao.",
                      elec_content))

# ----------------- ABOUT PAGE -----------------
about_content = """
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">About Vijay Electronics</h1>
            <p>Your Trusted Local Partner for Complete Electronics Solutions in Unnao.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="vijay electronics shop.jpeg" alt="Vijay Electronics Shop" style="border-radius: 12px; box-shadow: var(--box-shadow);">
                </div>
                <div style="flex: 1.5; min-width: 300px;">
                    <h2 style="color: var(--primary-color);">Over a Decade of Trust & Service</h2>
                    <p style="margin-bottom: 15px;">Based in the heart of Unnao, Uttar Pradesh, <strong>Vijay Electronics</strong> has established itself as the leading provider of smart automation, security, and electronic repair services.</p>
                    <p style="margin-bottom: 15px;">We specialize in "School Digital Board & CCTV Setups", acting as a single-window solution. From smart school bells and audio integration to CP plus & Hikvision camera installations, we plan, install, and maintain it all.</p>
                    <h3 style="color: var(--secondary-color); margin-top: 30px;">Why We Are #1 in Unnao</h3>
                    <ul style="list-style: none; margin-top: 15px;">
                        <li style="margin-bottom: 10px;"><strong>📍 Local Experience:</strong> Hundreds of successful projects in Unnao, Kanpur, and surrounding educational institutes.</li>
                        <li style="margin-bottom: 10px;"><strong>💼 Single Window Solution:</strong> Avoid the hassle of multiple vendors. We handle sales, installation, wiring, and maintenance.</li>
                        <li style="margin-bottom: 10px;"><strong>🛠️ Exceptional After-Sales:</strong> Rapid response for any technical issues, timetable resets, or camera relocation.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""
with open("about.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("About Vijay Electronics | Unnao's Top Electronics Provider",
                      "Learn more about Vijay Electronics, Unnao's trusted partner for smart school automation, CCTV security, and electronic repairs.",
                      about_content))

# ----------------- CONTACT PAGE -----------------
contact_content = """
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">Contact Us</h1>
            <p>Get in touch for quotations, AMC contracts, or doorstep service requests.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div style="flex: 1; min-width: 300px;">
                    <div class="glass-panel" style="padding: 30px; height: 100%;">
                        <h2 style="color: var(--primary-color); margin-bottom: 20px;">Get a Quote</h2>
                        <form onsubmit="event.preventDefault(); alert('Message Sent! We will contact you shortly.');" style="display: flex; flex-direction: column; gap: 15px;">
                            <input type="text" placeholder="Your Name" required style="padding: 12px; border: 1px solid #ddd; border-radius: 8px;">
                            <input type="tel" placeholder="Phone Number" required style="padding: 12px; border: 1px solid #ddd; border-radius: 8px;">
                            <select style="padding: 12px; border: 1px solid #ddd; border-radius: 8px;">
                                <option>School Bell System</option>
                                <option>CCTV Installation</option>
                                <option>Electronics Repair</option>
                                <option>Other Enquiry</option>
                            </select>
                            <textarea placeholder="Your Message / School Detail" rows="4" style="padding: 12px; border: 1px solid #ddd; border-radius: 8px;"></textarea>
                            <button type="submit" class="btn btn-primary">Send Message</button>
                        </form>
                    </div>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <h2 style="color: var(--primary-color); margin-bottom: 20px;">Contact Information</h2>
                    <ul style="list-style: none; font-size: 1.1rem; margin-bottom: 30px;">
                        <li style="margin-bottom: 15px;">📞 <strong>Phone:</strong> <a href="tel:8090090051" style="color: var(--secondary-color);">8090090051</a></li>
                        <li style="margin-bottom: 15px;">📱 <strong>WhatsApp:</strong> <a href="https://wa.me/918090090051" target="_blank" style="color: var(--secondary-color);">Click to Chat</a></li>
                        <li style="margin-bottom: 15px;">📍 <strong>Address:</strong> Unnao, Uttar Pradesh</li>
                        <li style="margin-bottom: 15px;">🎯 <strong>Service Areas:</strong> Unnao, Kanpur, Lucknow, Bangarmau, Safipur</li>
                    </ul>
                    <div style="border-radius: 12px; overflow: hidden; box-shadow: var(--box-shadow);">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d114099.9818817751!2d80.395754!3d26.540114!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399c41740fcfa5df%3A0xe7f920f26941bedf!2sUnnao%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
with open("contact.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("Contact Vijay Electronics Unnao | School Bells & CCTV",
                      "Contact Vijay Electronics at 8090090051 for smart school bells, CCTV quotes, and electronics repair services in Unnao.",
                      contact_content))


# ----------------- FAQ PAGE + SCHEMA -----------------
faq_content_text = ""
try:
    with open('High Ranking FAQ Section (10 Questions).txt', 'r', encoding='utf-8') as f:
        faq_text = f.read()
except:
    pass

faq_pairs_for_schema = [
    {
        "q": "Unnao school mein CCTV camera aur electronics school bell system ko service sabse best kaun deta hai?",
        "a": "Vijay Electronics Unnao provides the best and most complete service for school CCTV cameras and automatic electronics school bell systems. They offer Complete Electronics Solutions ranging from planning, installation, to maintenance."
    },
    {
        "q": "What is the cost of an Automatic MP3 Voice School Bell system in Unnao?",
        "a": "Pricing for a basic MP3 voice school bell system starts at approximately ₹12,400 per piece, varying based on audio integration and backup requirements."
    },
    {
        "q": "Do you provide CCTV AMC (Annual Maintenance Contract) in Unnao?",
        "a": "Yes, Vijay Electronics offers comprehensive AMC services for CCTV cameras (CP Plus, Hikvision) for schools, offices, and homes across Unnao, Kanpur, and Lucknow."
    },
    {
        "q": "Can the school bell be customized for different periods on winter/summer timings?",
        "a": "Yes, our electronic school bell timer controllers can be programmed easily to reflect different timetables, half-days, and seasonal timing changes."
    },
    {
        "q": "Which areas do you provide doorstep electronics repair?",
        "a": "We provide same-day doorstep service in Unnao, Kanpur, Safipur, Bangarmau, and Nawabganj for LED TVs, laptops, and inverters."
    }
]

faq_html_blocks = ""
schema_qa_list = []

for item in faq_pairs_for_schema:
    faq_html_blocks += f'''
        <div class="glass-panel" style="padding: 20px; margin-bottom: 20px;">
            <h3 style="color: var(--primary-color); font-size: 1.2rem; margin-bottom: 10px;">{item['q']}</h3>
            <p style="color: var(--text-color);">{item['a']}</p>
        </div>'''
    schema_qa_list.append({
        "@type": "Question",
        "name": item['q'],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": item['a']
        }
    })

faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": schema_qa_list
}
faq_schema_str = f'<script type="application/ld+json">\\n{json.dumps(faq_schema, indent=2)}\\n</script>'

faq_content = f"""
    <header class="sub-hero">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 15px;">Frequently Asked Questions</h1>
            <p>Your questions about Smart School Bells, CCTV, and Repairs answered here.</p>
        </div>
    </header>

    <section class="section">
        <div class="container" style="max-width: 800px;">
            {faq_html_blocks}
        </div>
    </section>
"""

with open("faq.html", "w", encoding="utf-8") as f:
    f.write(wrap_page("FAQ - Smart School Bells & CCTV Service | Vijay Electronics",
                      "Find answers to all your local queries regarding CCTV installation, automatic school bells, and electronics repair in Unnao.",
                      faq_content, faq_schema_str))

# ----------------- SITEMAP & ROBOTS -----------------

urls = [
    "index.html", "school-bell.html", "cctv-security.html", 
    "electronics-repair.html", "about.html", "faq.html", "contact.html"
]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
for url in urls:
    sitemap += f'  <url>\\n    <loc>https://vijayelectronicsunnao.com/{url}</loc>\\n    <changefreq>weekly</changefreq>\\n    <priority>0.8</priority>\\n  </url>\\n'
sitemap += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

robots = "User-agent: *\\nAllow: /\\n\\nSitemap: https://vijayelectronicsunnao.com/sitemap.xml"
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots)

print("Generated all files.")

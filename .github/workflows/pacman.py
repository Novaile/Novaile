import datetime

frames = [
    "😋     •",
    " 😋    •",
    "  😋   •",
    "   😋  •",
    "    😋 •",
    "     😋•",
    "      😋",
]

# pilih frame berdasarkan menit
now = datetime.datetime.utcnow()
idx = now.minute % len(frames)

# generate SVG
with open("pacman.svg", "w") as f:
    f.write("<svg xmlns='http://www.w3.org/2000/svg' width='200' height='40'>")
    f.write(f"<text x='10' y='25' font-size='24'>{frames[idx]}</text>")
    f.write("</svg>")

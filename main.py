# 17.07.2024 Mert Kus SOCRadar Development Intern
from pypdf import PdfReader, PdfWriter

reader = PdfReader("docs/ASD Cyber Threat Report.pdf")
writer = PdfWriter("docs/ASD Cyber Threat Report.pdf")

for i in range(reader.get_num_pages()):
    file_name = f"{i+1}_asd_cyber_threat_report.txt"
    with open(file_name, "w") as file:
        file.write(reader.pages[i].extract_text())


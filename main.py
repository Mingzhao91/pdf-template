from fpdf import FPDF
import pandas as pd


def set_footer():
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # w: width, 100% if it's set to 0
    # ln: break line, if it's set to 1, the next cell will start on the new line
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # pdf.line(10, 21, 200, 21)

    # set the footer
    pdf.ln(265)
    set_footer()

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # set the footer
        pdf.ln(277)
        set_footer()

pdf.output("output.pdf")


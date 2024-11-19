import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Tuition fees data

tuitionFees = {
    "Medicine (English)": {"listFee": 40000, "advanceFee": 36000},
    "Medicine (30% English)": {"listFee": 30000, "advanceFee": 27000},
    "Dentistry (English)": {"listFee": 32000, "advanceFee": 28800},
    "Dentistry (30% English 70% Turkish)": {"listFee": 30000, "advanceFee": 27000},
    "Pharmacy (English)": {"listFee": 18000, "advanceFee": 16200},
    "Pharmacy (Turkish)": {"listFee": 14000, "advanceFee": 12600},
    "Law (30% English)": {"listFee": 10000, "advanceFee": 9000},
    "Nursing (English)": {"listFee": 7000, "advanceFee": 6300},
    "Nursing (Turkish)": {"listFee": 7000, "advanceFee": 6300},
    "Physiotherapy and Rehabilitation (English)": {"listFee": 7000, "advanceFee": 6300},
     "Physiotherapy and Rehabilitation (Turkish)": {"listFee": 7000, "advanceFee": 6300},
     "Nutrition and Dietetics (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Health Management (English)": {"listFee": 5500, "advanceFee": 4950},
     "Health Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Audiology (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Orthotics and Prosthetics (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Child Development (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Midwifery (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Ergotherapy (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Social Services (Turkish)": {"listFee": 5500, "advanceFee": 4950},
    "English Teaching 100% Englisht": {"listFee": 5000, "advanceFee": 4500},
     "Speech and Language Therapy (English)": {"listFee": 5500, "advanceFee": 4950},
     "Speech and Language Therapy (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Electrical-Electronic Engineering (English)": {"listFee": 6500, "advanceFee": 5850},
     "Biomedical Engineering (English)": {"listFee": 7000, "advanceFee": 6300},
     "Industrial Engineering (English)": {"listFee": 5500, "advanceFee": 4950},
     "Computer Engineering (English)": {"listFee": 7000, "advanceFee": 6300},
     "Civil Engineering (English)": {"listFee": 6500, "advanceFee": 5850},
     "Civil Engineering (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Business Administration (English)": {"listFee": 5500, "advanceFee": 4950},
     "Economics and Finance (English)": {"listFee": 5500, "advanceFee": 4950},
     "International Trade and Finance (English)": {"listFee": 5500, "advanceFee": 4950},
     "International Trade and Finance (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Management Information Systems (English)": {"listFee": 5500, "advanceFee": 4950},
     "Management Information Systems (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Logistic Management (English)": {"listFee": 5500, "advanceFee": 4950},
     "Logistic Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Human Resources Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Aviation Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Banking and Insurance (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Psychology (English)": {"listFee": 5500, "advanceFee": 4950},
     "Psychology (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Political Science and International Relations (English)": {"listFee": 5500, "advanceFee": 4950},
     "Political Science and Public Administration (English)": {"listFee": 5500, "advanceFee": 4950},
     "Political Science and Public Administration (Turkish)": {"listFee": 5500, "advanceFee": 4950},
     "Architecture (English)": {"listFee": 5000, "advanceFee": 4500},
     "Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Industrial Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Interior Architecture and Environmental Design (English)": {"listFee": 5000, "advanceFee": 4500},
     "Interior Architecture and Environmental Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Visual Communication Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "(Turkish) Music Art (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Gastronomy and Culinary Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Urban Design and Landscape Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Psychological Counselling and Guidance (English)": {"listFee": 5000, "advanceFee": 4500},
     "Psychological Counselling and Guidance (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "(English) Teaching (English)": {"listFee": 5000, "advanceFee": 4500},
     "Primary Mathematics Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Special Education Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Preschool Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Journalism (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Public Relations and Advertising (English)": {"listFee": 5000, "advanceFee": 4500},
     "Public Relations and Advertising (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Media and Visual Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "New Media and Communication (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Radio Television and Cinema (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Nutrition and Dietetics (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Child Development (Turkish) (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Midwifery (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Physiotherapy and Rehabilitation (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Audiology (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Social Services (Turkish)": {"listFee": 5000, "advanceFee": 4500},
     "Justice (Turkish)": {"listFee": 3500, "advanceFee": 2800},
     "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Operating Room Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Anesthesia (English)": {"listFee": 4000, "advanceFee": 3600},
     "Anesthesia (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Dental Prosthetics Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600},
     "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Dental Prosthesis Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600},
     "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Pharmacy Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Physiotherapy (English)": {"listFee": 3500, "advanceFee": 3150},
     "Physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "First and Emergency Aid (English)": {"listFee": 4000, "advanceFee": 3600},
     "First and Emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Occupational Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Pathology Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Radiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Prosthetics and Orthotics (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Operation Room Service (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Anesthesia (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Computer Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Biomedical Device Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Dental Prosthesis Technology (Haliç) ": {"listFee": 3500, "advanceFee": 3150},
     "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Interior Design (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "First and emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Construction Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Occiptional Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Architectural Restoration (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Civil Aviation Transportation Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
    "Foreign Trade": {"listFee": 3500, "advanceFee": 3150},
     "Banking and Insurance (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Foreign Trade (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Public Relations and Publicity (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Human Resources Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Business Administration (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Logistics (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Finance (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Accounting and Taxation (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Radio and Television Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Civil Aviation Cabin Services": {"listFee": 3500, "advanceFee": 3150},
     "Social Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Sports Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
     "Applied English and Translation (English)": {"listFee": 3500, "advanceFee": 3150},
     "English Language Teaching (English)": {"listFee": 4500, "advanceFee": 4050},
     "Pre-School Teaching (Turkish)": {"listFee": 1200, "advanceFee": 1200},
}

# Layout
app.layout = dbc.Container([
    html.H1("University Program Revenue Calculator", className="text-center mb-4"),

    dbc.Row([
        dbc.Col(html.Label("Select Program:"), width="auto"),
        dbc.Col(dcc.Dropdown(
            id="program-dropdown",
            options=[{"label": program, "value": program} for program in tuitionFees.keys()],
            placeholder="Select a program"
        )),
    ], justify="start", className="mb-3"),

    dbc.Row([
        dbc.Col(html.Label("List Fee ($):")),
        dbc.Col(html.Div(id="list-fee", children="N/A")),
        dbc.Col(html.Label("Advance Fee ($):")),
        dbc.Col(html.Div(id="advance-fee", children="N/A")),
    ], className="mb-4"),

    # Existing layout components...
], fluid=True)

# Callback to update fees based on selected program
@app.callback(
    [Output("list-fee", "children"), Output("advance-fee", "children")],
    [Input("program-dropdown", "value")]
)
def update_fee_display(selected_program):
    if selected_program and selected_program in tuitionFees:
        list_fee = tuitionFees[selected_program]["listFee"]
        advance_fee = tuitionFees[selected_program]["advanceFee"]
        return f"${list_fee}", f"${advance_fee}"
    return "N/A", "N/A"

if __name__ == "__main__":
    app.run_server(debug=True)

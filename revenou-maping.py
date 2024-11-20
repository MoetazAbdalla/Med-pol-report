import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import io
import base64
import dash_bootstrap_components as dbc
from difflib import get_close_matches


# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server



tuitionFees = {
    "Medicine (English)": {"listFee": 40000, "advanceFee": 36000, "Deposit": 20000},
    "Medicine (30% English)": {"listFee": 30000, "advanceFee": 27000, "Deposit": 15000},
    "Dentistry (English)": {"listFee": 32000, "advanceFee": 28800, "Deposit": 16000},
    "Dentistry (30% English 70% Turkish)": {"listFee": 30000, "advanceFee": 27000, "Deposit": 15000},
    "Pharmacy (English)": {"listFee": 18000, "advanceFee": 16200, "Deposit": 9000},
    "Pharmacy (Turkish)": {"listFee": 14000, "advanceFee": 12600, "Deposit": 7000},
    "Law (30% English)": {"listFee": 10000, "advanceFee": 9000, "Deposit": 5000},
    "Nursing (English)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Nursing (Turkish)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Physiotherapy and Rehabilitation (English)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Physiotherapy and Rehabilitation (Turkish)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Nutrition and Dietetics (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Health Management (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Health Management (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    " Audiology (Haliç Campus) (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Orthotics and Prosthetics (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Child Development (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Midwifery (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Ergotherapy (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Social Services (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "English Teaching 100% English": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Speech and Language Therapy (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Speech and Language Therapy (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Electrical-Electronic Engineering (English)": {"listFee": 6500, "advanceFee": 5850, "Deposit": 3250},
    "Biomedical Engineering (English)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Industrial Engineering (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Computer Engineering (English)": {"listFee": 7000, "advanceFee": 6300, "Deposit": 3500},
    "Civil Engineering (English)": {"listFee": 6500, "advanceFee": 5850, "Deposit": 3250},
    "Civil Engineering (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Business Administration (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Economics and Finance (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "International Trade and Finance (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "International Trade and Finance (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Management Information Systems (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Management Information Systems (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Logistic Management (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Logistic Management (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Human Resources Management (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Aviation Management (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Banking and Insurance (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Psychology (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Psychology (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Political Science and International Relations (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Political Science and Public Administration (English)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Political Science and Public Administration (Turkish)": {"listFee": 5500, "advanceFee": 4950, "Deposit": 2750},
    "Architecture (English)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Industrial Design (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Interior Architecture and Environmental Design (English)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Interior Architecture and Environmental Design (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Visual Communication Design (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "(Turkish) Music Art (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Gastronomy and Culinary Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Urban Design and Landscape Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Psychological Counselling and Guidance (English)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Psychological Counselling and Guidance (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "(English) Teaching (English)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Primary Mathematics Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Special Education Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Preschool Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Journalism (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Public Relations and Advertising (English)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Public Relations and Advertising (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Media and Visual Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "New Media and Communication (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Radio Television and Cinema (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Nutrition and Dietetics (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Child Development (Turkish) (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Midwifery (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Physiotherapy and Rehabilitation (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Audiology (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Social Services (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},
    "Justice (Turkish)": {"listFee": 3500, "advanceFee": 2800, "Deposit": 1750},
    "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Operating Room Services (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Anesthesia (HALİÇ) (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Anesthesia (English)": {"listFee": 4000, "advanceFee": 3600, "Deposit": 2000},
    "Dental Prosthetics Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600, "Deposit": 2000},
    "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Dental Prosthesis Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600, "Deposit": 2000},
    "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Pharmacy Services (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Physiotherapy (English)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "First and Emergency Aid (English)": {"listFee": 4000, "advanceFee": 3600, "Deposit": 2000},
    "First and Emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Occupational Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Pathology Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Radiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Prosthetics and Orthotics (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Operation Room Service (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Anesthesia (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Computer Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Biomedical Device Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Dental Prosthesis Technology (Haliç) ": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Interior Design (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "First and emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Construction Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Occiptional Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Architectural Restoration (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Civil Aviation Transportation Management (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Foreign Trade": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Banking and Insurance (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Foreign Trade (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Public Relations and Publicity (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Human Resources Management (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Business Administration (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Logistics (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Finance (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Accounting and Taxation (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Radio and Television Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Civil Aviation Cabin Services": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Social Services (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Sports Management (Turkish)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "Applied English and Translation (English)": {"listFee": 3500, "advanceFee": 3150, "Deposit": 1750},
    "English Language Teaching (English)": {"listFee": 4500, "advanceFee": 4050, "Deposit": 1750},
    "Pre-School Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500, "Deposit": 2500},

}

# Mapping of listFee to current and total revenue
revenue_mapping = {
    40000: {"current_revenue": 17575, "total_revenue": 31485},
    30000: {"current_revenue": 13181, "total_revenue": 23727},
    32000: {"current_revenue": 14060, "total_revenue": 25308},
    18000: {"current_revenue": 7908, "total_revenue": 14235},
    14000: {"current_revenue": 6151, "total_revenue": 11072},
    10000: {"current_revenue": 3145, "total_revenue": 5661},
    7000: {"current_revenue": 3075, "total_revenue": 5336},
    6500: {"current_revenue": 2855, "total_revenue": 5140},
    5500: {"current_revenue": 2416, "total_revenue": 4350},
    5000: {"current_revenue": 2196, "total_revenue": 3954},
    4000: {"current_revenue": 1757.5, "total_revenue": 3163.5},
    3500: {"current_revenue": 1575, "total_revenue": 2835},
    # Add other specific listFee mappings here
}

# Normalize the dictionary keys for easier matching
normalized_tuitionFees = {k.lower(): v for k, v in tuitionFees.items()}

# Layout of the app
layout = dbc.Container([
    html.H1("Program Fee Mapper", className="text-center my-4"),

    # File upload component
    dcc.Upload(
        id="upload-data",
        children=html.Div([
            "Drag and Drop or ",
            html.A("Select Files")
        ]),
        style={
            "width": "100%",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px",
        },
        multiple=False
    ),

    html.Div(id="output-data-upload"),

    # Hidden div to store the processed file
    dcc.Store(id="processed-file-data"),

    # Download button for modified file
    html.Div([
        dbc.Button("Download Updated Excel", id="download-btn", color="primary", disabled=True, className="mt-3"),
        dcc.Download(id="download-dataframe-xlsx")
    ], className="text-center")
])


# Callback to process uploaded file and store in-memory data
def register_callbacks(app):
    @app.callback(
        Output("output-data-upload", "children"),
        Output("download-btn", "disabled"),
        Output("processed-file-data", "data"),
        Input("upload-data", "contents"),
        State("upload-data", "filename")
    )
    def process_upload(contents, filename):
        if contents is None:
            return "", True, None

        # Read the uploaded Excel file
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        file = io.BytesIO(decoded)

        try:
            df = pd.read_excel(file, engine="openpyxl")  # Specify engine explicitly
        except Exception as e:
            return dbc.Alert(f"Error reading Excel file: {e}", color="danger"), True, None

        # Normalize column names to handle case and whitespace differences
        df.columns = df.columns.str.strip().str.lower()

        # Check if 'program' column exists after normalization
        if 'program' not in df.columns:
            return dbc.Alert("The uploaded file does not contain a 'program' column.", color="danger"), True, None

        # Normalize and map fees based on the closest program match
        def get_fees(program):
            normalized_program = program.strip().lower()
            match = get_close_matches(normalized_program, normalized_tuitionFees.keys(), n=1, cutoff=0.8)
            if match:
                return normalized_tuitionFees[match[0]]
            else:
                return {"listFee": "N/A", "advanceFee": "N/A", "Deposit": "N/A"}

        # Apply the get_fees function to the program column
        df["listFee"] = df["program"].apply(lambda x: get_fees(x)["listFee"])
        df["advanceFee"] = df["program"].apply(lambda x: get_fees(x)["advanceFee"])
        df["Deposit"] = df["program"].apply(lambda x: get_fees(x)["Deposit"])

        # Map Current Revenue and Total Revenue based on listFee
        df["Current Revenue"] = df["listFee"].apply(lambda x: revenue_mapping.get(x, {}).get("current_revenue", "N/A"))
        df["Total Revenue"] = df["listFee"].apply(lambda x: revenue_mapping.get(x, {}).get("total_revenue", "N/A"))

        # Save the modified DataFrame to a BytesIO object
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        output.seek(0)

        # Encode the file in base64 to store it in the hidden div
        encoded_file = base64.b64encode(output.read()).decode("utf-8")

        return dbc.Alert(f"File {filename} uploaded and processed successfully!", color="success"), False, encoded_file


    # Callback to download the modified Excel file
    @app.callback(
        Output("download-dataframe-xlsx", "data"),
        Input("download-btn", "n_clicks"),
        State("processed-file-data", "data"),
        prevent_initial_call=True
    )
    def download_file(n_clicks, data):
        if data is None:
            return None

        # Decode the stored data back to bytes and prepare for download
        decoded = base64.b64decode(data)
        return dcc.send_bytes(decoded, "modified_file.xlsx")

# Initialize the Dash app and register callbacks
app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))

from dash import dcc, html, Input, Output, State, dash, callback_context
import pandas as pd
import io
import base64


# Define regions and corresponding countries
regions = {
    'Central & Eastern Europe': [
        "Albania", "BosniaandHerzegovina", "Bulgaria", "Croatia", "Cyprus",
        "CzechRepublic", "Estonia", "FormerYugoslavRepublicofMacedonia",
        "Greece", "Hungary", "Kosovo", "Latvia", "Lithuania", "Montenegro",
        "Poland", "Romania", "Serbia", "Slovakia", "Slovenia"],

    'Central Asia (CIS)': [
        "Armenia", "Azerbaijan", "Belarus", "Georgia",
        "Kazakhstan", "Kyrgyzstan", "Moldova",
        "Tajikistan", "Ukraine", "Uzbekistan"],

    'East, Southeast Asia & Pacific': [
        "AmericanSamoa", "Australia", "Brunei", "Cambodia", "China",
        "Christmas Island", "Cocos (Keeling) Islands", "Cook Islands",
        "EastTimor", "Federated States of Micronesia", "Fiji",
        "French Polynesia", "Guam", "Heard Island and McDonald Islands",
        "HongKong", "Japan", "Kiribati", "Laos", "Macau", "Malaysia",
        "Marshall Islands", "Mongolia", "Myanmar", "Nauru", "New Caledonia",
        "New Zealand", "Niue", "Norfolk Island", "North Korea",
        "Northern Mariana Islands", "Palau", "Papua New Guinea", "Philippines",
        "Pitcairn Islands", "Samoa", "Singapore", "Solomon Islands",
        "SouthKorea", "Taiwan", "Thailand", "Tokelau", "Tonga", "Tuvalu",
        "United States Minor Outlying Islands", "Vanuatu", "Vietnam","Samoa", "Japan", "Macau ", "Vanuatu"],

    'Indonesia': ["Indonesia"],

    'Iran': ["Iran"],

    'Latin America & The Caribbean': [
        "Anguilla", "AntiguaandBarbuda", "Argentina", "Aruba", "Barbados",
        "Belize", "Bermuda", "Bolivia", "Bouvet Island", "Brazil",
        "British Virgin Islands", "Caribbean Netherlands", "Cayman Islands",
        "Chile", "Colombia", "Costa Rica", "Cuba", "Curaçao", "Dominica",
        "Dominican Republic", "Ecuador", "El Salvador", "Falkland Islands",
        "French Guiana", "Grenada", "Guadeloupe", "Guatemala", "Guyana",
        "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Montserrat",
        "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico",
        "Saint Barthélemy", "SaintKittsandNevis", "SaintLucia",
        "Saint Vincent and the Grenadines", "Saint-Martin", "Sint Maarten",
        "Suriname", "The Bahamas", "Trinidad and Tobago", "Turks and Caicos Islands",
        "United States Virgin Islands", "Uruguay", "Venezuela"
    ],

    'MENA': [
        "Akrotiri and Dhekelia", "Algeria", "Bahrain", "British Indian Ocean Territory",
        "Egypt", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya",
        "Morocco", "Oman", "Palestine", "Qatar", "Sahrawi Arab Democratic Republic",
        "SaudiArabia", "Syria", "Tunisia", "UnitedArabEmirates", "Yemen"
    ],

    'North America': ["Canada", "UnitedStates"],

    'Northern & Western Europe': [
        "Aland", "Andorra", "Austria", "Belgium", "Denmark", "Faroe Islands",
        "Finland", "France", "Germany", "Gibraltar", "Greenland", "Guernsey",
        "Iceland", "Ireland", "Isle of Man", "Italy", "Jersey", "Liechtenstein",
        "Luxembourg", "Malta", "Monaco", "Netherlands", "Norway", "Portugal",
        "San Marino", "Spain", "Svalbard and Jan Mayen", "Sweden", "Switzerland",
        "UnitedKingdom", "Vatican City"
    ],

    'Russia': ["Russia"],

    'South Asia': [
        "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
        "Nepal", "Pakistan", "SriLanka"
    ],

    'Sub-Saharan Africa': [
        "Angola", "Benin", "Botswana", "BurkinaFaso", "Burundi", "Cameroon",
        "Cape Verde", "CentralAfricanRepublic", "Chad", "Comoros", "DemocraticRepublicoftheCongo", "Congo",
        "Djibouti", "EquatorialGuinea", "Eritrea", "Eswatini", "Ethiopia",
        "French Southern and Antarctic Lands", "Gabon", "Ghana", "Guinea",
        "Guinea-Bissau", "IvoryCoast", "Kenya", "Lesotho", "Liberia",
        "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mayotte",
        "Mozambique", "Namibia", "Niger", "Nigeria", "Réunion", "Rwanda",
        "Saint Helena, Ascension and Tristan da Cunha", "São Tomé and Príncipe",
        "Senegal", "Seychelles", "SierraLeone", "Somalia", "SouthAfrica",
        "SouthSudan", "Sudan", "Swaziland", "Tanzania", "TheGambia", "Togo",
        "Uganda", "Zambia", "Zimbabwe"
    ],

    'Türkiye': ["TurkishRepublicofNorthernCyprus", "Turkey"],
    'Turkmenistan': ["Turkmenistan"],
}


# Function to find region based on country
def find_region(country):
    for region, countries in regions.items():
        if country in countries:
            return region
    return 'Unknown'


# Define layout for Country-Region Mapping Page
layout = html.Div([
    html.H2("Country-Region Mapping", style={'textAlign': 'center', 'marginBottom': '20px'}),
    dcc.Upload(
        id="upload-country-data-mapping",  # Changed ID to avoid duplication
        children=html.Div(
            ["📂 Drag and Drop or ", html.A("Select a File", style={'color': '#007bff', 'cursor': 'pointer'})]),
        style={
            "width": "100%", "height": "80px", "lineHeight": "80px", "borderWidth": "2px", "borderStyle": "dashed",
            "borderRadius": "10px", "textAlign": "center", "margin": "10px 0", "backgroundColor": "#f9f9f9"
        },
        multiple=False,
    ),
    html.Button("Map Regions", id="map-region-button-mapping", n_clicks=0, style={
        "margin": "20px 0", "padding": "10px 20px", "fontSize": "16px", "backgroundColor": "#007bff", "color": "#fff",
        "border": "none", "borderRadius": "5px", "cursor": "pointer"
    }),
    html.Div(id="map-output-mapping", style={"margin": "10px 0", "color": "#28a745", "fontSize": "16px"}),
    dcc.Download(id="download-region-file-mapping")  # Download component
], style={"maxWidth": "600px", "margin": "0 auto", "padding": "20px", "boxShadow": "0px 0px 15px rgba(0, 0, 0, 0.1)",
          "borderRadius": "10px", "backgroundColor": "#ffffff"})


# Register the callback for mapping and downloading
def register_callbacks(app):
    @app.callback(
        Output("map-output-mapping", "children"),
        Output("download-region-file-mapping", "data"),
        Input("upload-country-data-mapping", "contents"),
        Input("map-region-button-mapping", "n_clicks"),
        State("upload-country-data-mapping", "filename")
    )
    def handle_country_region_mapping(contents, n_clicks, filename):
        if not contents:
            return "Please upload a file to map regions.", dash.no_update

        triggered_id = callback_context.triggered[0]["prop_id"].split(".")[0]

        if triggered_id == "upload-country-data-mapping" and contents:
            content_type, content_string = contents.split(",")
            decoded = io.BytesIO(base64.b64decode(content_string))
            df = pd.read_excel(decoded)

            if 'Nationality' not in df.columns:
                return "Error: 'Nationality' column not found in uploaded file.", dash.no_update

            return f"{filename} uploaded. Ready to map regions.", dash.no_update

        elif triggered_id == "map-region-button-mapping" and n_clicks > 0 and contents:
            content_type, content_string = contents.split(",")
            decoded = io.BytesIO(base64.b64decode(content_string))
            df = pd.read_excel(decoded)

            if 'Nationality' not in df.columns:
                return "Error: 'Nationality' column not found in uploaded file.", dash.no_update

            # Map regions to the 'Nationality' column
            df['Region'] = df['Nationality'].apply(find_region)

            # Convert DataFrame to an in-memory Excel file for download
            with io.BytesIO() as output:
                with pd.ExcelWriter(output, engine="openpyxl") as writer:  # Changed to openpyxl
                    df.to_excel(writer, index=False)
                output.seek(0)
                excel_data = output.read()

            return "Country to region mapping completed. Click below to download.", dcc.send_bytes(
                excel_data, filename="mapped_regions.xlsx"
            )

        return [], "Upload a file and click 'Map Regions' to proceed.", dash.no_update



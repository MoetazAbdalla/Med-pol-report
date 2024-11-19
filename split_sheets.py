from dash import dcc, html, Input, Output, State, callback_context, dash
import pandas as pd
import io
import base64
import re
import tempfile
import os

# Define the layout for the split sheets page
layout = html.Div(
    style={'maxWidth': '800px', 'margin': '0 auto', 'padding': '20px'},
    children=[
        html.H2("Split Excel Sheets by Column", style={'textAlign': 'center', 'marginBottom': '30px'}),

        dcc.Upload(
            id="upload-data",
            children=html.Div(["📁 Drag and Drop or ", html.A("Select Files", style={'color': '#007BFF'})]),
            style={
                "width": "100%", "height": "60px", "lineHeight": "60px", "borderWidth": "1px",
                "borderStyle": "dashed", "borderRadius": "5px", "textAlign": "center", "marginBottom": "20px",
                "backgroundColor": "#f9f9f9", "cursor": "pointer", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
            },
            multiple=False,
        ),

        html.Label("Select column to split by:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id="column-dropdown",
            placeholder="Select a column to split by",
            style={"marginBottom": "20px"}
        ),

        html.Button(
            "Split Sheets",
            id="split-button",
            n_clicks=0,
            style={
                "width": "100%", "padding": "12px", "fontSize": "16px",
                "backgroundColor": "#007BFF", "color": "white", "border": "none",
                "borderRadius": "5px", "cursor": "pointer", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)"
            }
        ),

        html.Div(id="split-output", style={'marginTop': '20px', 'fontSize': '16px', 'color': '#28A745'}),

        dcc.Loading(
            id="loading-icon",
            children=[dcc.Download(id="download-file")],
            type="circle"
        )  # Loading spinner
    ]
)


# Register the callbacks for the split sheets page
def register_callbacks(app):
    @app.callback(
        Output("column-dropdown", "options"),
        Output("split-output", "children"),
        Output("download-file", "data"),
        Input("upload-data", "contents"),
        Input("split-button", "n_clicks"),
        State("upload-data", "filename"),
        State("column-dropdown", "value")
    )
    def handle_upload_and_split(contents, n_clicks, filename, column):
        triggered_id = callback_context.triggered[0]["prop_id"].split(".")[0]

        # Handle file upload and populate dropdown
        if triggered_id == "upload-data" and contents:
            content_type, content_string = contents.split(",")
            decoded = io.BytesIO(base64.b64decode(content_string))
            df = pd.read_excel(decoded)
            df.columns = df.columns.str.strip()  # Clean column names

            # Populate dropdown with column names
            return [{"label": col, "value": col} for col in
                    df.columns], f"{filename} uploaded. Select a column.", dash.no_update

        # Handle split sheet functionality
        elif triggered_id == "split-button" and n_clicks and column and contents:
            content_type, content_string = contents.split(",")
            decoded = io.BytesIO(base64.b64decode(content_string))
            df = pd.read_excel(decoded)
            df.columns = df.columns.str.strip()

            if column not in df.columns:
                return dash.no_update, f"Column '{column}' not found in the data!", dash.no_update

            # Create a temporary file for the Excel output
            with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_file:
                output_path = tmp_file.name
                with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                    for agency_name, agency_df in df.groupby(column):
                        sanitized_agency_name = re.sub(r'[\\/*?:"<>|]', "", str(agency_name))[:31]
                        agency_df.to_excel(writer, sheet_name=sanitized_agency_name, index=False)

            # Prepare the file for download and show a success message
            success_message = f"✅ Data has been split by '{column}'. Click to download the file."
            return dash.no_update, success_message, dcc.send_file(output_path)

        return [], "Please upload a file to see column options and split sheets.", dash.no_update

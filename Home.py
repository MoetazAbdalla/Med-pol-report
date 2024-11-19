from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os
import logging

# Initialize the Dash app
app = Dash(__name__)
server = app.server

# Set up logging for error tracking
logging.basicConfig(filename="app.log", level=logging.DEBUG)

# Path to Excel file
excel_path = 'assets/5-year.xlsx'


# Load Data from Excel File
def load_data():
    if not os.path.exists(excel_path):
        logging.error(f"Excel file not found at {excel_path}")
        print(f"Excel file not found at {excel_path}")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found

    try:
        df = pd.read_excel(excel_path, sheet_name='2020-2025')
        logging.info(f"Data loaded successfully with shape: {df.shape}")
        print(f"Data loaded successfully: {df.shape}")

        # Debugging: Print out the column names for verification
        if df.empty:
            logging.warning("DataFrame is empty after loading.")
            print("DataFrame is empty after loading.")
        else:
            logging.info(f"Columns loaded: {df.columns.tolist()}")
            print(f"Columns loaded: {df.columns.tolist()}")

        return df
    except Exception as e:
        logging.error(f"Error loading data from Excel: {e}")
        print(f"Error loading data from Excel: {e}")
        return pd.DataFrame()


# Load the data at startup
data = load_data()

# Layout for Home page
layout = html.Div([
    html.H1('Istanbul MediPol University Reporting Dashboard', style={'textAlign': 'center', 'color': '#007BFF'}),

    # Tiles for metrics in a responsive grid
    html.Div([
        html.Div([html.H4('Total Students'), html.H2(id='total-students-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Total Payments'), html.H2(id='total-payments-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Program'), html.H2(id='top-program-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Status'), html.H2(id='top-status-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Performance'), html.H2(id='performance-metric-home', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
    ], className="row"),

    # Tabs for different visualizations
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div([
                html.Div([dcc.Graph(id='status-pie-chart-home', config={'displayModeBar': False})],
                         className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                html.Div([dcc.Graph(id='top-nationality-pie-chart-home', config={'displayModeBar': False})],
                         className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                html.Div([dcc.Graph(id='top-paid-countries-pie-chart-home', config={'displayModeBar': False})],
                         className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
            ], className="row"),
            html.Div([
                html.Div([dcc.Graph(id='top-regions-bar-chart-home', config={'displayModeBar': False})],
                         className='col-lg-6 col-md-12 mb-4 chart-container'),
                html.Div([dcc.Graph(id='top-programs-applied-pie-chart-home', config={'displayModeBar': False})],
                         className='col-lg-6 col-md-12 mb-4 chart-container'),
            ], className="row"),
        ])
    ]),
])


# Callbacks for updating the dashboard based on data
@app.callback(
    [Output('total-students-home', 'children'),
     Output('total-payments-home', 'children'),
     Output('top-nationality-home', 'children'),
     Output('top-program-home', 'children'),
     Output('top-status-home', 'children'),
     Output('performance-metric-home', 'children'),
     Output('status-pie-chart-home', 'figure'),
     Output('top-nationality-pie-chart-home', 'figure'),
     Output('top-paid-countries-pie-chart-home', 'figure'),
     Output('top-regions-bar-chart-home', 'figure'),
     Output('top-programs-applied-pie-chart-home', 'figure')],
    [Input('agent-dropdown-home', 'value')]
)
def update_dashboard(selected_sheet):
    df = data  # Use preloaded and cached data

    if df.empty:
        print("DataFrame is empty, cannot generate metrics.")
        return ["No data"] * 6 + [px.pie(), px.pie(), px.pie(), px.bar(), px.pie()]

    # Ensure necessary columns exist
    required_columns = ['Status', 'Nationality', 'Program', 'Region', 'Created By']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return ["Missing data"] * 6 + [px.pie(), px.pie(), px.pie(), px.bar(), px.pie()]

    # Top statistics calculations
    total_students = df.shape[0]
    top_nationality = df['Nationality'].value_counts().idxmax() if not df['Nationality'].empty else "N/A"
    top_program = df['Program'].value_counts().idxmax() if not df['Program'].empty else "N/A"
    top_status = df['Status'].value_counts().idxmax() if not df['Status'].empty else "N/A"
    total_paid = df['Status'].value_counts().get('Paid', 0)
    performance = (total_paid / total_students) * 100 if total_students > 0 else 0
    performance_metric = f"{performance:.2f}%"

    # Generate charts
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution", hole=0.4)

    top_nationality_counts = df['Nationality'].value_counts().reset_index()
    top_nationality_counts.columns = ['Nationality', 'Count']
    top_nationality_pie_chart = px.pie(top_nationality_counts.head(15), names='Nationality', values='Count',
                                       title="Top Nationalities", hole=0.4)

    top_paid_countries = df[df['Status'] == 'Paid']['Nationality'].value_counts().reset_index()
    top_paid_countries.columns = ['Country', 'Count']
    top_paid_countries_pie_chart = px.pie(top_paid_countries.head(15), names='Country', values='Count',
                                          title="Top Paid Countries", hole=0.4)

    region_counts = df['Region'].value_counts().reset_index()
    region_counts.columns = ['Region', 'Count']
    top_regions_bar_chart = px.bar(region_counts.head(6), x='Region', y='Count',
                                   title="Top 6 Regions by Student Count", text='Count')

    applied_programs = df[df['Status'] == 'Applied']['Program'].value_counts().reset_index()
    applied_programs.columns = ['Program', 'Count']
    top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                            title="Top 10 Programs Applied", hole=0.4)

    return (total_students, total_paid, top_nationality, top_program, top_status, performance_metric,
            pie_chart, top_nationality_pie_chart, top_paid_countries_pie_chart, top_regions_bar_chart,
            top_programs_applied_pie_chart)


# Set the layout and register callbacks
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)

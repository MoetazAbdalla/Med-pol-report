import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the new Excel file and get all sheet names (each sheet represents an International Office User)
excel_file = 'assets/Cls_data.xlsx'

# Attempt to read the sheet names, and print them for debugging purposes
try:
    # Reading the sheet names to ensure the file is correct
    sheet_names = pd.ExcelFile(excel_file).sheet_names
    print("Available Sheets in the file:", excel_file)
    print(sheet_names)
except FileNotFoundError as e:
    print(f"Error: File '{excel_file}' not found!")
    sheet_names = []
except Exception as e:
    print(f"An error occurred: {e}")
    sheet_names = []

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dashboard Layout with Tabs
layout = html.Div([
    html.Div([
        html.H1('Istanbul MediPol University CL1 Reporting Dashboard',
                style={'textAlign': 'center', 'color': '#007BFF'}),

        # Tiles for metrics in a responsive grid
        html.Div([
            html.Div([  # Total Students
                html.H4('Total Students'),
                html.H2(id='total-students-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Total Payments
                html.H4('Total Payments'),
                html.H2(id='total-payments-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Nationality
                html.H4('Top Nationality'),
                html.H2(id='top-nationality-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Program
                html.H4('Top Program'),
                html.H2(id='top-program-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Status
                html.H4('Top Status'),
                html.H2(id='top-status-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Performance
                html.H4('Performance'),
                html.H2(id='performance-metric-cperformance', className='metric-text'),  # Updated ID
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        ], className="row"),

        # Dropdown menu for selecting International Office User
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='user-dropdown-cperformance',  # Updated ID
                    options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                    value=sheet_names[0] if sheet_names else None,  # Default value (first sheet if available)
                    placeholder='Select an International Office User',
                    className='custom-dropdown',  # Add a custom class for styling
                ),
            ], className='col-lg-12'),  # Ensures the dropdown spans the full width
        ], className='row menu-bar mb-4 container-fluid'),

        # Tabs for different visualizations
        dcc.Tabs([
            dcc.Tab(label='Overview', children=[
                html.Div([
                    # Row for pie charts (responsive flexbox)
                    html.Div([
                        html.Div([dcc.Graph(id='status-pie-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-nationality-pie-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-countries-pie-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                    ], className="row"),

                    # Row for top regions and performance line chart
                    html.Div([
                        html.Div([dcc.Graph(id='top-regions-bar-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='performance-month-line-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Pie charts for top 10 programs applied and total paid for top 10 programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-programs-applied-pie-chart-cperformance', config={'displayModeBar': False })],  # Updated ID
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-programs-paid-pie-chart-cperformance', config={'displayModeBar': False})],  # Updated ID
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),
                ], className="container-fluid")
            ]),
        ], className="tabs-container")
    ], className='main-container'),
])


# Callbacks to update the dashboard based on selected International Office User
def register_callbacks(app):
    @app.callback(
        [Output('total-students-cperformance', 'children'),
         Output('total-payments-cperformance', 'children'),
         Output('top-nationality-cperformance', 'children'),
         Output('top-program-cperformance', 'children'),
         Output('top-status-cperformance', 'children'),
         Output('performance-metric-cperformance', 'children'),
         Output('status-pie-chart-cperformance', 'figure'),
         Output('top-nationality-pie-chart-cperformance', 'figure'),
         Output('top-paid-countries-pie-chart-cperformance', 'figure'),
         Output('top-regions-bar-chart-cperformance', 'figure'),
         Output('performance-month-line-chart-cperformance', 'figure'),
         Output('top-programs-applied-pie-chart-cperformance', 'figure'),
         Output('top-programs-paid-pie-chart-cperformance', 'figure')],
        [Input('user-dropdown-cperformance', 'value')]
    )
    def update_dashboard(selected_user):
        if not selected_user:
            # If no user is selected, return empty data
            return "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}

        # Load the data from the selected sheet
        try:
            df = pd.read_excel(excel_file, sheet_name=selected_user)
        except Exception as e:
            print(f"Error loading sheet '{selected_user}': {e}")
            return "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}

        # Clean column names by stripping whitespace
        df.columns = df.columns.str.strip()

        # Check if the DataFrame is empty
        if df.empty:
            return "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}

        # Ensure the 'Date' column is properly formatted and in datetime format
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')

        # Top statistics
        total_students = df.shape[0]
        top_nationality = df['Nationality'].value_counts().idxmax() if 'Nationality' in df.columns else "N/A"
        top_program = df['Program'].value_counts().idxmax() if 'Program' in df.columns else "N/A"
        top_status = df['Status'].value_counts().idxmax() if 'Status' in df.columns else "N/A"

        # Calculate total payments
        if 'Status' in df.columns:
            df['Status'] = df['Status'].str.strip().str.lower()  # Ensure consistency
            total_paid = df['Status'].value_counts().get('paid', 0)
        else:
            total_paid = 0

        # Calculate performance metric
        performance = (total_paid / total_students) * 100 if total_students > 0 else 0
        performance_metric = f"{performance:.2f}%"

        # Pie chart for status distribution
        if 'Status' in df.columns:
            status_counts = df['Status'].value_counts().reset_index()
            status_counts.columns = ['Status', 'Count']
            pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution", hole=0.4)
        else:
            pie_chart = {}

        # Pie chart for top nationality distribution
        if 'Nationality' in df.columns:
            top_nationality_counts = df['Nationality'].value_counts().reset_index()
            top_nationality_counts.columns = ['Nationality', 'Count']
            top_nationality_pie_chart = px.pie(top_nationality_counts.head(15), names='Nationality', values='Count',
                                               title="Top Nationalities", hole=0.4)
        else:
            top_nationality_pie_chart = {}

        # Pie chart for top paid countries distribution
        if 'Nationality' in df.columns and 'Status' in df.columns:
            top_paid_countries = df[df['Status'] == 'paid']['Nationality'].value_counts().reset_index()
            top_paid_countries.columns = ['Country', 'Count']
            top_paid_countries_pie_chart = px.pie(top_paid_countries.head(15), names='Country', values='Count',
                                                  title="Top Paid Countries", hole=0.4)
        else:
            top_paid_countries_pie_chart = {}

        # Bar chart for top 6 regions distribution
        if 'Region' in df.columns:
            region_counts = df['Region'].value_counts().reset_index()
            region_counts.columns = ['Region', 'Count']
            top_regions_bar_chart = px.bar(region_counts.head(6), x='Region', y='Count',
                                           title="Top 6 Regions by Student Count", text='Count')
        else:
            top_regions_bar_chart = {}

        # Line chart for performance over months
        if 'Date' in df.columns and df['Date'].notnull().any():
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.strftime('%b')
            month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            all_months_df = pd.DataFrame({'Month': month_order})
            month_counts = df.groupby(['Year', 'Month']).size().reset_index(name='Total Students')
            month_counts = pd.merge(all_months_df, month_counts, on='Month', how='left')
            month_counts['Total Students'].fillna(0, inplace=True)
            performance_month_chart = px.line(
                month_counts,
                x='Month',
                y='Total Students',
                color='Year',
                title="Total Number of Students Over Months",
                markers=True,
                line_shape='linear'
            )
            performance_month_chart.update_traces(mode='lines+markers', line=dict(width=3),
                                                  marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')))
            performance_month_chart.update_layout(xaxis_title="Month",
                                                  yaxis_title="Total Number of Students",
                                                  xaxis={'categoryorder': 'array', 'categoryarray': month_order},
                                                  template='plotly_white', showlegend=True)
        else:
            performance_month_chart = {}

        # Pie chart for top 10 programs applied
        if 'Status' in df.columns and 'Program' in df.columns:
            applied_programs = df[df['Status'] == 'applied']['Program'].value_counts().reset_index()
            applied_programs.columns = ['Program', 'Count']
            if not applied_programs.empty:
                top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                                        title="Top 10 Programs Applied", hole=0.4)
            else:
                top_programs_applied_pie_chart = px.pie(title="Top 10 Programs Applied", hole=0.4)
                top_programs_applied_pie_chart.update_traces(textinfo='none')
        else:
            top_programs_applied_pie_chart = px.pie(title="Top 10 Programs Applied", hole=0.4)
            top_programs_applied_pie_chart.update_traces(textinfo='none')

        # Stacked bar chart for top 7 paid programs
        # Stacked bar chart for top 7 paid programs
        if 'Status' in df.columns and 'Program' in df.columns:
            paid_programs = df[df['Status'] == 'paid'].groupby('Program').size().reset_index(name='Count')
            top_7_paid_programs = paid_programs.nlargest(7, 'Count')
            top_programs_paid_bar_chart = px.bar(
                top_7_paid_programs,
                x='Program',
                y='Count',
                title="Total Paid for Top 7 Programs",
                color='Program',
                text='Count'
            )
            top_programs_paid_bar_chart.update_traces(textposition='inside',
                                                      marker=dict(line=dict(width=1, color='black')),
                                                      width=0.6)
            top_programs_paid_bar_chart.update_xaxes(tickangle=-75)
            top_programs_paid_bar_chart.update_layout(height=600, width=620,
                                                      margin=dict(l=40, r=40, t=70, b=150), showlegend=False)
        else:
            top_programs_paid_bar_chart = {}

        return (total_students, total_paid, top_nationality, top_program, top_status,
                performance_metric, pie_chart, top_nationality_pie_chart, top_paid_countries_pie_chart,
                top_regions_bar_chart, performance_month_chart, top_programs_applied_pie_chart,
                top_programs_paid_bar_chart)

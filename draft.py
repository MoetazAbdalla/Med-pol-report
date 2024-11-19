import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Define the programs to exclude
excluded_programs = ["Bachelor of Medicine (English)", "Bachelor of Medicine (30% English)",
                     "Bachelor of Dentistry (30% English 70% Turkish)", "Bachelor of Dentistry (English)",
                     "Bachelor of Pharmacy (Turkish)", "Bachelor of Pharmacy (English)"]

# Load the Excel file and get all sheet names (each sheet represents an agent)
excel_file = 'assets/application-list-edited.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Create two separate DataFrames
df_excluded = df[df['Program'].isin(excluded_programs)]
df_filtered = df[~df['Program'].isin(excluded_programs)]

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dashboard Layout with Tabs
app.layout = html.Div([
    html.Div([
        html.H1('Istanbul MediPol University Reporting Dashboard',
                style={'textAlign': 'center', 'color': '#007BFF'}),

        # Tiles for metrics in a responsive grid
        html.Div([
            html.Div([  # Total Students
                html.H4('Total Students'),
                html.H2(id='total-students', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Total Payments
                html.H4('Total Payments'),
                html.H2(id='total-payments', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Nationality
                html.H4('Top Nationality'),
                html.H2(id='top-nationality', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Program
                html.H4('Top Program'),
                html.H2(id='top-program', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Status
                html.H4('Top Status'),
                html.H2(id='top-status', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Performance
                html.H4('Performance'),
                html.H2(id='performance-metric', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        ], className="row"),

        # Dropdown menu
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='agent-dropdown',
                    options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                    value=sheet_names[0],  # Default value (first sheet)
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
                        html.Div([dcc.Graph(id='agents-bar-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-nationality-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-countries-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                    ], className="row"),

                    # Row for top regions and performance line chart
                    html.Div([
                        html.Div([dcc.Graph(id='top-regions-bar-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-2 chart-container'),
                        html.Div([dcc.Graph(id='performance-month-line-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Pie charts for top 10 programs applied and total paid for top 10 programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-programs-applied-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-programs-paid-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Pie charts for top 10 paid English and Turkish programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-paid-english-programs-pie-chart',
                                            config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-turkish-programs-pie-chart',
                                            config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),
                    # Pie charts for top 10 applied English and Turkish programs
                    html.Div([
                        html.Div(
                            [dcc.Graph(id='top-applied-english-programs-pie-chart',
                                       config={'displayModeBar': False})],
                            className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div(
                            [dcc.Graph(id='top-applied-turkish-programs-pie-chart',
                                       config={'displayModeBar': False})],
                            className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    html.Div(
                        [dcc.Graph(id='Top-MED-bar-chart',
                                   config={'displayModeBar': False})],
                        className='col-lg-6 col-md-12 mb-4 chart-container'),
                ], className="container-fluid")
            ]),
        ], className="tabs-container")
    ], className='main-container'),
])


# Callbacks to update the dashboard based on selected sheet (agent)
@app.callback(
    [Output('total-students', 'children'),
     Output('total-payments', 'children'),
     Output('top-nationality', 'children'),
     Output('top-program', 'children'),
     Output('top-status', 'children'),
     Output('performance-metric', 'children'),
     Output('agents-bar-chart', 'figure'),
     Output('top-nationality-pie-chart', 'figure'),
     Output('top-paid-countries-pie-chart', 'figure'),
     Output('top-regions-bar-chart', 'figure'),
     Output('performance-month-line-chart', 'figure'),
     Output('top-programs-applied-pie-chart', 'figure'),
     Output('top-programs-paid-pie-chart', 'figure'),
     Output('top-paid-english-programs-pie-chart', 'figure'),
     Output('top-paid-turkish-programs-pie-chart', 'figure'),
     Output('top-applied-english-programs-pie-chart', 'figure'),
     Output('Top-MED-bar-chart', 'figure'),
     Output('top-applied-turkish-programs-pie-chart', 'figure')],
    [Input('agent-dropdown', 'value')]
)
def update_dashboard(selected_sheet):
    # Load the data from the selected sheet
    df = pd.read_excel(excel_file, sheet_name=selected_sheet)

    # Check if the DataFrame is empty
    if df.empty:
        return ("No data", "No data", "N/A", "N/A", "N/A", "0%",
                {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})

    # Ensure the 'Date' column is properly formatted and in datetime format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')

    # Top statistics
    total_students = df.shape[0]
    top_nationality = df['Nationality'].value_counts().idxmax() if 'Nationality' in df.columns else "N/A"
    top_program = df['Program'].value_counts().idxmax() if 'Program' in df.columns else "N/A"
    top_status = df['Status'].value_counts().idxmax() if 'Status' in df.columns else "N/A"
    total_paid = df['Status'].str.lower().value_counts().get('paid', 0) if 'Status' in df.columns else 0
    performance = (total_paid / total_students) * 100 if total_students > 0 else 0
    performance_metric = f"{performance:.2f}%"

    # Top 10 paid agents bar chart
    if 'Created By' in df.columns and 'Status' in df.columns:
        paid_agents = df[df['Status'].str.lower() == 'paid']['Created By'].value_counts().head(10).reset_index()
        paid_agents.columns = ['Agent', 'Paid Applications']
        top_paid_agents_bar_chart = px.bar(
            paid_agents, x='Agent', y='Paid Applications', title="Top 10 Paid Agents",
            text='Paid Applications'
        )
    else:
        top_paid_agents_bar_chart = {}

    # Top 10 nationality pie chart
    if 'Nationality' in df.columns:
        nationality_counts = df['Nationality'].value_counts().head(10).reset_index()
        nationality_counts.columns = ['Nationality', 'Count']
        top_nationality_pie_chart = px.pie(nationality_counts, names='Nationality', values='Count',
                                           title="Top 10 Applied Countries", hole=0.4)
    else:
        top_nationality_pie_chart = {}

    # Top 10 paid countries pie chart
    if 'Nationality' in df.columns and 'Status' in df.columns:
        paid_countries = df[df['Status'].str.lower() == 'paid']['Nationality'].value_counts().head(10).reset_index()
        paid_countries.columns = ['Country', 'Count']
        top_paid_countries_pie_chart = px.pie(paid_countries, names='Country', values='Count',
                                              title="Top 10 Paid Countries", hole=0.4)
    else:
        top_paid_countries_pie_chart = {}

    # Top regions bar chart (Total Applications and Total Paid)
    if 'Region' in df.columns and 'Status' in df.columns:
        top_regions = df['Region'].value_counts().nlargest(7).index
        total_applications_counts = df['Region'].value_counts().reindex(top_regions).fillna(0).reset_index()
        total_applications_counts.columns = ['Region', 'Total Applications']
        paid_counts = df[df['Status'].str.lower() == 'paid']['Region'].value_counts().reindex(top_regions).fillna(
            0).reset_index()
        paid_counts.columns = ['Region', 'Total Paid']
        combined_regions = pd.merge(total_applications_counts, paid_counts, on='Region').fillna(0)
        combined_region_chart = px.bar(
            combined_regions.melt(id_vars='Region', value_vars=['Total Applications', 'Total Paid']),
            x='Region',
            y='value',
            color='variable',
            barmode='group',
            title="Top 7 Regions by Total Applications and Total Paid",
            labels={'value': 'Count', 'variable': 'Category'},
            text_auto=True  # Display the count on top of each bar

        )
        # Update the text position for each bar
        combined_region_chart.update_traces(
            selector=dict(name="Total Applications"),
            textposition="inside"
        )
        combined_region_chart.update_traces(
            selector=dict(name="Total Paid"),
            textposition="outside"
        )
    else:
        combined_region_chart = {}

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

    # Top programs pie charts
    def generate_pie_chart(column, status, title):
        if column in df.columns and 'Status' in df.columns:
            filtered_df = df[df['Status'].str.lower() == status][column].value_counts().head(10).reset_index()
            filtered_df.columns = [column, 'Count']
            return px.pie(filtered_df, names=column, values='Count', title=title, hole=0.4)
        return {}

    # Bar chart for excluded programs
    excluded_program_counts = df_excluded['Program'].value_counts().reset_index()
    excluded_program_counts.columns = ['Program', 'Count']
    excluded_programs_bar = px.bar(
        excluded_program_counts,
        x='Program',
        y='Count',
        title="Excluded Programs Applications",
        text='Count'
    )

    top_programs_applied_pie_chart = generate_pie_chart('Program', 'applied', "Top 10 Programs Applied")
    top_programs_paid_pie_chart = generate_pie_chart('Program', 'paid', "Top 10 Programs Paid")
    top_paid_english_programs_pie_chart = generate_pie_chart('Program', 'paid', "Top 10 Paid English Programs")
    top_paid_turkish_programs_pie_chart = generate_pie_chart('Program', 'paid', "Top 10 Paid Turkish Programs")
    top_applied_english_programs_pie_chart = generate_pie_chart('Program', 'applied', "Top 10 Applied English Programs")
    top_applied_turkish_programs_pie_chart = generate_pie_chart('Program', 'applied', "Top 10 Applied Turkish Programs")

    return (
        total_students, total_paid, top_nationality, top_program, top_status, performance_metric,
        top_paid_agents_bar_chart, top_nationality_pie_chart, top_paid_countries_pie_chart, combined_region_chart,
        performance_month_chart, top_programs_applied_pie_chart, top_programs_paid_pie_chart,
        top_paid_english_programs_pie_chart, top_paid_turkish_programs_pie_chart,
        top_applied_english_programs_pie_chart, top_applied_turkish_programs_pie_chart
    )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

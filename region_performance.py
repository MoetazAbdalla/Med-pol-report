import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the new Excel file and get all sheet names (each sheet represents an International Office User)
excel_file = 'assets/Region_data.xlsx'

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
        html.H1('Istanbul MediPol University Region Dashboard',
                style={'textAlign': 'center', 'color': '#007BFF'}),

        # Tiles for metrics in a responsive grid
        html.Div([
            html.Div([  # Total Students
                html.H4('Total Students'),
                html.H2(id='total-students-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Total Payments
                html.H4('Total Payments'),
                html.H2(id='total-payments-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Nationality
                html.H4('Top Nationality'),
                html.H2(id='top-nationality-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Program
                html.H4('Top Program'),
                html.H2(id='top-program-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Status
                html.H4('Top Status'),
                html.H2(id='top-status-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Performance
                html.H4('Performance'),
                html.H2(id='performance-metric-region', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        ], className="row"),

        # Dropdown menu for selecting International Office User
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='user-dropdown-region',
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
                        html.Div([dcc.Graph(id='status-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-nationality-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-countries-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                    ], className="row"),

                    # Row for top regions and performance line chart
                    html.Div([
                        html.Div([dcc.Graph(id='top-agents-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='performance-month-line-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Pie charts for top 10 programs applied and total paid for top 10 programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-programs-applied-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-programs-paid-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Pie charts for top 10 paid English and Turkish programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-paid-english-programs-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-turkish-programs-pie-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),
                    # Pie charts for top 10 applied English and Turkish programs
                    html.Div([
                        html.Div(
                            [dcc.Graph(id='top-applied-english-programs-pie-chart-region', config={'displayModeBar': False})],
                            className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div(
                            [dcc.Graph(id='top-applied-turkish-programs-pie-chart-region', config={'displayModeBar': False})],
                            className='col-lg-6 col-md-12 mb-4 chart-container'),
                    ], className="row"),
                    # Bar chart for top 10 paid agents
                    html.Div([
                        html.Div([dcc.Graph(id='top-paid-agents-bar-chart-region', config={'displayModeBar': False})],
                                 className='col-lg-12 col-md-12 mb-4 chart-container'),
                    ], className="row"),
                ], className="container-fluid")
            ]),
        ], className="tabs-container")
    ], className='main-container'),
])

# Callbacks to update the dashboard based on selected International Office User
def register_callbacks(app):
    @app.callback(
        [Output('total-students-region', 'children'),
         Output('total-payments-region', 'children'),
         Output('top-nationality-region', 'children'),
         Output('top-program-region', 'children'),
         Output('top-status-region', 'children'),
         Output('performance-metric-region', 'children'),
         Output('status-pie-chart-region', 'figure'),
         Output('top-nationality-pie-chart-region', 'figure'),
         Output('top-paid-countries-pie-chart-region', 'figure'),
         Output('top-agents-pie-chart-region', 'figure'),
         Output('performance-month-line-chart-region', 'figure'),
         Output('top-programs-applied-pie-chart-region', 'figure'),
         Output('top-programs-paid-pie-chart-region', 'figure'),
         Output('top-paid-english-programs-pie-chart-region', 'figure'),
         Output('top-paid-turkish-programs-pie-chart-region', 'figure'),
         Output('top-applied-english-programs-pie-chart-region', 'figure'),
         Output('top-applied-turkish-programs-pie-chart-region', 'figure'),
         Output('top-paid-agents-bar-chart-region', 'figure')],
        [Input('user-dropdown-region', 'value')]
    )
    def update_dashboard(selected_user, df=None):
        if not selected_user:
            print("No user selected")
            return (
                "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
                {}, {})

        # Load the data from the selected sheet
        try:
            df = pd.read_excel(excel_file, sheet_name=selected_user)
            print("Data loaded successfully for user:", selected_user)
            print(df.head())  # Debugging: Show the first few rows
        except Exception as e:
            print(f"Error loading sheet '{selected_user}': {e}")
            return (
                "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
                {}, {})

        # Clean column names by stripping whitespace
        df.columns = df.columns.str.strip()

        # Check if the DataFrame is empty
        if df.empty:
            print("DataFrame is empty after loading data.")
            return (
                "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
                {}, {})

        # Ensure the 'Date' column is properly formatted and in datetime format
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')
            print("Date column converted successfully")

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
        status_counts = df['Status'].value_counts().reset_index() if 'Status' in df.columns else pd.DataFrame()
        status_counts.columns = ['Status', 'Count']
        pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution", hole=0.4)

        # Pie chart for top nationality distribution
        top_nationality_counts = df[
            'Nationality'].value_counts().reset_index() if 'Nationality' in df.columns else pd.DataFrame()
        top_nationality_counts.columns = ['Nationality', 'Count']
        top_nationality_pie_chart = px.pie(top_nationality_counts.head(10), names='Nationality', values='Count',
                                           title="Top Applied Countries", hole=0.4)

        # Pie chart for top paid countries distribution
        top_paid_countries = df[df['Status'] == 'paid'][
            'Nationality'].value_counts().reset_index() if 'Nationality' in df.columns and 'Status' in df.columns else pd.DataFrame()
        top_paid_countries.columns = ['Country', 'Count']
        top_paid_countries_pie_chart = px.pie(top_paid_countries.head(10), names='Country', values='Count',
                                              title="Top Paid Countries", hole=0.4)

        # Calculate the top 10 agents for "Applied"
        applied_agents_counts = (
            df[df['Status'] == 'applied']['Created By']
            .value_counts()
            .nlargest(10)
            .reset_index()
        )
        applied_agents_counts.columns = ['Agent', 'Count']
        applied_agents_counts['Status'] = 'Applied'  # Add status label

        # Calculate the top 10 agents for "Paid"
        paid_agents_counts = (
            df[df['Status'] == 'paid']['Created By']
            .value_counts()
            .nlargest(10)
            .reset_index()
        )
        paid_agents_counts.columns = ['Agent', 'Count']
        paid_agents_counts['Status'] = 'Paid'  # Add status label

        # Concatenate the "Applied" and "Paid" data without merging agent names
        combined_agents = pd.concat([applied_agents_counts, paid_agents_counts], ignore_index=True)

        # Plot the chart
        combined_agents_chart = px.bar(
            combined_agents,
            x='Agent',
            y='Count',
            color='Status',
            text='Count',  # Display counts
            title="Top 10 Agents Applied Vs. Paid"
        )

        # Customize layout
        combined_agents_chart.update_layout(
            title_font=dict(size=18, color='#333333', family="Arial"),
            xaxis_title="Agent",
            yaxis_title="Count",
            legend_title_text="Status",
            xaxis_tickangle=-45  # Tilt x-axis labels for readability
        )

        # Set text positions separately for "Applied" and "Paid"
        combined_agents_chart.update_traces(
            selector=dict(name="Applied"),
            textposition="inside",  # Inside for Applied
            textfont=dict(color="white")  # White text for contrast on blue bars
        )

        combined_agents_chart.update_traces(
            selector=dict(name="Paid"),
            textposition="outside",  # Outside for Paid
            textfont=dict(color="black", size=9)  # Larger, darker text for visibility
        )

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
        applied_programs = df[df['Status'] == 'applied'][
            'Program'].value_counts().reset_index() if 'Status' in df.columns and 'Program' in df.columns else pd.DataFrame()
        applied_programs.columns = ['Program', 'Count']
        top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                                title="Top 10 Programs Applied", hole=0.4)

        # Pie chart for top 10 paid English programs
        paid_english_programs = df[df['Status'] == 'paid'][
            df['Program'].str.contains(r'\(English\)', case=False, na=False)]
        paid_english_programs = paid_english_programs[
            'Program'].value_counts().reset_index() if 'Program' in df.columns else pd.DataFrame()
        paid_english_programs.columns = ['Program', 'Count']
        top_paid_english_programs_pie_chart = px.pie(paid_english_programs.head(10), names='Program', values='Count',
                                                     title="Top 10 Paid English Programs", hole=0.4)

        # Pie chart for top 10 paid Turkish programs
        paid_turkish_programs = df[df['Status'] == 'paid'][
            df['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        paid_turkish_programs = paid_turkish_programs[
            'Program'].value_counts().reset_index() if 'Program' in df.columns else pd.DataFrame()
        paid_turkish_programs.columns = ['Program', 'Count']
        top_paid_turkish_programs_pie_chart = px.pie(paid_turkish_programs.head(10), names='Program', values='Count',
                                                     title="Top 10 Paid Turkish Programs", hole=0.4)

        # Pie chart for top 10 applied English programs
        applied_english_programs = df[df['Program'].str.contains(r'\(English\)', case=False, na=False)]
        applied_english_counts = applied_english_programs[
            'Program'].value_counts().reset_index() if 'Program' in df.columns else pd.DataFrame()
        applied_english_counts.columns = ['Program', 'Count']
        top_applied_english_programs_pie_chart = px.pie(applied_english_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied English Programs", hole=0.4)

        # Pie chart for top 10 applied Turkish programs
        applied_turkish_programs = df[df['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        applied_turkish_counts = applied_turkish_programs[
            'Program'].value_counts().reset_index() if 'Program' in df.columns else pd.DataFrame()
        applied_turkish_counts.columns = ['Program', 'Count']
        top_applied_turkish_programs_pie_chart = px.pie(applied_turkish_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied Turkish Programs", hole=0.4)

        # Calculate total payments for top 10 programs
        if 'Program' in df.columns and 'Status' in df.columns:
            total_payments_per_program = df[df['Status'] == 'paid'].groupby('Program').size().reset_index(
                name='Total Payments')
            top_paid_programs = total_payments_per_program.nlargest(10, 'Total Payments')
            top_programs_paid_pie_chart = px.pie(top_paid_programs, names='Program', values='Total Payments',
                                                 title="Total Payments for Top 10 Programs", hole=0.4)
        else:
            top_programs_paid_pie_chart = {}

        # Calculate total payments for top 10 agents
        if 'Created By' in df.columns and 'Status' in df.columns:
            total_payments_per_agent = df[df['Status'] == 'paid'].groupby('Created By').size().reset_index(
                name='Total Payments')
            top_paid_agents = total_payments_per_agent.nlargest(10, 'Total Payments')
            top_paid_agents_bar_chart = px.bar(top_paid_agents, x='Created By', y='Total Payments',
                                               title="Top Payments for Top 10 Agents", text='Total Payments')
        else:
            top_paid_agents_bar_chart = {}

        return (total_students, total_paid, top_nationality, top_program, top_status,
                performance_metric, pie_chart, top_nationality_pie_chart, top_paid_countries_pie_chart,
                combined_agents_chart, performance_month_chart, top_programs_applied_pie_chart,
                top_programs_paid_pie_chart, top_paid_english_programs_pie_chart, top_paid_turkish_programs_pie_chart,
                top_applied_english_programs_pie_chart, top_applied_turkish_programs_pie_chart,
                top_paid_agents_bar_chart)


# Register callbacks
register_callbacks(app)

# Set app layout
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

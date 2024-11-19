import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Load the Excel file with one sheet
excel_file = 'assets/weekly-15-11-2024.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dashboard Layout with Tabs
layout = html.Div([
    html.Div([
        html.H1('Istanbul MediPol University Weekly Reporting Dashboard',
                style={'textAlign': 'center', 'color': '#007BFF'}),

        # Tiles for metrics in a responsive grid
        html.Div([
            html.Div([  # Total Students
                html.H4('Total Students'),
                html.H2(id='total-students', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom

            html.Div([  # Total Payments
                html.H4('Total Payments'),
                html.H2(id='total-payments', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom

            html.Div([  # Top Nationality
                html.H4('Top Nationality'),
                html.H2(id='top-nationality', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom

            html.Div([  # Top Program
                html.H4('Top Program'),
                html.H2(id='top-program', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom

            html.Div([  # Top Status
                html.H4('Top Status'),
                html.H2(id='top-status', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom

            html.Div([  # Performance
                html.H4('Performance'),
                html.H2(id='performance-metric', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-2 tile'),  # Reduce margin-bottom
        ], className="row justify-content-center"),  # Center the row


        # Dropdown menu
        html.Div([
            dcc.Dropdown(
                id='agent-dropdown',
                options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                value=sheet_names[0],  # Default value
                className='custom-dropdown',
                style={
                    'width': '700px',  # Adjust width as needed
                    'margin': '0 auto',
                    'fontSize': '25px',
                    'padding': '5px 10px',
                    'borderRadius': '30px',
                    'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.15)',
                    'border': '0px solid #00000000',
                    'backgroundColor': '#ffffffff',
                    'textAlign': 'center'
                },
            ),
        ], className='d-flex justify-content-center mt-3'),

        # Tabs for different visualizations
        dcc.Tabs([
            dcc.Tab(label='Overview', children=[
                html.Div([
                    # Row for pie charts (responsive flexbox)
                    html.Div([
                        html.Div([dcc.Graph(id='status-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-2 chart-container'),  # Reduce margin-bottom
                        html.Div([dcc.Graph(id='top-nationality-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-2 chart-container'),  # Reduce margin-bottom
                        html.Div([dcc.Graph(id='top-paid-countries-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-2 chart-container'),  # Reduce margin-bottom
                    ], className="row"),

                    # Pie charts for top 10 programs applied and total paid for top 10 programs
                    html.Div([
                        html.Div([dcc.Graph(id='top-programs-applied-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-2 chart-container'),  # Reduce margin-bottom
                        html.Div([dcc.Graph(id='top-programs-paid-pie-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-2 chart-container'),  # Reduce margin-bottom
                    ], className="row"),

                    # New row for top 10 agents bar chart and regions performance pie chart
                    html.Div([
                        html.Div([
                            dcc.Graph(id='top-agents-bar-chart', config={'displayModeBar': False}),
                        ], className='col-lg-6 col-md-12 mb-2 chart-container'),  # Reduce margin-bottom

                        html.Div([  # Top paid regions pie chart
                            dcc.Graph(id='top-paid-regions-pie-chart', config={'displayModeBar': False}),
                        ], className='col-lg-6 col-md-12 mb-2 chart-container'),  # Reduce margin-bottom
                    ], className="row"),

                    # Bar chart for top 10 paid agents
                    html.Div([
                        html.Div([dcc.Graph(id='top-paid-agents-bar-chart', config={'displayModeBar': False})],
                                 className='col-lg-12 col-md-12 mb-4 chart-container'),
                    ], className="row"),

                    # Row for top regions
                    html.Div([
                        html.Div([dcc.Graph(id='top-regions-bar-chart', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-2 chart-container'),  # Reduce margin-bottom
                    ], className="row"),
                ], className="container-fluid")
            ]),
        ], className="tabs-container")
    ], className='main-container'),
])


# Callbacks to update the dashboard based on selected sheet (agent)
def register_callbacks(app):
    @app.callback(
        [Output('total-students', 'children'),
         Output('total-payments', 'children'),
         Output('top-nationality', 'children'),
         Output('top-program', 'children'),
         Output('top-status', 'children'),
         Output('performance-metric', 'children'),
         Output('status-pie-chart', 'figure'),
         Output('top-nationality-pie-chart', 'figure'),
         Output('top-paid-countries-pie-chart', 'figure'),
         Output('top-regions-bar-chart', 'figure'),
         Output('top-agents-bar-chart', 'figure'),
         Output('top-paid-regions-pie-chart', 'figure'),
         Output('top-programs-applied-pie-chart', 'figure'),
         Output('top-programs-paid-pie-chart', 'figure'),
         Output('top-paid-agents-bar-chart', 'figure')],  # Add this output
        [Input('agent-dropdown', 'value')]
    )
    def update_dashboard(selected_sheet):
        # Load the data from the selected sheet
        df = pd.read_excel(excel_file, sheet_name=selected_sheet)

        # Clean column names and ensure proper formatting
        df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

        # Check if the DataFrame is empty
        if df.empty:
            return "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

        # Ensure the 'Status' column is properly formatted
        if 'Status' in df.columns:
            df['Status'] = df['Status'].str.strip().str.lower()  # Strip spaces and convert to lowercase

        # Ensure the 'Date' column is properly formatted and in datetime format
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')

        # Top statistics
        total_students = df.shape[0]
        top_nationality = df['Nationality'].value_counts().idxmax() if 'Nationality' in df.columns else "N/A"
        top_program = df['Program'].value_counts().idxmax() if 'Program' in df.columns else "N/A"
        top_status = df['Status'].value_counts().idxmax() if 'Status' in df.columns else "N/A"
        total_paid = df['Status'].value_counts().get('paid', 0)
        performance = (total_paid / total_students) * 100 if total_students > 0 else 0
        performance_metric = f"{performance:.2f}%"

        # Pie chart for status distribution
        if 'Status' in df.columns:
            status_counts = df['Status'].value_counts().reset_index()
            status_counts.columns = ['Status', 'Count']
            pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution(paid/applied)", hole=0.4)
        else:
            pie_chart = {}

        # Pie chart for top nationality distribution
        if 'Nationality' in df.columns:
            top_nationality_counts = df['Nationality'].value_counts().reset_index()
            top_nationality_counts.columns = ['Nationality', 'Count']
            top_nationality_pie_chart = px.pie(top_nationality_counts.head(10), names='Nationality', values='Count',
                                               title="Top 10 Nationalities Applied", hole=0.4)
        else:
            top_nationality_pie_chart = {}

        # Pie chart for top paid countries distribution
        if 'Status' in df.columns and 'Nationality' in df.columns:
            top_paid_countries = df[df['Status'] == 'paid']['Nationality'].value_counts().reset_index()
            top_paid_countries.columns = ['Country', 'Count']
            top_paid_countries_pie_chart = px.pie(top_paid_countries.head(10), names='Country', values='Count',
                                                  title="Top 10 Paid Countries", hole=0.4)
        else:
            top_paid_countries_pie_chart = {}

        # Ensure 'Region' and 'Status' columns are present
        if 'Region' in df.columns and 'Status' in df.columns:
            # Get the overall count for each region, regardless of status
            total_region_counts = df['Region'].value_counts().nlargest(8).reset_index()  # Get top 8 regions
            total_region_counts.columns = ['Region', 'Total']

            # Filter the original dataframe for the top regions identified
            top_regions = total_region_counts['Region'].tolist()
            filtered_df = df[df['Region'].isin(top_regions)]

            # Count total applications (including 'Applied' and 'Paid') for these top regions
            total_applications_counts = filtered_df['Region'].value_counts().reindex(top_regions,
                                                                                     fill_value=0).reset_index()
            total_applications_counts.columns = ['Region', 'Total Applications']

            # Count "Paid" applications for these top regions
            paid_counts = filtered_df[filtered_df['Status'].str.lower() == 'paid']['Region'].value_counts().reindex(
                top_regions, fill_value=0).reset_index()
            paid_counts.columns = ['Region', 'Total Paid']

            # Merge the counts for total applications and paid applications
            combined_regions = pd.merge(total_applications_counts, paid_counts, on='Region', how='outer').fillna(0)

            # Ensure the columns are numeric for plotting
            combined_regions['Total Applications'] = combined_regions['Total Applications'].astype(int)
            combined_regions['Total Paid'] = combined_regions['Total Paid'].astype(int)

            # Create a grouped bar chart
            combined_region_chart = px.bar(
                combined_regions,
                x='Region',
                y=['Total Applications', 'Total Paid'],
                barmode='group',
                title="Top 8 Regions by Total Applications and Total Paid",
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

        # Pie chart for top 10 programs applied
        if 'Status' in df.columns and 'Program' in df.columns:
            applied_programs = df[df['Status'] == 'applied']['Program'].value_counts().reset_index()
            applied_programs.columns = ['Program', 'Count']
            if not applied_programs.empty:
                top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                                        title="Top 10 Programs Applied", hole=0.4)
            else:
                top_programs_applied_pie_chart = {}
        else:
            top_programs_applied_pie_chart = {}

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
            top_programs_paid_bar_chart.update_traces(
                textposition='inside',
                marker=dict(line=dict(width=1, color='black')),
                width=0.6
            )
            top_programs_paid_bar_chart.update_xaxes(tickangle=-75)
            top_programs_paid_bar_chart.update_layout(
                height=600,
                width=620,
                margin=dict(l=40, r=40, t=70, b=150),
                showlegend=False
            )
        else:
            top_programs_paid_bar_chart = {}

        # Bar chart for top 10 agents by application count
        if 'Created By' in df.columns:
            agent_counts = df['Created By'].value_counts().reset_index()
            agent_counts.columns = ['Agent', 'Application Count']
            top_10_agents = agent_counts.head(10)
            top_agents_bar_chart = px.bar(
                top_10_agents,
                x='Agent',
                y='Application Count',
                title='Top 10 Agents by Application Number',
                text='Application Count'
            )
            top_agents_bar_chart.update_traces(textposition='inside')
            top_agents_bar_chart.update_layout(
                xaxis_title="Agent",
                yaxis_title="Application Count",
                height=400,
                width=600
            )
        else:
            top_agents_bar_chart = {}

        # Pie chart for top paid regions distribution
        if 'Status' in df.columns and 'Region' in df.columns:
            top_paid_regions = df[df['Status'] == 'paid']['Region'].value_counts().reset_index()
            top_paid_regions.columns = ['Region', 'Count']
            top_paid_regions_pie_chart = px.pie(top_paid_regions.head(10), names='Region', values='Count',
                                                title="Top Paid Regions", hole=0.4)
        else:
            top_paid_regions_pie_chart = {}

        # Calculate total payments for top 10 agents
        if 'Created By' in df.columns and 'Status' in df.columns:
            total_payments_per_agent = df[df['Status'] == 'paid'].groupby('Created By').size().reset_index(
                name='Total Payments')
            top_paid_agents = total_payments_per_agent.nlargest(10, 'Total Payments')
            top_paid_agents_bar_chart = px.bar(top_paid_agents, x='Created By', y='Total Payments',
                                               title="Top Payments for Top 10 Agents", text='Total Payments')
        else:
            top_paid_agents_bar_chart = {}

        # Return all necessary outputs
        return (total_students, total_paid, top_nationality, top_program, top_status, performance_metric, pie_chart,
                top_nationality_pie_chart, top_paid_countries_pie_chart, combined_region_chart,
                top_agents_bar_chart, top_paid_regions_pie_chart, top_programs_applied_pie_chart, top_programs_paid_bar_chart,
                top_paid_agents_bar_chart)  # Add this return value


# Set the layout and register callbacks
app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the Excel file and get all sheet names (assuming this file is present in the assets folder)
excel_file = 'assets/Agent_data.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Layout for Weekly Report
layout = html.Div([
    html.H1('Istanbul MediPol University Agent Reporting Dashboard',
            style={'textAlign': 'center', 'color': '#007BFF', 'marginBottom': '20px'}),

    # Metrics tiles
    html.Div([
        html.Div([html.H4('Total Students'), html.H2(id='total-students-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Total Payments'), html.H2(id='total-payments-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Program'), html.H2(id='top-program-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Top Status'), html.H2(id='top-status-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
        html.Div([html.H4('Performance'), html.H2(id='performance-metric-dashboard', className='metric-text')],
                 className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),
    ], className="row justify-content-center gap-3", style={'padding': '10px 0'}),

    # Dropdown menu for selecting the agent
    html.Div([
        dcc.Dropdown(
            id='agent-dropdown-dashboard',
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

    # Visualization tabs
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div([
                # Row for first set of pie charts (Status, Top Nationality, Top Paid Countries)
                html.Div([
                    html.Div(dcc.Loading(dcc.Graph(id='status-pie-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-4 col-md-12 mb-4 chart-container'),
                    html.Div(dcc.Loading(dcc.Graph(id='top-nationality-pie-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-4 col-md-12 mb-4 chart-container'),
                    html.Div(dcc.Loading(dcc.Graph(id='top-paid-countries-pie-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-4 col-md-12 mb-4 chart-container'),
                ], className="row"),

                # Row for combined region bar chart and performance line chart
                html.Div([
                    html.Div(dcc.Loading(dcc.Graph(id='combined-region-bar-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-6 col-md-12 mb-4 chart-container'),
                    html.Div(dcc.Loading(dcc.Graph(id='performance-month-line-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-6 col-md-12 mb-4 chart-container'),
                ], className="row"),

                # Row for the next set of charts (Top Programs Applied and Top Programs Paid)
                html.Div([
                    html.Div(dcc.Loading(dcc.Graph(id='top-programs-applied-pie-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-6 col-md-12 mb-4 chart-container'),
                    html.Div(dcc.Loading(dcc.Graph(id='top-programs-paid-bar-chart-dashboard', config={'displayModeBar': False})),
                             className='col-lg-6 col-md-12 mb-4 chart-container'),
                ], className="row"),
            ], className="container-fluid", style={'padding': '20px 0'}),
        ]),
    ]),
], style={'padding': '20px'})


# Callbacks to update the dashboard based on selected sheet (agent)
def register_callbacks(app):
    @app.callback(
        [Output('total-students-dashboard', 'children'),
         Output('total-payments-dashboard', 'children'),
         Output('top-nationality-dashboard', 'children'),
         Output('top-program-dashboard', 'children'),
         Output('top-status-dashboard', 'children'),
         Output('performance-metric-dashboard', 'children'),
         Output('status-pie-chart-dashboard', 'figure'),
         Output('top-nationality-pie-chart-dashboard', 'figure'),
         Output('top-paid-countries-pie-chart-dashboard', 'figure'),
         Output('combined-region-bar-chart-dashboard', 'figure'),
         Output('top-programs-applied-pie-chart-dashboard', 'figure'),
         Output('performance-month-line-chart-dashboard', 'figure'),
         Output('top-programs-paid-bar-chart-dashboard', 'figure')],
        [Input('agent-dropdown-dashboard', 'value')]
    )
    def update_dashboard(selected_sheet):
        # Try-except block to catch any errors when loading the data
        try:
            df = pd.read_excel(excel_file, sheet_name=selected_sheet)
            print(f"Loaded data for sheet: {selected_sheet}")
        except Exception as e:
            print(f"Error loading sheet {selected_sheet}: {e}")
            return ["Error loading data"] * 13  # Ensure we return 13 placeholder outputs

        # Check if DataFrame is empty or missing required columns
        required_columns = ['Status', 'Nationality', 'Program', 'Region', 'Date']
        if df.empty or any(col not in df.columns for col in required_columns):
            return ["No data available"] * 5 + [px.pie(), px.pie(), px.pie(), px.bar(), px.pie(), px.bar(), px.line()]

        # Fill missing 'Status' values with 'Unknown'
        df['Status'] = df['Status'].fillna('Unknown')

        # Standardize 'Status' column to lowercase to avoid case sensitivity issues
        df['Status'] = df['Status'].str.lower()

        # Convert 'Date' column to datetime if present
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')

        # Top statistics
        total_students = df.shape[0]
        top_nationality = df['Nationality'].value_counts().idxmax() if not df['Nationality'].isnull().all() else "N/A"
        top_program = df['Program'].value_counts().idxmax() if not df['Program'].isnull().all() else "N/A"
        top_status = df['Status'].value_counts().idxmax() if not df['Status'].isnull().all() else "N/A"
        total_paid = df['Status'].value_counts().get('paid', 0)
        performance = (total_paid / total_students) * 100 if total_students > 0 else 0
        performance_metric = f"{performance:.2f}%"

        # Pie chart for status distribution
        status_counts = df['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution", hole=0.4)

        # Pie chart for top nationality distribution
        top_nationality_counts = df['Nationality'].value_counts().reset_index()
        top_nationality_counts.columns = ['Nationality', 'Count']
        top_nationality_pie_chart = px.pie(top_nationality_counts.head(10), names='Nationality', values='Count',
                                           title="Top Nationalities", hole=0.4)

        # Pie chart for top paid countries distribution
        top_paid_countries = df[df['Status'] == 'paid']['Nationality'].value_counts().reset_index()
        top_paid_countries.columns = ['Country', 'Count']
        if not top_paid_countries.empty:
            top_paid_countries_pie_chart = px.pie(top_paid_countries.head(10), names='Country', values='Count',
                                                  title="Top Paid Countries", hole=0.4)
        else:
            top_paid_countries_pie_chart = px.pie(title="No Data Available")

            # Combined Region Chart (Top 6 Regions and Top 6 Paid Regions)
        if 'Region' in df.columns:
            regions_counts = df['Region'].value_counts().nlargest(6).reset_index()
            regions_counts.columns = ['Region', 'Applied']

            # Get the top 6 regions by count where Status is 'paid'
            paid_regions_counts = df.loc[df['Status'] == 'paid', 'Region'].value_counts().nlargest(6).reset_index()
            paid_regions_counts.columns = ['Region', 'Paid']

            # Merge the counts for applied and paid regions
            combined_regions = pd.merge(regions_counts, paid_regions_counts, on='Region', how='outer').fillna(0)

            # Create a bar chart
            combined_region_chart = px.bar(
                combined_regions,
                x='Region',
                y=['Applied', 'Paid'],
                barmode='group',
                title="Top 6 Regions Applied vs. Top 6 Paid Regions",
                labels={'value': 'Count', 'variable': 'Category'},
                text_auto=True
            )

        # Pie chart for top 10 programs applied
        applied_programs = df[df['Status'] == 'applied']['Program'].value_counts().reset_index()
        applied_programs.columns = ['Program', 'Count']
        if not applied_programs.empty:
            top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                                    title="Top 10 Programs Applied", hole=0.4)
        else:
            top_programs_applied_pie_chart = px.pie(title="No Data Available")

        # Bar chart for top 7 paid programs
        # Bar chart for top 7 paid programs
        paid_programs = df[df['Status'] == 'paid'].groupby('Program').size().reset_index(name='Count')
        if not paid_programs.empty:
            top_7_paid_programs = paid_programs.nlargest(7, 'Count')
            top_programs_paid_bar_chart = px.bar(
                top_7_paid_programs,
                x='Program',
                y='Count',
                title="Top 7 Programs Paid",
                color='Program',
                text='Count'  # Display the count value inside each bar
            )

            # Customize the layout to remove the legend and adjust text positioning
            top_programs_paid_bar_chart.update_layout(
                showlegend=False,  # Hide the legend
                xaxis=dict(
                    title=None,  # Remove x-axis title
                    showticklabels=False,  # Hide x-axis tick labels to focus on internal labels
                ),
                yaxis=dict(
                    title=None,  # Remove y-axis title
                    showgrid=False,  # Remove y-axis grid lines
                    zeroline=False  # Remove y-axis zero line
                ),
                title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
                template="plotly_white"  # Use a clean template
            )

            # Set text to appear inside the bars and display both program and count
            top_programs_paid_bar_chart.update_traces(
                texttemplate='%{x}<br>%{text}',  # Show program name and count on a new line
                textposition='inside',  # Position text inside the bars
                textfont=dict(size=16, color='black')  # Adjust text font size and color
            )
        else:
            top_programs_paid_bar_chart = px.bar(title="No Data Available")

        # Line chart for total students over months
        if 'Date' in df.columns and df['Date'].notnull().any():
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.strftime('%b')

            # Ensure all months are included even if no data (set missing values to 0)
            month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            all_months_df = pd.DataFrame({'Month': month_order})

            # Group by Year and Month
            month_counts = df.groupby(['Year', 'Month']).size().reset_index(name='Total Students')

            # Merge with all months to fill missing months with 0
            month_counts = pd.merge(all_months_df, month_counts, on='Month', how='left')
            month_counts['Total Students'].fillna(0, inplace=True)

            # Create line chart
            performance_month_chart = px.line(
                month_counts,
                x='Month',
                y='Total Students',
                color='Year',
                title="Total Number of Students Over Months",
                markers=True,
                line_shape='linear'
            )

            performance_month_chart.update_traces(
                mode='lines+markers',
                line=dict(width=3),
                marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')),
            )

            performance_month_chart.update_layout(
                xaxis_title="Month",
                yaxis_title="Total Number of Students",
                xaxis={'categoryorder': 'array', 'categoryarray': month_order},
                template='plotly_white',
                showlegend=True
            )
        else:
            performance_month_chart = px.line(title="No Data Available")

        # Return all necessary outputs
        return (total_students, total_paid, top_nationality, top_program, top_status, performance_metric, pie_chart,
                top_nationality_pie_chart, top_paid_countries_pie_chart, combined_region_chart,
                top_programs_applied_pie_chart, performance_month_chart, top_programs_paid_bar_chart)


# Initialize the Dash app and register callbacks
app = Dash(__name__)
app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)

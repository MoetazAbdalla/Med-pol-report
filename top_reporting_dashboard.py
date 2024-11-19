from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the Excel file and get all sheet names (each sheet represents an agent)
excel_file = 'assets/application-list-edited.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Initialize the Dash app
app = Dash(__name__)
server = app.server

# Dashboard Layout with Tabs
layout = html.Div([
    html.Div([
        html.H1('Istanbul MediPol University Top-Reporting Dashboard',
                style={'textAlign': 'center', 'color': '#007BFF'}),

        # Tiles for metrics in a responsive grid
        html.Div([

            html.Div([  # Total Students
                html.H4('Total Students'),
                html.H2(id='total-students-updated', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Total Payments
                html.H4('Total Payments'),
                html.H2(id='total-payments-updated', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Nationality
                html.H4('Top Nationality'),
                html.H2(id='top-nationality-updated', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Top Status
                html.H4('Top Status'),
                html.H2(id='top-status-updated', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

            html.Div([  # Performance
                html.H4('Performance'),
                html.H2(id='performance-metric-updated', className='metric-text'),
            ], className='col-lg-2 col-md-4 col-sm-6 mb-4 tile'),

        ], className="row justify-content-center"),  # Center the row

        # Dropdown menu
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='agent-dropdown-updated',
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

                        html.Div([dcc.Graph(id='status-pie-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-nationality-pie-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-paid-countries-pie-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-4 col-md-6 col-sm-12 mb-4 chart-container'),

                    ], className="row"),

                    # Row for top regions and performance line chart
                    html.Div([

                        html.Div([dcc.Graph(id='top-regions-bar-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='performance-month-line-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),

                    ], className="row"),

                    # Pie charts for top 10 programs applied and total paid for top 10 programs
                    html.Div([

                        html.Div([dcc.Graph(id='top-programs-applied-pie-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),
                        html.Div([dcc.Graph(id='top-programs-paid-pie-chart-updated', config={'displayModeBar': False})],
                                 className='col-lg-6 col-md-12 mb-4 chart-container'),

                    ], className="row"),

                    # New row for top 10 paid agents bar chart and top paid regions pie chart
                    html.Div([
                        html.Div([
                            dcc.Graph(id='top-paid-agents-bar-chart-updated', config={'displayModeBar': False}),
                        ], className='col-lg-6 col-md-12 mb-4 chart-container'),

                        html.Div([
                            dcc.Graph(id='top-paid-regions-pie-chart-updated', config={'displayModeBar': False}),
                        ], className='col-lg-6 col-md-12 mb-4 chart-container'),

                    ], className="row"),

                    # Add line chart for top agent performance ratio
                    html.Div([
                        dcc.Graph(id='top-agent-performance-ratio-line-chart-updated', config={'displayModeBar': False}),
                    ], className='col-lg-12 col-md-12 mb-4 chart-container'),  # Full-width for line chart

                ], className="container-fluid")
            ]),
        ], className="tabs-container")
    ], className='main-container'),
])

# Callbacks to update the dashboard based on selected sheet (agent)
def register_callbacks(app):
    @app.callback(
        [Output('total-students-updated', 'children'),
         Output('total-payments-updated', 'children'),
         Output('top-nationality-updated', 'children'),
         Output('top-status-updated', 'children'),
         Output('performance-metric-updated', 'children'),
         Output('status-pie-chart-updated', 'figure'),
         Output('top-nationality-pie-chart-updated', 'figure'),
         Output('top-paid-countries-pie-chart-updated', 'figure'),
         Output('top-regions-bar-chart-updated', 'figure'),
         Output('performance-month-line-chart-updated', 'figure'),
         Output('top-programs-applied-pie-chart-updated', 'figure'),
         Output('top-paid-agents-bar-chart-updated', 'figure'),
         Output('top-paid-regions-pie-chart-updated', 'figure'),
         Output('top-agent-performance-ratio-line-chart-updated', 'figure'),
         Output('top-programs-paid-pie-chart-updated', 'figure')],
        [Input('agent-dropdown-updated', 'value')]
    )
    def update_dashboard(selected_sheet):
        # Load the data
        try:
            df = pd.read_excel(excel_file, sheet_name=selected_sheet)
            print(f"Loaded data for sheet: {selected_sheet}")
            print(df.head())
        except Exception as e:
            print(f"Error loading sheet {selected_sheet}: {e}")
            return ["Error"] * 15  # Updated to match the number of outputs

        # Check if DataFrame is empty
        if df.empty:
            print("DataFrame is empty.")
            return ["No data"] * 15

        # Ensure necessary columns exist and handle missing data
        required_columns = ['Status', 'Nationality', 'Program', 'Region', 'Date', 'Created By']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return ["Missing data"] * 15

        # Standardize 'Status' column to lowercase
        df['Status'] = df['Status'].str.lower()

        # Fill missing 'Created By' values
        df['Created By'] = df['Created By'].fillna('Unknown')

        # Top statistics
        total_students = df.shape[0]
        top_nationality = df['Nationality'].value_counts().idxmax() if 'Nationality' in df.columns else "N/A"
        top_status = df['Status'].value_counts().idxmax() if 'Status' in df.columns else "N/A"
        total_paid = df['Status'].value_counts().get('paid', 0)
        performance = (total_paid / total_students) * 100 if total_students > 0 else 0
        performance_metric = f"{performance:.2f}%"

        # Pie chart for status distribution
        status_counts = df['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        pie_chart = px.pie(status_counts, names='Status', values='Count', title="Status Distribution (paid vs applied)", hole=0.4)

        # Pie chart for top nationality distribution
        top_nationality_counts = df['Nationality'].value_counts().reset_index()
        top_nationality_counts.columns = ['Nationality', 'Count']
        top_nationality_pie_chart = px.pie(top_nationality_counts.head(15), names='Nationality', values='Count',
                                           title="Top Nationalities Applied", hole=0.4)

        # Pie chart for top paid countries distribution
        top_paid_countries = df[df['Status'] == 'paid']['Nationality'].value_counts().reset_index()
        top_paid_countries.columns = ['Country', 'Count']
        top_paid_countries_pie_chart = px.pie(top_paid_countries.head(15), names='Country', values='Count',
                                              title="Top Paid Countries", hole=0.4)

        # Ensure 'Region' and 'Status' columns are present
        if 'Region' in df.columns and 'Status' in df.columns:
            # Get the overall count for each region, regardless of status
            total_region_counts = df['Region'].value_counts().nlargest(6).reset_index()  # Get top 8 regions
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
                title="Top 6 Regions by Total Applications and Total Paid",
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

        # Line chart for performance over months
        if 'Date' in df.columns and df['Date'].notnull().any():
            df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')
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
            performance_month_chart = {}

        # Pie chart for top 10 programs applied
        applied_programs = df[df['Status'] == 'applied']['Program'].value_counts().reset_index()
        applied_programs.columns = ['Program', 'Count']
        if not applied_programs.empty:
            top_programs_applied_pie_chart = px.pie(applied_programs.head(10), names='Program', values='Count',
                                                    title="Top 10 Programs Applied", hole=0.4)
        else:
            top_programs_applied_pie_chart = px.pie(title="No Data Available")

        # Pie chart for top 7 paid programs
        paid_programs = df[df['Status'] == 'paid']['Program'].value_counts().reset_index()
        paid_programs.columns = ['Program', 'Count']
        top_7_paid_programs = paid_programs.nlargest(7, 'Count')
        if not top_7_paid_programs.empty:
            top_programs_paid_bar_chart = px.bar(top_7_paid_programs, x='Program', y='Count',
                                                 title="Total Paid for Top 7 Programs", color='Program', text='Count')
        else:
            top_programs_paid_bar_chart = px.bar(title="No Data Available")

        # Logic for the top 10 paid agents based on paid applications
        if 'Created By' in df.columns and 'Status' in df.columns:
            # Filter for paid applications
            paid_df = df[df['Status'] == 'paid']

            # Group by 'Created By' and count the number of paid applications
            paid_agent_counts = paid_df['Created By'].value_counts().reset_index()
            paid_agent_counts.columns = ['Agent', 'Paid Applications']

            # Get top 10 agents by paid applications
            top_10_paid_agents = paid_agent_counts.head(10)

            if not top_10_paid_agents.empty:
                # Create a bar chart for the top 10 paid agents
                top_paid_agents_bar_chart = px.bar(
                    top_10_paid_agents,
                    x='Agent',
                    y='Paid Applications',
                    title="Top 10 Paid Agents by Number of Paid Applications",
                    text='Paid Applications',
                    color='Agent'  # Optional: Add color for better visualization
                )

                # Update layout for consistency
                top_paid_agents_bar_chart.update_traces(textposition='auto')
                top_paid_agents_bar_chart.update_layout(
                    xaxis_title="Agent",
                    yaxis_title="Number of Paid Applications",
                    title_x=0.5,
                    height=400,
                    template="plotly_white",
                    showlegend=False
                )
            else:
                top_paid_agents_bar_chart = px.bar(title="No Paid Applications Found")
        else:
            top_paid_agents_bar_chart = px.bar(title="No Data Available")

        # Pie chart for top paid regions distribution
        top_paid_regions = df[df['Status'] == 'paid']['Region'].value_counts().reset_index()
        top_paid_regions.columns = ['Region', 'Count']
        if not top_paid_regions.empty:
            top_paid_regions_pie_chart = px.pie(top_paid_regions.head(10), names='Region', values='Count',
                                                title="Top Paid Regions", hole=0.4)
        else:
            top_paid_regions_pie_chart = px.pie(title="No Data Available")

        # Line chart for top agent performance ratio (Paid/Total Applications)
        if 'Created By' in df.columns and 'Status' in df.columns:
            # Total applications per agent
            total_applications_by_agent = df['Created By'].value_counts().reset_index()
            total_applications_by_agent.columns = ['Agent', 'Total Applications']

            # Paid applications per agent
            paid_applications_by_agent = df[df['Status'] == 'paid']['Created By'].value_counts().reset_index()
            paid_applications_by_agent.columns = ['Agent', 'Paid Applications']

            # Merge data and calculate performance ratio
            agent_performance_df = pd.merge(total_applications_by_agent, paid_applications_by_agent, on='Agent',
                                            how='left')
            agent_performance_df['Paid Applications'].fillna(0, inplace=True)
            agent_performance_df['Performance Ratio'] = (agent_performance_df['Paid Applications'] /
                                                         agent_performance_df['Total Applications']) * 100

            # Sort by Total Applications and select top 20 agents
            top_20_agents_df = agent_performance_df.nlargest(20, 'Total Applications')

            # Sort by Performance Ratio (from highest to lowest)
            top_20_agents_df = top_20_agents_df.sort_values(by='Performance Ratio', ascending=False)

            if not top_20_agents_df.empty:
                # Create the line chart for performance ratio with percentage
                top_agent_performance_ratio_chart = px.line(
                    top_20_agents_df,
                    x='Agent',
                    y='Performance Ratio',
                    title='Top 20 Agent Applications and Performance Ratios (Paid/Total)',
                    markers=True,
                    text=top_20_agents_df['Performance Ratio'].apply(lambda x: f'{x:.2f}%')  # Display percentage as text
                )

                # Customize chart appearance
                top_agent_performance_ratio_chart.update_traces(
                    mode='lines+markers+text',  # Show text above markers
                    line=dict(width=2),
                    marker=dict(size=6),  # Reduce marker size for better visibility
                    textposition='bottom center',  # Move text below markers to avoid overlap
                    textfont=dict(size=9)  # Reduce text size for better visibility
                )

                # Customize x-axis labels to avoid crowding and improve visibility
                top_agent_performance_ratio_chart.update_layout(
                    height=600,  # Increase chart height for more space
                    xaxis_title="Agent",
                    yaxis_title="Performance Ratio (%)",
                    margin=dict(l=40, r=40, t=110, b=200),  # Increase bottom margin for better x-axis label spacing
                    xaxis_tickangle=-45,  # Adjust label rotation for better readability
                    xaxis=dict(tickfont=dict(size=9)),  # Reduce x-axis label font size for better spacing
                    showlegend=False
                )
            else:
                top_agent_performance_ratio_chart = px.line(title="No Data Available")
        else:
            top_agent_performance_ratio_chart = px.line(title="No Data Available")

            # Calculate total payments for top 10 agents
            if 'Created By' in df.columns and 'Status' in df.columns:
                total_payments_per_agent = df[df['Status'] == 'paid'].groupby('Created By').size().reset_index(
                    name='Total Payments')
                top_paid_agents = total_payments_per_agent.nlargest(10, 'Total Payments')
                top_paid_agents_bar_chart = px.bar(top_paid_agents, x='Created By', y='Total Payments',
                                                   title="Top Payments for Top 10 Agents", text='Total Payments')
            else:
                top_paid_agents_bar_chart = {}

        # Return all outputs including the updated top paid agents chart
        return (total_students, total_paid, top_nationality, top_status, performance_metric, pie_chart,
                top_nationality_pie_chart, top_paid_countries_pie_chart, combined_region_chart,
                performance_month_chart, top_programs_applied_pie_chart, top_paid_agents_bar_chart,
                top_paid_regions_pie_chart, top_agent_performance_ratio_chart, top_programs_paid_bar_chart)


# Initialize the Dash app and register callbacks
app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)

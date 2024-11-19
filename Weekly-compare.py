import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the Excel file
excel_file = 'assets/weekly-final-8-11 - compare.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dashboard Layout for comparing two weeks
layout = html.Div([
    html.H1('Istanbul MediPol University Weekly Reporting Dashboard',
            style={'textAlign': 'center', 'color': '#0056b3', 'padding': '10px'}),

    html.Div([
        # Week 1 Section
        html.Div([
            dcc.Dropdown(
                id='week-1-dropdown-Weekly',
                options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                value=sheet_names[0],  # Default value for Week 1
                className='custom-dropdown'
            ),
            html.Div([
                html.Div([html.H4('Total Students'), html.H2(id='total-students-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('Total Payments'), html.H2(id='total-payments-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('Top Program'), html.H2(id='top-program-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('Performance'), html.H2(id='performance-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('Start Date'), html.H2(id='min-date-week1-Weekly')], className='mb-2'),
                html.Div([html.H4('End Date'), html.H2(id='max-date-week1-Weekly')], className='mb-2')
            ], className='metrics-section'),
            html.Div([dcc.Graph(id='status-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-nationality-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-countries-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-regions-bar-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-agents-bar-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-regions-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-programs-applied-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-programs-paid-pie-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-agents-bar-chart-week1-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'})
        ], className='col-lg-6', style={'padding': '10px', 'flex': '1'}),  # Week 1 (left side)

        # Week 2 Section
        html.Div([
            dcc.Dropdown(
                id='week-2-dropdown-Weekly',
                options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                value=sheet_names[1] if len(sheet_names) > 1 else sheet_names[0],  # Default value for Week 2
                className='custom-dropdown'
            ),
            html.Div([
                html.Div([html.H4('Total Students'), html.H2(id='total-students-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('Total Payments'), html.H2(id='total-payments-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('Top Program'), html.H2(id='top-program-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('Performance'), html.H2(id='performance-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('Start Date'), html.H2(id='min-date-week2-Weekly')], className='mb-2'),
                html.Div([html.H4('End Date'), html.H2(id='max-date-week2-Weekly')], className='mb-2')
            ], className='metrics-section'),
            html.Div([dcc.Graph(id='status-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-nationality-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-countries-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-regions-bar-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-agents-bar-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-regions-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-programs-applied-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-programs-paid-pie-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'}),
            html.Div([dcc.Graph(id='top-paid-agents-bar-chart-week2-Weekly')], className='chart-container', style={'margin': '5px 0', 'padding': '0'})
        ], className='col-lg-6', style={'padding': '10px', 'flex': '1'})  # Week 2 (right side)
    ], className='row', style={'display': 'flex', 'justifyContent': 'space-between', 'gap': '10px'})  # Create a row with two columns
])


# Callback for Week 1
def register_callbacks(app):
    @app.callback(
        [Output('total-students-week1-Weekly', 'children'),
         Output('total-payments-week1-Weekly', 'children'),
         Output('top-nationality-week1-Weekly', 'children'),
         Output('top-program-week1-Weekly', 'children'),
         Output('performance-week1-Weekly', 'children'),
         Output('min-date-week1-Weekly', 'children'),
         Output('max-date-week1-Weekly', 'children'),
         Output('status-pie-chart-week1-Weekly', 'figure'),
         Output('top-nationality-pie-chart-week1-Weekly', 'figure'),
         Output('top-paid-countries-pie-chart-week1-Weekly', 'figure'),
         Output('top-regions-bar-chart-week1-Weekly', 'figure'),
         Output('top-agents-bar-chart-week1-Weekly', 'figure'),
         Output('top-paid-regions-pie-chart-week1-Weekly', 'figure'),
         Output('top-programs-applied-pie-chart-week1-Weekly', 'figure'),
         Output('top-programs-paid-pie-chart-week1-Weekly', 'figure'),
         Output('top-paid-agents-bar-chart-week1-Weekly', 'figure')],
        [Input('week-1-dropdown-Weekly', 'value')]
    )
    def update_week1_dashboard(selected_sheet):
        df_week1 = pd.read_excel(excel_file, sheet_name=selected_sheet)
        df_week1.columns = df_week1.columns.str.strip()

        if df_week1.empty:
            return "No data", "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}

        df_week1['Status'] = df_week1['Status'].str.strip().str.lower()
        if 'Date' in df_week1.columns:
            df_week1['Date'] = pd.to_datetime(df_week1['Date'], format='%d.%m.%Y', errors='coerce')

        total_students = df_week1.shape[0]
        total_paid = df_week1['Status'].value_counts().get('paid', 0) if 'Status' in df_week1.columns else 0
        top_nationality = df_week1['Nationality'].value_counts().idxmax() if 'Nationality' in df_week1.columns else "N/A"
        top_program = df_week1['Program'].value_counts().idxmax() if 'Program' in df_week1.columns else "N/A"
        performance = f"{(total_paid / total_students) * 100:.2f}%" if total_students > 0 else "0%"
        min_date = df_week1['Date'].min().strftime('%d.%m.%Y') if 'Date' in df_week1.columns and not df_week1[
            'Date'].isna().all() else "N/A"
        max_date = df_week1['Date'].max().strftime('%d.%m.%Y') if 'Date' in df_week1.columns and not df_week1[
            'Date'].isna().all() else "N/A"

        status_counts = df_week1['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'count']
        status_pie_chart = px.pie(status_counts, names='Status', values='count', title="Status Distribution(paid vs applied)")

        nationality_counts = df_week1['Nationality'].value_counts().nlargest(10).reset_index()
        nationality_counts.columns = ['Nationality', 'count']
        nationality_pie_chart = px.pie(nationality_counts, names='Nationality', values='count',
                                       title="Top 10 Nationalities Applied")

        paid_countries_counts = df_week1[df_week1['Status'] == 'paid']['Nationality'].value_counts().nlargest(
            10).reset_index()
        paid_countries_counts.columns = ['Nationality', 'count']
        paid_countries_pie_chart = px.pie(paid_countries_counts, names='Nationality', values='count',
                                          title="Top 10 Paid Countries")

        # Ensure 'Region' and 'Status' columns are present
        if 'Region' in df_week1.columns and 'Status' in df_week1.columns:
            # Get the overall count for each region, regardless of status
            total_region_counts = df_week1['Region'].value_counts().nlargest(5).reset_index()  # Get top 5 regions
            total_region_counts.columns = ['Region', 'Total']

            # Filter the original dataframe for the top regions identified
            top_regions = total_region_counts['Region'].tolist()
            filtered_df = df_week1[df_week1['Region'].isin(top_regions)]

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
                title="Top 5 Regions by Total Applications and Total Paid",
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

        agents_counts = df_week1['Created By'].value_counts().nlargest(10).reset_index()
        agents_counts.columns = ['Agent', 'count']
        agents_bar_chart = px.bar(agents_counts, x='Agent', y='count', title="Top 10 Agents",
                                   text='count')

        paid_regions_counts = df_week1[df_week1['Status'] == 'paid']['Region'].value_counts().nlargest(10).reset_index()
        paid_regions_counts.columns = ['Region', 'count']
        paid_regions_pie_chart = px.pie(paid_regions_counts, names='Region', values='count',
                                        title="Top 10 Paid Regions")

        programs_applied_counts = df_week1[df_week1['Status'] == 'applied']['Program'].value_counts().nlargest(
            10).reset_index()
        programs_applied_counts.columns = ['Program', 'count']
        if programs_applied_counts.empty:
            programs_applied_pie_chart = {
                "data": [],
                "layout": {
                    "title": "No data available for Top Programs Applied"
                }
            }
        else:
            programs_applied_pie_chart = px.pie(programs_applied_counts, names='Program', values='count',
                                                title="Top 10 Programs Applied")

        programs_paid_counts = df_week1[df_week1['Status'] == 'paid']['Program'].value_counts().nlargest(10).reset_index()
        programs_paid_counts.columns = ['Program', 'count']
        programs_paid_bar_chart = px.bar(programs_paid_counts, x='Program', y='count', title="Top 10 Programs Paid",
                                         text='count')

        paid_agents_counts = df_week1[df_week1['Status'] == 'paid']['Created By'].value_counts().nlargest(10).reset_index()
        paid_agents_counts.columns = ['Agent', 'count']
        paid_agents_bar_chart = px.bar(paid_agents_counts, x='Agent', y='count', title="Top 10 Paid Agents",
                                       text='count')

        return (total_students, total_paid, top_nationality, top_program, performance, min_date, max_date, status_pie_chart,
                nationality_pie_chart, paid_countries_pie_chart, combined_region_chart, agents_bar_chart,
                paid_regions_pie_chart, programs_applied_pie_chart, programs_paid_bar_chart, paid_agents_bar_chart)


# Callback for Week 2 (similar to Week 1)
    @app.callback(
        [Output('total-students-week2-Weekly', 'children'),
         Output('total-payments-week2-Weekly', 'children'),
         Output('top-nationality-week2-Weekly', 'children'),
         Output('top-program-week2-Weekly', 'children'),
         Output('performance-week2-Weekly', 'children'),
         Output('min-date-week2-Weekly', 'children'),
         Output('max-date-week2-Weekly', 'children'),
         Output('status-pie-chart-week2-Weekly', 'figure'),
         Output('top-nationality-pie-chart-week2-Weekly', 'figure'),
         Output('top-paid-countries-pie-chart-week2-Weekly', 'figure'),
         Output('top-regions-bar-chart-week2-Weekly', 'figure'),
         Output('top-agents-bar-chart-week2-Weekly', 'figure'),
         Output('top-paid-regions-pie-chart-week2-Weekly', 'figure'),
         Output('top-programs-applied-pie-chart-week2-Weekly', 'figure'),
         Output('top-programs-paid-pie-chart-week2-Weekly', 'figure'),
         Output('top-paid-agents-bar-chart-week2-Weekly', 'figure')],
        [Input('week-2-dropdown-Weekly', 'value')]
    )
    def update_week2_dashboard(selected_sheet):
        df_week2 = pd.read_excel(excel_file, sheet_name=selected_sheet)
        df_week2.columns = df_week2.columns.str.strip()

        if df_week2.empty:
            return "No data", "No data", "No data", "No data", "No data", "No data", "No data", {}, {}, {}, {}, {}, {}, {}, {}, {}

        df_week2['Status'] = df_week2['Status'].str.strip().str.lower()
        if 'Date' in df_week2.columns:
            df_week2['Date'] = pd.to_datetime(df_week2['Date'], format='%d.%m.%Y', errors='coerce')

        total_students = df_week2.shape[0]
        total_paid = df_week2['Status'].value_counts().get('paid', 0) if 'Status' in df_week2.columns else 0
        top_nationality = df_week2['Nationality'].value_counts().idxmax() if 'Nationality' in df_week2.columns else "N/A"
        top_program = df_week2['Program'].value_counts().idxmax() if 'Program' in df_week2.columns else "N/A"
        performance = f"{(total_paid / total_students) * 100:.2f}%" if total_students > 0 else "0%"
        min_date = df_week2['Date'].min().strftime('%d.%m.%Y') if 'Date' in df_week2.columns and not df_week2[
            'Date'].isna().all() else "N/A"
        max_date = df_week2['Date'].max().strftime('%d.%m.%Y') if 'Date' in df_week2.columns and not df_week2[
            'Date'].isna().all() else "N/A"

        status_counts = df_week2['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'count']
        status_pie_chart = px.pie(status_counts, names='Status', values='count', title="Status Distribution (paid vs applied)")

        nationality_counts = df_week2['Nationality'].value_counts().nlargest(10).reset_index()
        nationality_counts.columns = ['Nationality', 'count']
        nationality_pie_chart = px.pie(nationality_counts, names='Nationality', values='count',
                                       title="Top 10 Nationalities Applied")

        paid_countries_counts = df_week2[df_week2['Status'] == 'paid']['Nationality'].value_counts().nlargest(
            10).reset_index()
        paid_countries_counts.columns = ['Nationality', 'count']
        paid_countries_pie_chart = px.pie(paid_countries_counts, names='Nationality', values='count',
                                          title="Top 10 Paid Countries")

        # Ensure 'Region' and 'Status' columns are present
        if 'Region' in df_week2.columns and 'Status' in df_week2.columns:
            # Get the overall count for each region, regardless of status
            total_region_counts = df_week2['Region'].value_counts().nlargest(5).reset_index()  # Get top 5 regions
            total_region_counts.columns = ['Region', 'Total']

            # Filter the original dataframe for the top regions identified
            top_regions = total_region_counts['Region'].tolist()
            filtered_df = df_week2[df_week2['Region'].isin(top_regions)]

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
                title="Top 5 Regions by Total Applications and Total Paid",
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

        agents_counts = df_week2['Created By'].value_counts().nlargest(10).reset_index()
        agents_counts.columns = ['Agent', 'count']
        agents_bar_chart = px.bar(agents_counts, x='Agent', y='count', title="Top 10 Agents",
                                  text='count')
        paid_regions_counts = df_week2[df_week2['Status'] == 'paid']['Region'].value_counts().nlargest(10).reset_index()
        paid_regions_counts.columns = ['Region', 'count']
        paid_regions_pie_chart = px.pie(paid_regions_counts, names='Region', values='count',
                                        title="Top 10 Paid Regions ")

        programs_applied_counts = df_week2[df_week2['Status'] == 'applied']['Program'].value_counts().nlargest(
            10).reset_index()
        programs_applied_counts.columns = ['Program', 'count']
        if programs_applied_counts.empty:
            programs_applied_pie_chart = {
                "data": [],
                "layout": {
                    "title": "No data available for Top Programs Applied"
                }
            }
        else:
            programs_applied_pie_chart = px.pie(programs_applied_counts, names='Program', values='count',
                                                title="Top 10 Programs Applied")

        programs_paid_counts = df_week2[df_week2['Status'] == 'paid']['Program'].value_counts().nlargest(10).reset_index()
        programs_paid_counts.columns = ['Program', 'count']
        programs_paid_bar_chart = px.bar(programs_paid_counts, x='Program', y='count', title="Top 10 Programs Paid",
                                         text='count')

        paid_agents_counts = df_week2[df_week2['Status'] == 'paid']['Created By'].value_counts().nlargest(10).reset_index()
        paid_agents_counts.columns = ['Agent', 'count']
        paid_agents_bar_chart = px.bar(paid_agents_counts, x='Agent', y='count', title="Top 10 Paid Agents  ",
                                       text='count')
        return (total_students, total_paid, top_nationality, top_program, performance, min_date, max_date, status_pie_chart,
                nationality_pie_chart, paid_countries_pie_chart, combined_region_chart, agents_bar_chart,
                paid_regions_pie_chart, programs_applied_pie_chart, programs_paid_bar_chart, paid_agents_bar_chart)


# Register callbacks
register_callbacks(app)

# Set app layout
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

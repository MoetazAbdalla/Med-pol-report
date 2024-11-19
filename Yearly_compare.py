import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the Excel file
excel_file = 'assets/2020-2025_Data.xlsx'
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Include Bootstrap CSS as an external stylesheet for styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dashboard Layout for comparing two weeks
layout = html.Div([
    html.Div([
        html.H1(
            'Istanbul MediPol University Yearly Reporting Dashboard',
            style={'textAlign': 'center', 'color': '#0056b3', 'padding': 20}
        ),

        # Week 1 Section
        html.Div([
            html.H3(''),
            dcc.Dropdown(
                id='week-1-dropdown',
                options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                value=sheet_names[0],  # Default value for Week 1
                className='custom-dropdown'
            ),
            html.Div([
                html.Div([html.H4('Total Students'), html.H2(id='total-students-week1')], className='mb-2'),
                html.Div([html.H4('Total Payments'), html.H2(id='total-payments-week1')], className='mb-2'),
                html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-week1')], className='mb-2'),
                html.Div([html.H4('Top Program'), html.H2(id='top-program-week1')], className='mb-2'),
                html.Div([html.H4('Performance'), html.H2(id='performance-week1')], className='mb-2'),
                html.Div([html.H4('Start Date'), html.H2(id='min-date-week1')], className='mb-2'),
                html.Div([html.H4('End Date'), html.H2(id='max-date-week1')], className='mb-2')
            ], className='metrics-section'),
            html.Div([dcc.Graph(id='status-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-nationality-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-countries-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='combined-region-bar-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='combined-agents-bar-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-programs-applied-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-programs-paid-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-english-programs-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-turkish-programs-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-applied-english-programs-pie-chart-week1')], className='chart-container'),
            html.Div([dcc.Graph(id='top-applied-turkish-programs-pie-chart-week1')], className='chart-container'),
        ], className='col-lg-6'),

        # Week 2 Section
        html.Div([
            html.H3(''),
            dcc.Dropdown(
                id='week-2-dropdown',
                options=[{'label': sheet, 'value': sheet} for sheet in sheet_names],
                value=sheet_names[1] if len(sheet_names) > 1 else sheet_names[0],
                className='custom-dropdown'
            ),
            html.Div([
                html.Div([html.H4('Total Students'), html.H2(id='total-students-week2')], className='mb-2'),
                html.Div([html.H4('Total Payments'), html.H2(id='total-payments-week2')], className='mb-2'),
                html.Div([html.H4('Top Nationality'), html.H2(id='top-nationality-week2')], className='mb-2'),
                html.Div([html.H4('Top Program'), html.H2(id='top-program-week2')], className='mb-2'),
                html.Div([html.H4('Performance'), html.H2(id='performance-week2')], className='mb-2'),
                html.Div([html.H4('Start Date'), html.H2(id='min-date-week2')], className='mb-2'),
                html.Div([html.H4('End Date'), html.H2(id='max-date-week2')], className='mb-2')
            ], className='metrics-section'),
            html.Div([dcc.Graph(id='status-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-nationality-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-countries-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='combined-region-bar-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='combined-agents-bar-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-programs-applied-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-programs-paid-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-english-programs-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-paid-turkish-programs-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-applied-english-programs-pie-chart-week2')], className='chart-container'),
            html.Div([dcc.Graph(id='top-applied-turkish-programs-pie-chart-week2')], className='chart-container')
        ], className='col-lg-6')
    ], className='row'),

    # Section for new and removed nationalities comparison
    html.Div([
        html.H3('Nationalities Comparison between Selection 1 and Selection 2'),

        # Section for nationalities removed in Selection 2
        html.Div([
            html.H4('Removed Nationalities in Selection 2'),
            html.P("Total Applications: ", style={'font-weight': 'bold'}),
            html.Div(id='total-removed-applications', className='total-count', style={'margin-bottom': '10px'}),

            html.Table(id='removed-nationalities-list', className='table table-striped',
                       style={'width': '100%', 'margin-bottom': '20px', 'font-weight': 'bold'}),
        ], className='chart-container',
            style={'padding': '20px', 'border': '1px solid #ddd', 'border-radius': '5px', 'margin': '10px 0'}),

        # Section for new nationalities in Selection 2
        html.Div([
            html.H4('New Nationalities in Selection 2'),
            html.P("Total New Applications: ", style={'font-weight': 'bold'}),
            html.Div(id='total-new-applications', className='total-count', style={'margin-bottom': '10px'}),

            html.Table(id='new-nationalities-list', className='table table-striped',
                       style={'width': '100%', 'margin-bottom': '20px', 'font-weight': 'bold'}),
        ], className='chart-container',
            style={'padding': '20px', 'border': '1px solid #ddd', 'border-radius': '5px', 'margin': '10px 0'}),
    ])
])


# Callback for Week 1
def register_callbacks(app):
    @app.callback(
        [Output('total-students-week1', 'children'),
         Output('total-payments-week1', 'children'),
         Output('top-nationality-week1', 'children'),
         Output('top-program-week1', 'children'),
         Output('performance-week1', 'children'),
         Output('min-date-week1', 'children'),
         Output('max-date-week1', 'children'),
         Output('status-pie-chart-week1', 'figure'),
         Output('top-nationality-pie-chart-week1', 'figure'),
         Output('top-paid-countries-pie-chart-week1', 'figure'),
         Output('combined-region-bar-chart-week1', 'figure'),
         Output('combined-agents-bar-chart-week1', 'figure'),  # Combined chart for applied and paid agents
         Output('top-programs-applied-pie-chart-week1', 'figure'),
         Output('top-programs-paid-pie-chart-week1', 'figure'),
         Output('top-paid-english-programs-pie-chart-week1', 'figure'),
         Output('top-paid-turkish-programs-pie-chart-week1', 'figure'),
         Output('top-applied-english-programs-pie-chart-week1', 'figure'),
         Output('top-applied-turkish-programs-pie-chart-week1', 'figure')],
        [Input('week-1-dropdown', 'value')]
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
        top_nationality = df_week1[
            'Nationality'].value_counts().idxmax() if 'Nationality' in df_week1.columns else "N/A"
        top_program = df_week1['Program'].value_counts().idxmax() if 'Program' in df_week1.columns else "N/A"
        performance = f"{(total_paid / total_students) * 100:.2f}%" if total_students > 0 else "0%"
        min_date = df_week1['Date'].min().strftime('%d.%m.%Y') if 'Date' in df_week1.columns and not df_week1[
            'Date'].isna().all() else "N/A"
        max_date = df_week1['Date'].max().strftime('%d.%m.%Y') if 'Date' in df_week1.columns and not df_week1[
            'Date'].isna().all() else "N/A"

        status_counts = df_week1['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'count']
        status_pie_chart = px.pie(status_counts, names='Status', values='count',
                                  title="Status Distribution (paid/Applied)")

        nationality_counts = df_week1['Nationality'].value_counts().nlargest(10).reset_index()
        nationality_counts.columns = ['Nationality', 'count']
        nationality_pie_chart = px.pie(nationality_counts, names='Nationality', values='count',
                                       title="Top 10 Nationalities Applications ")

        paid_countries_counts = df_week1[df_week1['Status'] == 'paid']['Nationality'].value_counts().nlargest(
            10).reset_index()
        paid_countries_counts.columns = ['Nationality', 'count']
        paid_countries_pie_chart = px.pie(paid_countries_counts, names='Nationality', values='count',
                                          title="Top 10 Paid Countries")

        # Combined Region Chart (Top 6 Regions and Top 6 Paid Regions)
        # Get the top 6 regions by overall count
        regions_counts = df_week1['Region'].value_counts().nlargest(6).reset_index()
        regions_counts.columns = ['Region', 'Applied']

        # Get the top 6 regions by count where Status is 'paid'
        paid_regions_counts = df_week1.loc[df_week1['Status'] == 'paid', 'Region'].value_counts().nlargest(
            6).reset_index()
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
            text_auto=True  # Show numbers inside the bars
        )

        # Optional: Customize text size and color (if desired)
        combined_region_chart.update_traces(
            selector=dict(name="Applied"),
            textposition="inside",  # Inside for Applied
            textfont=dict(color="white")  # White text for contrast on blue bars
        )

        combined_region_chart.update_traces(
            selector=dict(name="Paid"),
            textposition="outside",  # Outside for Paid
            textfont=dict(color="black", size=16)  # Larger, darker text for visibility
        )

        # Calculate the top 10 agents for "Applied"
        applied_agents_counts = (
            df_week1[df_week1['Status'] == 'applied']['Created By']
            .value_counts()
            .nlargest(10)
            .reset_index()
        )
        applied_agents_counts.columns = ['Agent', 'Count']
        applied_agents_counts['Status'] = 'Applied'  # Add status label

        # Calculate the top 10 agents for "Paid"
        paid_agents_counts = (
            df_week1[df_week1['Status'] == 'paid']['Created By']
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
            textfont=dict(color="black", size=20)  # Larger, darker text for visibility
        )

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

        programs_paid_counts = df_week1[df_week1['Status'] == 'paid']['Program'].value_counts().nlargest(
            10).reset_index()
        programs_paid_counts.columns = ['Program', 'count']
        programs_paid_bar_chart = px.bar(programs_paid_counts, x='Program', y='count', title="Top 10 Programs Paid",
                                         text='count')

        # Generate new pie charts for top 10 paid English and Turkish programs
        paid_english_programs = df_week1[(df_week1['Status'] == 'paid') &
                                         (df_week1['Program'].str.contains(r'\(English\)', case=False, na=False))]
        paid_english_programs = paid_english_programs['Program'].value_counts().reset_index()
        paid_english_programs.columns = ['Program', 'Count']
        top_paid_english_programs_pie_chart = px.pie(
            paid_english_programs.head(10),
            names='Program',
            values='Count',
            title="Top 10 Paid English Programs",
            hole=0.4
        )

        paid_turkish_programs = df_week1[df_week1['Status'] == 'paid'][
            df_week1['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        paid_turkish_programs = paid_turkish_programs['Program'].value_counts().reset_index()
        paid_turkish_programs.columns = ['Program', 'Count']
        top_paid_turkish_programs_pie_chart = px.pie(paid_turkish_programs.head(10), names='Program', values='Count',
                                                     title="Top 10 Paid Turkish Programs", hole=0.4)

        applied_english_programs = df_week1[df_week1['Program'].str.contains(r'\(English\)', case=False, na=False)]
        applied_english_counts = applied_english_programs['Program'].value_counts().reset_index()
        applied_english_counts.columns = ['Program', 'Count']
        top_applied_english_programs_pie_chart = px.pie(applied_english_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied English Programs", hole=0.4)

        applied_turkish_programs = df_week1[df_week1['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        applied_turkish_counts = applied_turkish_programs['Program'].value_counts().reset_index()
        applied_turkish_counts.columns = ['Program', 'Count']
        top_applied_turkish_programs_pie_chart = px.pie(applied_turkish_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied Turkish Programs", hole=0.4)

        return (total_students, total_paid, top_nationality, top_program, performance, min_date, max_date,
                status_pie_chart, nationality_pie_chart, paid_countries_pie_chart, combined_region_chart,
                combined_agents_chart, programs_applied_pie_chart, programs_paid_bar_chart,
                top_paid_english_programs_pie_chart, top_paid_turkish_programs_pie_chart,
                top_applied_english_programs_pie_chart, top_applied_turkish_programs_pie_chart)

    # Callback for Week 2 (similar to Week 1)
    @app.callback(
        [Output('total-students-week2', 'children'),
         Output('total-payments-week2', 'children'),
         Output('top-nationality-week2', 'children'),
         Output('top-program-week2', 'children'),
         Output('performance-week2', 'children'),
         Output('min-date-week2', 'children'),
         Output('max-date-week2', 'children'),
         Output('status-pie-chart-week2', 'figure'),
         Output('top-nationality-pie-chart-week2', 'figure'),
         Output('top-paid-countries-pie-chart-week2', 'figure'),
         Output('combined-region-bar-chart-week2', 'figure'),
         Output('combined-agents-bar-chart-week2', 'figure'),
         Output('top-programs-applied-pie-chart-week2', 'figure'),
         Output('top-programs-paid-pie-chart-week2', 'figure'),
         Output('top-paid-english-programs-pie-chart-week2', 'figure'),
         Output('top-paid-turkish-programs-pie-chart-week2', 'figure'),
         Output('top-applied-english-programs-pie-chart-week2', 'figure'),
         Output('top-applied-turkish-programs-pie-chart-week2', 'figure')],
        [Input('week-2-dropdown', 'value')]
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
        top_nationality = df_week2[
            'Nationality'].value_counts().idxmax() if 'Nationality' in df_week2.columns else "N/A"
        top_program = df_week2['Program'].value_counts().idxmax() if 'Program' in df_week2.columns else "N/A"
        performance = f"{(total_paid / total_students) * 100:.2f}%" if total_students > 0 else "0%"
        min_date = df_week2['Date'].min().strftime('%d.%m.%Y') if 'Date' in df_week2.columns and not df_week2[
            'Date'].isna().all() else "N/A"
        max_date = df_week2['Date'].max().strftime('%d.%m.%Y') if 'Date' in df_week2.columns and not df_week2[
            'Date'].isna().all() else "N/A"

        status_counts = df_week2['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'count']
        status_pie_chart = px.pie(status_counts, names='Status', values='count',
                                  title="Status Distribution (paid/Applied)")

        nationality_counts = df_week2['Nationality'].value_counts().nlargest(10).reset_index()
        nationality_counts.columns = ['Nationality', 'count']
        nationality_pie_chart = px.pie(nationality_counts, names='Nationality', values='count',
                                       title="Top 10 Nationalities Applications")

        paid_countries_counts = df_week2[df_week2['Status'] == 'paid']['Nationality'].value_counts().nlargest(
            10).reset_index()
        paid_countries_counts.columns = ['Nationality', 'count']
        paid_countries_pie_chart = px.pie(paid_countries_counts, names='Nationality', values='count',
                                          title="Top 10 Paid Countries")

        # Combined Region Chart (Top 6 Regions and Top 6 Paid Regions)
        # Get the top 6 regions by overall count
        regions_counts = df_week2['Region'].value_counts().nlargest(6).reset_index()
        regions_counts.columns = ['Region', 'Applied']

        # Get the top 6 regions by count where Status is 'paid'
        paid_regions_counts = df_week2.loc[df_week2['Status'] == 'paid', 'Region'].value_counts().nlargest(
            6).reset_index()
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
            text_auto=True  # Show numbers inside the bars
        )

        # Optional: Customize text size and color (if desired)
        combined_region_chart.update_traces(
            selector=dict(name="Applied"),
            textposition="inside",  # Inside for Applied
            textfont=dict(color="white")  # White text for contrast on blue bars
        )

        combined_region_chart.update_traces(
            selector=dict(name="Paid"),
            textposition="outside",  # Outside for Paid
            textfont=dict(color="black", size=16)  # Larger, darker text for visibility
        )
        # Calculate the top 10 agents for "Applied"
        applied_agents_counts = (
            df_week2[df_week2['Status'] == 'applied']['Created By']
            .value_counts()
            .nlargest(10)
            .reset_index()
        )
        applied_agents_counts.columns = ['Agent', 'Count']
        applied_agents_counts['Status'] = 'Applied'  # Add status label

        # Calculate the top 10 agents for "Paid"
        paid_agents_counts = (
            df_week2[df_week2['Status'] == 'paid']['Created By']
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
            textfont=dict(color="black", size=16)  # Larger, darker text for visibility
        )

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

        programs_paid_counts = df_week2[df_week2['Status'] == 'paid']['Program'].value_counts().nlargest(
            10).reset_index()
        programs_paid_counts.columns = ['Program', 'count']
        programs_paid_bar_chart = px.bar(programs_paid_counts, x='Program', y='count', title="Top 10 Programs Paid",
                                         text='count')

        # Generate new pie charts for top 10 paid English and Turkish programs
        paid_english_programs = df_week2[(df_week2['Status'] == 'paid') &
                                         (df_week2['Program'].str.contains(r'\(English\)', case=False, na=False))]
        paid_english_programs = paid_english_programs['Program'].value_counts().reset_index()
        paid_english_programs.columns = ['Program', 'Count']
        top_paid_english_programs_pie_chart = px.pie(
            paid_english_programs.head(10),
            names='Program',
            values='Count',
            title="Top 10 Paid English Programs",
            hole=0.4
        )

        paid_turkish_programs = df_week2[df_week2['Status'] == 'paid'][
            df_week2['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        paid_turkish_programs = paid_turkish_programs['Program'].value_counts().reset_index()
        paid_turkish_programs.columns = ['Program', 'Count']
        top_paid_turkish_programs_pie_chart = px.pie(paid_turkish_programs.head(10), names='Program', values='Count',
                                                     title="Top 10 Paid Turkish Programs", hole=0.4)

        applied_english_programs = df_week2[df_week2['Program'].str.contains(r'\(English\)', case=False, na=False)]
        applied_english_counts = applied_english_programs['Program'].value_counts().reset_index()
        applied_english_counts.columns = ['Program', 'Count']
        top_applied_english_programs_pie_chart = px.pie(applied_english_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied English Programs", hole=0.4)

        applied_turkish_programs = df_week2[df_week2['Program'].str.contains(r'\(Turkish\)', case=False, na=False)]
        applied_turkish_counts = applied_turkish_programs['Program'].value_counts().reset_index()
        applied_turkish_counts.columns = ['Program', 'Count']
        top_applied_turkish_programs_pie_chart = px.pie(applied_turkish_counts.head(10), names='Program',
                                                        values='Count',
                                                        title="Top 10 Applied Turkish Programs", hole=0.4)

        return (total_students, total_paid, top_nationality, top_program, performance, min_date, max_date,
                status_pie_chart, nationality_pie_chart, paid_countries_pie_chart, combined_region_chart,
                combined_agents_chart, programs_applied_pie_chart, programs_paid_bar_chart,
                top_paid_english_programs_pie_chart, top_paid_turkish_programs_pie_chart,
                top_applied_english_programs_pie_chart, top_applied_turkish_programs_pie_chart)

    # Callback to update new nationalities in Week 2 compared to Week 1
    @app.callback(
        [Output('new-nationalities-list', 'children'),
         Output('total-new-applications', 'children'),
         Output('removed-nationalities-list', 'children'),
         Output('total-removed-applications', 'children')],
        [Input('week-1-dropdown', 'value'),
         Input('week-2-dropdown', 'value')]
    )
    def update_new_nationalities(week1_sheet, week2_sheet):
        # Load data for both weeks
        df_week1 = pd.read_excel(excel_file, sheet_name=week1_sheet)
        df_week2 = pd.read_excel(excel_file, sheet_name=week2_sheet)

        # Clean column names and trim spaces
        df_week1.columns = df_week1.columns.str.strip()
        df_week2.columns = df_week2.columns.str.strip()

        # Get unique nationalities in each dataset
        nationalities_week1 = set(df_week1['Nationality'].dropna().unique())
        nationalities_week2 = set(df_week2['Nationality'].dropna().unique())

        # Find nationalities that are in Selection 1 but not in Selection 2
        removed_nationalities = nationalities_week1 - nationalities_week2
        removed_nationalities_df = df_week1[df_week1['Nationality'].isin(removed_nationalities)]
        removed_nationalities_counts = removed_nationalities_df['Nationality'].value_counts().reset_index()
        removed_nationalities_counts.columns = ['Nationality', 'Count']
        total_removed_applications = removed_nationalities_counts['Count'].sum()

        # Format removed nationalities into table rows
        removed_nationalities_rows = []
        for i in range(0, len(removed_nationalities_counts), 5):
            row_cells = [
                html.Td(f"{row['Nationality']}: {row['Count']}") for _, row in
                removed_nationalities_counts.iloc[i:i + 5].iterrows()
            ]
            removed_nationalities_rows.append(html.Tr(row_cells))
        # Add total row for removed nationalities
        removed_nationalities_rows.append(html.Tr([html.Td(f"Total Removed Applications: {total_removed_applications}",
                                                           colSpan=5, style={'font-weight': 'bold'})]))

        # Find nationalities that are in Selection 2 but not in Selection 1
        new_nationalities = nationalities_week2 - nationalities_week1
        new_nationalities_df = df_week2[df_week2['Nationality'].isin(new_nationalities)]
        new_nationalities_counts = new_nationalities_df['Nationality'].value_counts().reset_index()
        new_nationalities_counts.columns = ['Nationality', 'Count']
        total_new_applications = new_nationalities_counts['Count'].sum()

        # Format new nationalities into table rows
        new_nationalities_rows = []
        for i in range(0, len(new_nationalities_counts), 5):
            row_cells = [
                html.Td(f"{row['Nationality']}: {row['Count']}") for _, row in
                new_nationalities_counts.iloc[i:i + 5].iterrows()
            ]
            new_nationalities_rows.append(html.Tr(row_cells))
        # Add total row for new nationalities
        new_nationalities_rows.append(html.Tr(
            [html.Td(f"Total New Applications: {total_new_applications}", colSpan=5, style={'font-weight': 'bold'})]))

        # Return updated components
        return (
            new_nationalities_rows,  # New nationalities list as table rows
            f"Total New Applications: {total_new_applications}",  # Total new applications
            removed_nationalities_rows,  # Removed nationalities list as table rows
            f"Total Removed Applications: {total_removed_applications}"  # Total removed applications
        )

# Register callbacks
register_callbacks(app)

# Set app layout
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

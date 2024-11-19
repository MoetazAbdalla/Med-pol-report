from dash import dcc, html, Input, Output, dash
import importlib.util
import logging

# Initialize the Dash app with external stylesheets
external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)


# Set up logging to track errors and performance issues
logging.basicConfig(filename="app.log", level=logging.ERROR)

# Function for styling sidebar menu items
def sidebar_menu_style(active=False):
    return {
        'display': 'flex',
        'alignItems': 'center',
        'marginBottom': '20px',
        'color': '#FFFFFF' if active else '#B0BEC5',
        'fontSize': '18px',
        'fontWeight': '500',
        'padding': '10px 20px',
        'backgroundColor': '#1d4ed8' if active else '',
        'borderRadius': '5px',
        'textDecoration': 'none',
        'transition': 'all 0.3s ease',
        'cursor': 'pointer'
    }

# Sidebar with menu items
sidebar = html.Div(
    className="sidebar",
    style={
        'backgroundColor': '#263238',
        'width': '250px',
        'height': '100vh',
        'padding': '20px',
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'boxShadow': '3px 0 10px rgba(0, 0, 0, 0.2)',
        'borderRadius': '10px',
        'overflowY': 'auto'
    },
    children=[
        # Logo Section
        html.Div([
            html.Img(
                src='/assets/medipol-logo.png',
                style={
                    'height': '80px',
                    'width': '80px',
                    'borderRadius': '50%',
                    'border': '3px solid #fff',
                    'padding': '5px',
                    'backgroundColor': '#1d4ed8',
                    'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
                }
            ),
            html.H3("Medipol University", style={
                'color': '#FFFFFF',
                'textAlign': 'center',
                'fontSize': '18px',
                'marginTop': '10px',
                'textTransform': 'uppercase',
                'fontWeight': '600'
            })
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'width': '100%',
            'marginBottom': '30px'
        }),
        # Sidebar Menu Items
        html.Div(className="menu", style={'width': '100%'}, children=[
            html.H4("Reporting", style={
                'color': '#FFFFFF',
                'margin': '20px 0 10px',
                'padding': '10px 20px',
                'fontSize': '23px',
                'fontWeight': 'bold'
            }),
            html.A([html.I(className="fas fa-university", style={'marginRight': '10px'}), "University Report"],
                   href="/university-report", style=sidebar_menu_style()),
            html.A([html.I(className="fas fa-calendar-week", style={'marginRight': '10px'}), "Weekly Report"],
                   href="/weekly-report", style=sidebar_menu_style()),
            html.A([html.I(className="fas fa-signal", style={'marginRight': '10px'}), "Individual Agent"],
                   href="/signal-agent", style=sidebar_menu_style()),
            html.A([html.I(className="fas fa-chart-line", style={'marginRight': '10px'}), "Top Reporting Dashboard"],
                   href="/top-reporting-dashboard", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-star", style={'marginRight': '10px'}), "CL1 Performance"],
                   href="/cl1-performance", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-registered", style={'marginRight': '10px'}), "Regions Performance"],
                   href="/region_performance", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-code-compare", style={'marginRight': '10px'}), "Weekly compare"],
                   href="/Weekly-compare", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-code-compare", style={'marginRight': '10px'}), "Yearly compare"],
                   href="/Yearly_compare", style=sidebar_menu_style()),


            # Add Tools title
            html.H4("Tools", style={
                'color': '#FFFFFF',
                'margin': '20px 0 10px',
                'padding': '10px 20px',
                'fontSize': '23px',
                'fontWeight': 'bold'
            }),

            # Tools section
            html.A([html.I(className="fa-solid fa-file-excel", style={'marginRight': '10px'}), "Regions"],
                   href="/Region_countries", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-file-excel", style={'marginRight': '10px'}), "Split Sheet"],
                   href="/split_sheets", style=sidebar_menu_style()),
            html.A([html.I(className="fa-solid fa-dollar-sign", style={'marginRight': '10px'}), "Revenue"],
                   href="/revenou-maping", style=sidebar_menu_style()),
        ])
    ]
)

# Main Content Area that will change based on the URL
content = html.Div(
    className="content",
    style={
        'marginLeft': '270px',
        'padding': '20px',
        'backgroundColor': '#ffffff',
        'minHeight': '100vh'
    },
    children=[
        html.H1("Istanbul-Medipol Reporting Dashboard", style={
            'fontSize': '36px',
            'textAlign': 'center',
            'color': '#333',
            'marginBottom': '30px',
            'textTransform': 'uppercase',
            'letterSpacing': '3px'
        }),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', style={
            'marginTop': '40px',
            'padding': '20px',
            'backgroundColor': '#f0f0f0',
            'borderRadius': '10px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
            'minHeight': '400px'
        })
    ]
)

# App layout
app.layout = html.Div(children=[sidebar, content])

# Dictionary to track registered callbacks
callbacks_registered = {}


# Load layout dynamically from a given file
def load_layout_from_file(filepath):
    try:
        spec = importlib.util.spec_from_file_location(filepath.split('.')[0], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.layout
    except Exception as e:
        logging.error(f"Error loading layout from file {filepath}: {e}")
        return html.Div([html.H3('Error'), html.P('Failed to load layout.')])


# Register callbacks only once and cache the result
def register_callbacks(filepath):
    try:
        if filepath not in callbacks_registered:
            spec = importlib.util.spec_from_file_location(filepath.split('.')[0], filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.register_callbacks(app)
            callbacks_registered[filepath] = True
    except Exception as e:
        logging.error(f"Error registering callbacks from file {filepath}: {e}")


# Dynamically load the page based on the URL pathname
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    page_map = {
        '/university-report': 'university_report.py',
        '/weekly-report': 'weekly-report.py',
        '/signal-agent': 'signal-agent.py',
        '/top-reporting-dashboard': 'top_reporting_dashboard.py',
        '/cl1-performance': 'cl1-performance.py',
        '/region_performance': 'region_performance.py',
        '/Weekly-compare': 'Weekly-compare.py',
        '/Yearly_compare': 'Yearly_compare.py',
        '/split_sheets': 'split_sheets.py',
        '/Region_countries': 'Region_countries.py',  # Ensure this matches the correct path
        '/revenou-maping': 'revenou-maping.py'
    }

    filepath = page_map.get(pathname, None)
    if filepath:
        register_callbacks(filepath)
        return load_layout_from_file(filepath)

    # Custom introduction content with improved UI
    return html.Div([
        html.Div([
            html.H3('Welcome to the Istanbul-Medipol Reporting Dashboard', style={
                'textAlign': 'center', 'color': '#333', 'marginBottom': '20px', 'fontWeight': 'bold', 'fontSize': '40px'
            }),
            html.P(
                'This dashboard provides comprehensive reporting and analysis tools for monitoring academic and administrative data at Istanbul Medipol University.',
                style={'fontSize': '20px', 'textAlign': 'center', 'color': '#555', 'margin': '10px 0',
                       'fontWeight': 'bold'}
            ),
            html.P(
                'With features including university and agent reports, regional performance tracking, and tools for data analysis and processing, this platform aims to support data-driven decision-making across various departments.',
                style={'fontSize': '20px', 'textAlign': 'center', 'color': '#555', 'margin': '10px 0',
                       'fontWeight': 'bold'}
            ),
            html.P('Select an option from the sidebar to begin exploring the reports and tools available to you.',
                   style={'fontSize': '20px', 'textAlign': 'center', 'color': '#555', 'margin': '20px 0',
                          'fontWeight': 'bold'}
                   ),
            # PDF Link with Icon
            html.A(
                [html.I(className="fas fa-file-pdf", style={'marginRight': '8px', 'color': '#e74c3c'}),
                 "Read the Dashboard Guide (PDF)"],
                href="assets/Read.me.pdf",  # Replace with your actual PDF file path
                target="_blank",
                style={
                    'display': 'inline-block', 'fontSize': '18px', 'color': '#007bff', 'marginTop': '20px',
                    'textDecoration': 'none', 'fontWeight': 'bold'
                }
            )
        ], style={
            'padding': '30px', 'backgroundColor': '#ffffff', 'borderRadius': '10px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
            'width': '90%', 'margin': '0 auto', 'textAlign': 'center'
        })
    ])


# Update sidebar links based on the current pathname
@app.callback(
    Output('sidebar', 'children'),
    Input('url', 'pathname')
)
def update_sidebar(pathname):
    links = [
        {'href': '/university-report', 'label': 'University Report'},
        {'href': '/weekly-report', 'label': 'Weekly Report'},
        {'href': '/signal-agent', 'label': 'Individual Agent'},
        {'href': '/top-reporting-dashboard', 'label': 'Top Reporting Dashboard'},
        {'href': '/cl1-performance', 'label': 'CL1 Performance'},
        {'href': '/region_performance', 'label': 'Regions Performance'},
        {'href': '/Weekly-compare', 'label': 'Weekly compare'},
        {'href': '/Yearly_compare', 'label': 'Yearly compare'},
        {'href': '/split_sheets', 'label': 'Split Sheets'},
        {'href': '/Region_countries', 'label': 'Region'},
        {'href': '/revenou-maping', 'label': 'Revenue'}
    ]

    sidebar_links = []
    for link in links:
        active = pathname == link['href']
        sidebar_links.append(html.A(
            [html.I(className="fas fa-university", style={'marginRight': '10px'}), link['label']],
            href=link['href'],
            style=sidebar_menu_style(active=active)
        ))

    return sidebar_links


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
